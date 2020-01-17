#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
        difference = limit - weights[i]
        result_difference = hash_table_retrieve(ht, difference)
        if result_difference is not None:
            return (result_difference, i)

    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
