#%%
from random import randint,choice
from webbrowser import open
#from secrets import token_urlsafe
#Functions for the website
def welcome():
    print()
    print('Main menu')
    print('Enter 1 to play online slot game')
    print('Enter 2 to play tictactoe')
    print('Enter 3 to play online sudoku')
    print('Enter 4 to play rock,paper,scissors')
    print('Enter 5 to exit')
    a=int(input('Enter your choice: '))
    if a==1:
        return slot_machine_welcome()
    elif a==2:
        return tictactoe_welcome()
    elif a==3:
        return sudoku_welcome()
    elif a==4:
        return rock_paper_scissors_welcome()
    elif a==5:
        print('Thank you')
        return exit()
    else:
        print('Invalid input')
        return welcome()
def start():
    print()
    print('Welcome to arcade123.com')
    print('To login enter 1')
    print('If you are new here then sign up by entering 2')
    print('If you forgot your password, you can reset it by entering 3')
    print('Or if you don\'t want to play then you can exit by entering 4') 
    choice_website()
def choice_website():
    a=input('Enter your choice: ')
    if a=='1':
        return login()
    elif a=='2':
        signup()
    elif a=='3':
        return password_reset()
    elif a=='4':
        return exit()
    else:
        print('Invalid input.')
        return choice()
def login():
    global usernames
    global passwords
    value=True
    print()
    while value:
        username=input('Username: ')
        if username in usernames:
            count=0
            m=0
            for i in usernames:
                if i==username:
                    m=count
                count+=1
            k=3
            while k>0:    
                password=input('Password: ')
                if password==passwords[m]:
                    print('Logged in sucessfully')
                    print()
                    print()
                    return welcome() 
                elif password!=passwords[m]:
                    k-=1
                    if k==0:
                        print('Too many wrong password entries')
                        return exit()
                    print('Wrong password')
                    print('you have',k,'tries left')
            value=False
        else:
            print('Username does not exist. Try again')
def signup():
    global usernames
    global passwords
    print()
    print('Note- Do Not give any personal details while entering your username of password')
    first_name=input('Enter your first name: ')
    last_name=input('Enter your last name: ')
    email_verification()
    value=True
    while value:
        username=input('Enter a desired username: ')
        if username in usernames:
            print('Username already exists. Enter a different username')
        else:
            usernames.append(username)
            password=input('Enter a password: ')
            passwords.append(password)
            value=False
    print('Signed up sucessfully and logged in')
    return welcome()
def email_verification():
    print()
    while True:    
        email=input('Enter your email address(only gmail): ')
        domain='@gmail.com'
        l1=len(email)
        l2=len(domain)
        sub=email[l1-l2:]
        if sub==domain:
            if l1==l2:
                print('Invalid Email id, Try again')
            else:
                print('Valid Email id')
                break
        else:
            print('Invalid Email id, Try again')
def password_reset():
    print()
    global usernames 
    value=True
    while value:
        username=input('Username: ')
        if username in usernames:
            print('Username found.')
            print('Now we will redirect you to the password reset website')
            value=False
        else:
            print('Username does not exist. Try again')
    reset_domain='https://arcade123.com/reset='
    url=reset_domain
    '''+token_urlsafe'''
    '''secrets.token_urlsafe() creates a hard-to-guess temporary URL containing a
    security token suitable for password recovery applications.
    reference- secrets module in python docs'''
    print('Redirecting to',url)
    open(url)
    print('Password reset sucessful!')
    return welcome()
