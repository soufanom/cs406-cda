# Define a function to showcase list operations
def list_operations():
    my_list = [1, 2, 3, 4, 5]
    print("Original List:", my_list)
    my_list.append(6)  # Add an element to the end
    print("After appending 6:", my_list)
    my_list.remove(3)  # Remove the element 3
    print("After removing 3:", my_list)

# Define a function to showcase tuple operations
def tuple_operations():
    my_tuple = (1, 2, 3, 4, 5)
    print("Tuple:", my_tuple)
    # Tuples are immutable, so we can't add or remove elements
    print("Tuple length:", len(my_tuple))
    print("Element at index 2:", my_tuple[2])

# Define a function to showcase set operations
def set_operations():
    my_set = {1, 2, 3, 4, 5}
    print("Original Set:", my_set)
    my_set.add(6)  # Add an element
    print("After adding 6:", my_set)
    my_set.discard(3)  # Remove an element
    print("After discarding 3:", my_set)

# Define a function to showcase dictionary operations
def dictionary_operations():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original Dictionary:", my_dict)
    my_dict['d'] = 4  # Add a new key-value pair
    print("After adding {'d': 4}:", my_dict)
    del my_dict['b']  # Remove key-value pair 'b'
    print("After deleting 'b':", my_dict)
    print("Keys:", list(my_dict.keys()))
    print("Values:", list(my_dict.values()))

# Main function to call the above-defined functions
def main():
    print("List Operations:")
    list_operations()
    print("\nTuple Operations:")
    tuple_operations()
    print("\nSet Operations:")
    set_operations()
    print("\nDictionary Operations:")
    dictionary_operations()

# Call the main function
if __name__ == "__main__":
    main()
