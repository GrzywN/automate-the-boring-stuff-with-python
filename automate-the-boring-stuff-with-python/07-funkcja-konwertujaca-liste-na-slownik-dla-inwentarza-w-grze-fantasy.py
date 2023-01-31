def display_inventory(inventory):
    print("Inwentarz:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v

    print(f"Całkowita liczba przedmiotów: {str(item_total)}")


def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


if __name__ == "__main__":
    inv = {'złote monety': 42, 'lina': 1}
    dragon_loot = ['złote monety', 'sztylet', 'złote monety', 'złote monety', 'ruby']
    add_to_inventory(inv, dragon_loot)
    display_inventory(inv)
