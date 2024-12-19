import argparse
import re

class Solution:
    def __init__(self, testing: False) -> None:
        namefile = ""
        if testing:
            namefile = r"input-test.txt"
        else:
            namefile = r"input.txt"
        file = open(namefile, "r")
        input = file.read()
        file.close()
        self.arr = input.split('\n\n')
        pattern = r"(\d+)\D*(\d+)"
        for i in range(len(self.arr)):
            temp = re.findall(pattern, self.arr[i])
            arr = []
            for j in range(3):
                arr.append([int(temp[j][0]), int(temp[j][1])])
            self.arr[i] = arr
        
    def part1(self) -> int:
        ans = 0
        for i in range(len(self.arr)):
            ans += (self.helper(self.arr[i][0], self.arr[i][1], self.arr[i][2], False))
        return ans
    
    def part2(self) -> int:   
        ans = 0
        for i in range(len(self.arr)):
            ans += (self.helper(self.arr[i][0], self.arr[i][1], self.arr[i][2], True))
            
        return ans

    def helper(self, a, b, target, partTwo: bool):
        if partTwo:
            target[0] += 10000000000000
            target[1] += 10000000000000
        
        # Formula for find two var from two equations
        # a[0]x + b[0]y = target[0] 
        # a[1]x + b[1]y = target[1]
        # x = (target[0] - b[0]y) // a[0]
        # y = (target[1] - a[1]x) // b[1]
        # y = (target[1] - a[1] * (target[0] - b[0]y) // a[0]) //b[1]
        # b[1]y = (target[1] *  a[0] - a[1] * target[0] + a[1] * b[0]y) // a[0]
        # a[0]b[1]y = target[1]a[0] - a[1]target[0] + a[1]b[0]y
        # y = (target[1] * a[0] - a[1] * target[0]) // (a[0] * b[1] - a[1] * b[0])

        mod = (target[1] * a[0] - a[1] * target[0]) % (a[0] * b[1] - a[1] * b[0])
        if mod != 0:
            return 0

        y = (target[1] * a[0] - a[1] * target[0]) // (a[0] * b[1] - a[1] * b[0])
        if (target[0] - b[0] * y) % a[0] != 0:
            return 0
            
        x = (target[0] - b[0] * y) // a[0]
        return x * 3 + y

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Set a test flag')
    args = parser.parse_args()
    
    solution = Solution(args.test)

    print(solution.part1())
    print(solution.part2())
