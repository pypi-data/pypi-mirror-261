__version__ = '0.3.0'

# Standard Library Imports
# ------------------------
from functools import lru_cache
import importlib
import keyword
import logging
import os
from pathlib import Path
import re
import sys
from typing import Dict, List, Optional
from xml.etree import ElementTree

# Related Third Party Imports
# ---------------------------
# Declare the variables for the Qt libraries as None initially
QtCore = QtGui = QtWidgets = QtSvg = None

# Define the mappings of API names
API_NAMES = {
    'pyqt5': 'PyQt5',
    'pyside2': 'PySide2',
    'pyqt6': 'PyQt6',
    'pyside6': 'PySide6',
}

# Assign API to QT_API or, if it's not set or empty, to QT_PREFERRED_BINDING
API = (os.environ.get('QT_API', '') or os.environ.get('QT_PREFERRED_BINDING', '')).lower()


def use_backend(lib_name: Optional[str] = None):
    """Sets the preferred Qt library specified by the user.

    This function attempts to import QtCore, QtGui, QtWidgets, and QtSvg from the specified
    library. If no library is specified, it will try to import the libraries based on
    the QT_API environment variable (or QT_PREFERRED_BINDING as a fallback) or default order.

    Args:
        lib_name (str, optional): The preferred Qt library. If not provided, the function defaults to the
            value from QT_API or QT_PREFERRED_BINDING or a default order.
    """
    global QtCore, QtGui, QtWidgets, QtSvg

    # If lib_name is specified, try to import the modules from that Qt library
    if lib_name:
        # Try to import the modules from the specified Qt library
        QtCore = importlib.import_module(f"{lib_name}.QtCore")
        QtGui = importlib.import_module(f"{lib_name}.QtGui")
        QtWidgets = importlib.import_module(f"{lib_name}.QtWidgets")

        # Some libraries may not support QtSvg, handle it separately
        try:
            QtSvg = importlib.import_module(f"{lib_name}.QtSvg")
        except ModuleNotFoundError:
            # If QtSvg is not available, log a warning and set QtSvg as None
            QtSvg = None
            logging.warning(
                f'The QtSvg module could not be imported from {lib_name}. SVG icon functionality may not be available.')
        return

    # If no lib_name is provided and QT_API is set, use that
    if API in API_NAMES:
        try:
            # Attempt to use the current library
            use_backend(API_NAMES[API])
            logging.info(f'Successfully imported {API_NAMES[API]}')
            return
        except ModuleNotFoundError:
            pass

    # Try to import the libraries in the following order: ["PyQt5", "PySide2", "PyQt6", "PySide6"].
    # Loop through the list of Qt libraries in order of preference
    for lib_name in API_NAMES.values():
        try:
            # Attempt to use the current library
            use_backend(lib_name)
            logging.info(f'Successfully imported {lib_name}')
            return
        except ModuleNotFoundError:
            # If the current library is not found, continue to the next one
            continue

    # If none of the libraries could be imported, raise an ImportError
    raise ImportError(
        'No Qt libraries could be imported. Please ensure that at least one of PyQt6, PyQt5, PySide6, or PySide2 is installed.')


# Call the use_backend function to ensure the right backend is set
use_backend()

# Constant Definitions
# --------------------
TABLER_ICONS_SVG_DIRECTORY = Path(__file__).parent / 'icons'


