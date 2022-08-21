import csv, random
from math import *
import matplotlib.pyplot as plt


# These functions are used in the beginning
def new_csv_list() :
    '''This method will take the given csv PokeList and add 2 more columns to use throughout the program and return a newly formated list while
    printing out that newly formatted csv file.'''

    # rewrite pokelist with a 'Current CP' and a 'Current Level' column
    # opens the PokeList.csv file and reads all info into a list
    file = open('PokeList.csv','r')
    poke_list_reader = csv.reader(file,delimiter = ',')
    orig_poke_list = list(poke_list_reader)
    file.close()

    # creating my new_PokeList.csv file to use throughout the program
    file = open('new_PokeList.csv','w',newline = '')
    file_writer = csv.writer(file,delimiter = ',')

    # this is the first row with the column headers
    file_writer.writerow([orig_poke_list[0][0], orig_poke_list[0][1], orig_poke_list[0][2], orig_poke_list[0][3],'Current CP','Level','Rarity'])

    # for loop populating the new csv file with the additional defaul valus of '{min cp value} and the default level '1' value
    for i in range(len(orig_poke_list)) :
     # this if statement determines the rarity of each pokemon
     if i != 0 :
        if int(orig_poke_list[i][2]) < 100 :
         rarity_label = 'Common'
        elif int(orig_poke_list[i][2]) < 200 :
         rarity_label = 'Uncommon'
        elif int(orig_poke_list[i][2]) < 300 :
         rarity_label = 'Rare'
        elif int(orig_poke_list[i][2]) < 400 :
         rarity_label = 'Scarce'
        elif int(orig_poke_list[i][2]) >= 400 :
         rarity_label = 'Legendary'
        else :
         rarity_label = 'IDK'
     if i != 0 :
        file_writer.writerow([orig_poke_list[i][0],orig_poke_list[i][1],orig_poke_list[i][2],orig_poke_list[i][3],orig_poke_list[i][2],'1',rarity_label])
    file.close()

    # reads the new formatted file and storing into a list to return to main program
    file = open('new_PokeList.csv','r')
    file_reader = csv.reader(file,delimiter = ',')
    new_poke_list = list(file_reader)

    # loop reassigns whole new_poke_list with the type values of ints (more efficient than typecasting throughout the whole program
    for i in range(len(new_poke_list)) :
        if i != 0 :
            new_poke_list[i] = [int(new_poke_list[i][0]),new_poke_list[i][1],int(new_poke_list[i][2]),int(new_poke_list[i][3]),int(new_poke_list[i][4]),int(new_poke_list[i][5]),new_poke_list[i][6]]

    return new_poke_list
def create_collections(num_of_users,list) :
    '''This method will create an empty Pokemon collection .csv file for each user in the user list'''
    for i in range(num_of_users) :
     user_file = open('{}.collection.csv'.format(list[i]),'w',newline = '')
     user_writer = csv.writer(user_file,delimiter = ',')
     user_writer.writerow([' {}\'s Pokemon Collection'.format(list[i])])
     user_writer.writerow(['Total Candy : {}'.format('0')])
     user_writer.writerow(['Index','Pokemon Name','CP','Level','Rarity'])
     user_file.close()
def usernames(user_tot) :
    '''This method will ask for each username and return a list of string value of each name.'''
    usernames_list = []
    for num in range(int(user_tot)) :
        name = str(input('\tWhat is User{} username : '.format(num+1)))
        usernames_list.append(name)
    return usernames_list
def total_users() :
    '''This method simply ask user in the beginning of the program how many users will be played and return that number.'''

    try :
        num = int(input('\nHow many users will be playing "Gotta Catch One of \'Em" (No more than 3): '))
    except ValueError :
        num = int(input('\nTry again.\nHow many users will be playing "Gotta Catch One of \'Em" (No more than 3): '))
        while num < 1 :
            num = int(
                input('\nTry again.\nHow many users will be playing "Gotta Catch One of \'Em" (No more than 3): '))

    while num > 3 :
        print('Please try again. ')
        num = int(input('How many users will be playing "Gotta Catch One of \'Em" (No more than 3): '))
    list = usernames(num)
    return num, list

