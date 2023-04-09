N,K=map(int,input().split())
UP=1
DOWN=1
for i in range(K):
    UP*=(N-i)
    DOWN*=(i+1)
print((UP//DOWN)%10007)