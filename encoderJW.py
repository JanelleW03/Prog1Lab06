# janelle whiteside
def menu():
    print("Menu")
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(p):
    encoded_password = []
    p = list(p)

    for i in range(len(p)):
        turn_int = int(p[i])
        encoded_turn_int = turn_int + 3
        encoded_password.append(encoded_turn_int)
    for i in range(len(encoded_password)):
        encoded_password[i] = str(encoded_password[i])

    encoded_password = "".join(encoded_password)
    return encoded_password

if __name__ == "__main__":
    while True:
        menu()
        print("")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = int(input('Please enter your password to encode:'))
            print('Your password has been encoded and stored!')
            print('')
        elif option == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {password}")
        elif option == 3:
            break
