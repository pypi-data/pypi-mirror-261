from collections.abc import Sequence
from typing import Any

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandera as pa
import shapely
from matplotlib.patches import Patch
from numpy.typing import NDArray
from pandera.typing import Series
from pandera.typing.geopandas import GeoSeries
from pydantic import field_validator

from ribasim.input_base import SpatialTableModel

__all__ = ("Node",)


class NodeSchema(pa.SchemaModel):
    node_id: Series[int]
    name: Series[str] = pa.Field(default="")
    node_type: Series[str] = pa.Field(default="")
    subnetwork_id: Series[pd.Int64Dtype] = pa.Field(
        default=pd.NA, nullable=True, coerce=True
    )
    geometry: GeoSeries[Any] = pa.Field(default=None, nullable=True)

    class Config:
        add_missing_columns = True
        coerce = True


class Node(SpatialTableModel[NodeSchema]):
    """The Ribasim nodes as Point geometries."""

    # TODO: Remove as soon as add api has been merged
    @field_validator("df", mode="before")
    @classmethod
    def add_node_id_column(cls, df: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        if "node_id" not in df.columns:
            df.insert(0, "node_id", df.index)
        return df

    @staticmethod
    def node_ids_and_types(*nodes):
        # TODO Not sure if this staticmethod belongs here
        data_types = {"node_id": int, "node_type": str}
        node_type = pd.DataFrame(
            {col: pd.Series(dtype=dtype) for col, dtype in data_types.items()}
        )

        for node in nodes:
            if not node:
                continue

            ids, types = node.node_ids_and_types()
            node_type_table = pd.DataFrame(
                data={
                    "node_id": ids,
                    "node_type": types,
                }
            )
            node_type = node_type._append(node_type_table)

        node_type = node_type.drop_duplicates(subset="node_id")
        node_type = node_type.sort_values("node_id")

        node_id = node_type.node_id.tolist()
        node_type = node_type.node_type.tolist()

        return node_id, node_type

    def geometry_from_connectivity(
        self, from_id: Sequence[int], to_id: Sequence[int]
    ) -> NDArray[Any]:
        """
        Create edge shapely geometries from connectivities.

        Parameters
        ----------
        node : Ribasim.Node
        from_id : Sequence[int]
            First node of every edge.
        to_id : Sequence[int]
            Second node of every edge.

        Returns
        -------
        edge_geometry : np.ndarray
            Array of shapely LineStrings.
        """
        assert self.df is not None
        geometry = self.df["geometry"]
        from_points = shapely.get_coordinates(geometry.loc[from_id])
        to_points = shapely.get_coordinates(geometry.loc[to_id])
        n = len(from_points)
        vertices = np.empty((n * 2, 2), dtype=from_points.dtype)
        vertices[0::2, :] = from_points
        vertices[1::2, :] = to_points
        indices = np.repeat(np.arange(n), 2)
        return shapely.linestrings(coords=vertices, indices=indices)

    def connectivity_from_geometry(
        self, lines: NDArray[Any]
    ) -> tuple[NDArray[Any], NDArray[Any]]:
        """
        Derive from_node_id and to_node_id for every edge in lines. LineStrings
        may be used to connect multiple nodes in a sequence, but every linestring
        vertex must also a node.

        Parameters
        ----------
        node : Node
        lines : np.ndarray
            Array of shapely linestrings.

        Returns
        -------
        from_node_id : np.ndarray of int
        to_node_id : np.ndarray of int
        """
        assert self.df is not None
        node_index = self.df.index
        node_xy = shapely.get_coordinates(self.df.geometry.values)
        edge_xy = shapely.get_coordinates(lines)

        xy = np.vstack([node_xy, edge_xy])
        _, inverse = np.unique(xy, return_inverse=True, axis=0)
        _, index, inverse = np.unique(
            xy, return_index=True, return_inverse=True, axis=0
        )
        uniques_index = index[inverse]

        node_node_id, edge_node_id = np.split(uniques_index, [len(node_xy)])
        if not np.isin(edge_node_id, node_node_id).all():
            raise ValueError(
                "Edge lines contain coordinates that are not in the node layer. "
                "Please ensure all edges are snapped to nodes exactly."
            )

        edge_node_id = edge_node_id.reshape((-1, 2))
        from_id = node_index[edge_node_id[:, 0]].to_numpy()
        to_id = node_index[edge_node_id[:, 1]].to_numpy()
        return from_id, to_id

    def plot_allocation_networks(self, ax=None, zorder=None) -> Any:
        if ax is None:
            _, ax = plt.subplots()
            ax.axis("off")

        COLOR_SUBNETWORK = "black"
        COLOR_MAIN_NETWORK = "blue"
        ALPHA = 0.25

        contains_main_network = False
        contains_subnetworks = False
        assert self.df is not None

        for subnetwork_id, df_subnetwork in self.df.groupby("subnetwork_id"):
            if subnetwork_id is None:
                continue
            elif subnetwork_id == 1:
                contains_main_network = True
                color = COLOR_MAIN_NETWORK
            else:
                contains_subnetworks = True
                color = COLOR_SUBNETWORK

            hull = gpd.GeoDataFrame(
                geometry=[df_subnetwork.geometry.unary_union.convex_hull]
            )
            hull.plot(ax=ax, color=color, alpha=ALPHA, zorder=zorder)

        handles = []
        labels = []

        if contains_main_network:
            handles.append(Patch(facecolor=COLOR_MAIN_NETWORK, alpha=ALPHA))
            labels.append("Main network")
        if contains_subnetworks:
            handles.append(Patch(facecolor=COLOR_SUBNETWORK, alpha=ALPHA))
            labels.append("Subnetwork")

        return handles, labels

    def plot(self, ax=None, zorder=None) -> Any:
        """
        Plot the nodes. Each node type is given a separate marker.

        Parameters
        ----------
        ax : Optional
            The axis on which the nodes will be plotted.

        Returns
        -------
        None
        """
        if ax is None:
            _, ax = plt.subplots()
            ax.axis("off")

        MARKERS = {
            "Basin": "o",
            "FractionalFlow": "^",
            "LevelBoundary": "o",
            "LinearResistance": "^",
            "ManningResistance": "D",
            "TabulatedRatingCurve": "D",
            "Pump": "h",
            "Outlet": "h",
            "Terminal": "s",
            "FlowBoundary": "h",
            "DiscreteControl": "*",
            "PidControl": "x",
            "UserDemand": "s",
            "LevelDemand": "o",
            "": "o",
        }

        COLORS = {
            "Basin": "b",
            "FractionalFlow": "r",
            "LevelBoundary": "g",
            "LinearResistance": "g",
            "ManningResistance": "r",
            "TabulatedRatingCurve": "g",
            "Pump": "0.5",  # grayscale level
            "Outlet": "g",
            "Terminal": "m",
            "FlowBoundary": "m",
            "DiscreteControl": "k",
            "PidControl": "k",
            "UserDemand": "g",
            "LevelDemand": "k",
            "": "k",
        }
        assert self.df is not None

        for nodetype, df in self.df.groupby("node_type"):
            assert isinstance(nodetype, str)
            marker = MARKERS[nodetype]
            color = COLORS[nodetype]
            ax.scatter(
                df.geometry.x,
                df.geometry.y,
                marker=marker,
                color=color,
                zorder=zorder,
                label=nodetype,
            )

        assert self.df is not None
        geometry = self.df["geometry"]
        for text, xy in zip(self.df.index, np.column_stack((geometry.x, geometry.y))):
            ax.annotate(text=text, xy=xy, xytext=(2.0, 2.0), textcoords="offset points")

        return ax
