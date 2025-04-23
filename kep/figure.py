def p1(i,j,n,m):
    return i == j or i == 0 or j == m-1

def p2(i,j,n,m):
    return i in (0,n-1) or j in (0,m-1) or i==j or i+j==m-1

def p3(i,j,n,m):
    return (i==j or i+j==m-1) or j in (0,m-1)

def p4(i,j,n,m):
    return i in (0,n-1) or j in (0,m-1) or i+j==m-1

def p5(i,j,n,m):
    return i in (0,n-1) or j in (0,m-1) or i==j

def p6(i,j,n,m):
    return j==0 or i+j==m-1 or j==m-1

def p7(i,j,n,m):
    return i==j or i==n-1 or j==0

def p8(i,j,n,m):
    return i+j==m-1 or i==n-1 or j==m-1

def p9(i,j,n,m):
    return i==0 or j in (0,m-1)

def p10(i,j,n,m):
    return j <= i

def p11(i,j,n,m):
    return i == 0 or j >= i

def p12(i,j,n,m):
    return j >= m-1 - i

def p13(i,j,n,m):
    return i==0 or j <= n-1 - i

def p14(i,j,n,m):
    return j >= min(i, m-1-i) and j <= max(i, m-1-i)

def p15(i,j,n,m):
    lo = min(i, m-1-i)
    hi = max(i, m-1-i)
    return not (j >= lo and j <= hi)

patterns = [None, p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]

def draw(pattern, n=15, m=15):
    fn = patterns[pattern]
    for i in range(n):
        print("".join('*' if fn(i,j,n,m) else ' ' for j in range(m)))

for p in range(1,len(patterns)):
    print(f"\nФігура {p}")
    draw(p)
