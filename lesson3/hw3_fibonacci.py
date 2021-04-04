def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

# best practice:
#
# fib = [0, 1] + [0]*(5-1) # for number fibonacci for number 5.
# for i in range(2, 5+1):
#     fib[i] = fib[i-1]+fib[i-2]
# print(fib[len(fib)-1])


if __name__ == "__main__":
    print(fibonacci(5))
