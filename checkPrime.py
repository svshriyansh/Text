def checkPrime(n):
    if n == 0 or n == 1:
        print('Number is not prime ..!')
        return 
    mid = int(n/2)+1
    for i in range(2,mid):
        if n%i == 0:
            print('Number is not prime ..!')
            return
    print('Number is prime :)')

checkPrime(int(input('Please enter number : ')))
    