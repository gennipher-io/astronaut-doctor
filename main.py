import time
import random
from os import system, name

# define our clear function
def clear():
  # for windows
  if name == 'nt':
    _ = system('cls')
  
  # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')

def happy_dance():
  clear()
  print("""
         _____
  ___/     \___
  `-._)     (_,-`
     \O _ O/
       \ - /  BOOP
        )-
       ||
      _||_
     |-..-|
     |/. \|
  \\ |\__/| //
   ._|//\\|_,
   `-((  ))-'
    __\\//__ 
    >_ /\ _<,
      ''
    """)
  time.sleep(1)
  clear()

  print("""
         _____
 ___/     \___
`-._)     (_,-`
    \O _ O/
     \ - /
      `-(
       ||
      _||_
     |-..-|
     |/. \|
     |\__/|
   ._|//\\|_,
   `-((  ))-'
    __\\//__ 
    >_ /\ _<,
      ''
    """)
  time.sleep(1)
  clear()
  print("""
         _____
  ___/     \___
  `-._)     (_,-`
     \O _ O/
       \ - /  BOOP
        `)-
       ||
      _||_
     |-..-|
     |/. \|
  \\ |\__/| //
   ._|//\\|_,
   `-((  ))-'
    __\\//__ 
    >_ /\ _<,
      ''
    """)
  time.sleep(1)
  clear()
  print("""
         _____
 ___/     \___
`-._)     (_,-`
    \O _ O/
     \ - /
      `-(
       ||
      _||_
     |-..-|
     |/. \|
     |\__/|
   ._|//\\|_,
   `-((  ))-'
    __\\//__ 
    >_ /\ _<,
      ''
    """)
  time.sleep(5)
  clear()
  

def encounter_sick_inhabitant(medicine_bag,received_gifts):
  """This function is for encountering a sick inhabitant and inquiring
  about their symptoms."""

  print("You've encountered a sick inhabitant")
  time.sleep(2)
  print()
  print("They're not looking so well")
  time.sleep(2)
  print()
  print("You offer to treat their symptoms")
  time.sleep(2)
  print()
  print("Make sure to log their symptoms in your logbook...")
  print()
  input("Press ENTER to continue...")

  has_flu="no"
  has_flu=(check_symptoms(medicine_bag,received_gifts,has_flu))
  
  if has_flu=="yes":
    administer_medicine(has_flu,medicine_bag,received_gifts)
  if has_flu=="no":
    administer_joke()



def check_symptoms(medicine_bag,received_gifts,has_flu):
  """This funciton will take a list of symptoms and compare them to some
  dictionaries to identify ailment and right medicine to use"""

  symptom_list=[]

  clear()
  print("""
      __________________   __________________
.-/|    Astronaut    \ /                  |\-.
||||     Doctor's      |                   ||||
||||     Logbook       |       ~~*~~       ||||
||||    --==*==--      |                   ||||
||||                   |                   ||||
||||                   |                   ||||
||||                   |     --==*==--     ||||
||||                   |                   ||||
||||                   |                   ||||
||||                   |                   ||||
||||   Raelyn Ricks    |                   ||||
||||__________________ | __________________||||
||/===================\|/===================\||
`--------------------~___~-------------------''
  """)
  while True:
    print()
    symptom=input("What symptoms is the patient exhibiting? (Press q to stop) >>> ")
    if symptom=="q":
      break
    else:
      symptom_list.append(symptom)

  print("Logging symptoms...")
  time.sleep(5)
  clear()
  has_flu=(check_for_flu(symptom_list))
  return has_flu

def check_for_flu(symptoms):
  """Confirm if they have the flu and need to be treated"""

  flu=("fever", "chills", "body aches", "diarhhea", "runny nose", "sore throat", "headache", "fatigue")
  result="no"
  print("Astronaut Doctor Raelyn Ricks: Let's verify their symptoms, they are:")
  for symptom in symptoms:
    if any(symptom in i for i in flu):
      print(symptom, "- That is a symptom of the flu... Let's be cautious and treat them.")
      result="yes"
      break
    else:
      print(symptom, "- That is not a symptom of the flu...")
      result="no"
  print()
  input("Press ENTER to contiue...")
  clear()
  return result


