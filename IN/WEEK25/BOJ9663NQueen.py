N = int(input())

def Nqueen(num, collist, rulist, rdlist):
    if num == N:
        return 1
    ans = 0
    for i in range(N):
        if collist[i] and rulist[num+i] and rdlist[i-num+N]:
            collist[i] = 0
            rulist[num+i] = 0
            rdlist[i-num+N] = 0
            ans += Nqueen(num+1, collist, rulist, rdlist)
            collist[i] = 1
            rulist[num+i] = 1
            rdlist[i-num+N] = 1
    return ans

print(Nqueen(0, [1]*N, [1]*(2*N-1), [1]*(2*N)))