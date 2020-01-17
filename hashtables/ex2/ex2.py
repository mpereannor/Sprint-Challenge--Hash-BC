#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for x in range(length):
        ticket = tickets[x]
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    current_index = 0
    ticket_destination = hash_table_retrieve(hashtable, "NONE")
    while True:
        route[current_index] = ticket_destination
        current_index += 1
        ticket_destination = hash_table_retrieve(hashtable, ticket_destination)
        if ticket_destination == "NONE":
            route[current_index] = "NONE"
            break

    return route
