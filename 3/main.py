
def main():
    with open('3\input.txt') as f:
        lines = f.readlines()
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        score = 0
        for i in lines:
            halfList = int(len(i)/2)
            point = False
            for first in i[:halfList]:
                for second in i[halfList:]:
                    if first == second and point == False:
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