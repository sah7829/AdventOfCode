"""
author: Skyler H.
file: day1.py
File for the first day of Advent of Code
Finds calibrations values in text string
"""
numDict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
def trebuchet():
    with open("input.txt", "r") as f:
        file = f.readlines()
        total = 0
        for line in file:
            num1 = (None, None)
            num2 = (None, None)
            i = 0
            while i < len(line) and (num1 == (None, None) or num2 == (None, None)):
                if line[i].isdigit() and num1 == (None, None):
                    num1 = (line[i], i)
                i += 1
                if line[-i].isdigit() and num2 == (None, None):
                    num2 = (line[-i], len(line) - i)

            for number in numDict:
                first_index = line.find(number)
                last_index = line.rfind(number)
                if first_index != -1:
                    if num1 != (None, None) and num2 != (None, None):
                        if first_index < num1[1]:
                            num1 = (numDict[number], first_index)
                        if last_index > num2[1]:
                            num2 = (numDict[number], last_index)
                    else:
                        if num1 == (None, None):
                            num1 = (numDict[number], first_index)
                        if num1 is not None and num2 == (None, None):
                            num2 = (numDict[number], last_index)
            if num1 == (None, None):
                num1 = num2
            elif num2 == (None, None):
                num2 = num1
            
            total += int(num1[0] + num2[0])
        print(total)

def main():
    trebuchet()

if __name__ == "__main__":
    main()