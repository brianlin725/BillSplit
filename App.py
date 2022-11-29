import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
from subMenu.AddItemMenu import AddItemMenu
from subMenu.AddPerson import AddPerson
from Person import Person
from Tab import Tab
from Item import Item

class App(customtkinter.CTk):
    WIDTH = 900
    HEIGHT = 650

    BTN_COLOR = "#d1d5d8"
    BTN_HOVER = "#8e8d8e"
    def __init__(self):
        super().__init__()
        self.people = []
        self.items = []
        self.tabs = []

        self.title("Main Test")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        customtkinter.set_appearance_mode("Light")

        # setting column and row weight
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        frameLeft = customtkinter.CTkFrame(self, width = 180, corner_radius = 0)
        frameLeft.grid(row = 0, column = 0, sticky = "nswe")

        # Creating a notebook
        self.notebook = ttk.Notebook(self)

        frameMain = customtkinter.CTkFrame(self.notebook, width=450, corner_radius=7)
        frameMain.grid(row=0, column=1, sticky="nswe", padx=15, pady=15)
        frameMain.grid_columnconfigure(0, weight=1)
        frameMain.grid_rowconfigure(0, weight=1)

        self.notebook.add(frameMain, text = "Main")

        self.notebook.grid(row = 0, column = 1, sticky = "nswe", padx = 20, pady = 10)

        #Treeview
        self.itemTree = ttk.Treeview(frameMain, selectmode = "browse")
        self.itemTree["columns"] = ["item", "quantity", "price"]
        ttk.Style().configure("TreeviewItem", rowheight = 30)

        # formatting column
        self.itemTree.column("#0", width=0, stretch=NO)
        self.itemTree.column("item", anchor=W, width=120)
        self.itemTree.column("quantity", anchor=E, width=70)
        self.itemTree.column("price", anchor=E, width=70)

        # Treeview headings
        self.itemTree.heading("#0", text="", anchor=W)
        self.itemTree.heading("item", text="Item", anchor=W)
        self.itemTree.heading("quantity", text="Quantity", anchor=E)
        self.itemTree.heading("price", text="Total Price", anchor=E)

        # Grid the Tree
        self.itemTree.grid(row = 0, column = 0, sticky = "nswe", padx = 10, pady = 10)
        self.itemTree.insert(parent = "", index = "end", iid = 0, values = ("name", "qu", "p"))

        # Add person
        self.buttonInsert = customtkinter.CTkButton(frameLeft, text = "Add Person", command = self.addPersonWindow,
                                                    fg_color=self.BTN_COLOR, hover_color=self.BTN_HOVER,
                                                    corner_radius=0, height=35)
        self.buttonInsert.grid(row = 0, column = 0, padx = 0, pady = (16,0))

        # Add Item
        self.buttonAdd = customtkinter.CTkButton(frameLeft, text="Add Item", command = self.addItemWindow,
                                                 fg_color=self.BTN_COLOR,
                                                 hover_color=self.BTN_HOVER, corner_radius=0, height=35)
        self.buttonAdd.grid(row=1, column=0, padx=0, pady=0)

        # Remove Item
        self.buttonRemove = customtkinter.CTkButton(frameLeft, text="Remove Item", command=None,
                                                    fg_color=self.BTN_COLOR, hover_color=self.BTN_HOVER,
                                                    corner_radius=0, height=35)
        self.buttonRemove.grid(row=2, column=0, padx=0, pady=0)

        # Remove All
        self.buttonRemoveAll = customtkinter.CTkButton(frameLeft, text="Remove All", command=None,
                                                       fg_color=self.BTN_COLOR, hover_color=self.BTN_HOVER,
                                                       corner_radius=0, height=35)
        self.buttonRemoveAll.grid(row=3, column=0, padx=0, pady=0)

        # Scan Receipt
        self.buttonScan = customtkinter.CTkButton(frameLeft, text="Scan Receipt", command=None,
                                                  fg_color=self.BTN_COLOR, hover_color=self.BTN_HOVER,
                                                  corner_radius=0, height=35)
        self.buttonScan.grid(row=4, column=0, padx=0, pady=0)

    def add_tab(self, name):
        self.tabs.append(Tab(self, name))

    def addItemWindow(self):
        self.addItemWindow = AddItemMenu(self, self.people)

        #itm = self.addItemWindow.getItem()
        #print(f"{itm.getName()}{itm.getPrice()}{itm.getQuantity()}")
        #print(itm.getPeople())

    def addPersonWindow(self):
        self.addPerson = AddPerson(self)

    def on_closing(self):
        self.destroy()