# Class Definitions
# -----------------
class TablerQIconMeta(type):
    """Metaclass for TablerQIcon.

    This metaclass enables direct access to icons as attributes of the TablerQIcon class.
    It uses default arguments of the `_get_qicon` method when used without an instance.
    However, when used with an instance, it uses the arguments of the instance from
    the `get_qicon` method of the main class.

    Attributes:
        _icon_name_to_path_dict: A shared class variable as an empty dictionary to
            store the icon name and path.
    """
    # Class Constant Definitions
    # --------------------------
    # Define "outline" as a class constant
    DEFAULT_ICON_DIR = "outline"

    # Class Variable Definitions
    # --------------------------
    # Create a shared class variable as an empty dictionary to store the icon name and path
    _icon_name_to_path_dict: Dict[str, str] = dict()

    # Special Methods
    # ---------------
    def __getattr__(cls, name: str) -> QtGui.QIcon:
        """Allows direct access to the icons as attributes of the class.

        NOTE: This is a class-level method. It gets called when a user attempts
        to access an attribute that doesn't exist directly on the class (i.e.,
        without an instance). It employs the default arguments of the `_get_qicon`
        method to retrieve the requested attribute.

        Args:
            name (str): The name of the icon to retrieve.

        Returns:
            QtGui.QIcon : QIcon object for the given icon name.
        """
        return cls._get_qicon(name)

    def __setattr__(self, name: str, value) -> None:
        """Controls how attributes are set on instances of the class.

        This method overrides the default behavior for setting attributes.
        No attributes can be set in this metaclass, an attempt to do so will
        raise an AttributeError.

        Args:
            name (str): The name of the attribute to set.
            value : The value to set the attribute to.

        Raises:
            AttributeError: Raised when an attempt is made to set any attribute.
        """
        # No attributes can be set in this metaclass
        raise AttributeError(f"Cannot set attribute '{name}'. This attribute is not allowed.")

    # Class Methods
    # -------------
    @classmethod
    def _get_icon_name_to_path_dict(cls) -> Dict[str, str]:
        """Scans the icons directory recursively and constructs a dictionary mapping sanitized SVG file names
        to their respective file paths, appending directory names as suffixes for non-default directories.

        Returns:
            Dict[str, str]: Dictionary containing the icon name as key and the icon path as value.

        Raises:
            FileNotFoundError: If the predefined directory does not exist.
        """
        # If the class attribute _icon_name_to_path_dict is already populated, return it
        if cls._icon_name_to_path_dict:
            return cls._icon_name_to_path_dict

        # Ensure the specified directory exists before proceeding
        if not TABLER_ICONS_SVG_DIRECTORY.exists():
            # If the directory does not exist, raise a FileNotFoundError with a descriptive message
            raise FileNotFoundError(f"Directory {TABLER_ICONS_SVG_DIRECTORY} does not exist")

        # Create an empty dictionary to store the icon name and path
        icon_name_to_path_dict = dict()

        # Use pathlib's rglob method to get a list of all SVG files in any subdirectory under TABLER_ICONS_SVG_DIRECTORY
        svg_files = list(TABLER_ICONS_SVG_DIRECTORY.rglob('*.svg'))

        # Compile the regex pattern once to avoid recompilation in each loop iteration
        pattern = re.compile(r'[\W_]+')

        # For each SVG file, sanitize the file name to create the icon name
        for svg_file in svg_files:
            # Construct hierarchical names from file paths for structured and unique icon identification across directories
            relative_path = svg_file.relative_to(TABLER_ICONS_SVG_DIRECTORY)
            parts = relative_path.parts

            # Derive the base icon name from the SVG file name, excluding the file extension
            base_icon_name = pattern.sub('_', relative_path.stem)

            # Determine if the icon is in a special directory (not DEFAULT_ICON_DIR)
            if parts[0] != cls.DEFAULT_ICON_DIR and len(parts) > 1:
                # Join all parts except the last (filename) with underscores
                directory_suffix = '_'.join(parts[:-1])
                icon_name = f"{base_icon_name}_{directory_suffix}"
            else:
                icon_name = base_icon_name

            # Check if the icon name is a Python keyword or starts with a number
            if keyword.iskeyword(icon_name) or icon_name[0].isdigit():
                icon_name = "_" + icon_name

            # Add the icon name and path to the icon_name_to_path_dict
            icon_name_to_path_dict[icon_name] = svg_file

        # Store the constructed dictionary in the class attribute _icon_name_to_path_dict for future reference
        cls._icon_name_to_path_dict = icon_name_to_path_dict

        # Return the dictionary containing the icon name and path
        return cls._icon_name_to_path_dict

    @classmethod
    def _get_qicon(cls,
                   name: str,
                   color: QtGui.QColor = None,
                   size: int = 24,
                   view_box_size: int = 24,
                   stroke_width: int = 2,
                   opacity: float = 1.0,
                   flip: bool = False,
                   flop: bool = False) -> QtGui.QIcon:
        """Retrieves the icon as a QIcon object.

        Retrieves the path of the specified icon, checks if the path points to an
        existing file, and if it does, loads and returns the icon.

        Args:
            name (str): The name of the icon to retrieve.
            color (QtGui.QColor, optional): The color of the icon. If None, it defaults to the application's text color.
            size (int, optional): The size of the icon. Defaults to 24.
            view_box_size (int, optional): The size of the icon's view box. Defaults to 24.
            stroke_width (int, optional): The width of the icon's stroke. Defaults to 2.
            opacity (float, optional): The opacity of the icon. Defaults to 1.0.
            flip (bool, optional): If True, the icon will be flipped horizontally. Defaults to False.
            flop (bool, optional): If True, the icon will be flipped vertically. Defaults to False.

        Returns:
            QtGui.QIcon : QIcon object for the given icon name.
        """
        # Check if a color was provided. If not, use the application's default text color
        if color is None:
            # Use the application's text color if no color is specified
            app_instance = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
            color = app_instance.palette().color(QtGui.QPalette.ColorRole.Text)

        # Retrieve the dictionary mapping icon names to their paths
        icon_name_to_path_dict = cls._get_icon_name_to_path_dict()

        # Get the path of the icon from the dictionary using the name as the key
        svg_icon_path = icon_name_to_path_dict.get(name, str())

        # Check if the path obtained points to an existing file, if not log a warning and return an empty QIcon
        if not os.path.isfile(svg_icon_path):
            # Log a warning if the requested icon is not available or not a valid file
            logging.warning(f'Icon "{name}" is not available or not a valid file.')
            # Return an empty QIcon object
            return QtGui.QIcon()

        if QtSvg:
            # Load the original SVG file
            with open(svg_icon_path, 'r') as svg_file:
                svg_str = svg_file.read()

            # Parse the SVG file as XML
            svg = ElementTree.fromstring(svg_str)
            # Set the stroke width of the icon
            svg.set('stroke-width', str(stroke_width))
            svg_bytes = ElementTree.tostring(svg)

            # Create a renderer object to render the SVG file
            renderer = QtSvg.QSvgRenderer(svg_bytes)
            # Set the view box size
            renderer.setViewBox(QtCore.QRectF(0, 0, view_box_size, view_box_size))

            # Create a QPixmap object to hold the rendered image
            pixmap = QtGui.QPixmap(size, size)

            # Fill the pixmap with transparent color
            pixmap.fill(QtCore.Qt.GlobalColor.transparent)

            # Create a QPainter object to draw on the QPixmap
            painter = QtGui.QPainter(pixmap)

            # Render the SVG file to the pixmap
            renderer.render(painter)

        else:
            # Load the SVG file as a QPixmap
            pixmap = QtGui.QPixmap(str(svg_icon_path))

            # Set the size of the pixmap
            pixmap = pixmap.scaled(size, size, QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                   QtCore.Qt.TransformationMode.SmoothTransformation)

            # Create a QPainter object to draw on the QPixmap
            painter = QtGui.QPainter(pixmap)

        # Set the opacity of the icon
        painter.setOpacity(opacity)
        # Set the composition mode to "SourceIn" to composite the color on the icon
        painter.setCompositionMode(QtGui.QPainter.CompositionMode.CompositionMode_SourceIn)
        # Fill the pixmap with the specified color
        painter.fillRect(pixmap.rect(), color)
        # End the painter
        painter.end()

        # Check if the icon needs to be flipped (horizontally) or flopped (vertically)
        if flip or flop:
            transform = QtGui.QTransform()
            if flip:
                transform.scale(-1, 1)
            if flop:
                transform.scale(1, -1)
            pixmap = pixmap.transformed(transform)

        # Create a QIcon object using the rendered image
        icon = QtGui.QIcon(pixmap)

        # Return the icon
        return icon


