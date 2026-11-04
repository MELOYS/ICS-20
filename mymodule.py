
def prosti(n):
    k = 0
    for i in range(2, n + 1):
        if n % i == 0:
            p = True
            for j in range(2, i):
                if i % j == 0:
                    p = False
                    break
            if p:
                k += 1
    return k

def dilniki(n):
    k = 0
    for i in range(1, n + 1):
        if n % i == 0:
            k += 1
    return k