#Functions for the slot machine
def slot_machine_welcome():
    print('                            indiancasino')
    print()
    print('                    Welcome to online slot machine')
    print()
    print('Here\'s your 100 dollers to start playing')
    print('   ____________________________________________________________________________________')
    print('  |                                                                                    |')
    print('  |                               The game is simple                                   |')
    print('  |                                                                                    |')
    print('  |  Each spin costs 25 dollers                                                        |')
    print('  |                                                                                    |')
    print('  |  There are 1-9 numbers which are randomly generated                                |')
    print('  |                                                                                    |')
    print('  |  If you got the middle row of numbers same then you get the Jackpot                |')
    print('  |  The Jackpot is ONE MILLION DOLLERS.                                               |')
    print('  |                                                                                    |')
    print('  |  If you get the upper or lower row of numbers matched then you get a free spin     |')
    print('  |  If you get the number matched up diagonally then you win 50 dollers               |')
    print('  |                                                                                    |')
    print('  |                                   GOOD LUCK!                                       |')
    print('  |                                                                                    |')
    print('   ____________________________________________________________________________________')
    print()
    a=input('do you want to play? (y/n): ')
    if money==0:
        print('Sorry no balance.Come again tommorow')
        return welcome()
    else:
        if a=='y':
            return slot_machine_choice()
        elif a=='n':
            print('Ok. Thank you!')
            return welcome()
        else:
            print('Invalid input')
            return slot_machine_welcome()
def slot_machine_choice():
    print()
    play=input('do you want to spin? (y/n) ')    
    if play=='y':
        return reduct_money_slot()
    elif play=='n':
        print('Ok. Thank you!')
        return welcome()
    else:
        print('invalid input')
        return slot_machine_choice()
def reduct_money_slot():
    global money
    money-=25
    return chance() #for slot machine
def balance():
    global money
    print('Your current balance is ',money)
def chance():
    for i in key:
        a[i]=randint(1,9)
    print()
    print('  ___________ ___________ ___________ ')
    print(' |           |           |           | ')
    print(' |     ',a['u_1'],'     |     ',a['u_2'],'     |     ',a['u_3'],'     |',sep='')
    print(' |           |           |           | ')
    print('  ___________ ___________ ___________ ')
    print(' |           |           |           | ')
    print(' |     ',a['m_1'],'     |     ',a['m_2'],'     |     ',a['m_3'],'     |',sep='')
    print(' |           |           |           | ')
    print('  ___________ ___________ ___________ ')
    print(' |           |           |           | ')
    print(' |     ',a['l_1'],'     |     ',a['l_2'],'     |     ',a['l_3'],'     |',sep='')
    print(' |           |           |           | ')
    print('  ___________ ___________ ___________ ')
    print()
    return result()
def result():
    global money
    if a['m_1']==a['m_2'] and a['m_2']==a['m_3']:
        return jackpot()
    elif a['u_1']==a['u_2'] and a['u_2']==a['u_3']: 
        print('Well you got all the numbers in the upper row same so here\'s your another chance')
        return chance()
    elif a['l_1']==a['l_2'] and a['l_2']==a['l_3']:
        print('Well you got the numbers in the lower row matched up so here\'s your another chance')
        return chance()
    elif a['u_1']==a['m_2'] and a['m_2']==a['l_3']:
        print('Congrats!')
        print('You got the numbers matched diagonally!')
        print('You won 50 dollers!')
        money+=50
        return balance(),slot_machine_choice()
    elif a['u_3']==a['m_2'] and a['m_2']==a['l_1']:
        print('Congrats!')
        print('You got the numbers matched diagonally!')
        money+=50
        return balance(),slot_machine_choice()
    else:
        print('Better luck next time')
        balance()
        if money<=0:
            print('Sorry insufficient balance')
            print('Come again tommorow')
            return welcome()
        else:
            return slot_machine_choice()
def jackpot():
    global money
    print()
    print('Woah you won 1 million dollers!')
    money+=1000000
    print('Congratulations!')
    balance()
    print('Sorry but the game went bankrupt because of you,we had to shut down')
    print('Have a nice day')
    return exit()
#functions for Tictactoe game
def tictactoe_welcome():
    print()
    print()
    print('You might know to play this game well')
    print('Player 1 is X')
    print('Player 2 is O')
    print('All you have to do is enter the co-ordinates of the place where you want to play')
    print('For example, u,1 is a valid co-ordinate')
    print()
    a=input('Do you want to play? (y/n) :')
    if a=='y':
        return tictactoe_board(),chance_tictactoe()
    elif a=='n':
        print('Ok. Thank you!')
        return welcome()
    else:
        print('Invalid input')
        return tictactoe_welcome()
