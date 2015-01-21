phonebook = {
    "John" : 4151234567,
    "Jack" : 4157891234,
    "Jill" : 4151239876
}

phonebook["Jake"] = 938273443
del phonebook["Jill"]
# print phonebook

# cleared_book = phonebook.clear()
# print cleared_book

# copy_book = phonebook.copy()
# print copy_book

new_dict = dict.fromkeys(phonebook)
print new_dict