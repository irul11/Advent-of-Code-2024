import argparse
from collections import deque

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
        self.arr = input.split('\n')
        for i in range(len(self.arr)):
            self.arr[i] = list(self.arr[i])
            
        self.DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
    def part1(self) -> int:
        m, n = len(self.arr), len(self.arr[0])
        ans = 0
        sets = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in sets:
                    self.temp = 0
                    cset = set()
                    ans += self.helper1(i, j, self.arr[i][j], cset) * self.temp
                    sets.update(cset)
            
        return ans
        
    def helper1(self, i: int, j: int, curr: str, sets: set) -> int:
        if i < 0 or i >= len(self.arr) or j < 0 or j >= len(self.arr[0]) or self.arr[i][j] != curr:
            return 1

        if (i, j) in sets:
            return 0
        
        res = 0
        sets.add((i, j))
        self.temp += 1
        bot = self.helper1(i + 1, j, curr, sets)
        top = self.helper1(i - 1, j, curr, sets)
        right = self.helper1(i, j + 1, curr, sets)
        left = self.helper1(i, j - 1, curr, sets)
        res += bot + top + right + left

        return res

    def part2(self) -> int:   
        m, n = len(self.arr), len(self.arr[0])
        ans = 0
        sets = set()

        def count_shared_sides(region: set[tuple[int, int]]) -> int:
            """Count shared sides between points in a grid region."""
            count = 0
            for x, y in region:
                if (x - 1, y) in region:
                    for y2 in [y - 1, y + 1]:
                        if (x, y2) not in region and (x - 1, y2) not in region:
                            count += 1
                if (x, y - 1) in region:
                    for x2 in [x - 1, x + 1]:
                        if (x2, y) not in region and (x2, y - 1) not in region:
                            count += 1
            return count
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in sets:
                    self.temp = 0
                    cset: set[tuple[int, int]] = set()
                    
                    perimeter = self.helper1(i, j, self.arr[i][j], cset)
                    share_sides = count_shared_sides(cset)
                    perimeter -= share_sides
                    ans += self.temp * perimeter
                    sets.update(cset)
            
        return ans
    
    def helper2(self, i: int, j: int, curr: str, sets: set) -> int:
        if i < 0 or i >= len(self.arr) or j < 0 or j >= len(self.arr[0]) or self.arr[i][j] != curr:
            return 1

        if (i, j) in sets:
            return 0
        
        sets.add((i, j))
        self.temp += 1
        bot = self.helper2(i + 1, j, curr, sets)
        top = self.helper2(i - 1, j, curr, sets)
        right = self.helper2(i, j + 1, curr, sets)
        left = self.helper2(i, j - 1, curr, sets)

        if bot + left == 2:
            self.temp2 += 1

        if bot + right == 2:
            self.temp2 += 1
        if top + left == 2:
            self.temp2 += 1
        if top + right == 2:
            self.temp2 += 1

        return 0
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Set a test flag')
    args = parser.parse_args()
    
    solution = Solution(args.test)

    print(solution.part1())
    print(solution.part2())
