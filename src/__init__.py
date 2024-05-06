if __name__ != "__main__":
    try:
        import os
        import sys
        import platform
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start SuperCopy",
            f"A problem occurred whilst trying to start SuperCopy (__init__.py).\nMore Details: {error}")

    SEPARATOR = os.sep

    def up(path: str) -> str:
        return path[::-1].split(SEPARATOR, 1)[-1][::-1]

    base_path = up(up(__file__))

    sys.pycache_prefix = base_path + SEPARATOR + "temporary"

    supercopy_src_path = base_path + SEPARATOR + "src"
    supercopy_utility_path = supercopy_src_path + SEPARATOR + "utility"

    sys.path.append(
        supercopy_src_path)

    sys.path.append(
        supercopy_utility_path)

    import supercopy_main

    if platform.system() == "Windows":
        import ctypes
        VERSION = supercopy_main.get_version()
        myappid = f"PycraftDev.SuperCopy._.{VERSION}"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        del myappid
        del ctypes

    del sys
    del platform
    del base_path
    del up
    del SEPARATOR

    def start() -> None:
        supercopy_main.init()

else:
    MESSAGE = "You need to run this as part of SuperCopy. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
