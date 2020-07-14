"""Print out all the melons in our inventory."""


# from melons import melon_names, melon_seedlessness, melon_prices


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])

# New script

from melons import *


def add_info(inventory, new_category):

    for k in inventory:
        inventory[k].setdefault(new_category, None)

    return inventory

# print(add_info(melon_inventory, 'Define Local'))




def print_melon_new(melon_inventory):

    add_info(melon_inventory, 'Define Local')

    for melon in melon_inventory.items():

        print(f"{melon[0].upper()}")

        for k, v in melon[1].items():
            print(f"     {k}: {melon[1][k]}")

print_melon_new(melon_inventory)