# ----------------------------------------------------------------

# Start Method
def start(num_of_users,list_of_users,poke_list) :
    '''This method creates a PokeList for each user and assigns a random pokemon to each collection.csv file.'''
    create_collections(num_of_users, list_of_users)
    for i in range(1) :  # populates with 1 random pokemon
        rand_Poke_append(num_of_users, list_of_users,poke_list)
# Mini Methods
def rand_Poke_append(num_of_users,list_of_users,poke_list) :
    '''This method appends a new line on the users PokemonCollection.csv file with a random pokemon from the PokeList.
        ONLY USE TO APPEND WITH POKEMON INFO FROM THE POKELIST, NOT FROM ANOTHER USERS COLLECTION.'''
    for i in range(num_of_users) :
        random_Poke = random.randint(1, 150)
        user_file = open('{}.collection.csv'.format(list_of_users[i]),'r')
        user_file_reader = csv.reader(user_file,delimiter = ',')
        user_file_len = len(list(user_file_reader))
        #print(list(user_file_reader))
        user_file.close()
        index = user_file_len - 2 #- (user_file_len - 3)
        new_Poke_info = [index, poke_list[random_Poke][1], poke_list[random_Poke][4], poke_list[random_Poke][5],poke_list[random_Poke][6]]
        append_pokemon(list_of_users[i], new_Poke_info)

# ----------------------------------------------------------------

# Main Menu Loop
def main_menu():
    '''This method is just a string format for the Main Menu of the Program.'''

    print('\n------------------------Main Menu--------------------------',
          '\n\t1. Play Gotta Catch One of \'Em (Single Player) ',
          '\n\t2. Battle in Gotta Catch One of \'Em (Double Player)',
          '\n\t3. Quit Gotta Catch One of \'Em ')
    print('-----------------------------------------------------------')
    return input('\nChoose from one of the options above (1-3) : ')

# Mini Methods
def user_menu(list_of_users) :
    '''This method prints out a user menu to select from and returns the string of the username    '''
    print('\n-------------------Select Your Username--------------------')
    string = ''
    for i in range(len(list_of_users)) :
        string += '{}. {}\n'.format(i+1,list_of_users[i])
    print(string)
    print('-----------------------------------------------------------')
    inp = input('\nChoose from one of the options above (1-{}) : '.format(len(list_of_users)))
    return list_of_users[int(inp)-1]


# ----------------------------------------------------------------

# Play Method
def play(username,poke_list) :
    '''This method begins the 'Play' part of the program that is a single player function and loops until they
       decide to go back to the main menu'''
    user_menu_input = ''

    while user_menu_input != 'menu' :
        user_menu_input = play_menu()
        if user_menu_input == '1' :
            view_collection(username)
        elif user_menu_input == '2' :
            candy = total_candy(username)
            print_candy(candy)
        elif user_menu_input == '3' :
            level_up(username)
        elif user_menu_input == '4' :
            catch(username,poke_list)
        elif user_menu_input == '5' :
            break

# Mini Methods
def play_menu():
    '''This method is just a string format for the Play Menu of the Program.
       It returns the num val according to the options.'''

    print('\n------------------------User Menu--------------------------',
          '\n\t1. View Pokemon Collection ',
          '\n\t2. Candy Total',
          '\n\t3. Level Up Pokemon ',
          '\n\t4. Catch a new Pokemon',
          '\n\t5. Back to Main Menu')

    print('-----------------------------------------------------------')
    return input('\nChoose from one of the options above (1-5) : ')