def administer_joke():
  """This funciton will provide a joke to try and cheer up the inhabitant
     v2 of the game I would like to expand this function to read random 
     jokes from a joke file!"""
  print("Maybe they're just feeling a bit down. Let's see if we can cheer them up with a funny joke.")
  print()
  print("Why did the chicken cross the road...")
  print()
  input("Press ENTER to contiue...")

def administer_medicine(flu, medicine_bag,received_gifts):
  """This funciton will distribute appropriate medicine to inhabitant
  It will also reduce your medical items"""
  print("We should have something to help them, let's check our medicine bag...")
  print()
  print("~~~rUfFlinG In bAg~~~")
  print()
  print("""
   mmm
   )-(
  (   )     
  |   |
  |   |
  |___|
  """)

  use=''
  print("Here's what Raelyn has in her bag:")
  print()
  for items in medicine_bag:
    print(items, ':', medicine_bag[items])
  print()

  check="false"
  while check=="false":
    use=str.lower(input("What do you want to treat them with? >>> "))
    if use in medicine_bag:
      check="true"
    else:
      print("That item is not in your bag")
      check="false"

  enough=(medicine_bag.get(use))

  medicine_bag[use]=medicine_bag[use]-1
  if medicine_bag[use]==0:
    del medicine_bag[use]
    print("      NOTE: You are out of {}".format(use), "now")

  print()
  print("...")
  time.sleep(3)



def receive_gift(received_gifts,items_needed,gifts):
  """This function will keep track of your gifts received and sort
  Them into appropriate dictionaries based on if it's a needed spaceshuttle 
  item or not a needed spaceshuttle item. This is also where we check
  for completed spaceshuttle item list"""

  received=""
  happy_dance()
  print("They seem to be feeling better!")
  print()
  print("They are offering you a gift...")
  received=random.choice(gifts)
  print("You received a {}".format(received))
  print()
  received_gifts.append(received)
  print("Here are the items you've received so far:")
  for gift in received_gifts:
    print(gift)
  if received in items_needed:
    items_needed.remove(received)
  gifts.remove(received)
  print()
  if len(items_needed)>0:
    print("You are not ready to repair your ship. Here are the items you still need:")
    for item in items_needed:
      print(item)
  print()
  input("Press ENTER to contiue...")


def ready_to_repair(items_needed):
  """This function checks if you're ready to repair your ship or not, do you
  have all the necessary items?"""

  if len(items_needed)==0:
    return True
  else:
    return False

  

def go_explore(medicine_bag,received_gifts,items_needed,gifts):
  """This is the main driver of the game"""
  clear()
  
  print("""Astronaut Doctor Raelyn has decided to go explore...


               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
  """)
  time.sleep(2)
  encounter_sick_inhabitant(medicine_bag,received_gifts)
  receive_gift(received_gifts,items_needed,gifts)

def repair_ship():
  """This function will repair the ship and ask the player if they want
  to continue treating sick inhabitants until their medicine bag is empty
  or leave the planet to head home"""
  clear()
  print("CONGRATULATIONS!")
  print("You and Astronaut Doctor Raelyn Ricks have repaired the ship...")
  print()
  input("Press ENTER for BLASTOFF!")
  clear()
  print("""BLASTOFF!!
                                       _,'/
                                  _.-''._:
                          ,-:`-.-'    .:.|
                         ;-.''       .::.|
          _..------.._  / (:.       .:::.|
       ,'.   .. . .  .`/  : :.     .::::.|
     ,'. .    .  .   ./    \ ::. .::::::.|
   ,'. .  .    .   . /      `.,,::::::::.;\
  /  .            . /       ,',';_::::::,:_:
 / . .  .   .      /      ,',','::`--'':;._;
: .             . /     ,',',':::::::_:'_,'
|..  .   .   .   /    ,',','::::::_:'_,'
|.              /,-. /,',':::::_:'_,'
| ..    .    . /) /-:/,'::::_:',-'
: . .     .   // / ,'):::_:',' ;
 \ .   .     // /,' /,-.','  ./
  \ . .  `::./,// ,'' ,'   . /
   `. .   . `;;;,/_.'' . . ,'
    ,`. .   :;;' `:.  .  ,'
   /   `-._,'  ..  ` _.-'
  (     _,'``------''  
   `--'
  """)
