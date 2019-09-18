def main():
    k = ['s', 's', 's', 'u', 'u']
    count = 0
    while k[count] == 's':
        count += 1
        if k[count] != 's':
            k = new_list(k, count)
    print(k)
    return k


main()