def tictactoe_board():
    print()
    print('         1           2           3')
    print('               |           |             ')
    print(' u       ',b['u,1'],'     |     ',b['u,2'],'     |     ',b['u,3'],'     ',sep='')
    print('               |           |            ')
    print('    ___________ ___________ ___________ ')
    print('               |           |            ')
    print(' m       ',b['m,1'],'     |     ',b['m,2'],'     |     ',b['m,3'],'      ',sep='')
    print('               |           |            ')
    print('    ___________ ___________ ___________ ')
    print('               |           |            ')
    print(' l       ',b['l,1'],'     |     ',b['l,2'],'     |     ',b['l,3'],'     ',sep='')
    print('               |           |            ')
    print()
    return result_tictactoe()
def chance_tictactoe():
    global done
    global i
    global b
    print()
    print('Player',i%2+1)
    pos=input('Enter the co-ordinates of your move: ')
    if pos not in positions:
        print('Sorry, that co-ordinate doesn\'t exist')
        print()
        print('Remember to input co-ordinates like "u,1",etc ')
        print('enter again')
        return chance_tictactoe()
    elif pos in positions:
        if pos in done:
            print('That space is occupied,enter again')
            return chance_tictactoe()
        else:
            i+=1
            done.append(pos)
            if i%2==1:
                b[pos]='X'
                return tictactoe_board()
            elif i%2==0:
                b[pos]='O'
                return tictactoe_board()        
def result_tictactoe():
    if b['u,1']==b['u,2'] and b['u,2']==b['u,3'] and b['u,1']!=' ':
        if b['u,1']=='O' and b['u,1']==b['u,2'] and b['u,2']==b['u,3']:
            print('Player 2 won!')
            return welcome()
        elif b['u,1']=='X' and b['u,1']==b['u,2'] and b['u,2']==b['u,3']:
            print('Player 1 won!')
            return welcome()
    elif b['m,1']==b['m,2'] and b['m,2']==b['m,3'] and b['m,1']!=' ':
        if b['m,1']=='O' and b['m,1']==b['m,2'] and b['m,2']==b['m,3']:
            print('Player 2 won!')
            return welcome()
        elif b['m,1']=='X' and b['m,1']==b['m,2'] and b['m,2']==b['m,3']:
            print('Player 1 won!')
            return welcome()
    elif b['l,1']==b['l,2'] and b['l,2']==b['l,3'] and b['l,1']!=' ':
        if b['l,1']=='O' and b['l,1']==b['l,2'] and b['l,2']==b['l,3']:
            print('Player 2 won!')
            return welcome()
        elif b['l,1']=='X' and b['l,1']==b['l,2'] and b['l,2']==b['l,3']:
            print('Player 1 won!')
            return welcome()
    elif b['u,1']==b['m,2'] and b['m,2']==b['l,3'] and b['u,1']!=' ':
        if b['u,1']=='O' and b['u,1']==b['m,2'] and b['m,2']==b['l,3']:
            print('Player 2 won!')
            return welcome()
        elif b['u,1']=='X' and b['u,1']==b['m,2'] and b['m,2']==b['l,3']:
            print('Player 1 won!')
            return welcome()
    elif b['u,3']==b['m,2'] and b['m,2']==b['l,1'] and b['l,1']!=' ':
        if b['u,3']=='O' and b['u,3']==b['m,2'] and b['m,2']==b['l,1']:
            print('Player 2 won!')
            return welcome()
        elif b['u,3']=='X' and b['u,3']==b['m,2'] and b['m,2']==b['l,1']:
            print('Player 1 won!')
            return welcome()
    elif b['u,1']==b['m,1'] and b['m,1']==b['l,1'] and b['m,1']!=' ':
        if b['u,1']=='O' and b['u,1']==b['m,1'] and b['m,1']==b['l,1']:
            print('Player 2 won!')
            return welcome()
        elif b['u,1']=='X' and b['u,1']==b['m,1'] and b['m,1']==b['l,1']:
            print('Player 1 won!')
            return welcome()
    elif b['u,2']==b['m,2'] and b['m,2']==b['l,2'] and b['m,2']!=' ':
        if b['u,2']=='O' and b['u,2']==b['m,2'] and b['m,2']==b['l,2']:
            print('Player 2 won!')
            return welcome()
        elif b['u,2']=='X' and b['u,2']==b['m,2'] and b['m,2']==b['l,2']:
            print('Player 1 won!')
    elif b['u,3']==b['m,3'] and b['m,3']==b['l,3'] and b['m,3']!=' ':
        if b['u,3']=='O' and b['u,3']==b['m,3'] and b['m,3']==b['l,3']:
            print('Player 2 won!')
            return welcome()
        elif b['u,3']=='X' and b['u,3']==b['m,3'] and b['m,3']==b['l,3']:
            print('Player 1 won!')
            return welcome()
    elif done==positions:
        print('Its a tie')
    else:
        for i in range(0,9):
            if positions[i] not in done:
                return chance_tictactoe()
        else:
            print('It\'s a tie')
            print('Thanks for playing')
            print('Exiting to main menu')
            return welcome()
