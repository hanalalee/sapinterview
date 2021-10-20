# def prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True



def prime2(n):
    if n == 1:
        return False
        
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True



if __name__ == "__main__":
    i = int(input())
    print(prime2(i))