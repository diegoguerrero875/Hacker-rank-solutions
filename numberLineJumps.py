#Number line jump problem on hacker rank
def kangaroo(x1, v1, x2, v2):
    ret = "NO"
    for x in range(10000):
        
        i = x*v1 + x1
        j = x*v2 + x2
        if i == j:
            ret = "YES"

    return ret
