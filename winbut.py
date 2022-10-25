import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont


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
        # END------建立背景
        # ------建立Label
        helv36 = tkFont.Font(family='Helvetica',
                             size=36, weight='bold')
        tk.Label(mainCanvas, text="職能發展學院", font=('arial', 30),
                 background='#C9C8CD').place(x=370, y=80)
        # END------建立Label


def main():
    window = Window()
    window.title("Frame框架")
    window.resizable(0, 0)
    window.geometry("640x427+300+200")
    window.mainloop()


if __name__ == "__main__":
    main()
