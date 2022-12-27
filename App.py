import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import customtkinter
from subMenu.AddItemMenu import AddItemMenu
from subMenu.AddPerson import AddPerson
from Person import Person
from Tab import Tab
from Item import Item
from utils import RemoveTab, RemoveItem

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

        # binding event
        self.bind("<Delete>", self.delTab)

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
        self.itemTree = ttk.Treeview(frameMain, selectmode = "extended")
        self.itemTree["columns"] = ["item", "quantity", "price"]
        ttk.Style().configure("TreeviewItem", rowheight = 35)

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
        self.itemTree.tag_configure('noPeople', background="#eceeef")

        # Grid the Tree
        self.itemTree.grid(row = 0, column = 0, sticky = "nswe", padx = 10, pady = 10)

        # Scrollbar for the tree
        scrollbar = customtkinter.CTkScrollbar(frameMain, command = self.itemTree.yview, fg_color=self.BTN_COLOR)
        scrollbar.grid(row = 0, column = 1, sticky = "ns")
        self.itemTree.configure(yscrollcommand=scrollbar.set)

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
        self.buttonRemove = customtkinter.CTkButton(frameLeft, text="Remove Item", command=self.delTab,
                                                    fg_color=self.BTN_COLOR, hover_color=self.BTN_HOVER,
                                                    corner_radius=0, height=35)
        self.buttonRemove.grid(row=2, column=0, padx=0, pady=0)

        # Remove All
        self.buttonRemoveAll = customtkinter.CTkButton(frameLeft, text="Remove All", command=self.removeAll,
                                                       fg_color=self.BTN_COLOR, hover_color=self.BTN_HOVER,
                                                       corner_radius=0, height=35)
        self.buttonRemoveAll.grid(row=3, column=0, padx=0, pady=0)

        # Scan Receipt
        self.buttonScan = customtkinter.CTkButton(frameLeft, text="Scan Receipt", command=None,
                                                  fg_color=self.BTN_COLOR, hover_color=self.BTN_HOVER,
                                                  corner_radius=0, height=35)
        self.buttonScan.grid(row=4, column=0, padx=0, pady=0)

        # Stats
        self.frameStat = customtkinter.CTkFrame(frameMain, width=450, corner_radius=5, height=50)
        self.frameStat.grid(row=1, column=0, sticky="nswe", padx=10, pady=(5, 15))

        # Number of items
        self.numLabelVar = tkinter.StringVar()
        self.numLabelVar.set("Items: 0")
        self.numLabel = customtkinter.CTkLabel(self.frameStat, textvariable=self.numLabelVar, corner_radius=5,
                                               anchor = "w")
        self.numLabel.grid(row=0, column=0, sticky="w", padx = 5, pady = 5)

        # Total Price
        self.priceLabelVar = tkinter.StringVar()
        self.priceLabelVar.set("Price: $0.00")
        self.priceLabel = customtkinter.CTkLabel(self.frameStat, textvariable=self.priceLabelVar, corner_radius=5,
                                               anchor="w")
        self.priceLabel.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        # Tax
        self.taxLabel = customtkinter.CTkLabel(self.frameStat, text = "Tax: ", anchor = "e")
        self.taxLabel.grid(row = 0, column = 3, sticky = "e", padx = (5,1), pady = 5)

        self.frameStat.columnconfigure(0, weight=1)
        self.frameStat.columnconfigure(1, weight=1)
        self.frameStat.columnconfigure(2, weight = 12)
        self.frameStat.columnconfigure(3, weight=1)
        self.frameStat.columnconfigure(4, weight=1)
        self.frameStat.columnconfigure(5, weight=1)

        self.taxEntry = customtkinter.CTkEntry(self.frameStat, placeholder_text = 0.00,
                                               placeholder_text_color="#8e8d83",
                                               validate = "key", justify = RIGHT, width = 50)

        self.taxEntry.grid(row = 0, column = 4, sticky = "e", padx = (1,0), pady = 5)
        self.currEntry = self.taxEntry.get()
        self.taxEntry.bind("<KeyRelease>", self.validate)

        percentlabel = customtkinter.CTkLabel(self.frameStat, text= "%", anchor = "w")
        percentlabel.grid(row = 0, column = 5, sticky = "e", padx = (0,5), pady = 5)

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

    def validate(self, e):
        entry = self.taxEntry.get()
        if len(entry) == 0:
            self.updatePrices()
            return
        try:
            float(entry.strip("."))
            self.currEntry = entry
            self.updatePrices()
        except:
            self.taxEntry.delete(0, END)
            self.taxEntry.insert(0, self.currEntry)
            self.updatePrices()

    def updatePrices(self):
        if len(self.taxEntry.get()) == 0:
            taxPercentageFloat = 1
        else:
            taxPercentageFloat = float(self.taxEntry.get().strip("%")) / 100 + 1

        # For main window
        totPrice = 0.0
        for item in self.items:
            totPrice += float("{:.2f}".format(float(item.getPrice())))

        totPrice *= taxPercentageFloat
        self.priceLabelVar.set(f"Price: ${round(totPrice, 2)}")

        # For every tab
        for tab in self.tabs:
            totPrice = 0.0
            for row in tab.tree.get_children():
                totPrice += float(tab.tree.item(row)["values"][2])

            totPrice *= taxPercentageFloat
            tab.priceLabelVar.set(f"Price: $ {round(totPrice, 2)}")

            # update tax
            tab.taxLabelVar.set(f"Tax: {round(float(self.taxEntry.get()),2)}%")

    # Function deletes tab and items according to selections
    def delTab(self, e=None):
        # Finds the current tab
        index = self.notebook.index(self.notebook.select())

        name = self.notebook.tab(self.notebook.select(), "text")
        tree = None

        if index == 0:
            tree = self.itemTree
        else:
            for t in self.tabs:
                if t.name == name:
                    tree = t.tree

        if len(tree.selection()) == 0:
            # Deletes tab
            index = self.notebook.index(self.notebook.select())

            # Check if this is the main tab
            if index == 0:
                return

            # Double check
            response = messagebox.askyesno("info", "Remove person?")
            if response != 1:
                return

            RemoveTab.removeTabHelper(self, index, self.notebook.tab(index)["text"])
        else:
            # Deletes Item
            RemoveItem.removeItemHelper(self, self.notebook.index(self.notebook.select()), self.itemTree.selection())

    def removeAll(self, e = None):
        # Finds the current tab
        index = self.notebook.index(self.notebook.select())

        name = self.notebook.tab(self.notebook.select(), "text")
        tree = None

        if index == 0:
            tree = self.itemTree
        else:
            for t in self.tabs:
                if t.name == name:
                    tree = t.tree

        RemoveItem.removeAllHelper(self, self.notebook.index(self.notebook.select()), self.itemTree.selection())