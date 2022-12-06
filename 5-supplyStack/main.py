def main():
    stacks = []
    with open('5-supplyStack\start.txt') as f:
        start= f.readlines()
        for stack in zip(*start):
            try:
                tempStack = []
                if int(stack[-1]) > 0:
                    for item in stack:
                        if item != (" "):
                            tempStack.append(item)
                tempStack.reverse()
                stacks.append(tempStack)
            except:
                None
        
    with open('5-supplyStack\input.txt') as f:
        lines = f.readlines()
        for command in lines:
            command = command.split(" ")
            Move = int(command[1])
            From = int(command[3])
            To = int(command[5])
            for i in range(Move):
                pick = (-Move+i)
                stacks[To-1].append(stacks[From-1][pick])
            for i in range(Move):
                stacks[From-1].pop()
                
    for stack in stacks:
        print(stack)            
if __name__ == "__main__":
    main()