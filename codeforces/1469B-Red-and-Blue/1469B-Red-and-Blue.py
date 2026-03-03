def colors():

    no_test_cases=int(input())


    for _ in range(no_test_cases):
        n=int(input())

        red=list(map(int, input().split()))

        m=int(input())

        blue=list(map(int, input().split()))


        prefix=[0]*n
        prefix_blue=[0]*m

        


        for  i in range(n):
            prefix[i]=prefix[i-1]+red[i]
            
        

        for j in range(m):
            prefix_blue[j]=prefix_blue[j-1]+blue[j]
        
     
        

        



        ans=max(prefix)+max(prefix_blue)
        final_ans=max(0, ans, max(prefix), max(prefix_blue))
        print(final_ans)

        
    
        
        
colors()