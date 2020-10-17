from enum import Enum
from tkinter import BOTH


class Board:
    def __init__(self):
        self.widthNumOfTiles = 40
        self.heightNumOfTiles = 40
        self.tiles = []

        for x in range(0, 40):
            col = []
            for y in range(0, 40):
                col.append(Tile(x, y))
            self.tiles.append(col)

    def draw(self, canvas):
        for row in self.tiles:
            for col in row:
                col.draw(canvas)
        canvas.pack(fill=BOTH, expand=1)


class Tile:
    def __init__(self, pos_x, pos_y, outline_color="#fff", fill_color="#0f9", outline_width=0):
        self.x_position = pos_x
        self.y_position = pos_y
        self.tileWidth = 20
        self.tileHeight = 20
        self.outlineColor = outline_color
        self.fillColor = fill_color
        self.outlineWidth = outline_width

    def draw(self, canvas):
        pos_x0 = self.x_position * self.tileWidth
        pos_y0 = self.y_position * self.tileHeight
        canvas.create_rectangle(pos_x0, pos_y0, pos_x0 + self.tileWidth, pos_y0 + self.tileHeight,
                                outline=self.outlineColor, fill=self.fillColor, width=self.outlineWidth)


class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


class Food(Tile):
    def __init__(self, pos_x, pos_y):
        self.eaten = False
        Tile.__init__(self, pos_x=pos_x, pos_y=pos_y, fill_color="#f00")


class Snake:
    def __init__(self):
        self.size = 1
        self.tiles = []
        self.direction = Direction.LEFT
        self.tiles.append(Tile(20, 20, fill_color="#ff0"))

    def get_head_position(self):
        head = self.tiles[0]
        return head.x_position, head.y_position

    def get_tail_position(self):
        tail = self.tiles[len(self.tiles) - 1]
        return tail.x_position, tail.y_position

    def add_tile(self, x_pos, y_pos):
        self.tiles.append(Tile(x_pos, y_pos, fill_color="#ff0"))

    def draw(self, canvas):
        for tile in self.tiles:
            tile.draw(canvas)
        canvas.pack(fill=BOTH, expand=1)

    def change_direction(self, direction):
        if direction == 'Left' and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        if direction == 'Right' and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
        if direction == 'Up' and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        if direction == 'Down' and self.direction != Direction.UP:
            self.direction = Direction.DOWN

    def move(self):
        head = self.tiles[0]

        previous_tile_pos = head.x_position, head.y_position

        self.move_snake_tiles_without_head(previous_tile_pos)

        self.move_head_by_direction(head)

    def move_snake_tiles_without_head(self, previous_tile_pos):
        for idx in range(1, len(self.tiles)):
            current_tile = self.tiles[idx]
            temp_position = current_tile.x_position, current_tile.y_position
            current_tile.x_position = previous_tile_pos[0]
            current_tile.y_position = previous_tile_pos[1]
            previous_tile_pos = temp_position

    def move_head_by_direction(self, head):
        if self.direction == Direction.LEFT:
            head.x_position -= 1
        elif self.direction == Direction.RIGHT:
            head.x_position += 1
        elif self.direction == Direction.UP:
            head.y_position -= 1
        elif self.direction == Direction.DOWN:
            head.y_position += 1
        else:
            raise RuntimeError
