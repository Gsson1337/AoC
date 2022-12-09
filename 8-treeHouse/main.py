def main():
    with open('8-treeHouse\input.txt') as f:
        lines = f.readlines()
        trees = []
        for line in lines:
            row = []
            for tree in line:
                row.append(tree)
            trees.append(row)
        visible = 0
        maximumSeeTrees = 0
        
        for row in range(0, len(trees)):
            for col in range(0, len(trees[0])-1):

                introw = int(row)
                intcol = int(col)

                lookLeft = intcol -1
                lookRight = intcol +1
                lookUp = introw -1
                lookDown = introw +1

                left = False
                right = False
                up = False
                down = False
                seeTrees = 0
                totalSeeTrees = 1

                while(left == False and lookLeft > -1):
                    seeTrees += 1
                    if(int(trees[introw][lookLeft]) >= int(trees[introw][intcol]) ):
                        left = True
                    lookLeft -= 1
                totalSeeTrees *= seeTrees 
                seeTrees = 0

                while(right == False and lookRight < len(trees)):
                    seeTrees += 1
                    if(int(trees[introw][lookRight]) >= int(trees[introw][intcol]) ):
                        right = True
                    lookRight += 1
                totalSeeTrees *= seeTrees 
                seeTrees = 0

                while(up == False and lookUp > -1):
                    seeTrees += 1
                    if(int(trees[lookUp][intcol]) >= int(trees[introw][intcol]) ):
                        up = True
                    lookUp -= 1
                totalSeeTrees *= seeTrees 
                seeTrees = 0
                
                while(down == False and lookDown < len(trees) ):
                    seeTrees += 1
                    if(int(trees[lookDown][intcol]) >= int(trees[introw][intcol]) ):
                        down = True
                    
                    lookDown += 1
                totalSeeTrees *= seeTrees 
                seeTrees = 0

                if (left == False or right == False or up == False or down == False):
                    visible += 1

                if maximumSeeTrees < totalSeeTrees:
                    maximumSeeTrees = totalSeeTrees

        print(visible)
        #1 klar

        print(maximumSeeTrees)
        #2 klar

if __name__ == "__main__":
    main()