def view_collection(username) :
    '''This method will print the Collection list or the certain pokemon selected based off the input.
    Returns Strings to console'''
    view_inp = True
    while view_inp == True :
        print_pokemon(username) # this prints the whole collection
        inp = input('\nDo you want to view a certain Pokemon (yes/no) : ')
        if inp == 'yes' :
            index = int(input('What Pokemon would you like to view (Index #) : '))
            print_pokemon(username,index)
            break
        elif inp == 'no' :
            inp_two = input('Do you want to go back to User Menu (yes/no) : ')
            if inp_two == 'yes' :
                #view_inp == False
                break
        else :
            print('Please try again.')
def print_candy(total) :
    '''This method will print the candy menu'''
    total = int(total)
    print('\n-----------------------Candy Total-------------------------',
          '\n\tCandy Total :', str(total),
          '\n Levels 1 - 30 cost 2 candy | Levels 31 - 40 cost 5 candy ',
          '\n-----------------------------------------------------------')


#           LEVEL UP METHODS
def level_up(username) :
    '''This method will run the level up funciton.'''
    level_inp = ''
    while level_inp != 'no' :

        print('-------------------------Level Up--------------------------\n')
        print_pokemon(username)
        print()
        level_inp = (input('Would you like to level up a Pokemon (yes/no) : '))
        if level_inp == 'yes' :
            poke_index = int(input('What Pokemon would you like to level up : '))
            poke_list = users_coll(username)
            index = poke_index + 2
            level = int(poke_level(username,poke_index))
            if level <= 30 :
                candy = 2
                total_candy(username,candy,True,True)
                poke_list = users_coll(username)
                new_lev = level + 1
                poke_list[index][3] = new_lev
                new_cp = float(poke_list[index][2]) + float(cp_30(username, new_lev,poke_index))
                poke_list[index][2] = new_cp
                user_file = open('{}.collection.csv'.format(username), 'w', newline='')
                file_writer = csv.writer(user_file, delimiter=',')
                for line in poke_list:
                    file_writer.writerow(line)
                user_file.close()

            elif level > 30 and level < 40:
                candy = 5
                total_candy(username,candy,True,True)
                poke_list = users_coll(username)
                new_lev = level + 1
                poke_list[index][3] = new_lev
                new_cp = float(poke_list[index][2]) + float(cp_30(username, new_lev,poke_index))
                poke_list[index][2] = new_cp
                user_file = open('{}.collection.csv'.format(username), 'w', newline='')
                file_writer = csv.writer(user_file, delimiter=',')
                for line in poke_list:
                    file_writer.writerow(line)
                user_file.close()
            else :
                print('The pokemon is at the max level 40.')
            poke_list = users_coll_list(username)
            index = poke_index - 1
            print('-------------------------Level Up--------------------------',
                  '\nPokemon {} \n\t\tName : {} \n\t\tCP : {} \n\t\tLevel : {} \n\t\t',
                  'Rarity : {}'.format(poke_index, poke_list[index][1],poke_list[index][2],poke_list[index][3],poke_list[index][4]))


def cp_30(username, level, poke_index) :
    '''This method calculates the cp increase.'''
    list = users_coll(username)
    index = poke_index + 2
    cp = float(list[index][2])
    new_cp = (cp *  0.0093) / (0.094 * sqrt(level))
    new_cp = '{:.2}'.format(new_cp)
    new_cp = float(new_cp)
    return new_cp

def cp_40(username, level, poke_index) :
    '''This method calculates the cp increase.'''
    list = users_coll(username)
    index = poke_index + 2
    cp = float(list[index][2])
    new_cp = (cp *  0.0044) / (0.094 * sqrt(level))
    new_cp = '{:.2}'.format(new_cp)
    new_cp = float(new_cp)
    return new_cp


def poke_level(username,poke_index) :
    '''This method returns the level of a certain pokemon from a users collection.'''
    list = users_coll(username)
    index = poke_index+2
    level = list[index][3]
    return level






