def i():

    arr=[]


    for i in range(5):
        curr=list(map(int, input().split()))
        arr.append(curr)

    

    for i in range(5):
        for j in range(5):
            if arr[i][j]==1:
                row, col=i,j

                print(abs(row-2)+abs(col-2))
                return
i()