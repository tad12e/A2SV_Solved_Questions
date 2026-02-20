def casino():

    nums=int(input())

    for i in range(nums):

        n, k=map(int, input().split())

    

       

        lest=[]

        for i in range(n):
            li, ri, reali=map(int, input().split())
            lest.append([li, ri, reali])
        lest.sort(key=lambda x:x[0])


        for i in range(len(lest)):
            if lest[i][0]<=k and k<=lest[i][1]:
                
                k=max(k,lest[i][2])
        print(k)

       
casino()
        
