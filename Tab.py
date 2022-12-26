import tkinter

import customtkinter
from tkinter import ttk
from tkinter import *


class Tab:
    def __init__(self, master, name):
        self.master = master
        self.name = name

        self.frame = customtkinter.CTkFrame(self.master.notebook, width=450, corner_radius=5)
        self.frame.grid(row=0, column=0, sticky="nswe", padx=15, pady=(15, 5))
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        self.master.notebook.add(self.frame, text=name)
        self.master.notebook.update()

        self.tree = ttk.Treeview(self.frame, selectmode="browse")
        self.tree["columns"] = ["item", "quantity", "price"]
        ttk.Style().configure("TreeviewItem", rowheight=30)

        # formatting column
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("item", anchor=W, width=120)
        self.tree.column("quantity", anchor=E, width=70)
        self.tree.column("price", anchor=E, width=70)

        # Treeview headings
        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("item", text="Item", anchor=W)
        self.tree.heading("quantity", text="Quantity", anchor=E)
        self.tree.heading("price", text="Total Price", anchor=E)

        self.tree.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        # Stats
        self.frameStat = customtkinter.CTkFrame(self.frame, width=450, corner_radius=5, height=50)
        self.frameStat.grid(row=1, column=0, sticky="nswe", padx=10, pady=(5, 15))

        # Number of items
        self.numLabelVar = tkinter.StringVar()
        self.numLabelVar.set("Items: 0")
        self.numLabel = customtkinter.CTkLabel(self.frameStat, textvariable=self.numLabelVar, corner_radius=5,
                                               anchor="w")
        self.numLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # Total Price
        self.priceLabelVar = tkinter.StringVar()
        self.priceLabelVar.set("Price: $0.00")
        self.priceLabel = customtkinter.CTkLabel(self.frameStat, textvariable=self.priceLabelVar, corner_radius=5,
                                                 anchor="w")
        self.priceLabel.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        # Sales Tax
        self.taxLabelVar = tkinter.StringVar()

        # Sets text variable
        if len(self.master.taxEntry.get()) == 0:
            var = "Tax: 0.00%"
        else:
            var = f"Tax: {self.master.taxEntry.get()}"
        self.taxLabelVar.set(var)

        self.frameStat.columnconfigure(0, weight=1)
        self.frameStat.columnconfigure(1, weight=1)
        self.frameStat.columnconfigure(2, weight=12)
        self.frameStat.columnconfigure(3, weight=1)

        self.taxLabel = customtkinter.CTkLabel(self.frameStat, textvariable=self.taxLabelVar, anchor="e")
        self.taxLabel.grid(row=0, column=3, sticky="e", padx=15, pady=5)

    def getFrame(self):
        return self.frame

    def getName(self):
        return self.name

    def updateStat(self):
        pass