# catch methods
#possibly reassign the pokemon list with another value column of rareity(like 1-4 based on min cp)

def rarity_target(rarity_label) :
    '''This method recieves a rarity label and returns the size of the target for the catch game.'''
    if rarity_label == 'Common' :
        rarity_size = 50
    elif rarity_label == 'Uncommon' :
        rarity_size = 40
    elif rarity_label == 'Rare' :
        rarity_size = 30
    elif rarity_label == 'Scarce' :
        rarity_size = 20
    elif rarity_label == 'Legendary' :
        rarity_size = 10
    else :
        rarity_size = 100
    return rarity_size
def rand_Poke(username,poke_list) :
    '''This method will take a user and it's collection and return a random pokemon list value from the
       pokemon list and assign it with the correct index value if it were to be appended to the users colleciton'''
    random_Poke = random.randint(1, 150)
    user_file = open('{}.collection.csv'.format(username),'r')
    user_file_reader = csv.reader(user_file,delimiter = ',')
    user_file_len = len(list(user_file_reader))
    #print(list(user_file_reader))
    user_file.close()
    index = user_file_len - 2 #- (user_file_len - 3)
    new_Poke_info = [index, poke_list[random_Poke][1], poke_list[random_Poke][4], poke_list[random_Poke][5],poke_list[random_Poke][6], rarity_target(poke_list[random_Poke][6])]
    # the last value of the pokemon object is the diameter of the target for the graph to be caught
    return new_Poke_info



def get_basics():
   """Takes user selections for active bird and planet. Returns (bird, planet). 'Bird' includes
      name, color and size. 'Planet' includes name and gravity. """
   #a = bird_picker()                                  # Runs fn to provide bird menu
   b = ['Earth',9.807]                                # Runs fn to provide planet menu
   return b
def trajectory_y(x, g, vo, angle):
   """Returns (y-value) of the trajectory for a given x-val, gravity, initial velocity,and angle."""
   angle = radians(angle)
   return (x*tan(angle))-(g*x**2)/(2*(vo**2)*cos(angle)**2)
def get_guesses() :
   '''This method will ask the user for their guess input.'''
   print('Enter the following variables below.')
   inp_one = float(input('Input an Initial Velocity : '))
   inp_two = float(input('Input an Initial Theta : '))
   return inp_one,inp_two
def trajectory(g, v_guess, theta_guess) :
   '''This method will calculate the x and y values of the 'catch'.'''
   gravity = g[1]
   y = 0
   x = 0
   x_list = []
   y_list = []

   while y >=0 :
      x_list.append(x)
      y_list.append(y)
      x += 2
      y = trajectory_y(x, gravity, v_guess, theta_guess)
      #print(x_list)
      #print(y_list)
   return x_list, y_list
def hit(x, y, target) :
   '''This method calculates based on the target size if the trajectory will hit the target. This returns a boolean value.'''
   target_x = target[0]
   target_y = target[1]
   target_size = (target[2][5] / 2)
   target_left_x = target_x - target_size
   target_right_x = target_x + target_size

   target_up_y = target_y + target_size
   target_down_y = target_y - target_size

   hit_bool = False

   for i in range(len(x)) :
      if target_left_x <= x[i] <= target_right_x :
         if target_up_y >= y[i] >= target_down_y :
            hit_bool = True

   return hit_bool
def orig_plot(target, bool = False) :
   '''This method will just display the graph before the user guesses.'''
   if target[2][4] == 'Common' :
      color = 'gray'
   if target[2][4] == 'Uncommon':
       color = 'yellow'
   if target[2][4] == 'Rare':
       color = 'aqua'
   if target[2][4] == 'Scarce':
       color = 'magenta'
   if target[2][4] == 'Legendary':
       color = 'crimson'

   name = target[2][1]

   if bool == False :
      figure, axes = plt.subplots()
      draw_circle = plt.Circle((target[0], target[1]), target[2][5],color = color)
      plt.xlim(0,1000)
      plt.ylim(0,400)

      axes.set_aspect(1)
      axes.add_artist(draw_circle)
      plt.title('Catch a {}!'.format(name))
      plt.show()

