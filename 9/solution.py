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
    
    def part1(self):
        ans = 0
        curr = 0
        arr = []
        for i in range(len(self.input)):
            if i & 1:
                arr += [-1]*int(self.input[i])
            else:
                arr += [curr]*int(self.input[i])
                curr += 1

        l, r = 0 , len(arr) - 1
        while l < r:
            while l < len(arr) and arr[l] >= 0:
                l += 1
            while r >= 0 and arr[r] < 0:
                r -= 1
            arr[l] = arr[r]
            arr[r] = -1
            r -= 1
            l += 1
        
        for i in range(l+1):
            ans += arr[i] * i
        
        return ans

    def part2(self):        
        ans = 0
        curr = 0
        length = 0

        arr = []
        dots = []
        digs = []

        for i in range(len(self.input)):
            if i & 1:
                arr += [0]*int(self.input[i])
                dots.append([length, length + int(self.input[i])])
            else:
                arr += [curr]*int(self.input[i])
                digs.append([length, length + int(self.input[i])])
                curr += 1
            length += int(self.input[i])

        for i in range(len(digs)-1, -1, -1):
            for j in range(i):
                while digs[i][1] - digs[i][0] > 0 and digs[i][1] - digs[i][0] <= dots[j][1] - dots[j][0]:
                    arr[dots[j][0]] = i
                    arr[digs[i][0]] = 0
                    dots[j][0] += 1
                    digs[i][0] += 1
        
        for i in range(len(arr)):
            ans += arr[i] * i
            
        return ans

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Set a test flag')
    args = parser.parse_args()
    
    solution = Solution(args.test)

    print(solution.part1())
    print(solution.part2())
