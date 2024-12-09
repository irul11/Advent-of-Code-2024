def solution():
    ans = 0

    while True:
        inp = input()

        if inp == "":
            break
        
        curr = list(map(int, inp.split()))
        for i in range(len(curr)):
            temp = helper(curr[:i] + curr[i+1:])
            if temp == 1:
                break
        ans += temp

    return ans
    
def helper(arr):
    if len(arr) <= 1:
        return 1

    isinc = arr[1] - arr[0] > 0
    for i in range(1, len(arr)):
        if not(isinc ^ (arr[i] - arr[i-1] > 0)) and 1 <= abs(arr[i] - arr[i - 1]) <= 3:
            pass
        else:
            return 0

    return 1


if __name__ == '__main__':
    print(solution())
