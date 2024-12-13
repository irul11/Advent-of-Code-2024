import argparse

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
            self.arr[i] = list(map(int, list(self.arr[i])))
            
    def part1(self):
        self.ans2 = 0
        m, n = len(self.arr), len(self.arr[0])

        for i in range(m):
            for j in range(n):
                if self.arr[i][j] == 0:
                    sets = set()
                    self.helper1(i, j, m, n, -1, sets)
                    self.ans2 += len(sets)

        return self.ans2

    def helper1(self, i, j, m, n, prev, sets):
        if i < 0 or i >= m or j < 0 or j >= n or self.arr[i][j] - prev != 1:
            return
        if self.arr[i][j] == 9:
            sets.add((i, j))
        
        self.helper1(i+1, j, m, n, self.arr[i][j], sets)
        self.helper1(i-1, j, m, n, self.arr[i][j], sets)
        self.helper1(i, j+1, m, n, self.arr[i][j], sets)
        self.helper1(i, j-1, m, n, self.arr[i][j], sets)

    def part2(self):        
        self.ans2 = 0
        m, n = len(self.arr), len(self.arr[0])

        for i in range(m):
            for j in range(n):
                if self.arr[i][j] == 0:
                    self.ans2 += self.helper2(i, j, m, n, -1)

        return self.ans2
    
    def helper2(self, i, j, m, n, prev):
        if i < 0 or i >= m or j < 0 or j >= n or self.arr[i][j] - prev != 1:
            return 0
        if self.arr[i][j] == 9:
            return 1
        
        return (
            self.helper2(i+1, j, m, n, self.arr[i][j]) +
            self.helper2(i-1, j, m, n, self.arr[i][j]) +
            self.helper2(i, j+1, m, n, self.arr[i][j]) +
            self.helper2(i, j-1, m, n, self.arr[i][j])
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Set a test flag')
    args = parser.parse_args()
    
    solution = Solution(args.test)

    print(solution.part1())
    print(solution.part2())
