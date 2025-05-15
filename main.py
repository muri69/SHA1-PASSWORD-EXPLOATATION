import hashlib

def convert_text_to_sha1(text):
    digest = hashlib.sha1(text.encode()).hexdigest()
    return digest

def main():
    user_sha1 = input("Enter the SHA1 to crack: ")
    cleaned_user_sha1 = user_sha1.strip().lower()


    try:
        with open("1000-most-common-passwords.txt") as f:
            for line in f:
                password = line.strip()
                converted_sha1 = convert_text_to_sha1(password)
                
                if cleaned_user_sha1 == converted_sha1:
                    print(f"Password found: {password}")
            

        print("Could not find the password")  

    except FileNotFoundError:
        print("The file '1000-most-common-passwords.txt' was not found.")

# Apelăm funcția principală pentru a rula codul
main()



     