#functions defined for sudoku
def sudoku_welcome():
    print()
    print('Welcome to online sudoku')
    a=input('do you want to play? (y/n): ')
    if a=='y':
        return board_number()
    elif a=='n':
        print('Ok. Thank you!')
        return welcome()
    else:
        print('Invalid input')
        return sudoku_welcome()
def sudoku_board():
    print()
    print('       a      b       c       d       e       f       g       h       i')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')
    print('  |       |       |       |       |       |       |       |       |       |',sep='')
    print('1 |   ',board_1[x]['a,1'],'   |   ',board_1[x]['b,1'],'   |   ',board_1[x]['c,1'],'   |   ',board_1[x]['d,1'],'   |   ',board_1[x]['e,1'],'   |   ',board_1[x]['f,1'],'   |   ',board_1[x]['g,1'],'   |   ',board_1[x]['h,1'],'   |   ',board_1[x]['i,1'],'   |',sep='')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')     
    print('  |       |       |       |       |       |       |       |       |       |',sep='')
    print('2 |   ',board_1[x]['a,2'],'   |   ',board_1[x]['b,2'],'   |   ',board_1[x]['c,2'],'   |   ',board_1[x]['d,2'],'   |   ',board_1[x]['e,2'],'   |   ',board_1[x]['f,2'],'   |   ',board_1[x]['g,2'],'   |   ',board_1[x]['h,2'],'   |   ',board_1[x]['i,2'],'   |',sep='')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')     
    print('  |       |       |       |       |       |       |       |       |       |',sep='')
    print('3 |   ',board_1[x]['a,3'],'   |   ',board_1[x]['b,3'],'   |   ',board_1[x]['c,3'],'   |   ',board_1[x]['d,3'],'   |   ',board_1[x]['e,3'],'   |   ',board_1[x]['f,3'],'   |   ',board_1[x]['g,3'],'   |   ',board_1[x]['h,3'],'   |   ',board_1[x]['i,3'],'   |',sep='')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')     
    print('  |       |       |       |       |       |       |       |       |       |',sep='')
    print('4 |   ',board_1[x]['a,4'],'   |   ',board_1[x]['b,4'],'   |   ',board_1[x]['c,4'],'   |   ',board_1[x]['d,4'],'   |   ',board_1[x]['e,4'],'   |   ',board_1[x]['f,4'],'   |   ',board_1[x]['g,4'],'   |   ',board_1[x]['h,4'],'   |   ',board_1[x]['i,4'],'   |',sep='')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')     
    print('  |       |       |       |       |       |       |       |       |       |',sep='')
    print('5 |   ',board_1[x]['a,5'],'   |   ',board_1[x]['b,5'],'   |   ',board_1[x]['c,5'],'   |   ',board_1[x]['d,5'],'   |   ',board_1[x]['e,5'],'   |   ',board_1[x]['f,5'],'   |   ',board_1[x]['g,5'],'   |   ',board_1[x]['h,5'],'   |   ',board_1[x]['i,5'],'   |',sep='')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')     
    print('  |       |       |       |       |       |       |       |       |       |',sep='')
    print('6 |   ',board_1[x]['a,6'],'   |   ',board_1[x]['b,6'],'   |   ',board_1[x]['c,6'],'   |   ',board_1[x]['d,6'],'   |   ',board_1[x]['e,6'],'   |   ',board_1[x]['f,6'],'   |   ',board_1[x]['g,6'],'   |   ',board_1[x]['h,6'],'   |   ',board_1[x]['i,6'],'   |',sep='')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')     
    print('  |       |       |       |       |       |       |       |       |       |',sep='')
    print('7 |   ',board_1[x]['a,7'],'   |   ',board_1[x]['b,7'],'   |   ',board_1[x]['c,7'],'   |   ',board_1[x]['d,7'],'   |   ',board_1[x]['e,7'],'   |   ',board_1[x]['f,7'],'   |   ',board_1[x]['g,7'],'   |   ',board_1[x]['h,7'],'   |   ',board_1[x]['i,7'],'   |',sep='')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')     
    print('  |       |       |       |       |       |       |       |       |       |',sep='')
    print('8 |   ',board_1[x]['a,8'],'   |   ',board_1[x]['b,8'],'   |   ',board_1[x]['c,8'],'   |   ',board_1[x]['d,8'],'   |   ',board_1[x]['e,8'],'   |   ',board_1[x]['f,8'],'   |   ',board_1[x]['g,8'],'   |   ',board_1[x]['h,8'],'   |   ',board_1[x]['i,8'],'   |',sep='')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')     
    print('  |       |       |       |       |       |       |       |       |       |',sep='')
    print('9 |   ',board_1[x]['a,9'],'   |   ',board_1[x]['b,9'],'   |   ',board_1[x]['c,9'],'   |   ',board_1[x]['d,9'],'   |   ',board_1[x]['e,9'],'   |   ',board_1[x]['f,9'],'   |   ',board_1[x]['g,9'],'   |   ',board_1[x]['h,9'],'   |   ',board_1[x]['i,9'],'   |',sep='')
    print('   _______ _______ _______ _______ _______ _______ _______ _______ _______')
    print()
    return winning()
