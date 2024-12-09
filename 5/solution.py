from collections import defaultdict

class Solution:
    def __init__(self) -> None:
        file = open(r"input.txt", "r")
        self.input = file.read()
        file.close()
        self.sect1, self.sect2 = self.input.split("\n\n")
        self.sect1 = self.sect1.split('\n')
        self.sect2 = self.sect2.split('\n')
        self.maps = defaultdict(set)

        for ss1 in self.sect1:
            b, a = ss1.split('|')
            self.maps[b].add(a)
    
    def part1(self):
        ans = 0
            
        for ss in self.sect2:
            temp = ss.split(",")    
            
            ans += int(self.helper1(temp, self.maps))

        return ans
    
    def helper1(self, arr, maps):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] not in maps[arr[i]]:
                    return 0
        
        return arr[len(arr)//2]

    def part2(self):
        ans = 0

        for ss in self.sect2:
            temp = ss.split(",")    
            
            ans += int(self.helper2(temp, self.maps))
            
        return ans

    def helper2(self, arr, maps):
        incorrect = False
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] not in maps[arr[i]]:
                    incorrect = True
                    arr[j], arr[i] = arr[i], arr[j]
        
        return arr[len(arr)//2] if incorrect else "0"

if __name__ == "__main__":
    solution = Solution()

    print(solution.part1())
    print(solution.part2())