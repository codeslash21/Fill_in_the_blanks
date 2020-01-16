import math

#Paragraphs to Play fill_in_the_blanks Game:

paragraph_list = ['''An important goal of ___1___'s developers is making it ___2___ to use. This is reflected in the origin of the name,which comes from Monty ___1___, and in
an occasionally playful approach to tutorials and reference materials, such as using examples that refer to spam and ___3___ instead of the standard ___4___ and bar. ''', 

'''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes byadding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___
if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,tuple, and ___4___ or can be more complicated such as objects and lambda functions.''', 

'''Python ___1___s are available for many operating ___2___, allowing Python code to run on a wide variety of ___2___. Using third-party tools, such as Py2exe or Pyinstaller, Python
code can be ___3___ into stand-alone ___4___ programs for some of the most popular operating ___2___, so Python-based software can be distributed to, 
and used on, those environments with no need to ___5___ a Python ___1___.''']

#Answer to the Blanks:

answer_list = [["Python", "fun", "eggs", "foo"],
               ["function", "parameters", "None", "list"],
               ["interpreter", "systems", "packaged", "excecutable", "install"]]

#Numbering of Blanks:

blank_list = [['___1___', '___2___', '___3___', '___4___' ],
              ['___1___', '___2___', '___3___', '___4___' ],
              ['___1___', '___2___', '___3___', '___4___', '___5___']]

#Levels of the Game:

levels = ['EASY', 'MEDIUM', 'HARD']

#Welcome Message to the Player:

print('***---------------------------------------------------------------------***')
print('                "WELCOME Back to Fill_In_The_Blanks Game"')
print('***---------------------------------------------------------------------***')
print()

#Build the main function of the Game:

def main():
    Play = True
    while Play == True:
        INDEX = get_level(levels)
        total_guesses = set_guess()
        play_game(paragraph_list,answer_list,blank_list,total_guesses,INDEX)
        Play = play_more()
        

#Get the Level from the Player:--
#--------------------------------

def get_level(levels):
    print('GAME LEVELS : "EASY"  "MEDIUM"  "HARD" ')
    user_level = input('Enter Your Level :- ').upper()
    L = False
    while L !=True:
        L1 = 0
        if user_level in levels:
            L1 = 1
        if L1 == 1:
            print('______OK, so You want to play "'+user_level+'" level_______')
            print()
            L = True
        else:
            user_level = input('Please, enter the valid level:-  ').upper()
    indx = levels.index(user_level)
    return indx

#Check total_guess is valid or not:

def valid_guess(total_guess):
    if (0< total_guess <=20) != True:
        return False
    else:
        return True

#Get total_guess from Player:

def set_guess() :
    total_guess = input('You can use upto 20 guesses. How many guess you want to use? :-  ')
    t = False
    while t != True:
        try:
            if round(float(total_guess)) != float(total_guess) or valid_guess(float(total_guess)) != True:
                total_guess = input('Please enter a valid input under 20 :-  ')
            else:
                t = True
   
        except:
            total_guess = input('Please enter a valid input under 20 :-  ')
    print()
    print('Ok, you will get '+total_guess+'guesses to fill in all the blanks.')
    print()
    return int(total_guess)

# Build check_guess Function:

def check_guess(guess,ans):
    try:
        guess = float(guess)
        T = False
    except:
        T = True
    if T == True:
        if ans.lower() in guess.lower():
            return True
        else:
            return False
    else:
        return False

# Build Success Message:

def success_message(paragraph,guess,blank_left,used_guess):
    print()
    print('Success!! "'+guess+'" is correct!')
    print()
    print('The updated paragraph is : ')
    print("___________________________________________________________")
    print(paragraph)
    if blank_left == 0 :
        print()
        print("Wow, You're good!!! You filled in all the blanks correctly with "+str(used_guess)+" guesses.")

# Build Wrong Message:

def wrong_message(guess,guess_left):
    if guess_left == 0:
        print()
        print('Ohh No!! the blank is not "'+str(guess)+'" and you have no more guesses left. Game over :)')
    else:
        print()
        print('Ohh No!! the blank is not "'+str(guess)+'" and you have "'+str(guess_left)+'" guesses left.')
        
#Build play_game Function:

def play_game(paragraph_list,answer_list,blank_list,total_guesses,INDEX):
    guess_left = total_guesses
    blanks = blank_list[INDEX]
    answers = answer_list[INDEX]
    blank_left = len(blanks)
    paragraph = paragraph_list[INDEX]
    print('---------------||  Your Paragraph Is Here!! ||--------------')
    print()
    print(paragraph)
    print()
    print('_______________: Fill Up The Blanks Correctly : _______________')
    for ans in answers:
        current_blank = blanks[answers.index(ans)]
        print()
        while guess_left != 0:
            guess = input('Guess what should be in place of "'+current_blank+'" :__ ')
            guess_left = guess_left - 1
            if check_guess(guess,ans) == True:
                blank_left = blank_left - 1
                used_guess = total_guesses - guess_left
                paragraph = paragraph.replace(current_blank,ans)
                success_message(paragraph,guess,blank_left,used_guess)
                break
            else:
                wrong_message(guess,guess_left)
                    
# Build play_more:

def play_more():
    print()
    print('__________________"Thanks For Playing"___________________')
    print()
    res = input("Are you want to play game again : 'YES' OR 'NO' -  ")
    print()
    if res.upper() == "YES" :
        print("OK, Let's start.")
        return True
    else:
        print("OK, Good Bye. Hope see you soon.")
        return False



main()


