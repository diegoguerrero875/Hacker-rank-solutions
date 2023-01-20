#hacker rank solution for Between two sets
def getTotalX(a, b):
    count = 0
    for i in range(1, max(b)+1):
        factor_of_all = True
        for num1 in a:
            if i % num1 != 0:
                factor_of_all = False
                break
        if factor_of_all:
            for num2 in b:
                if num2 % i != 0:
                    factor_of_all = False
                    break
            if factor_of_all:
                count += 1
    return count