def sudoku_check():
    global board_1
    co_ord=input('enter the co-ordinate(eg- a,1 ) (Enter 0 to abandon): ')
    if co_ord=='0':
        print('okay!')
        return welcome()
    if co_ord in keys:
        no=input('Enter the number (0 to cancel the co-ordinates): ')
        if no=='0':
            return print('Enter again'),sudoku_check()
        else:
            if no in valid:
                if answer[x][co_ord]==no:
                     print('correct!')
                     board_1[x][co_ord]=no
                     return sudoku_board()
                else:
                    print('Incorrect number!')
                    return print('Enter again'),sudoku_check()
            else:
                print('Invalid number!')
                return print('Enter again'),sudoku_check()
    else:
        print('Incorrect co-ordinate')
        return print('Enter again'),sudoku_check()
def winning():
    if board_1==answer:
        print('you won!')
        return welcome()
    else:
        return sudoku_check()
def board_number():
    global x
    x=randint(0,2)
    return sudoku_board()
#functions defined for rock,paper,scissors
def rock_paper_scissors_welcome():
    global option
    print('\nWelcome to Online Rock paper scissors \n')
    print("What kind of match would you like to play??")
    print("For Single pointer, Press 1")
    print("For Best of three,Press 3")
    print("For Best of Five, Press 5")
    option = int(input("Enter your option: "))
    return rock_paper_scissors_game()
def rock_paper_scissors_game():
    print('\nEnter your choice for \nrock as r,\nscissors as s,\npaper as p\n')
    print("Enjoy Playing!!\n")
    comp=0
    u=0
    for i in range(option):
        options = ['r','s','p']
        comp_choice = choice(options)
        user_choice = input("\nEnter your choice: ")
        if comp_choice == user_choice:
            print("Computer selected:" + comp_choice)
            print("Its a draw!Try harder")
            comp+=1
            u+=1
            print('\ncomputer:',comp,'user:',u)
        elif comp_choice =='r' and user_choice =='s':
            print("Computer selected:" + comp_choice)
            print("Computer won this round!try again")
            comp+=1
            print('\ncomputer:',comp,'user:',u)
        elif comp_choice =='r' and user_choice =='p':
            print("Computer selected:" + comp_choice)
            print("you won this round!congratulations!")
            u+=1
            print('\ncomputer:',comp,'user:',u)
        elif comp_choice == 'p' and user_choice =='r':
            print("Computer selected:" + comp_choice)
            print("Computer won this round!try again")   
            comp+=1
            print('\ncomputer:',comp,'user:',u)
        elif comp_choice == 'p' and user_choice =='s':
            print("Computer selected:" + comp_choice)
            print("you won this round!congratulations!")
            u+=1
            print('\ncomputer:',comp,'user:',u)
        elif comp_choice == 's' and user_choice =='p':
            print("Computer selected:" + comp_choice)
            print("Computer won this round!try again")
            comp+=1
            print('\ncomputer:',comp,'user:',u)
        elif comp_choice == 's' and user_choice =='r':   
            print("Computer selected:" + comp_choice)
            print("you won this round!congratulations!")
            u+=1
            print('\ncomputer:',comp,'user:',u)
    if comp>u:
        print("\nComputer won this game.Try Harder!")
        return welcome()
    elif u>comp:
        print("\nCongratulations!!You won!")
        return welcome()
    else:
        print("\nIts a Draw!!Try again later!")
        return welcome()
