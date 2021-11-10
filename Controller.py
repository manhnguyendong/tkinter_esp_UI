from tkinter import mainloop
from Model import MODEL
from View import VIEW

class CONTROL:
    def __init__(self) -> None:
        model = MODEL()
        view = VIEW()


def main():
    control = CONTROL()
    mainloop()

if __name__ == "__main__":
    main()