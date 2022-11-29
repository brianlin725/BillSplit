from tkinter import messagebox

import customtkinter
from tkinter import *
from Person import Person


class AddPerson:
    def __init__(self, master):
        self.master = master
        self.itm = None
        self.window = customtkinter.CTkToplevel(master)
        self.window.title("Add Person")
        self.window.geometry("250x60")

        # Entry to enter name
        self.nameEntry = customtkinter.CTkEntry(self.window)
        self.nameEntry.grid(row=0, column=0, padx=5, pady=5, sticky="nswe")

        # Enter Button
        self.insertButton = customtkinter.CTkButton(self.window, text="Insert",
                                                    fg_color="#bdbebe",
                                                    hover_color="#8d8e8d",
                                                    command=self.insertEvent,
                                                    width = 80)
        self.insertButton.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nswe")
        self.window.bind("<Return>", self.insertEvent)

    def insertEvent(self, e = None):
        name = self.nameEntry.get()
        if len(name) == 0:
            response = messagebox.showinfo("info", "Name entry is empty")
            return

        for i in self.master.people:
            if i.getName() == name:
                response = messagebox.showinfo("info", "Name already exist")
                return

        self.master.people.append(Person(name))
        self.master.add_tab(name)

        self.window.destroy()
