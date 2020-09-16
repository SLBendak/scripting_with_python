rome_file = open('rome.txt', 'a')

numbers = [1,2,3]
for i in range(len(numbers)):
    num = numbers[i]
    rome_file.write("{}\n".format(num))

# write to the file
# rome_file.write('\nHello\n')
rome_file.close()

# read a file
# print(rome_file.read())

# close a file


# If the file isn't found, one will be created
adam_file = open('adam.txt', 'w')
adam_file.write('Adam')
adam_file.close()


# look up how to read lines from a file in python
new_file = open('new_file.txt')
file_items = new_file.readlines()\
# print(file_items)

# new_file.close()
for i in range(len(file_items)):
    each_item = file_items[i]
    print('Before: {}'.format(each_item))
    print(each_item[0:-1])
print(file_items)

new_file.close()
