import tkinter as tk

from core.model import Model
from core.view import View
from core.controller import Controller

def main():
    root = tk.Tk()

    model = Model()
    view = View(root)
    controller = Controller(model, view)

    root.mainloop()

main()