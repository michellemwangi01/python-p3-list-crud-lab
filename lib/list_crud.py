def create_an_empty_list():
    return list()

def create_a_list():
    my_new_list = [12,23,45,45]
    return my_new_list

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0,element)
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]

print(remove_element_from_start_of_list([1,2,3,4,5,6,6]))
# # APPEND()
# numbers = [21, 34, 54, 12]
# print("Before append ", numbers)
# numbers.append(100)
# print("After append ", numbers)
#
# # EXTEND()
# numbers.extend(['a', 'b', 'c', 'd', 'e'])
# print("Extended numbers", numbers)
#
# # INSERT()
# numbers.insert(0, 29)
# print("Inserted numbers", numbers)
#
# # == remove elements to a list ==
# # DEL()
# # Can remove a range of elements as opposed to  a single element
# del (numbers[7:])
# print("without deleted numbers", numbers)
#
# # REMOVE()
# # used to remove elements when we don't have or know their index'
# numbers.remove(100)
# print("without removed numbers", numbers)
#
# # POP()
# # removes items from the end of the list
# numbers.pop()
# print("After popping last number", numbers)
# # also accepts a single parameter which is the index of the element we want to remove.
# numbers.pop(2)
# print("After popping specific index number", numbers)