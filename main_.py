import hashlib ,random ,string ,re

class PasswordHasher:
    def __init__(self, password: str):
        self.password = password

    def hash_password(self) -> str:
        """Hash a password using SHA-256."""
        return hashlib.sha256(self.password.encode()).hexdigest()

class PasswordGenerator:
    def __init__(self, length: int = 12):
        if length < 8:
            raise ValueError("Password length should be at least 8 characters.")
        self.length = length

    def generate(self) -> str:
        """Generate a random password of specified length."""
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(self.length))

class PasswordStrengthChecker:
    def __init__(self, password: str):
        self.password = password

    def check_strength(self) -> str:
        """Check the strength of a password."""
        if len(self.password) < 8:
            return "Weak"
        
        criteria = [
            r'[A-Z]',  # At least one uppercase letter
            r'[a-z]',  # At least one lowercase letter
            r'[0-9]',  # At least one digit
            r'[\W_]'   # At least one special character
        ]
        
        strength_count = sum(bool(re.search(criterion, self.password)) for criterion in criteria)
        
        if strength_count == 4 and len(self.password) >= 12:
            return "Very Strong"
        elif strength_count == 4:
            return "Strong"
        elif strength_count == 3:
            return "Moderate"
        else:
            return "Weak"

class PasswordManager:
    def __init__(self):
        self.password = None

    def get_user_choice(self) -> bool:
        """Prompt the user to choose whether to input their own password or generate a random one."""
        while True:
            choice = input("Do you want to input your own password? (y/n): ").strip().lower()
            if choice in ['y', 'n']:
                return choice == 'y'
            print("Invalid input, please enter 'y' or 'n'.")

    def get_password_from_user(self) -> str:
        """Get a password from the user and ensure it is not weak."""
        while True:
            password = input("Enter your password: ")
            confirm_password = input("Confirm your password: ")
            if password != confirm_password:
                print("Passwords do not match. Please try again.")
                continue
            
            strength_checker = PasswordStrengthChecker(password=password)
            strength = strength_checker.check_strength()
            print(f"Password Strength: {strength}")
            if strength == "Weak":
                print("Your password is too weak. Please try again.")
            else:
                return password

    def get_generated_password(self) -> str:
        """Generate a random password based on user-specified length."""
        while True:
            try:
                length = int(input("Enter the desired length for the random password (at least 8): "))
                password_generator = PasswordGenerator(length=length)
                password = password_generator.generate()
                print(f"Generated Password: {password}")
                
                # Check and display the strength of the generated password
                strength_checker = PasswordStrengthChecker(password=password)
                strength = strength_checker.check_strength()
                print(f"Password Strength: {strength}")
                
                return password
            except ValueError as e:
                print(e)

    def save_hashed_password(self, hashed_password: str):
        """Save the hashed password to a file."""
        with open("hashed_passwords.txt", "a") as file:
            file.write(hashed_password + "\n")
        print("Hashed password saved to hashed_passwords.txt")

    def run(self):
        """Run the password manager."""
        if self.get_user_choice():
            self.password = self.get_password_from_user()
        else:
            self.password = self.get_generated_password()

        # Hash the password
        password_hasher = PasswordHasher(password=self.password)
        hashed_password = password_hasher.hash_password()
        print(f"Hashed Password: {hashed_password}")

        # Save the hashed password
        self.save_hashed_password(hashed_password)

if __name__ == "__main__":
    manager = PasswordManager()
    manager.run()
