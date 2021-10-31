# Learning lists

# Lists - списки

guests = list()     # create list

guests = ['Parents', 'My Classmates', 'Acquaintances']  # assign a values
print(guests)

guests.remove('Acquaintances')      # delete element
print(guests)

guests.append('Friends')            # add element
print(guests)

guests[1]='Classmates'              #change element
print(guests)

print(guests[1:3])

# tuple - кортежи

my_data = ('Pushkin A.S.', 1799, True)
my_second_data = ('Lermontov M.Y.', 1814, True)
print(my_data)
print(my_data[1])
print('1984' not in my_data)        # check element in tuple

# print(guests + my_data)           - error
print(my_data + my_second_data)     # addition

cityes = ['Moscow', 'St. Petersburg', 'Yekaterinburg']  # enumeration
for city in cityes :
    print(city.replace('o', '0'))   # methods

