import random

locations = ['New York', 'Los Angeles', 'Las Vegas', 'Milwaukee', 'Seattle']

eateries = ['The Sticky Menu Diner', 'Mama Mia Italian Ristorante', 'Le Terible Vegan Restaurant', 'The Meat Wagon', 'Shanghai Surprise' ]

modes = ['Ferrari', 'Limousine', 'Luxury Train', 'Helicopter', 'Schooner']

shows = ['Dave Chappelle', 'Joe Rogan', 'Neil Young', 'Barbara Streisand', 'Aaron Rodgers']

def loc_sel_rand (loc_list):
   random_loc = random.randint (0, len(loc_list)-1)
   return loc_list [random_loc]

def eat_sel_rand (eat_list):
   random_eat = random.randint (0, len(eat_list)-1)
   return eat_list [random_eat]

def mode_sel_rand (mode_list):
   random_mode = random.randint (0, len(mode_list)-1)
   return mode_list [random_mode]

def show_sel_rand (show_list):
   random_show = random.randint (0, len(show_list)-1)
   return show_list [random_show]

banner = ('***Powered by Radon Technologies (c) 2022  ****** WELCOME TO THE MARC CHERRIES TRIP PLANNER!****** Powered by Radon Technologies (c) 2022 ***')

print (banner)

str(input('Please press ENTER to randomly select a LOCATION for your trip. '))

#start of continuous loop to allow user to restart application
while True:
    loc_res = loc_sel_rand(locations)

    decide_loc=(input(f'The LOCATION you will be travelling to is {loc_res}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a LOCATION, please press "R" '))

    while decide_loc != '':
        loc_res = loc_sel_rand(locations)
        decide_loc = str(input(f'The LOCATION you will be travelling to is {loc_res}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a LOCATION, please press "R" '))

    str(input('Please press ENTER to randomly select an EATERY for your trip. '))

    eat_res = eat_sel_rand(eateries)

    decide_eat = str(input(f'The EATERY you will be dining at is {eat_res}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect an EATERY, please press "R" '))

    while decide_eat != '':
        eat_res = eat_sel_rand(eateries)
        decide_eat = str(input(f'The EATERY you will be dining at is {eat_res}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect an EATERY, please press "R" '))

    str(input('Please press ENTER to randomly select a MODE OF TRANSPORTATION for your trip. '))

    mode_res = mode_sel_rand(modes)

    decide_mode = str(input(f'The MODE OF TRANSPORTATION you will be using is {mode_res}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a MODE OF TRANSPORTATION, please press "R" '))

    while decide_mode != '':
        mode_res = mode_sel_rand(modes)
        decide_mode = str(input(f'The MODE OF TRANSPORTATION you will be using is {mode_res}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a MODE OF TRANSPORTATION, please press "R" '))

    str(input('Please press ENTER to randomly select ENTERTAINMENT for your trip. '))

    show_res = show_sel_rand(shows)

    decide_show = str(input(f'The ENTERTAINMENT you will be seeing is {show_res}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a show, please press "R" '))

    while decide_show != '':  
        show_res = show_sel_rand(shows)
        decide_show = str(input(f'The ENTERTAINMENT you will be seeing is {show_res}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect ENTERTRAINMENT, please press "R" '))

    readout = input('Okay! Looks like you have made some nice selections today.  Let us recap, shall we? Please press ENTER to continue ')
    if readout == '':
        print (f'LOCATION:                           {loc_res}') 
        print (f'EATERY:                             {eat_res}') 
        print (f'MODE OF TRANSPORTATION:             {mode_res}') 
        print (f'ENTERTRAINMENT:                     {show_res}') 

    restart = str(input('Does everything look good to you?  If you are satisfied with these selections, please press ENTER.  If you would like to START OVER, please press "X" '))
    if restart != '':  
        continue
    #changing this to 'not equal empty string' instead of  == x made it work.  Need to learn more about this.
    
    print (f'Congratulations! Your trip is all set. You will be travelling to {loc_res} by way of {mode_res} and dining at the fabulous {eat_res}.  But the fun doesnt end there! You will cap the evening off with a private show preformed by none-other-than the great {show_res}! Have a great time!')
    break

    #Questions for the instructors during code review:
    #str() on inputs
    #main while loop/break/continue
    #whitespace
    #.upper
    #ascii art
    #apostrophes in strings
    