def poke_plot(x, y, target, bool = False) :
   '''This method will take in the necessary x and y values with the target size and color,
   plot the graph, and determine to end the catch game.'''
   if target[2][4] == 'Common' :
      color = 'gray'
   if target[2][4] == 'Uncommon':
       color = 'yellow'
   if target[2][4] == 'Rare':
       color = 'aqua'
   if target[2][4] == 'Scarce':
       color = 'magenta'
   if target[2][4] == 'Legendary':
       color = 'crimson'

   name = target[2][1]

   if bool == False :
      figure, axes = plt.subplots()
      draw_circle = plt.Circle((target[0], target[1]), target[2][5],color = color )
      plt.xlim(0,1000)
      plt.ylim(0,400)
      plt.plot(x, y, '--', markeredgecolor = 'black')

      axes.set_aspect(1)
      axes.add_artist(draw_circle)
      plt.title('Catch a {}!'.format(name))
      plt.show()

   if bool == True :
      figure, axes = plt.subplots()
      #draw_circle = plt.Circle((target[0], target[1]), target[2],color = 'r')
      plt.annotate('X',(target[0],target[1]), c = 'red',size = 20)
      plt.xlim(0,1000)
      plt.ylim(0,400)
      plt.plot(x, y,  '--', markeredgecolor = 'black')

      axes.set_aspect(1)
      #axes.add_artist(draw_circle)
      plt.title('Catch a {}!'.format(name))
      plt.show()
def rand_candy(rarity) :
    '''This method will return the proper candy amount based on rarity of pokemon caught.'''
    if rarity == 'Common' :
        candy = 2
    elif rarity == 'Uncommon' :
        candy = 3
    elif rarity == 'Rare' :
        candy = 5
    elif rarity == 'Scarce' :
        candy = 7
    elif rarity == 'Legendary' :
        candy = 10
    else :
        candy = 100
    return candy
# main method below
def catch(username,poke_list) :
    '''This method executes the 'catch' play option for the user. '''
    pokemon_counter = 0
    again = 'y'
    while again == 'y':

        new_pokemon = rand_Poke(username,poke_list)
        # Program will pick a random distance (x from 10-1000), height (y from 0-50) and size of a target
        target = [random.randint(10, 1000), random.randint(0, 100), new_pokemon]

        orig_plot(target) # this shows the pokemon before they guess

        # Takes initial guesses
        g = get_basics()  # Runs fn to get bird and planet information
        v_guess, theta_guess = get_guesses()  # Runs fn to get velocity and angle guesses

        # Loops guesses until bird hits target
        x, y = trajectory(g, v_guess, theta_guess)  # Create current x- and y- value lists
        guess_counter = 1 # this counts how many times they attempt to catch it
        while not hit(x, y, target) and guess_counter < 3:  # Program cycles until throw hits the target or hit 6 guesses

            guess_counter += 1
            poke_plot(x, y, target)  # Plots trajectory & target of miss
            v_guess, theta_guess = get_guesses()  # Gets updated guesses from user
            x, y = trajectory(g, v_guess, theta_guess)  # Creates updated lists of x- and y-values

        #these two if statements check if they either ran out of guesses or caught the pokemon
        if hit(x, y, target) == True :
            # Handles winning case and asks if user would like to play again
            new_list = target[2][0:5] # this excludes the target list that has the pokemon target size
            append_pokemon(username,new_list)
            add_candy = rand_candy(target[2][4])
            total_candy(username,add_candy,True)
            print('You caught a {}!'.format(target[2][1]))
            pokemon_counter += 1
            poke_plot(x, y, target, True)
            again = input('Would you like to play again? (y/n)')
            while again not in {'y', 'n'}:
                again = input('Please type either y or n only. Would you like to play again? (y/n)')
        elif hit(x, y, target) == False :
            print('You caught nothing.')
            poke_plot(x, y, target)
            again = input('Would you like to play again? (y/n)')
            while again not in {'y', 'n'}:
                again = input('Please type either y or n only. Would you like to play again? (y/n)')

    # Exiting when user decides to quit
    print('\nThanks for playing! You caught %d pokemon(s) today!' % pokemon_counter)


