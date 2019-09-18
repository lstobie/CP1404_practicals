import csv


def main():
    with open('movies.csv') as File:
        reader = csv.reader(File)
        for row in reader:
            print(row)


main()
