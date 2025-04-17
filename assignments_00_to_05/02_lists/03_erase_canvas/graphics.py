
import tkinter as tk

class Canvas:
    def __init__(self, width, height):
        self.tk = tk.Tk()
        self.tk.title("Eraser Canvas")
        self.canvas = tk.Canvas(self.tk, width=width, height=height, bg='white')
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.last_click = None

        self.canvas.bind("<Motion>", self._motion)
        self.canvas.bind("<Button-1>", self._click)

        self.tk.update()

    def _motion(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def _click(self, event):
        self.last_click = (event.x, event.y)

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def get_mouse_x(self):
        return self.mouse_x

    def get_mouse_y(self):
        return self.mouse_y

    def moveto(self, obj, x, y):
        coords = self.canvas.coords(obj)
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        self.canvas.coords(obj, x, y, x + width, y + height)
        self.tk.update()

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def set_color(self, obj, color):
        self.canvas.itemconfig(obj, fill=color)

    def wait_for_click(self):
        self.last_click = None
        while self.last_click is None:
            self.tk.update()
        return

    def get_last_click(self):
        return self.last_click
