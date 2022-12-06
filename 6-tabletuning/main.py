def main():
    with open('6-tabletuning\input.txt') as f:
        lines = f.readlines()
        for i in range(0,len(lines[0])):
            found = True
            letters = []
            for x in range(0,14):
                letters.append(lines[0][i+x])
            items = []
            for item in letters:
                for item2 in items:
                    if item2 == item:
                        found = False
                items.append(item)
            if found == True:
                print(i+14)
                print(letters)
                break

if __name__ == "__main__":
    main()