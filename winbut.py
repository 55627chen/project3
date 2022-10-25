import tkinter as tk
from PIL import Image, ImageTk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # ----建立背景
        bgImage = Image.open('bg.jpg')
        self.tkImage = ImageTk.PhotoImage(bgImage)
        buImage = Image.open('1_.png')
        self.butImage = ImageTk.PhotoImage(buImage)
        mainCanvas = tk.Canvas(self)
        mainCanvas.create_image(0, 0, anchor=tk.NW, image=self.tkImage)
        #tk.Button(mainCanvas, text="click", image=self.butImage).pack()
        mainCanvas.pack(fill=tk.BOTH, expand=True)
        # ------建立背景


def main():
    window = Window()
    window.title("Frame框架")
    window.resizable(0, 0)
    window.geometry("640x427+300+200")
    window.mainloop()


if __name__ == "__main__":
    main()
