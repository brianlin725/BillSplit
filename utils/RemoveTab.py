def removeTabHelper(master, index, name):
    tab = None
    for t in master.tabs:
        if t.name == name:
            tab = t

    # Starts to remove person from every field
    for person in master.people:
        if person.getName() == name:
            master.people.remove(person)

    for item in master.items:
        for person in item.people:
            if person == name:
                item.people.remove(name)
                break

    master.notebook.forget(index)

    if len(master.taxEntry.get()) == 0:
        taxPercentageFloat = 1
    else:
        taxPercentageFloat = float(master.taxEntry.get().strip("%")) / 100 + 1

    # Updating price

    # For main window
    totPrice = 0.0
    for item in master.items:
        totPrice += float("{:.2f}".format(float(item.getPrice())))

    totPrice *= taxPercentageFloat
    master.priceLabelVar.set(f"Price: ${round(totPrice, 2)}")

    # Updating every tab item; This is very ugly, hopefully i would change this soon
    # Finding each person
    for person in master.people:
        # Finding the tab that corresponds to the person
        for t in master.tabs:
            if t.name == person.name:
                # Loop through the tree
                for row in t.tree.get_children():
                    # Looping through the person's items to find the price
                    for item in person.items:
                        if item.name == t.tree.item(row)["values"][0]:
                            name = t.tree.item(row)["values"][0]
                            quantity = t.tree.item(row)["values"][1]

                            # Price is based on how many people share the item
                            price = float("{:.2f}".format(float(item.getPrice()) / len(item.people)))
                            t.tree.item(row, values=(name, quantity, price))
                            break

    # For every tab
    for tab in master.tabs:
        totPrice = 0.0
        for row in tab.tree.get_children():
            totPrice += float(tab.tree.item(row)["values"][2])

        totPrice *= taxPercentageFloat
        tab.priceLabelVar.set(f"Price: $ {round(totPrice, 2)}")

    # Gray out non-claimed items
    for row in master.itemTree.get_children():
        for item in master.items:
            if item.name == master.itemTree.item(row)["values"][0]:
                if len(item.getPeople()) == 0:
                    master.itemTree.item(row, tags=("noPeople",))
                    break

    master.itemTree.update()
