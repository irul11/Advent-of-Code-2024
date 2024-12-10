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
        for i in range(len(self.arr)):
            self.arr[i] = list(self.arr[i])
        
        self.maps: dict[str, list] = dict()
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if self.arr[i][j] == ".":
                    continue
                
                if self.arr[i][j] not in self.maps:
                    self.maps[self.arr[i][j]] = [(i, j)]
                else:
                    self.maps[self.arr[i][j]].append((i, j))
    
    def part1(self):
        sets = set()
        m, n = len(self.arr), len(self.arr[0])
        
        for key in self.maps.keys():
            for i in range(len(self.maps[key])):
                ai, aj = self.maps[key][i]
                for j in range(i + 1, len(self.maps[key])):
                    bi, bj = self.maps[key][j]
                    y, x = bi-ai, bj-aj

                    x1, y1 = bj + x, bi + y
                    x2, y2 = aj - x, ai - y
                    if 0 <= x1 < m and 0 <= y1 < n:
                        sets.add((y1, x1))
                    if 0 <= x2 < m and 0 <= y2 < n:
                        sets.add((y2, x2))
        
        return len(sets)

    def part2(self):
        sets = set()
        m, n = len(self.arr), len(self.arr[0])
        
        for key in self.maps.keys():
            for i in range(len(self.maps[key])):
                ai, aj = self.maps[key][i]
                sets.add((ai, aj))
                for j in range(i + 1, len(self.maps[key])):
                    bi, bj = self.maps[key][j]
                    y, x = bi-ai, bj-aj

                    x1, y1 = bj + x, bi + y
                    x2, y2 = aj - x, ai - y
                    while 0 <= x1 < m and 0 <= y1 < n:
                        sets.add((y1, x1))
                        x1, y1 = x1 + x, y1 + y
                        
                    while 0 <= x2 < m and 0 <= y2 < n:
                        sets.add((y2, x2))
                        x2, y2 = x2 - x, y2 - y
                
        return len(sets)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Set a test flag')
    args = parser.parse_args()
    
    solution = Solution(args.test)

    print(solution.part1())
    print(solution.part2())
