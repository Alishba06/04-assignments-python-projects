
def print_divisors(num):
    
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ') 
    print()  
def main():
   
    num = int(input("Enter a number: "))
    print(f"Here are the divisors of {num}")
    print_divisors(num)



if __name__ == '__main__':
    main()