# ----------------------------------------------------------------

# Universal Methods
def users_coll(username) :
    '''This method will return a list data value with a list containing the entire csv in list format'''

    user_file = open('{}.collection.csv'.format(username), 'r')
    file_reader = csv.reader(user_file, delimiter=',')
    users_collection = list(file_reader)
    return users_collection
def create_collection(username,list) :
    '''This method is writing a collections.csv file with given just the line list of the pokemons.'''
    user_file = open('{}.collection.csv'.format(username),'w',newline = '')
    user_writer = csv.writer(user_file,delimiter = ',')
    user_writer.writerow([' {}\'s Pokemon Collection'.format(username)])
    user_writer.writerow(['Total Candy : {}'.format('0')])
    user_writer.writerow(['Index','Pokemon Name','CP','Level','Rarity'])
    #now I am writing the rows of just the pokemon
    for line in list :
        user_writer.writerow(line)
        #print(line)
    user_file.close()
def trade_pokemon(user_loosing,user_gaining,pokemon_index) :
    '''This method lets the user trade to another user. By using the index value of their own pokemon in there list, they choose accordingly.
       After it trades one pokemon to another user, it then deletes that pokemon from the users collection.'''
    # obtains the list of pokemon from the loosing user
    user_loosing_coll = users_coll_list(user_loosing)
    # selects the pokemon of the desired index from the users collection
    index = -1 + pokemon_index
    pokemon = user_loosing_coll[index]
    # changes the pokemons info(specifically the index) to the correct index for the new users collection
    pokemon = poke_line_from_other_user(user_gaining,pokemon)
    # appends the new pokemon modified info to the winning user
    append_pokemon(user_gaining,pokemon)

    #   Now I have to remove the pokemon from the users collection that lost the pokemon
    remove_pokemon(user_loosing, pokemon_index)
    #   Now I have to reassign the index values of that collection
    reassign_index_collection(user_loosing)
def total_candy(username, new_candy = 0, bool = False, neg = False) :
    '''This method will read how many candies are recorded in the csv file. If the extra parameters are filled, then
       the candy total is edited.'''
    user_file = open('{}.collection.csv'.format(username),'r')
    file_reader = csv.reader(user_file,delimiter = ',')
    user_list = list(file_reader)
    user_file.close()
    value = user_list[1][0]
    candy = value.split(':')
    candy = candy[1].strip()
    candy = int(candy)
    if bool == True :
        if neg :
            candy_total = candy - new_candy
        #candy_total = candy + new_candy
        user_list[1][0] = 'Total Candy : {}'.format(candy_total)
        user_file = open('{}.collection.csv'.format(username),'w',newline = '')
        file_writer = csv.writer(user_file,delimiter = ',')
        for line in user_list :
            file_writer.writerow(line)
        user_file.close()
    return int(candy)
# def edit_candy(username, new_candy) :
#     '''This method will take a candy amount and calculate and edit the user's csv file to reprint with
#        the correct amount.'''
#     candy_total = total_candy(username)
#     candy_total = candy_total + new_candy
#
#     user_list = users_coll(username)


# Mini Methods
def users_coll_list(username) : #this changes collection if you add lines before index 1 of pokemon
    '''This method will return a list data value with a list containing only pokemon data in each element'''

    user_file = open('{}.collection.csv'.format(username),'r')
    file_reader = csv.reader(user_file,delimiter = ',')
    users_collection = list(file_reader)
    users_collection = users_collection[3:len(users_collection)]
    return users_collection
