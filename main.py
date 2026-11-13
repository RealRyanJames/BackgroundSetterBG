from tkinter import *

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
    l = Label(tk, text=f"Title: Hex To RGB")

    posWin = PosWin(True,  int(250 * 2), int(25 * 10))


    while running:

        text = Text(tk, height=-5, width=30, pady=10, padx=10)
        value = getValue(text)


        def rgb(color):
            return "#%02x%02x%02x" % color

        def click() -> None:
            if not value:
                print("Empty")
            else:
                tk.configure(bg=rgb((
                    int(text.get("1.0", "end")),
                    int(text.get("1.0", "end")),
                    int(text.get("1.0", "end"))
                )))




        b = Button(tk, text=f"{"Set".upper()}", padx=4, pady=4, width=int(80), command=click)
        b.config(bg="black", fg="white")


        if posWin.get():

            tk.geometry(posWin.getGeo())

        l.pack()
        text.pack()

        b.pack(side="bottom", anchor="n")
    
        tk.mainloop()

main()
