for _ in range(int(input())):
    m,n = map(int,input().split())
    st = input()
    while n>0:
        s1 = st[:n]
        st = s1[::-1]+st[n:]
        n-=1
    print(st)