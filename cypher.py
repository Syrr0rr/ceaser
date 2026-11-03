def print_start():
    '''confirms user input and returns 1,2 or 3'''
    print("""
    CAESAR CIPHER MESSAGING

    -----------------------

    1. Start a message

    2. Read and reply to a message

    3. Quit """)
#CONFIRMATION-------------------------------------------------------------------
def is_integer_string(s):
    '''returns true for negative and postive numbers, false for anything that cant be converted to int'''
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_valid_start_input():
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
    num = input(phrase)
    result = is_integer_string(num)
    while result == False:
        print("Errror")
        num = input(phrase)
        result = is_integer_string(num)
    num = int(num)
    return num

#ENCRYPTION CODE --------------------------------------------------------------

def start_crypt(shift): #maybe store in a list or if not a string
    encypted = []
    supported_characters = list(input("Enter support characters in order (Alphabet or numbers, NO REPEATS): ")) #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    shifted_characters = supported_characters[shift:] + supported_characters[:shift]
    message =  list(input("Message"))
    for letter in message: 
        if letter not in supported_characters:
            letter = "?"
            encypted.append(letter) #just appends letters in list to encrypted
        else:
            crypt_letter = supported_characters.index(letter)   #finds the h in encypted not normal list
            encypted.append(shifted_characters[crypt_letter]) #just appends letters in list to encrypted
    print(shifted_characters)
    print(encypted)
    str_encrypted = "".join(encypted)
    return str_encrypted

#FILE HANDLING----------------------------------------------------------------------

def create_message(text):
    '''appends crypted text to the conversation file, location of file is set by user'''
    file_name = input("Name of file to send text to (or what to name a file that will be created)")
    file_path = f"Encrypted_stuff/{file_name}.txt"
    with open(file_path, "a") as file: #resets every time ( change 2 to something else ) ((used to be w))
        file.write(text)

def reply2message():
    file_name = input("File name")
    r = True
    while r:
        try:
            with open(f"Encrypted_stuff/{file_name}.txt", "r") as file:
                print("Yay file found and opened all working ")
                content = file.read() #Prints entire contents of file
                for line in content:
                    print(line)
                print(content)                 #^Loop through the file to get all the different lines as a list
                r = False                      #    ^print the last 2 
        except FileNotFoundError:              #        ^decrypt the last two 
            print("File not found; Try again")
            file_name = input("File name")
            
#DEBUG TOOLS-----------------------------------------------------------------------------------

def reset_file():
    '''debug tool'''
    file_name = input("File location (RESET)")
    file_path = f"Encrypted_stuff/{file_name}.txt"
    with open(file_path, "w") as file: #w overwrites
        file.write("")

#MAIN-------------------------------------------------------------------------------------------
#reset_file()

def main():
    while True:
        print_start()
        start_input = get_valid_start_input()
        if start_input == 3:
            print("Im done")
            break
        elif start_input == 1:
            shift = get_digit("Enter Shift" )
            result = start_crypt(shift)
            create_message(f"\n {result}")
        else:
            reply2message()
main()





