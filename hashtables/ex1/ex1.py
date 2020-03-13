#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for data in range(0, length):
        hash_table_insert(ht, weights[data], data)

    for data in range(0, length):
        difference = limit - weights[data]
        result_difference = hash_table_retrieve(ht, difference)
        if result_difference is not None:
            return (result_difference, data)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
