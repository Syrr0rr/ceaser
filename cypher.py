def print_start():
    '''confirms user input and returns 1,2 or 3'''
    print("""
    CAESAR CIPHER MESSAGING

    -----------------------

    1. Start a message

    2. Read and reply to a message

    3. Quit """)

#DEBUG TOOLS-----------------------------------------------------------------------------------

def reset_file():
    '''debug tool'''
    file_name = input("File location (RESET)")
    file_path = f"Encrypted_stuff/{file_name}.txt"
    with open(file_path, "w") as file: #w overwrites
        file.write("")
def sendtofile(text):
    '''create message in file h without input (debug tool)'''
    file_path = f"Encrypted_stuff/h.txt"
    with open(file_path, "a") as file: #appends text every time 
        file.write(text) 

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
# def start_crypt(shift): #maybe store in a list or if not a string
#     encypted = []
#     supported_characters = list(input("Enter support characters in order (Alphabet or numbers, NO REPEATS): ")) #ABCDEFGHIJKLMNOPQRSTUVWXYZ
#     #NOTE ^put this in sep fucntion, make it an argument in this one 
#     shifted_characters = supported_characters[shift:] + supported_characters[:shift]
#     message =  list(input("Message"))
#     for letter in message: 
#         if letter not in supported_characters:
#             letter = "?"
#             encypted.append(letter) #just appends letters in list to encrypted
#         else:
#             crypt_letter = supported_characters.index(letter)   #finds the h in encypted not normal list
#             encypted.append(shifted_characters[crypt_letter]) #just appends letters in list to encrypted
#     print(shifted_characters)
#     print(encypted)
#     str_encrypted = "".join(encypted)
#     sendtofile("".join(supported_characters))
#     sendtofile(f"\n{shift}")
#     return str_encrypted


def encrypt(): #need to add first option 
    encypted = []
    with open(f"Encrypted_stuff/h.txt", "r") as file:
            lines = file.readlines()
            supported_characters = lines[0]
            shift = int(lines[1]) * -1
            message = lines[-1] 

    shifted_characters = supported_characters[shift:] + supported_characters[:shift]
    for letter in message:
        if letter not in supported_characters:
            encypted.append("?")
        else:
            crypt_letter = supported_characters.index(letter)
            encypted.append(shifted_characters[crypt_letter])

    print(shifted_characters)
    print(encypted)
    return "".join(encypted)

#FILE HANDLING----------------------------------------------------------------------
def create_message(text):
    '''appends crypted text to the conversation file, location of file is set by user'''
    file_name = input("Name of file to send text to (h): ")
    file_path = f"Encrypted_stuff/{file_name}.txt"
    with open(file_path, "a") as file: 
        file.write(text) 

# def decrypt():
#     encypted = []
#     file_name = input("File name")
#     with open(f"Encrypted_stuff/{file_name}.txt", "r") as file:
#         lines = file.readlines()
#         supported_characters = lines[0]
#         shift = int(lines[1]) * -1
#         messages = lines[-2:] 
#     shifted_characters = supported_characters[shift:] + supported_characters[:shift]
    
#     for letter in messages: 
#         if letter not in supported_characters:
#             letter = "?"
#             encypted.append(letter) #just appends letters in list to encrypted
#         else:
#             crypt_letter = supported_characters.index(letter) 
#             encypted.append(shifted_characters[crypt_letter]) #just appends letters in list to encrypted
#     print(f"{shifted_characters} SHIFTED CHARACTERS")
#     print(f"{encypted} ENCRYPTED")
#     str_encrypted = "".join(encypted)
#     sendtofile("".join(supported_characters))
#     sendtofile(f"\n{shift}")
#     return str_encrypted
    

def reply2message():
    file_name = input("File name")
    r = True
    while r: #repeats until it can open file 
        try:
            with open(f"Encrypted_stuff/{file_name}.txt", "r") as file:
                print("Yay file found and opened all working ")
                    #content = file.read() #Prints entire contents of file
                lines = file.readlines()
                print(lines[0]) 
                                  
        except FileNotFoundError:             
            print("File not found; Try again")
            file_name = input("File name")
    
    

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
            decrypt()
main()

#

# if input == 1 then it needs to ask for alphabet and such 



