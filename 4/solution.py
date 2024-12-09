class Solution:
    def __init__(self) -> None:
        file = open(r"input.txt", "r")
        self.input = file.read()
        file.close()
        self.input: list[str] = self.input.split("\n")
    
    def part1(self):
        ans = 0
        ss = self.input
        m, n = len(ss), len(ss[0])
        pattern = "XMAS"
        for i in range(m):
            for j in range(n):
                if ss[i][j] != "X":
                    continue
                # north
                if i >= 3 and ss[i][j] + ss[i-1][j] + ss[i-2][j] + ss[i-3][j] == pattern:
                    ans += 1
                
                # north east
                if i >= 3 and j + 3 < n and ss[i][j] + ss[i-1][j+1] + ss[i-2][j+2] + ss[i-3][j+3] == pattern:
                    ans += 1

                # east
                if j + 3 < n and ss[i][j] + ss[i][j+1] + ss[i][j+2] + ss[i][j+3] == pattern:
                    ans += 1

                # south east
                if i + 3 < m and j + 3 < n and ss[i][j] + ss[i+1][j+1] + ss[i+2][j+2] + ss[i+3][j+3] == pattern:
                    ans += 1

                # south
                if i + 3 < m and ss[i][j] + ss[i+1][j] + ss[i+2][j] + ss[i+3][j] == pattern:
                    ans += 1

                # south west
                if i + 3 < m and j >= 3 and ss[i][j] + ss[i+1][j-1] + ss[i+2][j-2] + ss[i+3][j-3] == pattern:
                    ans += 1

                # west
                if j >= 3 and ss[i][j] + ss[i][j-1] + ss[i][j-2] + ss[i][j-3] == pattern:
                    ans += 1

                # north west
                if i >= 3 and j >= 3 and ss[i][j] + ss[i-1][j-1] + ss[i-2][j-2] + ss[i-3][j-3] == pattern:
                    ans += 1

        return ans

    def part2(self):
        ans = 0
        ss = self.input
        m, n = len(ss), len(ss[0])
        pattern = "MAS"
        for i in range(m):
            for j in range(n):
                if i < 1 or j < 1 or i + 1 >= m or j + 1 >= n or ss[i][j] != "A":
                    continue
                if (
                    (ss[i-1][j-1] == "M" and ss[i+1][j+1] == "S") or
                    (ss[i-1][j-1] == "S" and ss[i+1][j+1] == "M")
                ) and (
                    (ss[i+1][j-1] == "M" and ss[i-1][j+1] == "S") or
                    (ss[i+1][j-1] == "S" and ss[i-1][j+1] == "M")
                ):
                    ans += 1

        return ans

solution = Solution()

print(solution.part1())
print(solution.part2())