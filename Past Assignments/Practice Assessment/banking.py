input_file_name = 'data.txt'

def openFile(file):
    infile = open(file, 'r')
    lines = infile.readlines()
    infile.close()
    return lines
lines = openFile(input_file_name)

# check username
def checkUser(userName, lines):
    for i, line in enumerate(lines):
        if userName in line:
            print(line)
            return line
    print('Please enter a valid username.')
    exit()
    

def checkPW(password, correctUserLines):
    if password in correctUserLines:
        return userInfo(correctUserLines)
    else:
        print('Password incorrect, please try again.')
        password = input('Enter Password: ')
        checkPW(password, correctUserLines)


# print full name & account balance
def userInfo(printLine):
    user = printLine.split(',')
    balance = '{:,}'.format(int(user[3]))
    result = print(f'\n{user[2]}\'s balance is ${balance}.')
    return result


# get user
print('\n')
userName = input('Enter name: ')
# check username
correctLines = checkUser(userName, lines)
# get password
pw = input('Enter Password: ')
# check pw here
checkPW(pw, correctLines)