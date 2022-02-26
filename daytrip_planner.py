import random

locations = ['New York', 'Los Angeles', 'Las Vegas', 'Milwaukee', 'Seattle']

eateries = ['The Sticky Menu Diner', 'Mama Mia Italian Ristorante', 'Le Terible Vegan Restaurant', 'The Meat Wagon', 'Shanghai Surprise' ]

modes = ['The Batmobile', 'Tauntaun', 'The USS Enterprise', 'TARDIS', 'That Huge Flying Dog-Thing From The Neverending Story']

shows = ['Wyld Stallyns', 'Sonic Death Monkey', 'Oneders', 'Uptown Girl: An 80s Joel Experience', 'Drive Shaft']

#whew! I was able to cull this down to 2 functions from 8! It wasn't clicking for some reason at first but then I had an epiphany on how to do it while driving around
def sel_rand (list):
   random_sel = random.randint (0, len(list)-1)
   return list [random_sel]


#I am so proud of this one below, it was quite a breakthrough and took over an hour!
def dec_init (list, selection, list_type, list_verb):
    decide_sel=(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a {list_type}, please press "R" '))
    while decide_sel != '':
        selection = sel_rand(list)
        decide_sel = str(input(f'The {list_type} you will be {list_verb} is {selection}, are you satisfied with this selection?  If so, please press ENTER.  If you would like to reselect a {list_type}, please press "R" '))
    return selection

banner = ('***Powered by Radon Technologies (c) 2022  ****** WELCOME TO THE MARC CHERRIES TRIP PLANNER!****** Powered by Radon Technologies (c) 2022 ***')

print (banner)

str(input('Please press ENTER to randomly select a LOCATION for your trip. '))

#start of continuous loop to allow user to restart application
while True:
    loc_res = sel_rand(locations)

    loc_res = dec_init(locations, loc_res, 'LOCATION', 'travelling to')
    
    str(input('Please press ENTER to randomly select an EATERY for your trip. '))

    eat_res = sel_rand(eateries)

    eat_res = dec_init(eateries, eat_res, 'EATERY', 'dining at')

    str(input('Please press ENTER to randomly select a MODE OF TRANSPORTATION for your trip. '))

    mode_res = sel_rand(modes)

    mode_res = dec_init(modes, mode_res, 'MODE OF TRANSPORTATION', 'using')

    str(input('Please press ENTER to randomly select ENTERTAINMENT for your trip. '))

    show_res = sel_rand(shows)

    show_res = dec_init(shows, show_res, 'ENTERTAINMENT', 'enjoying')

    #possible function? only needed it once for this app
    readout = input('Okay! Looks like you have made some nice selections today.  Let us recap, shall we? Please press ENTER to continue ')
    if readout == '':
        print (f'LOCATION:                           {loc_res}')
        print (f'EATERY:                             {eat_res}') 
        print (f'MODE OF TRANSPORTATION:             {mode_res}') 
        print (f'ENTERTAINMENT:                      {show_res}') 

    #possible function? only needed it once for this app
    restart = str(input('Does everything look good to you?  If you are satisfied with these selections, please press ENTER.  If you would like to START OVER, please press "X" '))
    if restart != '':  
        continue
    
    print (f'Congratulations! Your trip is all set. You will be travelling to {loc_res} by way of {mode_res} and dining at the fabulous {eat_res}.  But the fun doesnt end there! You will cap the evening off with a private show preformed by none-other-than the great {show_res}! Have a great time!')
    break

 
    
