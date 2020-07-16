"""Randomly pick customer and print customer info"""

from customers import Customer
from customers import get_customers_from_file
import random


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)

    print("Tell {name} at {email} that they've won!".format(
        name=chosen_customer.name,
        email=chosen_customer.email
    ))


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)


run_raffle()