class TablerQIcon(metaclass=TablerQIconMeta):
    """Class that loads icons from the tabler-icons directory and makes them available as attributes.

    The class uses a metaclass to allow access to the icons as attributes.

    Attributes:
        _icon_name_to_path_dict (dict): A dictionary containing the icon name as key and the icon path as value.
        _color (QtGui.QColor): The color of the icon.
        _size (int): The size of the icon.
        _view_box_size (int): The size of the icon's view box.
        _stroke_width (int): The width of the icon's stroke.
        _opacity (float): The opacity of the icon.
    """

    class _Proxy:
        """Initializes the proxy object with the parent TablerQIcon instance and states for flip and flop transformations.

        Args:
            parent (TablerQIcon): The parent TablerQIcon instance.
            flip (bool, optional): Initial state for horizontal flip. Defaults to False.
            flop (bool, optional): Initial state for vertical flip. Defaults to False.
        """

        def __init__(self, parent, flip=False, flop=False):
            self._parent = parent
            self._flip = flip
            self._flop = flop

        @property
        def flip(self):
            """Return a new proxy object with flip set to True"""
            return TablerQIcon._Proxy(self._parent, flip=not self._flip, flop=self._flop)

        @property
        def flop(self):
            """Return a new proxy object with flop set to True"""
            return TablerQIcon._Proxy(self._parent, flip=self._flip, flop=not self._flop)

        def __getattr__(self, name: str):
            icon = self._parent.get_qicon(name, flip=self._flip, flop=self._flop)
            self._flip = self._flop = False  # reset flip and flop states
            return icon

    # Initialization and Setup
    # ------------------------
    def __init__(self,
                 color: QtGui.QColor = None,
                 size: int = 24,
                 view_box_size: int = 24,
                 stroke_width: int = 2,
                 opacity: float = 1.0):
        """Initialize the widget and load the icons from the tabler-icons directory.

        Args:
            color (QtGui.QColor): color of the icon
            size (int): size of the icon
            view_box_size (int): size of the view box of the icon
            stroke_width (int): width of the stroke of the icon
            opacity (float): opacity of the icon
        """
        # Save the properties
        self._color = color
        self._size = size
        self._view_box_size = view_box_size
        self._stroke_width = stroke_width
        self._opacity = opacity

    # Special Methods
    # ---------------
    def __call__(self, name: str) -> QtGui.QIcon:
        """Allows access to the icons using function call style.

        Args:
            name (str): The name of the icon to retrieve.

        Returns:
            QtGui.QIcon : QIcon object for the given icon name
        """
        return self.get_qicon(name)

    def __getattr__(self, name: str) -> QtGui.QIcon:
        """Allows access to the icons as attributes of the class instance.

        NOTE: This is an instance-level method. It gets called when a user
        attempts to access an attribute that doesn't exist on the class
        instance. It employs the instance's arguments of the `get_qicon`
        method to retrieve the requested attribute.

        Args:
            name (str): The name of the icon to retrieve.

        Returns:
            QtGui.QIcon : QIcon object for the given icon name.
        """
        return self.get_qicon(name)

    def __getitem__(self, name: str) -> QtGui.QIcon:
        """Allows access to the icons as index.

        Args:
            name (str): The name of the icon to retrieve.
        Returns:
            QtGui.QIcon : QIcon object for the given icon name
        """
        return self.get_qicon(name)

    def __setattr__(self, name: str, value) -> None:
        """Controls how attributes are set on instances of the class.

        Args:
            name (str): The name of the attribute to set.
            value : The value to set the attribute to.

        Raises:
            AttributeError: If an attempt is made to set an attribute that corresponds
                to an icon name accessed via __getattr__.
        """
        # Only allow attributes that are already defined to be set
        if name in ('_color', '_size', '_view_box_size', '_stroke_width', '_opacity'):
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Cannot set attribute '{name}'. This attribute is not allowed.")

    # Extended Methods
    # ----------------
    @lru_cache(maxsize=128)
    def get_qicon(self, name: str, flip: bool = False, flop: bool = False) -> QtGui.QIcon:
        """Get the icon as a QIcon object using a method.

        Args:
            name (str): The name of the icon to retrieve.
            flip (bool, optional): If True, the icon will be flipped horizontally. Defaults to False.
            flop (bool, optional): If True, the icon will be flipped vertically. Defaults to False.

        Returns:
            QtGui.QIcon : QIcon object for the given icon name
        """
        # Create the QIcon object using the metaclass's method, with the instance's arguments
        icon = self.__class__._get_qicon(name=name,
                                         color=self._color,
                                         size=self._size,
                                         view_box_size=self._view_box_size,
                                         stroke_width=self._stroke_width,
                                         opacity=self._opacity,
                                         flip=flip,
                                         flop=flop)

        # Return the icon
        return icon

    # Class Methods
    # -------------
    @classmethod
    def get_icon_name_to_path_dict(cls) -> Dict[str, str]:
        """Retrieves a dictionary mapping sanitized icon names to their respective file paths.

        Icon names in the dictionary are derived from SVG file names, where invalid characters
        have been replaced with underscores, and an underscore is prepended for names that are
        Python keywords or start with a digit.

        Returns:
            Dict[str, str]: A dictionary with sanitized SVG file names (icon names) as keys and
                their respective file paths as values.
        """
        # Return the dictionary containing the icon name and path
        return cls._get_icon_name_to_path_dict()

    @classmethod
    def get_icon_names(cls) -> List[str]:
        """Provides a list of all available icon names.

        Returns:
            List[str]: A list containing all the available icon names.
        """
        # Retrieve the dictionary mapping from icon names to their paths
        icon_name_to_path_dict = cls._get_icon_name_to_path_dict()

        # Return the list of icon names
        return list(icon_name_to_path_dict.keys())

    @classmethod
    def get_icon_path(cls, name: str = None) -> Optional[str]:
        """Provides the path of a specific icon or the icons directory.

        Args:
            name (str, optional): The name of the icon. If not provided, the method will return the icons directory.

        Returns:
            Optional[str]: Path of the icon if the name is provided and exists in the dictionary, else the icons directory.
                If the name is provided but doesn't match any in the dictionary, returns None.
        """
        # If no icon name is provided, return the directory of all icons
        if not name:
            return TABLER_ICONS_SVG_DIRECTORY

        # Retrieve the dictionary mapping from icon names to their paths
        icon_name_to_path_dict = cls._get_icon_name_to_path_dict()

        # Return the path corresponding to the provided icon name
        return icon_name_to_path_dict.get(name)

    # Properties
    # ----------
    @property
    def flip(self):
        """Return a proxy object with flip set to True"""
        return self._Proxy(self, flip=True)

    @property
    def flop(self):
        """Return a proxy object with flop set to True"""
        return self._Proxy(self, flop=True)


# Main Execution
# --------------
if __name__ == '__main__':
    from PyQt5 import QtWidgets

    # Set the PyQT backend to PyQt5, ensuring TablerQIcon uses the same framework as the QApplication.
    use_backend('PyQt5')

    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create instance
    tabler_icon = TablerQIcon(opacity=0.8)

    # Create a QPushButton and set the icon of the button to the flipped 'player_play' icon
    play_backward_button = QtWidgets.QPushButton('Play Backward')
    play_backward_button.setIcon(tabler_icon.flip.player_play)

    # Show the button
    play_backward_button.show()

    # Execute the application
    sys.exit(app.exec())