time.sleep(10)


#define your items for the game
medicine_bag={"motrin": 2,
              "chicken soup": 4,
              "box of tissue": 3}

gifts=["teddy bear","wrench", "door", "sucker"]

received_gifts=[]

items_needed=["door", "wrench"] 

print("""
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                             .                   .
         .              .                  .           .
          0     .
                 .          .                 ,                ,    ,
 .          \          .                         .
      .      \   ,
   .          o     .                 .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #  #O##\###                .                        .
   .        #*#  #\##\###                       .                     ,
        .   ##*#  #\##\##               .                     .
      .      ##*#  #o##\#         .                             ,       .
          .     *#  #\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^           ^^ ^  '\ ^          ^   Astronaut Doctor!
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __
      """)
time.sleep(5)
print("Raelyn wakes to rubble and ruin...")
time.sleep(3)
print("Her spaceshuttle crash landed on a planet")
time.sleep(3)
print("There are lots of repairs to make")
print("Good thing Astronaut Doctor Raelyn Ricks knows a thing or two about spaceshuttles!")
time.sleep(5)
print("She'll need to explore her surroundings for useful items to make repairs...")
time.sleep(3)
print("With a grin, Astronaut Doctor Raelyn Ricks thinks to herself:")
time.sleep(3)
clear()
print("""
 /////////////\\\\
(((((((((((((( \\\\
))) ~~      ~~  (((    These repairs
((( (*)     (*) )))
)))     <       (((     should be
((( '\______/`  )))
)))\___________/(((      easy peasy
       _) (_   +
      / \_/ \     ~  *     lemon squeezy! 
     /(     )\ (|)
    // )___( \\//          
    \\ (     )
     (       )
      |  |  |
       | | |
       | | |
      _|_|_|_
""")
time.sleep(5)
username=''
age=''

clear()

print("""
 /////////////\\\\
(((((((((((((( \\\\
))) ~~      ~~  (((    
((( (*)     (*) )))
)))     <       (((     
((( '\______/`  )))
)))\___________/(((      
       _) (_   +
      / \_/ \     ~  *      
     /(     )\ (|)
    // )___( \\//          
    \\ (     )
     (       )
      |  |  |
       | | |
       | | |
      _|_|_|_
""")

print("Astronaut Doctor Raelyn Ricks: Hi there!")
time.sleep(3)
username=input("Astronaut Doctor Raelyn Ricks: My name is Dr. Raelyn Ricks, what's yours? >>> ")
print("Astronaut Doctor Raelyn Ricks: It's great to meet you, {}".format(username))
time.sleep(3)
age=input("Astronaut Doctor Raelyn Ricks: How old are you? >>> ")
time.sleep(3)
print("Astronaut Doctor Raelyn Ricks: Wow! You've made {}".format(age), "trips around your sun. That's impressive!")
time.sleep(3)
print("Astronaut Doctor Raelyn Ricks: With that many years under your belt, you must be very smart.")
time.sleep(3)
answer=input("Astronaut Doctor Raelyn Ricks: Would you like to be my assistant? (Y/N) >>> ")
clear()
if answer=="N" or answer=="n":
  print("Astronaut Doctor Raelyn Ricks: Come back when you're ready to assist! Bye!")
  exit(0)
if answer=="Y" or answer=="y":
  print("Astronaut Doctor Raelyn Ricks: Great, this planet looks like it has inhabitants.")
  print("Maybe they have something useful for repairs. Let's get going!")
  print()
  input("Press ENTER to continue...")

while not ready_to_repair(items_needed):
  go_explore(medicine_bag,received_gifts,items_needed,gifts)

repair_ship()


