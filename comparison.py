""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.
    file_object = open(filename)
    file_data = file_object.read().strip().split("\n")
    file_object.close()

    return file_data

    pass


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    # Write your code below.
    fruits_in_common = []

    for fruit in lst1:
        if fruit in lst2:
            fruits_in_common.append(fruit)

    return fruits_in_common        

    pass


# Call your functions at the bottom, after they've been defined.

fruit1_list = open_and_read_file("fruits_1.txt") 
fruit2_list = open_and_read_file("fruits_2.txt")
fruits_in_common = compare(fruit1_list, fruit2_list)
print fruits_in_common
