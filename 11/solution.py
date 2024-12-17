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
        self.arr = input.split()
            
    def part1(self):
        return self.helper(25)
    
    def part2(self):
        return self.helper(75)
    
    def helper(self, cycle):   
        from collections import defaultdict

        def blink(stone_counts):
            new_stone_counts = defaultdict(int)
            
            for stone, count in stone_counts.items():
                # Handle the case where the stone is "0"
                if stone == '0':
                    new_stone_counts['1'] += count
                
                elif len(stone) % 2 == 0:
                    mid = len(stone) // 2
                    left = stone[:mid].lstrip("0") or "0"
                    right = stone[mid:].lstrip("0") or "0"
                    
                    new_stone_counts[left] += count
                    new_stone_counts[right] += count
                else:
                    new_stone = str(int(stone) * 2024)
                    new_stone_counts[new_stone] += count
            
            return new_stone_counts

        stone_counts = defaultdict(int)
        for stone in self.arr:
            stone_counts[stone] += 1

        for _ in range(cycle):
            stone_counts = blink(stone_counts)

        return (sum(stone_counts.values()))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Set a test flag')
    args = parser.parse_args()
    
    solution = Solution(args.test)

    print(solution.part1())
    print(solution.part2())