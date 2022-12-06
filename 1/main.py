import numpy as np
def main():
    with open('input.txt') as f:
        lines = f.readlines()
        x = 0
        max = [0,0,0]
        current = 0
        for i in lines:
            replaced = False
            if i == "\n":
                if current > min(max):
                    max[max.index(min(max))] = current
                
                current = 0
                x += 1
                print(str(x) + " "+ str(max))
            else:
                current += int(i)
        total = 0
        for i in max:
            total += i
        print(total)
if __name__ == "__main__":
    main()