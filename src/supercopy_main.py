if __name__ != "__main__":
    try:
        import tkinter as tk
        import tkinter.font as font

        from registry_utils import Registry

        import main_menu

        import tkinter_utils
        import copy_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start SuperCopy",
            f"A problem occurred whilst trying to start PSuperCopy (supercopy_main.py).\nMore Details: {error}")

    class Core(Registry):
        def __init__(self):
            Registry.tkinter_utils = tkinter_utils.TkinterUtils()
            Registry.copy_utility = copy_utils.Copier()

            Registry.root = tk.Tk()
            Registry.root.eval('tk::PlaceWindow . center')
            Registry.root.title("SuperCopy!")
            Registry.root.resizable(width=True, height=False)

            Registry.tkinter_utils.style("TLabel")
            Registry.tkinter_utils.style("TEntry")
            Registry.tkinter_utils.style("TButton")
            Registry.tkinter_utils.style("TFrame")
            Registry.tkinter_utils.style("Horizontal.TScrollbar")

            fonts = font.nametofont('TkTextFont').actual()
            Registry.default_font_size = fonts["size"]

            self.main_screen = main_menu.MainMenu()

        def main(self):
            Registry.tkinter_utils.basic_window_configuration()
            self.main_screen.main()

            Registry.root.mainloop()

    def init():
        Core().main()

    def get_version():
        return Registry.version
else:
    MESSAGE = "You need to run this as part of SuperCopy. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
