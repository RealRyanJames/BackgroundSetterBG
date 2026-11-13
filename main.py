from tkinter import *
from Conversion.rgb2hex import ConversionColor

running = True

class PosWin:
    def __init__(self, shown: bool, x, y):
        self.isShown = shown
        self.x = x
        self.y = y

    def get(self) -> bool:
        if self.isShown:
            return True
        return False

    def getGeo(self) -> str:
        return f"{self.x}x{self.y}"


def getValue(l: Text) -> str:
    return l.get("1.0", "end")


def main():

    tk = Tk()

    posWin = PosWin(True,  int(250 * 2), int(25 * 15))


    while running:

        try:

            l = Label(tk, text=f"Title: Hex To RGB", pady=20)

            rLabel = Label(tk, text="Enter R: ", font=('sans-serif', 20 - 10, 'bold'))
            r = Text(tk, height=-5, width=30, pady=10, padx=10)

            gLabel = Label(tk, text="Enter G: ", font=('sans-serif', 20 - 10, 'bold'))
            g = Text(tk, height=-5, width=30, pady=10, padx=10)
            g_Label = Label(tk, text="Enter B: ", font=('sans-serif', 20 - 10, 'bold'))
            text = Text(tk, height=-5, width=30, pady=10, padx=10)
            value = getValue(text)


            def rgb(color):
                return "#%02x%02x%02x" % color

            def click() -> None:
                if not value:
                    print("Empty")
                else:
                    tk.configure(bg=rgb((
                        int(r.get("1.0", "end-1c")),
                        int(g.get("1.0", "end-1c")),
                        int(text.get("1.0", "end-1c"))
                    )))

                    color_codesR = ConversionColor(int(r.get("1.0", "end")))
                    color_codesG = ConversionColor(int(g.get("1.0", "end")))
                    color_codesB = ConversionColor(int(text.get("1.0", "end")))

                    with open("color.txt", "a") as f:
                        f.write(str(f"R: {color_codesR.getColorR()}\n"))
                        f.write(str(f"G: {color_codesG.getColorR()}\n"))
                        f.write(str(f"B: {color_codesB.getColorR()}\n"))


            b = Button(tk, text=f"{"Set".upper()}", padx=4, pady=4, width=int(80), command=click)
            b.config(bg="black", fg="white")


            if posWin.get():

                tk.geometry(posWin.getGeo())

            l.pack()

            rLabel.pack()
            text.pack()

            gLabel.pack()
            r.pack()

            g_Label.pack()
            g.pack()

            b.pack(side="bottom", anchor="n")
            tk.resizable(False, False)
            tk.mainloop()
        except NameError:
            print("Error Not Running")


main()
