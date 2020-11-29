# credits - cs dojo - dynamic programming
## https://www.youtube.com/watch?v=vYquumk4nWw

# solving fibonnaci via recursion
def fibonacci_rec(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci_rec(n-1) + fibonacci_rec(n-2)
    return result

# Below 2 functions solve via memoization technique of Dynamic programming
def fib_2(n,memo):
    if memo[n] != None:
        return memo[n]
    if n ==1 or n ==2:
        result =1
    else:
        result = fib_2(n-1,memo) + fib_2(n-2,memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo =[None] *(n+1)
    return fib_2(n,memo)

# bottom up approach
def fib_bottom_up(n):
    if n==1 or n ==2:
        return 1
    else:
        bottom_up = [None] * (n+1)
        bottom_up[1] = 1
        bottom_up[2] = 1

        for i in range(3,n+1):
            bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        return bottom_up[n]





if __name__ == '__main__':
    print(fibonacci_rec(1))
    print(fibonacci_rec(5))
    print(fib_memo(35))
    print(fib_bottom_up(1000))  # cant use memoization for large numbers else we get max recursive depth reached error
    print(fib_bottom_up(10000))




