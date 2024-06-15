import random
import string

def generate_password(length, lowercase=True, uppercase=True, numbers=True, symbols=True):
  """
  Generates a random password based on user-specified criteria.

  Args:
      length (int): Desired length of the password.
      lowercase (bool, optional): Include lowercase letters. Defaults to True.
      uppercase (bool, optional): Include uppercase letters. Defaults to True.
      numbers (bool, optional): Include numbers. Defaults to True.
      symbols (bool, optional): Include symbols. Defaults to True.

  Returns:
      str: The generated random password.
  """

  # Define character sets based on user preferences
  char_sets = []
  if lowercase:
    char_sets.append(string.ascii_lowercase)
  if uppercase:
    char_sets.append(string.ascii_uppercase)
  if numbers:
    char_sets.append(string.digits)
  if symbols:
    char_sets.append(string.punctuation)

  # Combine character sets if any are selected
  all_chars = ''.join(char_sets)

  if not all_chars:
    raise ValueError("At least one character set must be selected.")

  # Generate random password
  password = ''.join(random.sample(all_chars, length))
  return password

def main():
  """
  Main function for user interaction and password generation.
  """

  while True:
    try:
      # Get password length from user
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

      # Get user preferences for character sets
      lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
      uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
      numbers = input("Include numbers (y/n)? ").lower() == 'y'
      symbols = input("Include symbols (y/n)? ").lower() == 'y'

      # Generate and display password
      password = generate_password(length, lowercase, uppercase, numbers, symbols)
      print("Your generated password:", password)

      # Ask if user wants to generate another password
      again = input("Generate another password (y/n)? ").lower() == 'y'
      if not again:
        break

    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
