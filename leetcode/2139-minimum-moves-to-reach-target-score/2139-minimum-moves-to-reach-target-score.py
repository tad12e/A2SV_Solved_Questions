class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        curr_num=1
        arr=[]
        num=target



        if maxDoubles==0:
            return target-curr_num
        if target==curr_num:
            return 0
       

        f=0
        while maxDoubles>f and target>0:
            if target%2==0:
                arr.append([target//2,0])
                target=target//2
            else:
                arr.append([(target-1)//2,1])
                target=(target-1)//2
            f+=1
        

        for i in arr[::-1]:
            val, intf=i

            if val==0:
                continue

            if intf==0:
                count+=(abs(curr_num-val))+1
                curr_num+=abs(curr_num-val)
                curr_num=curr_num*2
            else:
                count+=(abs(curr_num-val))+1
                curr_num+=abs(curr_num-val)
                curr_num=curr_num*2
        print(arr)
        if num%2!=0:
            return count+1
        else:
            return count
        




            
        print(arr)
        
        


       

        return count+(target-curr_num)



        