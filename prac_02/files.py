name = input("onamae wa?")
name_file = open("name.txt", 'w')
print("Your name is {}".format(name), file=name_file)
name_file.close()

