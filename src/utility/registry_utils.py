if __name__ != "__main__":
    try:
        import pathlib

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start SuperCopy",
            f"A problem occurred whilst trying to start SuperCopy (registry_utils.py).\nMore Details: {error}")

    class Registry:
        root = path_utils.Path(__file__)
        for _ in range(3):
            root.up()
        base_path = root.path
        version = "1.0.0"

else:
    MESSAGE = "You need to run this as part of SuperCopy. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
