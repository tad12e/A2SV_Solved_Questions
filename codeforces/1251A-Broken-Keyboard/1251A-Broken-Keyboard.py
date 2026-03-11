from collections import Counter
def pol():
    t=int(input())
    for _ in range(t):
        s=str(input())

        feq=Counter(s)

        res=[0]*26


        a=1
        ans=[]
        s += "#"
        if len(s)==1:
            print(s)
            continue

        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                a+=1
            else:
                if a==1:
                    res[ord(s[i])-ord("a")]=1

                elif a%2!=0:
                    res[ord(s[i])-ord("a")]=1
                a=1
        
        for i in range(26):
            if res[i]==1:
                ans.append(chr(i+ord("a")))
     
        print("".join(sorted(ans)))

pol()