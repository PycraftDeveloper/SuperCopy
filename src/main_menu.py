if __name__ != "__main__":
    try:
        import sys
        import tkinter as tk
        import tkinter.font as font
        import tkinter.filedialog as filedialog
        from tkinter import ttk
        import shutil
        from tkinter import messagebox
        import tkinter.filedialog as filedialog

        from registry_utils import Registry

        import path_utils
        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start SuperCopy",
            f"A problem occurred whilst trying to start SuperCopy (main_menu.py).\nMore Details: {error}")

    class MainMenu:
        def browse_source_directories(self):
            filename = filedialog.askdirectory()

            if filename == "":
                self.source_path = None
                return

            filename = path_utils.Path(filename).path
            self.selected_source_file_path_entry.config(state='normal')
            self.selected_source_file_path_entry.delete(0, tk.END)
            self.selected_source_file_path_entry.insert(tk.END, filename)
            self.selected_source_file_path_entry.config(state='readonly')
            self.source_path = filename

            if self.source_path != None:
                if self.destination_path != None:
                    self.start_button['state'] = tk.NORMAL
                    return

            self.start_button['state'] = tk.DISABLED

        def browse_destination_directories(self):
            filename = filedialog.askdirectory()

            if filename == "":
                self.destination_path = None
                return

            filename = path_utils.Path(filename).path
            self.selected_destination_file_path_entry.config(state='normal')
            self.selected_destination_file_path_entry.delete(0, tk.END)
            self.selected_destination_file_path_entry.insert(tk.END, filename)
            self.selected_destination_file_path_entry.config(state='readonly')
            self.destination_path = filename

            if self.source_path != None:
                if self.destination_path != None:
                    self.start_button['state'] = tk.NORMAL
                    return

            self.start_button['state'] = tk.DISABLED

        def __init__(self):
            self.source_path = None
            self.destination_path = None
            title_font = font.Font(Registry.root, size=Registry.default_font_size+7)
            content_font = font.Font(Registry.root, size=Registry.default_font_size)

            self.title_label = ttk.Label(Registry.root, text="SuperCopy!", font=title_font)

            self.start_button = ttk.Button(Registry.root, text="Start", command=lambda: Registry.copy_utility.start(self.source_path, self.destination_path))
            self.start_button['state'] = tk.DISABLED

            self.content_text = tk.Text(Registry.root, wrap="word", relief=tk.FLAT, height=3)
            self.content_text.configure(font=content_font)
            self.content_text.insert(
                tk.INSERT,
                "Welcome to SuperCopy! This application copies files super fast from the source \
directory to the destination directory by using multi-threading!")
            self.content_text.config(state=tk.DISABLED)
            self.content_text.config(highlightthickness = 0, borderwidth=0)

            self.source_entry_frame = ttk.Frame(Registry.root)

            label = ttk.Label(self.source_entry_frame, text="Source Directory:")
            label.pack(side=tk.LEFT, padx=5)

            select_button = ttk.Button(self.source_entry_frame, text="Select", command=self.browse_source_directories)
            select_button.pack(side=tk.LEFT, padx=5)

            horizontal_scrollbar = ttk.Scrollbar(self.source_entry_frame, orient="horizontal")
            horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X, padx=5)

            self.selected_source_file_path_entry = ttk.Entry(self.source_entry_frame, xscrollcommand=horizontal_scrollbar.set)
            self.selected_source_file_path_entry.pack(side=tk.TOP, fill=tk.X, expand=True, padx=5)

            horizontal_scrollbar.config(command=self.selected_source_file_path_entry.xview)

            ###

            self.destination_entry_frame = ttk.Frame(Registry.root)

            label = ttk.Label(self.destination_entry_frame, text="Destination Directory:")
            label.pack(side=tk.LEFT, padx=5)

            select_button = ttk.Button(self.destination_entry_frame, text="Select", command=self.browse_destination_directories)
            select_button.pack(side=tk.LEFT, padx=5)

            horizontal_scrollbar = ttk.Scrollbar(self.destination_entry_frame, orient="horizontal")
            horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X, padx=5)

            self.selected_destination_file_path_entry = ttk.Entry(self.destination_entry_frame, xscrollcommand=horizontal_scrollbar.set)
            self.selected_destination_file_path_entry.pack(side=tk.TOP, fill=tk.X, expand=True, padx=5)

            horizontal_scrollbar.config(command=self.selected_destination_file_path_entry.xview)

            Registry.progress_bar = ttk.Progressbar(Registry.root)

        def main(self):
            self.title_label.pack()
            self.content_text.pack(fill=tk.X)

            self.source_entry_frame.pack(fill=tk.X)
            self.destination_entry_frame.pack(fill=tk.X)

            self.start_button.pack()

            Registry.progress_bar.pack(fill=tk.X)

else:
    MESSAGE = "You need to run this as part of SuperCopy. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
