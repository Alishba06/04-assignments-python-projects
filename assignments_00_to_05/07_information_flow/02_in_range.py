
def in_range(n, low, high):
    """Returns True if n is between low and high (inclusive)."""
    return low <= n <= high

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower limit: "))
    high = int(input("Enter the upper limit: "))

    result = in_range(n, low, high)
    print(result)

if __name__ == '__main__':
    main()