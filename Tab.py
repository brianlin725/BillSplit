import customtkinter


class Tab:
    def __init__(self, master, name):
        self.master = master
        self.name = name

        self.frame = customtkinter.CTkFrame(self.master.notebook, width=450, corner_radius=5)
        self.frame.grid(row=0, column=0, sticky="nswe", padx=15, pady=15)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        self.master.notebook.add(self.frame, text=name)
        self.master.notebook.update()

    def getFrame(self):
        return self.frame

    def getName(self):
        return self.name
