from collections import defaultdict

class Solution:
    def __init__(self) -> None:
        file = open(r"input.txt", "r")
        self.input = file.read()
        file.close()
        self.map = self.input.split("\n")
        
        for i in range(len(self.map)):
            self.map[i] = list(self.map[i])
            
        self.direction = [[0,1], [1,0], [0,-1], [-1,0]]
    
    def part1(self):
        sets = set()
        i, j, dir = self.getInitPosition(self.map)
        while 0 <= i < len(self.map) and 0 <= j < len(self.map[0]):
            if self.map[i][j] == "#":
                i -= self.direction[dir][0]
                j -= self.direction[dir][1]
                dir = (dir + 1) % 4
                continue
                
            sets.add((i, j))

            i += self.direction[dir][0]
            j += self.direction[dir][1]

        return len(sets)

    def getInitPosition(self, arr):
        m, n = len(arr), len(arr[0])
        dir = [">", "v", "<", "^"]
        for i in range(m):
            for j in range(n):
                for k in range(len(dir)):
                    if arr[i][j] == dir[k]:
                        return [i, j, k]

    def part2(self):
        ans = 0
        sets = set()
        i, j, dir = self.getInitPosition(self.map)
        while 0 <= i < len(self.map) and 0 <= j < len(self.map[0]):
            if self.map[i][j] == "#":
                i -= self.direction[dir][0]
                j -= self.direction[dir][1]
                dir = (dir + 1) % 4
                continue
                
            sets.add((i, j))

            i += self.direction[dir][0]
            j += self.direction[dir][1]        

        i, j, dir = self.getInitPosition(self.map)
        for si, sj in sets:
            if si == i and sj == j:
                continue
            self.map[si][sj] = "#"
            ans += self.helper2(self.map, i, j, dir)
            self.map[si][sj] = "."
            # break
            
        return ans
    
    def helper2(self, arr, i, j, dir):
        sets = set()
        while 0 <= i < len(arr) and 0 <= j < len(arr[0]):
            if arr[i][j] == "#":
                i -= self.direction[dir][0]
                j -= self.direction[dir][1]
                dir = (dir + 1) % 4
                continue
            
            if (i, j, self.direction[dir][0], self.direction[dir][1]) in sets:
                sets.clear()
                return 1
            
            sets.add((i, j, self.direction[dir][0], self.direction[dir][1]))

            i += self.direction[dir][0]
            j += self.direction[dir][1]
        
        return 0


if __name__ == "__main__":
    solution = Solution()

    print(solution.part1())
    print(solution.part2())