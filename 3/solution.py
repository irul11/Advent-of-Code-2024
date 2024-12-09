def solution1():
    ans = 0

    while True:
        inp = input()
        
        if inp == "":
            break

        import re

        regex = r"mul\(\d+,\d+\)"
        arr = re.findall(regex, inp)
        for a in arr:
            ans += eval(a)        

    return ans

def solution2():
    ans = 0
    enabled = True
    ss = ""
    while True:
        inp = input()
        
        if inp == "":
            break

        ss += inp

    import re
    regex = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
    arr = re.findall(regex, ss)
    for a in arr:
        if a == "do()":
            enabled = True
        elif a == "don't()":
            enabled = False
        elif enabled:
            ans += eval(a)
        
    return ans

def mul(a, b):
    return a * b


if __name__ == '__main__':
    print(solution1())
    print(solution2())
