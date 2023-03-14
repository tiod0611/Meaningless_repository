# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1158n,k= map(int,input().split())
q= [i+1 for i in range(n)]
j=0
ans= []
for i in range(n):
    j+=k-1
    if j>=len(q):
        j%=len(q)
    ans.append(str(q.pop(j)))
print("<",", ".join(ans),">",sep="")