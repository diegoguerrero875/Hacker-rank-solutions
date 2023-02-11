#from hacker rank problem jumping on the clouds
def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    u = 0
    visited = set()
    while u not in visited:
        visited.add(u)
        u = (u + k) % n
        e -= 1 + (c[u] * 2)
    return e
