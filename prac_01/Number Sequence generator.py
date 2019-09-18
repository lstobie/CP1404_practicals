def num_seq_generator():
    x = int(input("from:"))
    y = int(input("to:"))
    series = []
    choice = input("""(E)vens, (O)dds, (S)quares, (Q)uit
    """).upper()
    while choice != 'Q':
        for i in range(x, y + 1):
            if choice == 'E':
                k = i % 2
                if k == 0:
                    series.append(i)
            elif choice == 'O':
                k = i % 2
                if k == 1:
                    series.append(i)
            elif choice == 'S':
                series.append(i ^ 2)
        print(series)
        choice = 'Q'


num_seq_generator()
