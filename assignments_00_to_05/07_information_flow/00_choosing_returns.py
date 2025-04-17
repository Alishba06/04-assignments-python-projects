
ADULT_AGE = 18  

def is_adult(age):
    """Returns True if the age is 18 or older, otherwise returns False."""
    return age >= ADULT_AGE  

def main():
    age = int(input("How old is this person?: "))
    
    print(is_adult(age))

if __name__ == '__main__':
    main()