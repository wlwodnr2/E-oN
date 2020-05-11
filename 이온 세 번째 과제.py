from collections import OrderedDict

n = int(input("작업수를 입력해주세요 : "))
m = int(input("작업 번호를 입력해주세요 : "))
priority = {}
priority = OrderedDict()
pt = 0
j = 0

if (0<n<=100 and 0<=m<=n-1) is True:
    for i in range(n):
        priority[i] = int(input("우선 순위를 정해주세요 : "))
    
    while True:
        if priority.get(j) != max(priority.values()):
            priority.move_to_end(j)
            j += 1
            if j > n-1:
                j = 0  
        
        elif priority.get(j) == max(priority.values()):
            del priority[j]
            j += 1
            pt += 1
            if j > n-1:
                j = 0  
            if (m in priority) is False:
                break
else:
    print ("조건이 만족하지 않습니다.")

      
print (pt,"분입니다")    


