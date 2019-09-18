def hello():
    name = input("Name?")
    print("This is a menu")
    choice = input("choice? Q, H, G").upper()
    while choice != 'Q':
        if choice == 'H':
            print("hello", name)
        elif choice == 'G':
            print("goodbye " + str(name))
        else:
            print("oof")
        print("This is a menu")
        choice = input("choice? Q, H, G").upper()
    print("this is a goodbye message")


hello()
