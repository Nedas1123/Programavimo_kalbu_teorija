class Num:
       
    def isPrime(self,n):
       if n <= 1 or n % 1 > 0:
           return False
       for i in range(2, n//2):
           if n % i == 0:
               return False
       return True
    
    def findSmaller(self,num):
        x=num
        while not self.isPrime(x):
            x=x-1  
        return x
        
    def findBigger(self,num):
        x=num
        while not self.isPrime(x):
            x=x+1  
        return x
        
data  =[]
answer = []
num=1
n=Num()

while num != 0:  
    num=int(input())
    if num!=0:
        data.append(num)      

for p in data:
    if n.isPrime(p):
        answer.append(0)
    else:
        a=n.findSmaller(p)
        b=n.findBigger(p)
        ans=b-a
        answer.append(ans)
        
print(answer)

