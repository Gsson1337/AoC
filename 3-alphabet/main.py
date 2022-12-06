def main():
    with open('3-alphabet\input.txt') as f:
        lines = f.readlines()
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        score = 0
        threeLines = [lines[i:i+3] for i in range(0, len(lines), 3)]
        for i in threeLines:
            point = False
            for first in i[0]:
                for second in i[1]:
                    for third in i [2]:

                        if first == second and first == third and point == False:
                            point = True
                            try: 
                                alphabet.index(first)
                                print(alphabet.index(first) +1)
                                score += alphabet.index(first) +1

                            except: 
                                alphabet.index(first.lower())
                                print(26 + alphabet.index(first.lower()) +1)
                                score += 26 + alphabet.index(first.lower()) +1
        print(score)



if __name__ == "__main__":
    main()