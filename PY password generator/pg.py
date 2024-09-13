import random
import string

def generate_password(length, include_uppercase=True, include_numbers=True, include_symbols=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''
    
    all_characters = lowercase_letters + uppercase_letters + digits + symbols
    
    if not all_characters:
        raise ValueError("No characters available to generate a password. Please enable at least one character type.")
  
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    

    password = generate_password(length, include_uppercase, include_numbers, include_symbols)
    print(f"Your generated password is: {password}")

main()
