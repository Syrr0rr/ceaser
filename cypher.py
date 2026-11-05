def print_start():
    '''prints starting menu
    '''
    print("""
    CAESAR CIPHER MESSAGING

    -----------------------

    1. Start a message

    2. Read and reply to a message

    3. Quit """)
#DEBUG TOOLS-----------------------------------------------------------------------------------
def reset_file():
    '''resets conversation file (h)'''
    file_name = input("File location (RESET)")
    file_path = f"Encrypted_stuff/{file_name}.txt"
    with open(file_path, "w") as file: #w overwrites
        file.write("")
#CONFIRMATION------------------------------------------------------------------------------------
def is_integer_string(s):
    '''returns true for negative and postive numbers, false for anything that cant be converted to int'''
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_valid_start_input():
    '''gets valid start input '''
    while True:
        u_input = input("Enter your choice: ")
        if not u_input.isdigit():
            print("Not digit")
            continue
        choice = int(u_input)
        if 1 <= choice <= 3:
            return choice
        print("Error, try again")

def get_digit(phrase):
    '''checks if a number can be an integer'''
    num = input(phrase)
    result = is_integer_string(num)
    while result == False:
        print("Errror")
        num = input(phrase)
        result = is_integer_string(num)
    num = int(num)
    return num
#ENCRYPTION CODE ---------------------------------------------------------------------------------
def encrypt(message, supported_characters, shift):
    '''the code that actually encrypts/decrypts the messages'''
    encrypted = []
    shift = shift % len(supported_characters)  # wrap the shift
    shifted_characters = supported_characters[shift:] + supported_characters[:shift]
    for letter in message:
        if letter not in supported_characters:
            encrypted.append("?")
        else:
            crypt_letter = supported_characters.index(letter)
            encrypted.append(shifted_characters[crypt_letter])

    return "".join(encrypted)
#FILE HANDLING--------------------------------------------------------------------------------------
def create_message():
    '''Resets the conversation file and asks for the first message to be sent to the folder'''
    supported_characters = input("Enter supported characters: ")
    shift = get_digit("Enter shift: ")
    message = input("Message: ")

    encrypted_message = encrypt(message, supported_characters, shift)

    file_name = input("Name of file: ")
    file_path = f"Encrypted_stuff/{file_name}.txt"

    with open(file_path, "w") as file:
        file.write(supported_characters + "\n")
        file.write(str(shift) + "\n")
        file.write(encrypted_message + "\n")

    print("Encrypted message:", encrypted_message)
    print("Message saved!")

def reply2message():
    '''lets the user see the last two messages and asks for a reply to tho'''
    file_name = input("File name: ")
    while True: #repeats until it can open file
        try:
            with open(f"Encrypted_stuff/{file_name}.txt", "r") as file:
                    #content = file.read() #Prints entire contents of file
                lines = file.readlines()
                print(f"supported characters: {lines[0]}")
                break
        except FileNotFoundError:            
            print("File not found; Try again")
            file_name = input("File name")
    supported_characters = lines[0].strip()
    shift = int(lines[1].strip())
    messages = lines[-2:]
    for message in messages[-2:]: #rints last two messages
        decrypted = encrypt(message.strip(), supported_characters, -shift)
        print(decrypted)
    reply = input("Enter your reply: ")
    encrypted_reply = encrypt(reply, supported_characters, shift)
    with open(f"Encrypted_stuff/{file_name}.txt", "a") as file:
        file.write(encrypted_reply + "\n")
#MAIN----------------------------------------------------------------------------------------------
def main():
    while True:
        print_start()
        start_input = get_valid_start_input()
        if start_input == 3:
            print("Goodbye")
            break
        elif start_input == 1:
            create_message()
        else:
            reply2message()
main()

#ABCDEFGHIJKLMNOPQRSTUVWXYZ 
