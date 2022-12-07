def main():
    with open('7-spaceLeft\input.txt') as f:
        lines = f.readlines()
        files = []
        current = []
        for line in lines:
            current = current
            if line.startswith('$ cd') and line.startswith('$ cd ..') == False :
                current.append(line.split(" ")[2])
            elif line.startswith('$ cd ..'): 
                current.pop()
            elif line.startswith('$ ls'):
                None
            elif line.startswith('dir') == False:
                    pathWay = ""
                    for path in current:
                        pathWay += path
                    files.append([pathWay, (line.split(' ')[1], ('file, size = ',line.split(' ')[0],))])
        pathways = []
        score = []

        for file in files:
            add = ""

            for i in range(len(file[0].split('\n'))-1):
                add += file[0].split("\n")[i] + "\n"
                try:
                    newScore = int(score[pathways.index(add)]) + int(file[1][1][1])
                    score[pathways.index(add)] = newScore
                    #print(add.split('\n'))
                except:
                    pathways.append(add)
                    score.append(file[1][1][1])
                    #print(add.split('\n'))
                #print(len(file[0].split('\n'))-1, file[0].split('\n'), " " ,add.split('\n'), " ", pathways.index(add))
                #print(pathways.index(add))

        
        total = 0
        for i in range(0, len(pathways)):
            if int(score[i]) < 100000:
                total += int(score[i])
        print(total)
        
        #1 klar

        minimum = 10000000
        path = 0
        for i in range(0, len(pathways)):
            if ((int(score[0]) - int(score[i])) <= 40000000) and int(score[i]) < minimum:
                minimum = int(score[i])
                path = i

        print(pathways[path].split('\n'), " ", minimum)

        #2 klar
        

if __name__ == "__main__":
    main()