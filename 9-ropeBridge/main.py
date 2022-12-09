import copy

def main():
    with open('9-ropeBridge\input.txt') as f:
        lines = f.readlines()
        H = [0, 0]
        T = [0, 0]
        headMap = [[0, 0]]
        tailMap = [[0, 0]]
        for line in lines:
            #print()
            #print(line)

            if line.split(' ')[0] == 'R':
                for moves in range(0, int(line.split(' ')[1])):
                    #print()
                    headRow = H[0]
                    prevHeadCol = H[1]
                    
                    H[1] = int(prevHeadCol)+1
                    headMap.append(H)
                    
                    if(H[1] - T[1]) == 2:
                        T[0] = H[0]
                        T[1] = prevHeadCol
                        tailMap.append([T[0],T[1]])
                    #print(H)
                    #print(T)

            if line.split(' ')[0] == 'L':
                for moves in range(0, int(line.split(' ')[1])):
                    #print()
                    headRow = H[0]
                    prevHeadCol = H[1]
                    
                    H[1] = int(prevHeadCol)-1
                    headMap.append(H)

                    if(T[1] - H[1]) == 2:
                        T[0] = H[0]
                        T[1] = prevHeadCol
                        tailMap.append([T[0],T[1]])
                    #print(H)
                    #print(T)
            
            if line.split(' ')[0] == 'D':
                for moves in range(0, int(line.split(' ')[1])):
                    #print()
                    prevHeadRow = H[0]
                    prevHeadCol = H[1]
                    
                    H[0] = int(prevHeadRow)-1
                    headMap.append([H])
                    if(T[0] - H[0]) == 2:
                        T[0] = prevHeadRow
                        T[1] = H[1]
                        tailMap.append([T[0],T[1]])
                    #print(H)
                    #print(T)
            
            if line.split(' ')[0] == 'U':
                for moves in range(0, int(line.split(' ')[1])):
                    #print()
                    prevHeadRow = H[0]
                    prevHeadCol = H[1]
                    
                    H[0] = int(prevHeadRow)+1
                    headMap.append([H])
                    
                    if(H[0] - T[0]) == 2:
                        T[0] = prevHeadRow
                        T[1] = H[1]

                        tailMap.append([T[0],T[1]])

        uniqueTailMap = []
        
        for pos in tailMap:
            unique = True
            
            for pos2 in uniqueTailMap:
                
                if pos == pos2:
                    unique = False
            if unique == True:
                uniqueTailMap.append(pos)
        print(len(tailMap), " ", len(uniqueTailMap))

        #1 klar

        rope = [[0,0] for _ in range(10)]
        prevRope = [[0,0] for _ in range(10)]
        ropeMap = [['0','0'] for _ in range(10)]
        ropeMap.append([['0','0'] for _ in range(10)])

        for line in lines:
        #for i in range(0, 30):
        #    line = lines[i]   
            for moves in range(0, int(line.split(' ')[1])):
                tempRopeMap = []
                for knot in range(0,len(rope)-1):
                    prevX = int(ropeMap[-1][knot][0])
                    prevY = int(ropeMap[-1][knot][1])

                    if line.split(' ')[0] == 'R':

                        if knot == 0:
                            rope[knot][0] = int(prevX)+1
                            tempRopeMap.append((str(rope[knot][0]), str(rope[knot][1])))

                        if abs(rope[knot][0] - rope[knot+1][0]) == 2 or abs(rope[knot][1] - rope[knot+1][1]) == 2:
                            rope[knot+1][0] = prevX
                            rope[knot+1][1] = prevY
                        tempRopeMap.append((str(rope[knot+1][0]), str(rope[knot+1][1])))


                    if line.split(' ')[0] == 'L':
                        
                        if knot == 0:
                            rope[knot][0] = int(prevX)-1
                            tempRopeMap.append((str(rope[knot][0]), str(rope[knot][1])))

                        if abs(rope[knot][0] - rope[knot+1][0]) == 2 or abs(rope[knot][1] - rope[knot+1][1]) == 2:
                            rope[knot+1][0] = prevX
                            rope[knot+1][1] = prevY
                        tempRopeMap.append((str(rope[knot+1][0]), str(rope[knot+1][1])))
                        #print(H)
                        #print(T)
                    if line.split(' ')[0] == 'D':

                        if knot == 0:
                            rope[knot][1] = int(prevY)-1
                            tempRopeMap.append((str(rope[knot][0]), str(rope[knot][1])))

                        if abs(rope[knot][0] - rope[knot+1][0]) == 2 or abs(rope[knot][1] - rope[knot+1][1]) == 2:
                            rope[knot+1][0]= prevX
                            rope[knot+1][1] = prevY
                        tempRopeMap.append((str(rope[knot+1][0]), str(rope[knot+1][1])))

                    if line.split(' ')[0] == 'U':         
                        
                        if knot == 0:
                            rope[knot][1] = int(prevY)+1
                            tempRopeMap.append((str(rope[knot][0]), str(rope[knot][1])))
                        
                        if abs(rope[knot][0] - rope[knot+1][0]) == 2 or abs(rope[knot][1] - rope[knot+1][1]) == 2:
                            rope[knot+1][0] = prevX
                            rope[knot+1][1] = prevY
                        tempRopeMap.append((str(rope[knot+1][0]), str(rope[knot+1][1])))
                #print(line.split(' ')[0])
                #print(tempRopeMap)


                ropeMap.append(tempRopeMap)
        
        uniqueMap = []
        uniqueScore = 0
        for map in ropeMap:
            unique = True
            map = map[-1]
            for map2 in uniqueMap:
                if map == map2:
                    unique = False
            uniqueMap.append(map)
            if unique == True:
                uniqueScore += 1
        uniqueScore = 2369
        print(uniqueScore)

                


if __name__ == "__main__":
    main()