#Global variables for the website
usernames=['richboy',\
           'joe',\
           'fred21',\
           'monkeyman'\
           '123']
passwords=['rolex',\
           'pizza',\
           'freddie',\
           'banana',\
           '123']
#Global Variables for the slot machine game
money=100
a={'u_1':' ',\
   'u_2':' ',\
   'u_3':' ',\
   'm_1':' ',\
   'm_2':' ',\
   'm_3':' ',\
   'l_1':' ',\
   'l_2':' ',\
   'l_3':' '} #co-ordinates
key=['u_1','u_2','u_3','m_1','m_2','m_3','l_1','l_2','l_3']
#global variables for tictactoe
i=0
b={'u,1':' ',\
   'u,2':' ',\
   'u,3':' ',\
   'm,1':' ',\
   'm,2':' ',\
   'm,3':' ',\
   'l,1':' ',\
   'l,2':' ',\
   'l,3':' '}
positions=['u,1','u,2','u,3',\
           'm,1','m,2','m,3',\
           'l,1','l,2','l,3']
done=[] #positions that are done
#Global functions for sudoku
x=0
board_1=[{'a,1':' ','b,1':' ','c,1':' ','d,1':' ','e,1':'8','f,1':' ','g,1':' ','h,1':' ','i,1':' ',\
         'a,2':'8','b,2':' ','c,2':'9','d,2':' ','e,2':'7','f,2':'1','g,2':' ','h,2':'2','i,2':' ',\
         'a,3':'4','b,3':' ','c,3':'3','d,3':'5','e,3':' ','f,3':' ','g,3':' ','h,3':' ','i,3':'1',\
         'a,4':' ','b,4':' ','c,4':' ','d,4':'1','e,4':' ','f,4':' ','g,4':' ','h,4':' ','i,4':'7',\
         'a,5':' ','b,5':' ','c,5':'2','d,5':' ','e,5':'3','f,5':'4','g,5':' ','h,5':'8','i,5':' ',\
         'a,6':'7','b,6':'3','c,6':' ','d,6':' ','e,6':' ','f,6':'9','g,6':' ','h,6':' ','i,6':'4',\
         'a,7':'9','b,7':' ','c,7':' ','d,7':' ','e,7':' ','f,7':' ','g,7':'7','h,7':' ','i,7':'2',\
         'a,8':' ','b,8':' ','c,8':'8','d,8':'2','e,8':' ','f,8':'5','g,8':' ','h,8':'9','i,8':' ',\
         'a,9':'1','b,9':' ','c,9':' ','d,9':' ','e,9':'4','f,9':' ','g,9':'3','h,9':' ','i,9':' '},\
         {'a,1':'1','b,1':' ','c,1':' ','d,1':'4','e,1':'8','f,1':'9','g,1':' ','h,1':' ','i,1':'6',\
         'a,2':'7','b,2':'3','c,2':' ','d,2':' ','e,2':'5','f,2':' ','g,2':' ','h,2':'4','i,2':' ',\
         'a,3':'4','b,3':'6','c,3':' ','d,3':' ','e,3':' ','f,3':'1','g,3':'2','h,3':'9','i,3':'5',\
         'a,4':'3','b,4':'8','c,4':'7','d,4':'1','e,4':'2','f,4':' ','g,4':'6','h,4':' ','i,4':' ',\
         'a,5':'5','b,5':' ','c,5':'1','d,5':'7','e,5':' ','f,5':'3','g,5':' ','h,5':' ','i,5':'8',\
         'a,6':' ','b,6':'4','c,6':'6','d,6':' ','e,6':'9','f,6':'5','g,6':'7','h,6':'1','i,6':' ',\
         'a,7':'9','b,7':'1','c,7':'4','d,7':'6','e,7':' ','f,7':' ','g,7':' ','h,7':'8','i,7':' ',\
         'a,8':' ','b,8':'2','c,8':' ','d,8':' ','e,8':'4','f,8':' ','g,8':' ','h,8':'3','i,8':'7',\
         'a,9':'8','b,9':' ','c,9':'3','d,9':'5','e,9':'1','f,9':'2','g,9':' ','h,9':' ','i,9':'4'},\
         {'a,1':'5','b,1':'3','c,1':' ','d,1':' ','e,1':'7','f,1':' ','g,1':' ','h,1':' ','i,1':' ',\
         'a,2':'6','b,2':' ','c,2':' ','d,2':'1','e,2':'9','f,2':'5','g,2':' ','h,2':' ','i,2':' ',\
         'a,3':' ','b,3':'9','c,3':'8','d,3':' ','e,3':' ','f,3':' ','g,3':' ','h,3':'6','i,3':' ',\
         'a,4':'8','b,4':' ','c,4':' ','d,4':' ','e,4':'6','f,4':' ','g,4':' ','h,4':' ','i,4':'3',\
         'a,5':'4','b,5':' ','c,5':' ','d,5':'8','e,5':' ','f,5':'3','g,5':' ','h,5':' ','i,5':'1',\
         'a,6':'7','b,6':' ','c,6':' ','d,6':' ','e,6':'2','f,6':' ','g,6':' ','h,6':' ','i,6':'6',\
         'a,7':' ','b,7':'6','c,7':' ','d,7':' ','e,7':' ','f,7':' ','g,7':'2','h,7':'8','i,7':' ',\
         'a,8':' ','b,8':' ','c,8':' ','d,8':'4','e,8':'1','f,8':'9','g,8':' ','h,8':' ','i,8':'5',\
         'a,9':' ','b,9':' ','c,9':' ','d,9':' ','e,9':'8','f,9':' ','g,9':' ','h,9':'7','i,9':'9'}]
