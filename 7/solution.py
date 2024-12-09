import argparse

class Solution:
    def __init__(self, testing: False) -> None:
        namefile = ""
        if testing:
            namefile = r"input-test.txt"
        else:
            namefile = r"input.txt"
        file = open(namefile, "r")
        self.input = file.read()
        file.close()
        self.arr = self.input.split("\n")
    
    def part1(self):
        ans = 0
        for i in range(len(self.arr)):
            arr: list[str] = self.arr[i].split(":")
            total = int(arr[0])
            eq = list(map(int, arr[1].strip().split(" ")))
            
            if self.dfs1(total, eq, 0, eq[0]):
                ans += total
                
        return ans
    
    def dfs1(self, total, equation, idx, sums):
        if sums == total and idx == len(equation) - 1:
            return True
        if sums > total or idx >= len(equation) - 1:
            return False
        
        if self.dfs1(total, equation, idx + 1, sums + equation[idx + 1]) or self.dfs1(total, equation, idx + 1, sums * equation[idx + 1]):
            return True

        return False

    def part2(self):
        ans = 0
        for i in range(len(self.arr)):
            arr: list[str] = self.arr[i].split(":")
            total = int(arr[0])
            eq = arr[1].strip().split(" ")
            
            if self.dfs2(total, eq, 0, int(eq[0])):
                ans += total
                
        return ans

    def dfs2(self, total, equation, idx, sums):
        if sums == total and idx == len(equation) - 1:
            return True
        if sums > total or idx >= len(equation) - 1:
            return False
        
        if (
            self.dfs2(total, equation, idx + 1, sums + int(equation[idx + 1])) or 
            self.dfs2(total, equation, idx + 1, sums * int(equation[idx + 1])) or 
            self.dfs2(total, equation, idx + 1, int(str(sums) + equation[idx + 1]))
            ):
            return True

        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Set a flag')
    args = parser.parse_args()
    
    solution = Solution(args.test)

    print(solution.part1())
    print(solution.part2())

# 1399219271639
# 1399219272963
# 1399219271639