def fibonacci(N):
    if N==0:
        print(N)
        return 0
    elif N==1:
        print(N)
        return 1
    return fibonacci(N-1)+fibonacci(N-2)

print(fibonacci(13))