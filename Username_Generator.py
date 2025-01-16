import random

# Predefined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Fast", "Clever", "Bold", "Shiny", "Witty", "Brave", "Lucky", "Charming"]
nouns = ["Tiger", "Dragon", "Phoenix", "Eagle", "Panther", "Wolf", "Hawk", "Bear", "Fox", "Lion"]

# Function to generate a random username
def generate_username(customize=False, length=None):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    if customize:
        number = str(random.randint(10, 99))
        special_char = random.choice(["!", "@", "#", "$", "%", "&", "*"])
        username += number + special_char

    if length and len(username) > length:
        username = username[:length]

    return username

# Function to save usernames to a file
def save_to_file(usernames, filename="usernames.txt"):
    try:
        with open(filename, "w") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"\nUsernames saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

# Main interactive function
def main():
    usernames = []
    print("\nWelcome to the Random Username Generator!\n")

    while True:
        print("\nMenu:")
        print("1. Generate a random username")
        print("2. Generate a customized username")
        print("3. Save usernames to a file")
        print("4. View generated usernames")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            username = generate_username()
            print("Generated Username:", username)
            usernames.append(username)

        elif choice == "2":
            try:
                length = input("Enter the maximum length for the username (or press Enter to skip): ").strip()
                length = int(length) if length.isdigit() else None
                username = generate_username(customize=True, length=length)
                print("Generated Customized Username:", username)
                usernames.append(username)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "3":
            if usernames:
                save_to_file(usernames)
            else:
                print("No usernames to save!")

        elif choice == "4":
            if usernames:
                print("\nGenerated Usernames:")
                for idx, username in enumerate(usernames, 1):
                    print(f"{idx}. {username}")
            else:
                print("No usernames generated yet!")

        elif choice == "5":
            print("Thank you for using the Random Username Generator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
