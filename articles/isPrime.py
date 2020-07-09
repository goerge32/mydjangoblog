def isPrime(num):
    a=2
    while a<num:
        if num%a==0:
            return False
        a+=1
    return True