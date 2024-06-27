import random 
import string


def Password_generate(length):
    characters = string.ascii_letters + string.digits
    password = []
    
    for i in range(length):
        rand_char = random.choice(characters)
        password.append(rand_char)

    password = ''.join(password)
    return password

def main():
    try:
        length = int(input("Enter the desired length of password: "))
        if length < 8:
            print("Password legnth should be atleast 8 characters.")
            return
        
        password = Password_generate(length)

        print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
