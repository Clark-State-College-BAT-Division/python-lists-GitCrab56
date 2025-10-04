import   random

#Create two seperate lists for player one and player two. 
#Each one  should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

PlayerOne = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
PlayerTwo = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
PlayerOneWins = 0
PlayerTwoWins = 0
UserInput = input("Please enter 0 to start: ")
RealInput = int(UserInput)

while RealInput >= 0:
    for x in range (10):
        PlayerOne[x] = random.randint(1, 50)
        PlayerTwo[x] = random.randint(1, 50)
        if PlayerOne[x] > PlayerTwo[x]: 
            PlayerOneWins += 1
        elif PlayerTwo[x] > PlayerOne[x]:
            PlayerTwoWins += 1

   
    print(f" Player One = {PlayerOne}")
    print(f" Player Two = {PlayerTwo}")

    print(f" Player One won {PlayerOneWins} times")
    print(f" Player Two won {PlayerTwoWins} times")
    
    MinimumP1 = min(PlayerOne)
    MindexP1 = PlayerOne.index(MinimumP1)
    print(f"Player One's lowest number was {MinimumP1} at index {MindexP1}")
    MaximumP1 = max(PlayerOne)
    MaxdexP1 = PlayerOne.index(MaximumP1)
    print(f"Player One's highest number was {MaximumP1} at index {MaxdexP1}")

  
  
   
    MinimumP2 = min(PlayerTwo)
    MindexP2 = PlayerTwo.index(MinimumP2)
    print(f"Player Two's lowest number was {MinimumP2} at index {MindexP2}")
    MaximumP2 = max(PlayerTwo)
    MaxdexP2 = PlayerTwo.index(MaximumP2)
    print(f"Player Two's highest number was {MaximumP2} at index {MaxdexP2}")
    
    PlayerOneWins = 0
    PlayerTwoWins = 0
    
    UserInput = input("Please Type 0 to continue and -1 to stop: ")
    RealInput =int(UserInput)