try:
    if __name__ == "__main__":
        import __init__
        __init__.start()
except Exception as error:
    from tkinter import messagebox

    messagebox.showerror(
        "Unable to start SuperCopy",
        f"A problem occurred whilst trying to start SuperCopy (main.py).\nMore Details: {error}")
