"""The visualizer class is used to show 3d scenes."""

from .points import Points
from .labels import Labels
from .lines import Lines
from .mesh import Mesh
from .camera import Camera
from .cuboid import Cuboid
from .polyline import Polyline
from .arrow import Arrow
from .circles_2d import Circles2D

import os
import sys
import shutil
import json
import numpy as np


class Visualizer:
    def __init__(self,
                 position: np.array = np.array([3.0, 3.0, 3.0]),
                 look_at: np.array = np.array([0.0, 0.0, 0.0]),
                 up: np.array = np.array([0.0, 0.0, 1.0]),
                 focal_length: float = 28.0):

        self.camera = Camera(
            position=np.array(position),
            look_at=np.array(look_at),
            up=np.array(up),
            focal_length=focal_length
        )
        self.elements = {"Camera_0": self.camera}

    def __parse_name(self,
                     name: str) -> str:
        """Makes sure the name does not contain invalid character combinations.

        :param name:
        :return:
        """
        return name.replace(':', ';')

    def save(self,
             path: str,
             port: int=6008,
             show_in_blender: bool=False,
             blender_output_path=None,
             blender_executable_path=None,
             verbose=True):
        """Creates the visualization and displays the link to it.

        :param path: The path to save the visualization files.
        :param port: The port to show the visualization.
        :param verbose: Whether to print the web-server message or not.
        """

        # Delete destination directory if it exists already
        directory_destination = os.path.abspath(path)
        if os.path.isdir(directory_destination):
            shutil.rmtree(directory_destination)

        # Copy website directory
        directory_source = os.path.realpath(os.path.join(os.path.dirname(__file__), "src"))
        shutil.copytree(directory_source, directory_destination)

        # Assemble binary data files
        nodes_dict = {}
        for name, e in self.elements.items():
            binary_file_path = os.path.join(directory_destination, name + ".bin")
            nodes_dict[name] = e.get_properties(name + ".bin")
            e.write_binary(binary_file_path)
            if show_in_blender:
                blender_file_oath = os.path.join(directory_destination, name + ".ply")
                e.write_blender(blender_file_oath)

        # Write json file containing all scene elements
        json_file = os.path.join(directory_destination, "nodes.json")
        with open(json_file, "w") as outfile:
            json.dump(nodes_dict, outfile)

        if not verbose:
            return

        # Display link
        http_server_string = "python -m SimpleHTTPServer " + str(port)
        if sys.version[0] == "3":
            http_server_string = "python -m http.server " + str(port)
        print("")
        print(
            "************************************************************************"
        )
        print("1) Start local server:")
        print("    cd " + directory_destination + "; " + http_server_string)
        print("2) Open in browser:")
        print("    http://localhost:" + str(port))
        print(
            "************************************************************************"
        )

        if show_in_blender:
            self.show_in_blender(path, blender_output_path, blender_executable_path, verbose)

    def show_in_blender(self,
                        path: str,
                        blender_output_path: str,
                        blender_executable_path: str,
                        verbose: bool=True):

        directory_destination = os.path.abspath(path)
        blender_script_path = os.path.join(directory_destination, "blender_script.py")
        with open(blender_script_path, "w") as outfile:
            outfile.write(
"import bpy\nimport os\n\
import sys\n\
sys.path.append(os.getcwd())\n\
import blender_tools\n\
blender_tools.main()")

        cmd = "cd " + directory_destination + "; " + blender_executable_path + " --background --python blender_script.py"
        if blender_output_path:
            cmd = cmd + " -- " + blender_output_path
        os.system(cmd)

        if verbose:
            print("")
            print("************************************************************************")
            print("Blender instructions")
            print(cmd)
            print("************************************************************************")
        
    def add_points(
        self,
        name: str,
        positions: np.array,
        colors: np.array=None,
        normals: np.array=None,
        point_size: int=25,
        resolution: int=5,
        visible: bool=True,
        alpha: float=1.0,
    ):
        """Add points to the visualizer.

        :param name: The name of the points displayed in the visualizer. Use ';' in the name to create sub-layers.
        :param positions: The point positions.
        :param normals: The point normals.
        :param colors: The point colors.
        :param point_size: The point size.
        :param resolution: The resolution of the blender sphere.
        :param visible: Bool if points are visible.
        :param alpha: Alpha value of colors.
        """

        assert positions.shape[1] == 3
        assert colors is None or positions.shape == colors.shape
        assert normals is None or positions.shape == normals.shape

        shading_type = 1  # Phong shading
        if colors is None:
            colors = np.ones(positions.shape, dtype=np.uint8) * 50  # gray
        if normals is None:
            normals = np.ones(positions.shape, dtype=np.float32)
            shading_type = 0  # Uniform shading when no normals are available

        positions = positions.astype(np.float32)
        colors = colors.astype(np.uint8)
        normals = normals.astype(np.float32)

        alpha = min(max(alpha, 0.0), 1.0)  # cap alpha to [0..1]

        self.elements[self.__parse_name(name)] = Points(
            positions, colors, normals, point_size, resolution, visible, alpha, shading_type
        )

    def add_labels(self,
                   name: str,
                   labels: list,
                   positions: np.array,
                   colors: np.array,
                   visible: bool=True):
        """Add labels to the visualizer.
        
        :param name: The name of the labels.
        :param labels: The text value of the labels.
        :param positions: The 3D positions of the labels.
        :param colors: The text color of the individual labels.
        :param visible: Bool if label is visible.
        """
        self.elements[self.__parse_name(name)] = Labels(labels, positions, colors, visible)

    def add_circles_2d(self,
                       name: str,
                       labels: list,
                       positions: np.array,
                       border_colors: np.array,
                       fill_colors: np.array,
                       visible: bool=True):
        """Add node to the visualizer.
        
        :param name: The name of the node.
        :param labels: The text value of the node.
        :param positions: The 3D positions of the node.
        :param border_colors: The text color of the individual node.
        :param fill_colors: The text color of the individual node.
        :param visible: Bool if lines are visible.
        """
        self.elements[self.__parse_name(name)] = Circles2D(labels, positions, border_colors, fill_colors, visible)

    def add_lines(self,
                  name: str,
                  lines_start: np.array,
                  lines_end: np.array,
                  colors: np.array=None,
                  visible: bool=True):
        """Add lines to the visualizer.

        :param name: The name of the lines displayed in the visualizer.
        :param lines_start: The start positions of the lines.
        :param lines_end: The end positions of the lines.
        :param colors: The line colors.
        :param visible: Bool if lines are visible.
        """

        assert lines_start.shape[1] == 3
        assert lines_start.shape == lines_end.shape
        assert colors is None or lines_start.shape == colors.shape

        if colors is None:
            colors = np.ones(lines_start.shape, dtype=np.uint8) * 50  # gray

        colors = colors.astype(np.uint8)
        lines_start = lines_start.astype(np.float32)
        lines_end = lines_end.astype(np.float32)
        self.elements[self.__parse_name(name)] = Lines(lines_start, lines_end, colors, colors, visible)

    def add_bounding_box(self,
                         name: str,
                         position: np.array,
                         size: np.array,
                         rotation: np.array=np.array([1.0, 0.0, 0.0, 0.0]),
                         color: np.array=np.array([255, 0, 0]),
                         alpha: float=1.0,
                         edge_width: float=0.01,
                         visible: bool=True):
        """Add oriented 3D bounding box."""
        rotation /= np.linalg.norm(rotation)  # normalize the orientation
        self.elements[self.__parse_name(name)] = Cuboid(position, size, rotation, color, alpha, edge_width, visible)

    def add_mesh(self,
                 name: str,
                 path: str,
                 translation: np.array=np.array([0.0, 0.0, 0.0]),
                 rotation: np.array=np.array([0, 0, 0, 1]),
                 scale: np.array=np.array([1, 1, 1]),
                 color: np.array=np.array([255, 255, 255]),
                 visible: bool=True):
        """Adds a polygon mesh to the scene as specified in the path.
         
          The path is currently limited to .obj files and the color is the uniform color of the objetc.
        """
        rotation /= np.linalg.norm(rotation)  # normalize the orientation
        self.elements[self.__parse_name(name)] = Mesh(path, translation=translation, rotation=rotation, scale=scale, color=color, visible=visible)

    def add_polyline(self,
                     name: str,
                     positions: np.array,
                     color: np.array=np.array([255, 0, 0]),
                     alpha: float=1.0,
                     edge_width: float=0.01,
                     visible: bool=True):
        """Add polyline.

        :param name: The bounding box name. (string)
        :param positions: The N 3D positions along the polyline. (float32, Nx3)
        :param color: The color. (int32, 3x1)
        :param alpha: The transparency. (float32)
        :param edge_width: The width of the edges. (float32)
        :param visible: Bool, whether visible or not.
        """

        self.elements[self.__parse_name(name)] = Polyline(positions, color, alpha, edge_width, visible)

    def add_arrow(self,
                  name:str,
                  start: np.array,
                  end: np.array,
                  color: np.array=np.array([255, 0, 0]),
                  alpha: float=1.0,
                  stroke_width: float=0.01,
                  head_width: float=0.03,
                  visible: bool=True):
        """Add an arrow."""

        self.elements[self.__parse_name(name)] = Arrow(start, end, color, alpha, stroke_width, head_width, visible)