answer=[{'a,1':'2','b,1':'1','c,1':'7','d,1':'6','e,1':'8','f,1':'3','g,1':'5','h,1':'4','i,1':'9',\
        'a,2':'8','b,2':'5','c,2':'9','d,2':'4','e,2':'7','f,2':'1','g,2':'6','h,2':'2','i,2':'3',\
        'a,3':'4','b,3':'6','c,3':'3','d,3':'5','e,3':'9','f,3':'2','g,3':'8','h,3':'7','i,3':'1',\
        'a,4':'5','b,4':'8','c,4':'4','d,4':'1','e,4':'2','f,4':'6','g,4':'9','h,4':'3','i,4':'7',\
        'a,5':'6','b,5':'9','c,5':'2','d,5':'7','e,5':'3','f,5':'4','g,5':'1','h,5':'8','i,5':'5',\
        'a,6':'7','b,6':'3','c,6':'1','d,6':'8','e,6':'5','f,6':'9','g,6':'2','h,6':'6','i,6':'4',\
        'a,7':'9','b,7':'4','c,7':'5','d,7':'3','e,7':'6','f,7':'8','g,7':'7','h,7':'1','i,7':'2',\
        'a,8':'3','b,8':'7','c,8':'8','d,8':'2','e,8':'1','f,8':'5','g,8':'4','h,8':'9','i,8':'6',\
        'a,9':'1','b,9':'2','c,9':'6','d,9':'9','e,9':'4','f,9':'7','g,9':'3','h,9':'5','i,9':'8'},\
        {'a,1':'1','b,1':'5','c,1':'2','d,1':'4','e,1':'8','f,1':'9','g,1':'3','h,1':'7','i,1':'6',\
        'a,2':'7','b,2':'3','c,2':'9','d,2':'2','e,2':'5','f,2':'6','g,2':'8','h,2':'4','i,2':'1',\
        'a,3':'4','b,3':'6','c,3':'8','d,3':'3','e,3':'7','f,3':'1','g,3':'2','h,3':'9','i,3':'5',\
        'a,4':'3','b,4':'8','c,4':'7','d,4':'1','e,4':'2','f,4':'4','g,4':'6','h,4':'5','i,4':'9',\
        'a,5':'5','b,5':'9','c,5':'1','d,5':'7','e,5':'6','f,5':'3','g,5':'4','h,5':'2','i,5':'8',\
        'a,6':'2','b,6':'4','c,6':'6','d,6':'8','e,6':'9','f,6':'5','g,6':'7','h,6':'1','i,6':'3',\
        'a,7':'9','b,7':'1','c,7':'4','d,7':'6','e,7':'3','f,7':'7','g,7':'5','h,7':'8','i,7':'2',\
        'a,8':'6','b,8':'2','c,8':'5','d,8':'9','e,8':'4','f,8':'8','g,8':'1','h,8':'3','i,8':'7',\
        'a,9':'8','b,9':'7','c,9':'3','d,9':'5','e,9':'1','f,9':'2','g,9':'9','h,9':'6','i,9':'4'},\
        {'a,1':'5','b,1':'3','c,1':'4','d,1':'6','e,1':'7','f,1':'8','g,1':'9','h,1':'1','i,1':'2',\
        'a,2':'6','b,2':'7','c,2':'2','d,2':'1','e,2':'9','f,2':'5','g,2':'3','h,2':'4','i,2':'8',\
        'a,3':'1','b,3':'9','c,3':'8','d,3':'3','e,3':'4','f,3':'2','g,3':'5','h,3':'6','i,3':'7',\
        'a,4':'8','b,4':'5','c,4':'9','d,4':'7','e,4':'6','f,4':'1','g,4':'4','h,4':'2','i,4':'3',\
        'a,5':'4','b,5':'2','c,5':'6','d,5':'8','e,5':'5','f,5':'3','g,5':'7','h,5':'9','i,5':'1',\
        'a,6':'7','b,6':'1','c,6':'3','d,6':'9','e,6':'2','f,6':'4','g,6':'8','h,6':'5','i,6':'6',\
        'a,7':'9','b,7':'6','c,7':'1','d,7':'5','e,7':'3','f,7':'7','g,7':'2','h,7':'8','i,7':'4',\
        'a,8':'2','b,8':'8','c,8':'7','d,8':'4','e,8':'1','f,8':'9','g,8':'6','h,8':'3','i,8':'5',\
        'a,9':'3','b,9':'4','c,9':'5','d,9':'2','e,9':'8','f,9':'6','g,9':'1','h,9':'7','i,9':'9'}]
