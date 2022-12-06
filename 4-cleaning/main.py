def main():
    with open('4-cleaning\input.txt') as f:
        lines = f.readlines()
        score = 0
        for i in lines:
            print("\nnew group:")
            both = i.split(",")
            print(both)
            first = both[0].split("-")
            second = both[1].split("-")
            print(first[0], "-", first[1], " ",second[0], "-", second[1])
            if ((int(first[0]) >= int(second[0])) and (int(first[0]) <= int(second[1]))):
                score += 1
                print(score)
            elif ((int(first[1]) >= int(second[0])) and (int(first[1]) <= int(second[1]))):
                score += 1
                print(score)
            elif ((int(second[0]) >= int(first[0])) and (int(second[0]) <= int(first[1]))):
                score += 1
                print(score)
            elif ((int(second[1]) >= int(first[0])) and (int(second[1]) <= int(first[1]))):
                score += 1
                print(score)
            """
            elif int(first[0]) < int(second[0]) and int(first[1]) > int(second[1]):
                score += 1
                print(score)
            elif int(first[0]) > int(second[0]) and int(first[1]) < int(second[1]):
                score += 1
                print(score)
            """
        print(score)
            


if __name__ == "__main__":
    main()