def removeItemHelper(master, tab, selection):
    # Getting the item names first
    items = []
    if master.notebook.tab(tab)["text"] == "Main":
        for index in selection:
            # Deletes item for all people
            # Delete item from main
            itemName = master.itemTree.item(index)["values"][0]

            for item in master.items:
                if item.getName() == itemName:
                    master.items.remove(item)
                    break

            # Deletes for everyone
            for people in master.people:
                for item in people.items:
                    if item.getName() == itemName:
                        people.items.remove(item)
                        break

    else:
        # some other tab
        name = master.notebook.tab(tab)["text"]

        for tab in master.tabs:
            if tab.name == name:
                # Finding the person corresponding to the tab name
                for person in master.people:
                    for index in selection:
                        itemName = tab.tree.item(index)["values"][0]

                        if person.getName() == name:
                            # Looping through the item list of the person
                            for item in person.items:
                                if item.name == itemName:
                                    person.items.remove(item)
                                    item.people.remove(person)
                                    break
    updateTreeview(master)


def removeAllHelper(master, tab, selection):
    # Remove every item
    if master.notebook.tab(tab)["text"] == "Main":
        master.items = []

        for person in master.people:
            person.items = []

    else:
        name = master.notebook.tab(tab)["text"]

        # Remove item from person
        for person in master.people:
            if person.getName() == name:
                person.items = []

        # Remove person from item
        for item in master.items:
            for person in item.people:
                if person == name:
                    item.people.remove(person)
    updateTreeview(master)


def updateTreeview(master):
    # Main Tab
    # Deletes everything in the treeview first
    for i in master.itemTree.get_children():
        master.itemTree.delete(i)

    totPrice = 0.0
    for i in master.items:
        if len(i.getPeople()) == 0:
            master.itemTree.insert(parent="",
                                   index="end",
                                   iid=master.items.index(i),
                                   values=(i.getName(), i.getQuantity(), float(i.getPrice())),
                                   tags=("noPeople",))
        else:
            master.itemTree.insert(parent="",
                                   index="end",
                                   iid=master.items.index(i),
                                   values=(i.getName(), i.getQuantity(), float(i.getPrice())))
        totPrice += float(i.getPrice())

    # Calculate tax
    if len(master.taxEntry.get()) == 0:
        taxPercentageFloat = 1
    else:
        taxPercentageFloat = float(master.taxEntry.get().strip("%")) / 100 + 1

    # Update Price
    totPrice *= float("{:.2f}".format(taxPercentageFloat))
    totPrice = float("{:.2f}".format(totPrice))
    master.priceLabelVar.set(f"Price: ${totPrice}")
    # Update item count
    master.numLabelVar.set(f"Items: {len(master.itemTree.get_children())}")

    master.update()

    # Update Price

    # Updates Each Person
    for tab in master.tabs:
        for person in master.people:
            if person.getName() == tab.name:
                # Deletes all entries
                for i in tab.tree.get_children():
                    tab.tree.delete(i)

                # Adds entry according to the items list
                totPrice = 0.0
                for item in person.getItems():
                    tab.tree.insert(parent="", index="end", iid=person.getItems().index(item),
                                    values=(item.getName(), item.getQuantity(), float(item.getPrice())))
                    totPrice += float(item.getPrice())

                # Update Price
                totPrice *= float("{:.2f}".format(taxPercentageFloat))
                totPrice = float("{:.2f}".format(totPrice))
                tab.priceLabelVar.set(f"Price: ${totPrice}")
                # Update item count
                tab.numLabelVar.set(f"Items: {len(tab.tree.get_children())}")

                tab.tree.update()
