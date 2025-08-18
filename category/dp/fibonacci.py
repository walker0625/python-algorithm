memo = {}

def fibo_top_down(n):
    
    if n == 1 or n == 2:
        return 1
    
    if n not in memo:
        memo[n] = fibo_top_down(n-1) + fibo_top_down(n-2)    
        
    return memo[n] # 저장된 값을 return 

print(fibo_top_down(7))
print(memo)

##############################################################

memo2 = {1: 1, 2: 1}

def fibo_bottom_up(n):
    
    for i in range(3, n+1):
        memo2[i] = memo2[i-1] + memo2[i-2]
        
    return memo2[n] # 저장된 값을 return 

print(fibo_bottom_up(7))
print(memo2)