import tkinter
import customtkinter
from tkinter import *
from Item import Item


class AddItemMenu:
    def __init__(self, master, people):
        self.itm = None
        self.window = customtkinter.CTkToplevel(master)
        self.window.title("Add Item")
        self.window.geometry("550x160")
        self.window.grab_set()
        self.people = people
        self.master = master
        self.currPeople = []

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_rowconfigure(3, weight=10)

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)

        # Frame for left
        self.frameEntries = customtkinter.CTkFrame(self.window, width=550, corner_radius=7)
        self.frameEntries.grid(row=0, column=0, sticky="nswe", columnspan=3, padx=10, pady=10)

        self.frameEntries.grid_columnconfigure(0, weight=1)
        self.frameEntries.grid_columnconfigure(1, weight=1)
        self.frameEntries.grid_columnconfigure(2, weight=1)
        # self.frameEntries.grid_columnconfigure(3, weight = 1)
        self.frameEntries.grid_rowconfigure(0, weight=1)
        self.frameEntries.grid_rowconfigure(1, weight=1)

        # Labels for Edit Window
        self.labelName = customtkinter.CTkLabel(master=self.frameEntries,
                                                text="Item")  # font name and size in px
        self.labelName.grid(row=0, column=0, pady=(10, 1), padx=2, sticky="nswe")

        self.labelQuantity = customtkinter.CTkLabel(master=self.frameEntries,
                                                    text="Quantity")  # font name and size in px
        self.labelQuantity.grid(row=0, column=1, pady=(10, 1), padx=2, sticky="nswe")

        self.labelPrice = customtkinter.CTkLabel(master=self.frameEntries,
                                                 text="Total Price")  # font name and size in px
        self.labelPrice.grid(row=0, column=2, pady=(10, 1), padx=2, sticky="nswe")

        # self.labelAssign = customtkinter.CTkLabel(master = self.frameEntries,
        #                                          text = "Assign People")
        # self.labelAssign.grid(row = 0, column = 3, pady = (10, 1), padx = 2, sticky = "nswe")

        # Entries
        self.entryName = customtkinter.CTkEntry(master=self.frameEntries)
        self.entryName.grid(row=1, column=0, padx=2, pady=(1, 5), sticky="nswe")

        self.entryQuantity = customtkinter.CTkEntry(master=self.frameEntries)
        self.entryQuantity.grid(row=1, column=1, padx=2, pady=(1, 5), sticky="nswe")

        self.entryPrice = customtkinter.CTkEntry(master=self.frameEntries)
        self.entryPrice.grid(row=1, column=2, padx=3, pady=(1, 5), sticky="nswe")

        self.choices = {}
        self.insertButton = customtkinter.CTkButton(self.frameEntries, text="Insert", fg_color="#bdbebe",
                                                    command=self.updateTreeview, hover_color="#8d8e8d")
        self.insertButton.grid(row=2, column=0, pady=5, sticky="nswe")

        # Menubox for the selectable person
        # self.menuBtn = Menubutton(self.frameEntries, text = "Select", indicatoron= True, relief = "raised", font = ("Roboto", 9))
        # self.menu = Menu(self.menuBtn, tearoff = False)
        # self.menuBtn.configure(menu = self.menu)
        # self.menuBtn.grid(row = 1, column = 3, padx = 3, pady = (1,5), sticky = "nswe")

        # self.choices = {}
        # for i in people:
        #    self.choices[i.getName()] = IntVar(value = 0)
        #    self.menu.add_checkbutton(label = i.getName(), variable = self.choices[i.getName()], onvalue = 1, offvalue = 0, font = ("Roboto", 9))
        self.assignFrame = customtkinter.CTkFrame(master=self.window, width=170, corner_radius=7)
        self.assignFrame.grid(row=0, column=3, sticky="nswe", padx=10, pady=(10, 0))

        self.assignLabel = customtkinter.CTkLabel(master=self.assignFrame, text="Assign People")
        self.assignLabel.grid(row=0, column=0, sticky="nswe", padx=5, pady=(10, 5))

        for i in range(len(self.people)):
            name = self.people[i].getName()
            self.choices[name] = IntVar()
            # Creating checkbox and binding it to a command
            customtkinter.CTkCheckBox(master=self.assignFrame, text=self.people[i].getName(),
                                      variable=self.choices[name], ).grid(row=i + 1,
                                                                          column=0,
                                                                          padx=5,
                                                                          pady=5,
                                                                          sticky="w")

    # Creates an Item of the things inside
    def updateTreeview(self):

        checked = []

        # save people to item
        for key in self.choices:
            if self.choices[key].get() == 1:
                for i in self.people:
                    if i.getName() == key:
                        checked.append(i.getName)

        self.itm = Item(self.entryName.get(), self.entryPrice.get(), self.entryQuantity.get(), checked)

        # save item to person
        for person in checked:
            person.addItem(self.itm)

        self.master.items.append(self.itm)

        # Deletes everything in the treeview first
        for i in self.master.itemTree.get_children():
            self.master.itemTree.delete(i)

        for i in self.master.items:
            self.master.itemTree.insert(parent = "",
                                        index = "end",
                                        iid = self.master.items.index(i),
                                        values = (i.getName(), i.getQuantity(), i.getPrice()))

        self.master.update()