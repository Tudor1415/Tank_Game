import arcade
import random as rd

"""
Global variables:
"""
# Set how many rows and columns we will have
ROW_COUNT = 15
COLUMN_COUNT = 15

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 1

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Tank game"

class cmdMap:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.map = self.generateMap()

    def initMap(self):
        return [[0 for _ in range(self.Y)] for i in range(self.X)]

    def generateMap(self):
        map = self.initMap()
        for i in range(self.X):
            map[i] = [rd.randint(0,1) for _ in range(self.Y)]
        return map

    def __str__(self):
        for i in range(self.X):
            print(self.map[i])
        return "Success"

    def __getitem__(self, row):
        return self.map[row]

class GraphicGrid(arcade.Window):
    """
    Main grid class.
    """

    def __init__(self, width, height, title):
        """
        Set up the grid.
        """

        super().__init__(width, height, title)

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = cmdMap(ROW_COUNT, COLUMN_COUNT)
        print(self.grid)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.BLACK
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                if self.grid[row][column] == 1:
                    arcade.draw_rectangle_filled(x, y, WIDTH//3, HEIGHT, color)
                else:
                    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0