keys=['a,1', 'b,1', 'c,1','d,1', 'e,1', 'f,1','g,1', 'h,1', 'i,1',\
      'a,2', 'b,2', 'c,2','d,2', 'e,2', 'f,2','g,2', 'h,2', 'i,2',\
      'a,3', 'b,3', 'c,3','d,3', 'e,3', 'f,3','g,3', 'h,3', 'i,3',\
      'a,4', 'b,4', 'c,4','d,4', 'e,4', 'f,4','g,4', 'h,4', 'i,4',\
      'a,5', 'b,5', 'c,5','d,5', 'e,5', 'f,5','g,5', 'h,5', 'i,5',\
      'a,6', 'b,6', 'c,6','d,6', 'e,6', 'f,6','g,6', 'h,6', 'i,6',\
      'a,7', 'b,7', 'c,7','d,7', 'e,7', 'f,7','g,7', 'h,7', 'i,7',\
      'a,8', 'b,8', 'c,8','d,8', 'e,8', 'f,8','g,8', 'h,8', 'i,8',\
      'a,9', 'b,9', 'c,9','d,9', 'e,9', 'f,9','g,9', 'h,9', 'i,9']
valid=['1','2','3','4','5','6','7','8','9']
#global variables for rock,paper,scissors
option=0
#initiator
start()
