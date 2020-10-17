import random
from tkinter import *

from board import Board, Snake, Food

interval = 200


class GameWindow:
    def __init__(self):
        self.width = 1000
        self.height = 800
        self.window = Tk()
        self.window.title("Simple snake")
        self.window.geometry(str(self.width) + "x" + str(self.height))
        self.canvas = Canvas(self.window, bg="blue", width=self.width, height=self.height)
        self.canvas.bind('<Key>', self.key_pressed)
        self.canvas.pack(expand=True, fill=BOTH)
        self.board = Board()
        self.snake = Snake()
        self.food = Food(17, 17)
        self.window.after(interval, self.game_loop)
        self.canvas.focus_set()

    def start(self):
        self.window.mainloop()

    def game_loop(self):
        food_eaten = False

        tail_position = self.snake.get_tail_position()
        head_position = self.snake.get_head_position()

        if self.is_game_over(head_position):
            self.canvas.create_text(self.width/2, self.height/2, fill="red", font="Times 40 bold", text="Game over")
            return

        if head_position[0] == self.food.x_position and head_position[1] == self.food.y_position:
            self.food = Food(random.randrange(0, 39), random.randrange(0, 39))
            food_eaten = True

        self.snake.move()

        if food_eaten:
            self.snake.add_tile(tail_position[0], tail_position[1])

        self.board.draw(canvas=self.canvas)
        self.snake.draw(canvas=self.canvas)
        self.food.draw(canvas=self.canvas)

        self.window.after(interval, self.game_loop)

    def key_pressed(self, event):
        event.__str__()
        self.snake.change_direction(event.keysym)

    def is_game_over(self, head_position):
        if head_position[0] < 0 or head_position[0] > 39 or head_position[1] < 0 or head_position[1] > 39:
            return True

        for snake_tile in self.snake.tiles[1:]:
            if head_position[0] == snake_tile.x_position and head_position[1] == snake_tile.y_position:
                return True

        return False


if __name__ == '__main__':
    gameWindow = GameWindow()
    gameWindow.start()
