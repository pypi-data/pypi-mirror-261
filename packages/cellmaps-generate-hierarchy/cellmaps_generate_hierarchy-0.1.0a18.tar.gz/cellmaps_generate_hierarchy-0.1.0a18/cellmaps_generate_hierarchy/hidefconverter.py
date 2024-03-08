import logging
import os
from ndex2.cx2 import RawCX2NetworkFactory
import ndex2.constants as constants
import cellmaps_utils.constants as cellmaps_constants

from cellmaps_generate_hierarchy.exceptions import CellmapsGenerateHierarchyError

logger = logging.getLogger(__name__)


class HierarchyToHiDeFConverter:
    """
    A class to convert a hierarchy network (in CX2 format) to a HiDeF format.
    """
    HIDEF_OUT_PREFIX = 'hidef_output_gene_names'

    def __init__(self, input_dir, output_dir):
        """
        Constructor

        :param output_dir: The directory containing the hierarchy file.
        :type output_dir: str
        :param output_dir: The directory where the output files will be stored.
        :type output_dir: str
        """
        self.output_dir = output_dir
        self.hierarchy_path = os.path.join(input_dir,
                                           cellmaps_constants.HIERARCHY_NETWORK_PREFIX + cellmaps_constants.CX2_SUFFIX)
        try:
            factory = RawCX2NetworkFactory()
            self.hierarchy = factory.get_cx2network(self.hierarchy_path)
        except Exception as e:
            logger.error(f"Failed to load hierarchy: {e}")
            raise CellmapsGenerateHierarchyError(f"Failed to load hierarchy: {e}")

    def generate_hidef_files(self):
        """
        Generates HiDeF files .nodes and .edges from the hierarchy network.
        """
        try:
            nodes = self.hierarchy.get_nodes()
            edges = self.hierarchy.get_edges()
            formatted_nodes = self._format_aspect(nodes, self._format_node)
            formatted_edges = self._format_aspect(edges, self._format_edge)
            nodes_path = HierarchyToHiDeFConverter.HIDEF_OUT_PREFIX + '.nodes'
            self._write_to_file(nodes_path, formatted_nodes)
            edges_path = HierarchyToHiDeFConverter.HIDEF_OUT_PREFIX + '.edges'
            self._write_to_file(edges_path, formatted_edges)
            return nodes_path, edges_path
        except Exception as e:
            logger.error(f"Error during HiDeF generation: {e}")
            raise

    @staticmethod
    def _format_aspect(aspect, format_function):
        """
        Formats aspect list (nodes or edges) using a specified format function.

        :param aspect: A list of aspect IDs (nodes or edges).
        :type aspect: dict
        :param format_function: A function to format a single entity.
        :type format_function: function
        :return: A list of formatted nodes or edges.
        :rtype: list
        """
        return [format_function(aspect_id) for aspect_id in aspect]

    def _format_node(self, node_id):
        """
        Formats a node for HiDeF output.

        :param node_id: The ID of the node to be formatted.
        :type node_id: int
        :return: A formatted string representing the node.
        :rtype: str
        """
        node = self.hierarchy.get_node(node_id)
        node_attr = node[constants.ASPECT_VALUES]
        formatted_node = (node_attr['name'], node_attr['CD_MemberList_Size'],
                          node_attr['CD_MemberList'], node_attr['HiDeF_persistence'])
        return "\t".join(map(str, formatted_node))

    def _format_edge(self, edge_id):
        """
        Formats an edge for HiDeF output.

        :param edge_id: The ID of the edge to be formatted.
        :type edge_id: int
        :return: A formatted string representing the edge.
        :rtype: str
        """
        edge = self.hierarchy.get_edge(edge_id)
        source_node = self._find_node_name_by_id(edge[constants.EDGE_SOURCE])
        target_node = self._find_node_name_by_id(edge[constants.EDGE_TARGET])
        return f"{source_node}\t{target_node}\tdefault"

    def _find_node_name_by_id(self, node_id):
        """
        Finds the name of a node given its ID.

        :param node_id: The ID of the node.
        :type node_id: int
        :return: The name of the node.
        :rtype: str
        """
        node = self.hierarchy.get_node(node_id)
        return node[constants.ASPECT_VALUES]['name']

    def _write_to_file(self, filename, lines):
        """
        Writes output to a file.

        :param filename: The name of the file to write to.
        :type filename: str
        :param lines: A list of strings to be written to the file.
        :type lines: list
        """
        file_path = os.path.join(self.output_dir, filename)
        with open(file_path, 'w') as file:
            file.write('\n'.join(lines))
