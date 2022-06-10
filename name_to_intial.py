def name_to_intial(name):
    """ Function that takes in first name and returns their intials as strings"""
    name_list = list(name.strip().split())
    for name in name_list:
        return str(name[0] + name[0])

name = 'Sandeep Singh'
print(name_to_intial(name))
