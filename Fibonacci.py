def fibonacci(n) :
        if n <= 0:
            return 0
        elif n == 1:
              return 0
        elif n == 2:
              return 1
        else:
              a, b = 0, 1
              for i in range(2,n):
                    a, b = b, a + b
                    return b
              
def cetakFibonacci(n):
      a, b = 0, 1
      for i in range (n):
            print(a, end="")
            a, b = b, a + b
n = int(input("masukkan nilai n: "))
print("Fibonacci sampai ke", n,"dari" ,fibonacci(n))
print("")
cetakFibonacci(n)