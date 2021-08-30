# generic file searching program

import os
import glob


print ('cwd: '+ os.getcwd())

def prompt():
    x = input('What do you want, the newest file? ').lower()
    while not(x=='y' or x=='yes' or x=='yeah' or x=='yea' or x=='yup'
              or x=='n' or x=='no' or x=='nah' or x=='nay' or x=='nope'):
        x = input('Latest file - yeah or nah? ')

    if (x=='y' or x=='yes' or x=='yeah' or x=='yea' or x=='yup'):
        print('yes')
    elif (x=='n' or x=='no' or x=='nah' or x=='nay' or x=='nope'):
        print('no')




def main():
    prompt()


if __name__ == '__main__':
    main()
