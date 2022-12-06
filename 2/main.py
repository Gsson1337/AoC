
def main():
    with open('2\input.txt') as f:
        lines = f.readlines()
        myTotal = 0
        for line in lines:
            RoPaSi = line.split()
            if RoPaSi[1] == 'X':
                myTotal += 0
                if RoPaSi[0] == 'A':
                    myTotal += 3
                elif RoPaSi[0] == 'B':
                    myTotal += 1
                elif RoPaSi[0] == 'C':
                    myTotal += 2

            if RoPaSi[1] == 'Y':
                myTotal += 3
                if RoPaSi[0] == 'A':
                    myTotal += 1
                elif RoPaSi[0] == 'B':
                    myTotal += 2
                elif RoPaSi[0] == 'C':
                    myTotal += 3

            if RoPaSi[1] == 'Z':
                myTotal += 6
                if RoPaSi[0] == 'A':
                    myTotal += 2
                elif RoPaSi[0] == 'B':
                    myTotal += 3
                elif RoPaSi[0] == 'C':
                    myTotal += 1
        print(myTotal)
        



if __name__ == "__main__":
    main()