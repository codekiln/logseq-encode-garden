created-by:: [[Person/codekiln]]
date-created:: [[2025/03]]
tags:: [[Py/Module]]

- # Sextant Grid - Unicode Sextant Character Mapping Utilities - Python module
	- ```python
	  """
	  Sextant Grid - Unicode Sextant Character Mapping Utilities
	  
	  This module provides a comprehensive implementation for working with Unicode sextant characters
	  from the "Symbols for Legacy Computing" Unicode block (U+1FB00 to U+1FBFF).
	  
	  Sextant characters are specialized Unicode symbols that divide a character cell into a 3×2 grid
	  (three rows, two columns), with each of the six sub-cells either activated or not. This allows
	  for higher resolution text-based graphics within a standard monospace character grid.
	  
	  Key features:
	  - Type-safe representation of sextant coordinates and characters
	  - Hierarchical organization of sextant characters by number of activated cells
	  - Efficient mapping between coordinate sets and their corresponding Unicode characters
	  - Simple string-based coordinate system ("1A", "1B", etc.)
	  
	  The module is designed to be used in any application requiring text-based graphics, such as:
	  - Terminal-based user interfaces
	  - ASCII/Unicode art generation
	  - Text-mode visualizations
	  - Retro-computing emulation
	  - Character-based animations
	  
	  References:
	  - Unicode Symbols for Legacy Computing: https://en.wikipedia.org/wiki/Symbols_for_Legacy_Computing
	  """
	  
	  from typing import (
	      NamedTuple,
	      Set,
	      Dict,
	      FrozenSet,
	      Literal,
	      TypeAlias,
	      List,
	      Tuple,
	      Type,
	      cast,
	  )
	  from abc import ABC, abstractmethod, isabstract
	  
	  
	  # Define a Literal type for valid sextant coordinate strings
	  SextantCoordinateString: TypeAlias = Literal["1A", "1B", "2A", "2B", "3A", "3B"]
	  
	  # Define a type for sets of sextant coordinate strings
	  SextantString: TypeAlias = Set[SextantCoordinateString]
	  
	  # Constants for coordinate strings
	  COORD_1A: SextantCoordinateString = "1A"
	  COORD_1B: SextantCoordinateString = "1B"
	  COORD_2A: SextantCoordinateString = "2A"
	  COORD_2B: SextantCoordinateString = "2B"
	  COORD_3A: SextantCoordinateString = "3A"
	  COORD_3B: SextantCoordinateString = "3B"
	  
	  
	  class SextantChar(NamedTuple):
	      """Represents a sextant Unicode character with its description."""
	  
	      unicode: str
	      char: str  # Visual representation for source code readability
	      description: str = ""
	  
	      def __str__(self) -> str:
	          """Returns the Unicode character when the object is converted to string."""
	          return self.unicode
	  
	  
	  class SextantCoord(NamedTuple):
	      """Represents a coordinate in the sextant grid with row (1-3) and column (0-1)."""
	  
	      row: int  # 1-3
	      col: int  # 0 for A, 1 for B
	  
	      @classmethod
	      def from_coordinate_string(
	          cls, coord_string: SextantCoordinateString
	      ) -> "SextantCoord":
	          """Creates a SextantCoord from a coordinate string (e.g., '1A')."""
	          row = int(coord_string[0])
	          col = 0 if coord_string[1] == "A" else 1
	          return cls(row=row, col=col)
	  
	      def to_coordinate_string(self) -> SextantCoordinateString:
	          """Converts the coordinate to its string representation."""
	          col_letter = "A" if self.col == 0 else "B"
	          coord_str = f"{self.row}{col_letter}"
	          return cast(SextantCoordinateString, coord_str)
	  
	  
	  class SextantCoordMapping(NamedTuple):
	      """Mapping between a set of coordinates and a Unicode character."""
	  
	      coordinate_strings: Tuple[SextantCoordinateString, ...]
	      sextant_char: SextantChar
	  
	      @property
	      def unicode_char(self) -> str:
	          """Returns the Unicode character for backward compatibility."""
	          return self.sextant_char.unicode
	  
	  
	  class SextantCellsActivated(ABC):
	      """Abstract base class for sextant character groups by cell count."""
	  
	      @classmethod
	      @abstractmethod
	      def get_coordinate_mappings(cls) -> List[SextantCoordMapping]:
	          """Returns a list of coordinate mappings for this cell count."""
	          pass
	  
	      @classmethod
	      def cell_count(cls) -> int:
	          """Returns the number of cells activated for this class."""
	          # Extract the number from the class name
	          for part in cls.__name__.split("Sextant"):
	              if part.endswith("CellsActivated"):
	                  num_str = part.split("Cells")[0]
	                  if num_str == "Zero":
	                      return 0
	                  elif num_str == "One":
	                      return 1
	                  elif num_str == "Two":
	                      return 2
	                  elif num_str == "Three":
	                      return 3
	                  elif num_str == "Four":
	                      return 4
	                  elif num_str == "Five":
	                      return 5
	                  elif num_str == "Six":
	                      return 6
	          return -1  # Should never happen
	  
	      @staticmethod
	      def _create_coord_mapping(
	          coords_to_chars: Dict[Tuple[SextantCoordinateString, ...], SextantChar]
	      ) -> List[SextantCoordMapping]:
	          """Helper method to create coordinate mappings from a dictionary of coordinates to characters.
	  
	          Args:
	              coords_to_chars: Dictionary mapping coordinate tuples to sextant characters
	  
	          Returns:
	              List of SextantCoordMapping objects
	          """
	          return [
	              SextantCoordMapping(coords, char)
	              for coords, char in coords_to_chars.items()
	          ]
	  
	      @classmethod
	      def get_all_subclasses(cls) -> List[Type["SextantCellsActivated"]]:
	          """Returns all concrete subclasses of SextantCellsActivated, sorted by cell count."""
	          # Get all direct and indirect subclasses
	          all_subclasses = []
	          for subclass in cls.__subclasses__():
	              all_subclasses.append(subclass)
	              all_subclasses.extend(subclass.__subclasses__())
	  
	          # Filter out any abstract classes
	          concrete_subclasses = [sc for sc in all_subclasses if not isabstract(sc)]
	  
	          # Sort by cell count
	          return sorted(concrete_subclasses, key=lambda sc: sc.cell_count())
	  
	  
	  # Define sextant characters grouped by cell count
	  class ZeroSextantCellsActivated(SextantCellsActivated):
	      """Sextant characters with no cells activated."""
	  
	      EMPTY = SextantChar("\U0001FB93", "⮓", "Empty sextant")
	  
	      @classmethod
	      def get_coordinate_mappings(cls) -> List[SextantCoordMapping]:
	          return cls._create_coord_mapping(
	              {
	                  (): cls.EMPTY,
	              }
	          )
	  
	  
	  class OneSextantCellActivated(SextantCellsActivated):
	      """Sextant characters with one cell activated."""
	  
	      TOP_LEFT = SextantChar("\U0001FB00", "🬀", "Top-left cell only")
	      TOP_RIGHT = SextantChar("\U0001FB01", "🬁", "Top-right cell only")
	      MIDDLE_LEFT = SextantChar("\U0001FB03", "🬃", "Middle-left cell only")
	      MIDDLE_RIGHT = SextantChar("\U0001FB07", "🬇", "Middle-right cell only")
	      BOTTOM_LEFT = SextantChar("\U0001FB0F", "🬏", "Bottom-left cell only")
	      BOTTOM_RIGHT = SextantChar("\U0001FB1E", "🬞", "Bottom-right cell only")
	  
	      @classmethod
	      def get_coordinate_mappings(cls) -> List[SextantCoordMapping]:
	          return cls._create_coord_mapping(
	              {
	                  (COORD_1A,): cls.TOP_LEFT,
	                  (COORD_1B,): cls.TOP_RIGHT,
	                  (COORD_2A,): cls.MIDDLE_LEFT,
	                  (COORD_2B,): cls.MIDDLE_RIGHT,
	                  (COORD_3A,): cls.BOTTOM_LEFT,
	                  (COORD_3B,): cls.BOTTOM_RIGHT,
	              }
	          )
	  
	  
	  class TwoSextantCellsActivated(SextantCellsActivated):
	      """Sextant characters with two cells activated."""
	  
	      TOP_ROW = SextantChar("\U0001FB02", "🬂", "Top row filled")
	      LEFT_TOP_TWO = SextantChar("\U0001FB04", "🬄", "Left column, top two cells")
	      TOP_LEFT_MIDDLE_RIGHT = SextantChar("\U0001FB08", "🬈", "Top-left and middle-right")
	      LEFT_TOP_BOTTOM = SextantChar("\U0001FB10", "🬐", "Left column, top and bottom")
	      TOP_LEFT_BOTTOM_RIGHT = SextantChar("\U0001FB1F", "🬟", "Top-left and bottom-right")
	      RIGHT_TOP_TWO = SextantChar("\U0001FB09", "🬉", "Right column, top two cells")
	      TOP_RIGHT_BOTTOM_LEFT = SextantChar("\U0001FB11", "🬑", "Top-right and bottom-left")
	      RIGHT_TOP_BOTTOM = SextantChar("\U0001FB20", "🬠", "Right column, top and bottom")
	      MIDDLE_ROW = SextantChar("\U0001FB0B", "🬋", "Middle row filled")
	      LEFT_BOTTOM_TWO = SextantChar("\U0001FB13", "🬓", "Left column, bottom two cells")
	      MIDDLE_LEFT_BOTTOM_RIGHT = SextantChar(
	          "\U0001FB22", "🬢", "Middle-left and bottom-right"
	      )
	      MIDDLE_RIGHT_BOTTOM_LEFT = SextantChar(
	          "\U0001FB16", "🬖", "Middle-right and bottom-left"
	      )
	      RIGHT_BOTTOM_TWO = SextantChar("\U0001FB26", "🬦", "Right column, bottom two cells")
	      BOTTOM_ROW = SextantChar("\U0001FB2D", "🬭", "Bottom row filled")
	  
	      @classmethod
	      def get_coordinate_mappings(cls) -> List[SextantCoordMapping]:
	          return cls._create_coord_mapping(
	              {
	                  (COORD_1A, COORD_1B): cls.TOP_ROW,
	                  (COORD_1A, COORD_2A): cls.LEFT_TOP_TWO,
	                  (COORD_1A, COORD_2B): cls.TOP_LEFT_MIDDLE_RIGHT,
	                  (COORD_1A, COORD_3A): cls.LEFT_TOP_BOTTOM,
	                  (COORD_1A, COORD_3B): cls.TOP_LEFT_BOTTOM_RIGHT,
	                  (COORD_1B, COORD_2B): cls.RIGHT_TOP_TWO,
	                  (COORD_1B, COORD_3A): cls.TOP_RIGHT_BOTTOM_LEFT,
	                  (COORD_1B, COORD_3B): cls.RIGHT_TOP_BOTTOM,
	                  (COORD_2A, COORD_2B): cls.MIDDLE_ROW,
	                  (COORD_2A, COORD_3A): cls.LEFT_BOTTOM_TWO,
	                  (COORD_2A, COORD_3B): cls.MIDDLE_LEFT_BOTTOM_RIGHT,
	                  (COORD_2B, COORD_3A): cls.MIDDLE_RIGHT_BOTTOM_LEFT,
	                  (COORD_2B, COORD_3B): cls.RIGHT_BOTTOM_TWO,
	                  (COORD_3A, COORD_3B): cls.BOTTOM_ROW,
	              }
	          )
	  
	  
	  class ThreeSextantCellsActivated(SextantCellsActivated):
	      """Sextant characters with three cells activated."""
	  
	      TOP_ROW_MIDDLE_LEFT = SextantChar("\U0001FB06", "🬆", "Top row and middle-left")
	      TOP_ROW_MIDDLE_RIGHT = SextantChar("\U0001FB0A", "🬊", "Top row and middle-right")
	      TOP_LEFT_MIDDLE_ROW = SextantChar("\U0001FB0C", "🬌", "Top-left and middle row")
	      TOP_RIGHT_MIDDLE_ROW = SextantChar("\U0001FB0D", "🬍", "Top-right and middle row")
	  
	      @classmethod
	      def get_coordinate_mappings(cls) -> List[SextantCoordMapping]:
	          return cls._create_coord_mapping(
	              {
	                  (COORD_1A, COORD_1B, COORD_2A): cls.TOP_ROW_MIDDLE_LEFT,
	                  (COORD_1A, COORD_1B, COORD_2B): cls.TOP_ROW_MIDDLE_RIGHT,
	                  (COORD_1A, COORD_2A, COORD_2B): cls.TOP_LEFT_MIDDLE_ROW,
	                  (COORD_1B, COORD_2A, COORD_2B): cls.TOP_RIGHT_MIDDLE_ROW,
	              }
	          )
	  
	  
	  class FourSextantCellsActivated(SextantCellsActivated):
	      """Sextant characters with four cells activated."""
	  
	      TOP_TWO_ROWS = SextantChar("\U0001FB0E", "🬎", "Top two rows filled")
	      TOP_ROW_MIDDLE_RIGHT_BOTTOM_LEFT = SextantChar(
	          "\U0001FB19", "🬙", "Top row, middle-right, bottom-left"
	      )
	      LEFT_COLUMN_MIDDLE_RIGHT_BOTTOM_LEFT = SextantChar(
	          "\U0001FB1B", "🬛", "Left column, middle-right, bottom-left"
	      )
	      TOP_RIGHT_MIDDLE_ROW_BOTTOM_LEFT = SextantChar(
	          "\U0001FB1C", "🬜", "Top-right, middle row, bottom-left"
	      )
	      TOP_ROW_MIDDLE_LEFT_BOTTOM_RIGHT = SextantChar(
	          "\U0001FB25", "🬥", "Top row, middle-left, bottom-right"
	      )
	      TOP_ROW_MIDDLE_RIGHT_BOTTOM_RIGHT = SextantChar(
	          "\U0001FB28", "🬨", "Top row, middle-right, bottom-right"
	      )
	      TOP_LEFT_MIDDLE_ROW_BOTTOM_RIGHT = SextantChar(
	          "\U0001FB2A", "🬪", "Top-left, middle row, bottom-right"
	      )
	      TOP_RIGHT_MIDDLE_ROW_BOTTOM_RIGHT = SextantChar(
	          "\U0001FB2B", "🬫", "Top-right, middle row, bottom-right"
	      )
	      TOP_BOTTOM_ROWS = SextantChar("\U0001FB30", "🬰", "Top and bottom rows filled")
	      LEFT_COLUMN_BOTTOM_ROW = SextantChar("\U0001FB32", "🬲", "Left column, bottom row")
	      TOP_RIGHT_MIDDLE_LEFT_BOTTOM_ROW = SextantChar(
	          "\U0001FB33", "🬳", "Top-right, middle-left, bottom row"
	      )
	      TOP_LEFT_MIDDLE_RIGHT_BOTTOM_ROW = SextantChar(
	          "\U0001FB36", "🬶", "Top-left, middle-right, bottom row"
	      )
	      TOP_RIGHT_MIDDLE_RIGHT_BOTTOM_ROW = SextantChar(
	          "\U0001FB37", "🬷", "Top-right, middle-right, bottom row"
	      )
	      MIDDLE_BOTTOM_ROWS = SextantChar("\U0001FB39", "🬹", "Middle and bottom rows filled")
	  
	      @classmethod
	      def get_coordinate_mappings(cls) -> List[SextantCoordMapping]:
	          return cls._create_coord_mapping(
	              {
	                  (COORD_1A, COORD_1B, COORD_2A, COORD_2B): cls.TOP_TWO_ROWS,
	                  (
	                      COORD_1A,
	                      COORD_1B,
	                      COORD_2B,
	                      COORD_3A,
	                  ): cls.TOP_ROW_MIDDLE_RIGHT_BOTTOM_LEFT,
	                  (
	                      COORD_1A,
	                      COORD_2A,
	                      COORD_2B,
	                      COORD_3A,
	                  ): cls.LEFT_COLUMN_MIDDLE_RIGHT_BOTTOM_LEFT,
	                  (
	                      COORD_1B,
	                      COORD_2A,
	                      COORD_2B,
	                      COORD_3A,
	                  ): cls.TOP_RIGHT_MIDDLE_ROW_BOTTOM_LEFT,
	                  (
	                      COORD_1A,
	                      COORD_1B,
	                      COORD_2A,
	                      COORD_3B,
	                  ): cls.TOP_ROW_MIDDLE_LEFT_BOTTOM_RIGHT,
	                  (
	                      COORD_1A,
	                      COORD_1B,
	                      COORD_2B,
	                      COORD_3B,
	                  ): cls.TOP_ROW_MIDDLE_RIGHT_BOTTOM_RIGHT,
	                  (
	                      COORD_1A,
	                      COORD_2A,
	                      COORD_2B,
	                      COORD_3B,
	                  ): cls.TOP_LEFT_MIDDLE_ROW_BOTTOM_RIGHT,
	                  (
	                      COORD_1B,
	                      COORD_2A,
	                      COORD_2B,
	                      COORD_3B,
	                  ): cls.TOP_RIGHT_MIDDLE_ROW_BOTTOM_RIGHT,
	                  (COORD_1A, COORD_1B, COORD_3A, COORD_3B): cls.TOP_BOTTOM_ROWS,
	                  (COORD_1A, COORD_2A, COORD_3A, COORD_3B): cls.LEFT_COLUMN_BOTTOM_ROW,
	                  (
	                      COORD_1B,
	                      COORD_2A,
	                      COORD_3A,
	                      COORD_3B,
	                  ): cls.TOP_RIGHT_MIDDLE_LEFT_BOTTOM_ROW,
	                  (
	                      COORD_1A,
	                      COORD_2B,
	                      COORD_3A,
	                      COORD_3B,
	                  ): cls.TOP_LEFT_MIDDLE_RIGHT_BOTTOM_ROW,
	                  (
	                      COORD_1B,
	                      COORD_2B,
	                      COORD_3A,
	                      COORD_3B,
	                  ): cls.TOP_RIGHT_MIDDLE_RIGHT_BOTTOM_ROW,
	                  (COORD_2A, COORD_2B, COORD_3A, COORD_3B): cls.MIDDLE_BOTTOM_ROWS,
	              }
	          )
	  
	  
	  class FiveSextantCellsActivated(SextantCellsActivated):
	      """Sextant characters with five cells activated."""
	  
	      ALL_EXCEPT_BOTTOM_RIGHT = SextantChar("\U0001FB1D", "🬝", "All except bottom-right")
	      ALL_EXCEPT_BOTTOM_LEFT = SextantChar("\U0001FB2C", "🬬", "All except bottom-left")
	      ALL_EXCEPT_MIDDLE_RIGHT = SextantChar("\U0001FB34", "🬴", "All except middle-right")
	      ALL_EXCEPT_MIDDLE_LEFT = SextantChar("\U0001FB38", "🬸", "All except middle-left")
	      ALL_EXCEPT_TOP_RIGHT = SextantChar("\U0001FB3A", "🬺", "All except top-right")
	      ALL_EXCEPT_TOP_LEFT = SextantChar("\U0001FB3B", "🬻", "All except top-left")
	  
	      @classmethod
	      def get_coordinate_mappings(cls) -> List[SextantCoordMapping]:
	          return cls._create_coord_mapping(
	              {
	                  (
	                      COORD_1A,
	                      COORD_1B,
	                      COORD_2A,
	                      COORD_2B,
	                      COORD_3A,
	                  ): cls.ALL_EXCEPT_BOTTOM_RIGHT,
	                  (
	                      COORD_1A,
	                      COORD_1B,
	                      COORD_2A,
	                      COORD_2B,
	                      COORD_3B,
	                  ): cls.ALL_EXCEPT_BOTTOM_LEFT,
	                  (
	                      COORD_1A,
	                      COORD_1B,
	                      COORD_2A,
	                      COORD_3A,
	                      COORD_3B,
	                  ): cls.ALL_EXCEPT_MIDDLE_RIGHT,
	                  (
	                      COORD_1A,
	                      COORD_2B,
	                      COORD_2B,
	                      COORD_3A,
	                      COORD_3B,
	                  ): cls.ALL_EXCEPT_MIDDLE_LEFT,
	                  (
	                      COORD_1A,
	                      COORD_2A,
	                      COORD_2B,
	                      COORD_3A,
	                      COORD_3B,
	                  ): cls.ALL_EXCEPT_TOP_RIGHT,
	                  (
	                      COORD_1B,
	                      COORD_2A,
	                      COORD_2B,
	                      COORD_3A,
	                      COORD_3B,
	                  ): cls.ALL_EXCEPT_TOP_LEFT,
	              }
	          )
	  
	  
	  class SixSextantCellsActivated(SextantCellsActivated):
	      """Sextant characters with all six cells activated."""
	  
	      FULL_BLOCK = SextantChar("\U0001FB8B", "🮋", "All cells filled (full block)")
	  
	      @classmethod
	      def get_coordinate_mappings(cls) -> List[SextantCoordMapping]:
	          return cls._create_coord_mapping(
	              {
	                  (
	                      COORD_1A,
	                      COORD_1B,
	                      COORD_2A,
	                      COORD_2B,
	                      COORD_3A,
	                      COORD_3B,
	                  ): cls.FULL_BLOCK,
	              }
	          )
	  
	  
	  # Function to convert mappings to a dictionary with frozensets as keys
	  def create_sextant_dict(
	      mappings: List[SextantCoordMapping],
	  ) -> Dict[FrozenSet[SextantCoordinateString], str]:
	      return {frozenset(m.coordinate_strings): m.sextant_char.unicode for m in mappings}
	  
	  
	  # Get all subclasses of SextantCellsActivated, sorted by cell count
	  SEXTANT_CELL_CLASSES = SextantCellsActivated.get_all_subclasses()
	  
	  # Get mappings from each class
	  SEXTANT_MAPPINGS_BY_COUNT: List[List[SextantCoordMapping]] = [
	      cls.get_coordinate_mappings() for cls in SEXTANT_CELL_CLASSES
	  ]
	  
	  # Create dictionaries for each cell count
	  CELL_MAPPINGS_BY_ACTIVE_CELLS = tuple(
	      create_sextant_dict(mappings) for mappings in SEXTANT_MAPPINGS_BY_COUNT
	  )
	  
	  # Create the main mapping dictionary from the flattened cell mappings
	  SEXTANT_CHAR_MAP: Dict[FrozenSet[SextantCoordinateString], str] = {
	      coords: char
	      for cell_count_dict in CELL_MAPPINGS_BY_ACTIVE_CELLS
	      for coords, char in cell_count_dict.items()
	  }
	  """
	  A dictionary mapping sets of string-based coordinates to their corresponding Unicode sextant characters.
	  
	  This dictionary uses frozensets of coordinate strings (e.g., frozenset(["1A", "1B"])) as keys,
	  and the corresponding Unicode sextant character as values.
	  
	  Example:
	      # The character with top row filled has coordinates "1A" and "1B" activated
	      char = SEXTANT_CHAR_MAP[frozenset(["1A", "1B"])]  # Returns "🬂"
	  """
	  
	  
	  def get_sextant_character(
	      active_cells: Set[SextantCoordinateString] | Set[SextantCoord],
	  ) -> str:
	      """
	      Returns the Unicode sextant character corresponding to the given set of active cells.
	  
	      This function maps a set of coordinates (either as strings or SextantCoord objects) within
	      a sextant grid to the appropriate Unicode character from the "Symbols for Legacy Computing"
	      block that visually represents those active positions.
	  
	      The coordinate system can use either:
	      1. String format where the first character is the row number (1-3) and the second
	         character is the column letter (A or B). For example: "1A", "1B", etc.
	      2. SextantCoord objects with row (1-3) and col (0 for A, 1 for B) attributes.
	  
	      Args:
	          active_cells: A set of coordinates (either strings like {"1A", "1B"} or
	                       SextantCoord objects) representing the positions that should be
	                       activated (filled) in the resulting character
	  
	      Returns:
	          A Unicode string containing a single sextant character with the specified cells activated.
	          Returns "?" if no matching character is found for the given set of coordinates.
	  
	      Examples:
	          # Using string coordinates
	          char = get_sextant_character({"1A", "3B"})  # Returns "🬟"
	  
	          # Using SextantCoord objects
	          char = get_sextant_character({SextantCoord(1, 0), SextantCoord(3, 1)})  # Returns "🬟"
	      """
	      # Convert SextantCoord objects to coordinate strings if needed
	      coord_strings: Set[SextantCoordinateString]
	      if active_cells and isinstance(next(iter(active_cells)), SextantCoord):
	          coord_strings = {
	              coord.to_coordinate_string()
	              for coord in cast(Set[SextantCoord], active_cells)
	          }
	      else:
	          coord_strings = cast(Set[SextantCoordinateString], active_cells)
	  
	      return SEXTANT_CHAR_MAP.get(
	          frozenset(coord_strings), "?"
	      )  # Return '?' if not found
	  
	  ```