def reassign_index_collection(username) :
    '''This method will reassign the users collection list with the correct indexes of each pokemons index if one is added/removed'''
    poke_list = users_coll_list(username)
    counter = 0
    for i in range(len(poke_list)) :
        counter += 1
        poke_list[i] = [counter,poke_list[i][1],poke_list[i][2],poke_list[i][3]]
    create_collection(username,poke_list)
def poke_line_from_other_user(username,poke_info) :
    '''This method converts the line from another users collection.csv to the proper format of the users(taking into
    account the necessary index) and return a list that can be appended to that collection.'''
    user_file = open('{}.collection.csv'.format(username), 'r')
    user_file_reader = csv.reader(user_file, delimiter=',')
    user_file_len = len(list(user_file_reader))
    user_file.close()
    index = user_file_len - 2
    new_Poke_info = [index,poke_info[1],poke_info[2],poke_info[3]]
    return new_Poke_info
def append_pokemon(username,new_Pokemon) :
    '''Taking a username and the new pokemon info, it appends a new line to the users collection.'''
    user_file = open('{}.collection.csv'.format(username), 'a', newline='')
    user_append = csv.writer(user_file, delimiter=',')
    user_append.writerow(new_Pokemon)
    user_file.close()
def remove_pokemon(user_loosing,pokemon_index) :
    '''This method will take the user who is going to loose a pokemon, that pokemons index from the csv, and the remove
       that line from the .csv file and rewrite the file.'''
    user_file = open('{}.collection.csv'.format(user_loosing), 'r')
    file_reader = csv.reader(user_file, delimiter=',')
    users_list = list(file_reader)
    pokemon_list_index = pokemon_index + 1
    users_list.pop(pokemon_list_index)
    user_file.close()
    user_file = open('{}.collection.csv'.format(user_loosing),'w',newline='')
    file_writer = csv.writer(user_file,delimiter = ',')
    for line in users_list :
        file_writer.writerow(line)
    user_file.close()
def print_pokemon(username,poke_index = -1) :
    '''This method either prints a specific pokemon from a users collection based off it's given index or prints the entire collection.'''
    if poke_index > 0 :
        poke_list = users_coll_list(username)
        index = poke_index - 1
        print('\nPokemon {} \n\t\tName : {} \n\t\tCP : {} \n\t\tLevel : {} \n\t\tRarity : {}'.format(poke_index, poke_list[index][1], poke_list[index][2],poke_list[index][3],poke_list[index][4]))

    else :
        poke_list = users_coll_list(username)
        print('     {}\'s'.format(username).center(40))
        print('-----------------Pokemon Collection-----------------------')
        for i in range(len(poke_list)) :
            print('Pokemon {} : Name : {} | CP : {} '.format(poke_list[i][0],poke_list[i][1],poke_list[i][2]))
        print('----------------------------------------------------------')




#                                                   MAIN PROGRAM

# Start of the program


poke_list = new_csv_list() #                                    Creates the PokeList
pokemon_orig_list = poke_list

num_of_users,list_of_users = total_users() #  Returns the # of users and a list of their usernames

start(num_of_users,list_of_users,poke_list) #  Creates each users collection with a random Pokemon appended from PokeList




#       Main Menu Loop
main_menu_inp = ''

while main_menu_inp != '3' :

    main_menu_inp = main_menu()

    if main_menu_inp == '1' : # PLAY
        username = user_menu(list_of_users)
        play(username,poke_list)
    elif main_menu_inp == '2' :
        print('Sadly, this was not completed.')



#            User Quits Game
print('\n-----------------------------------------------------------',
      '\n\t\tThank you for playing "Gotta Catch One of \'Em"',
      '\n-----------------------------------------------------------')