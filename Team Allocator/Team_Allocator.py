import random
#["Martin", "Craig", "Sue", "Claire", "Dave", "Alice", "Sonakshi", "Harry",
#         "Jack", "Rose", "Lexi", "Maria", "Thomas", "James", "William", "Ada",
#         "Grace", "Jean", "Marissa", "Alan", "Tansy"]
print("Welcome to Team Allocator!")
while True:
    players = []
    teams = []

    number_of_players = int(input("How many players are there? "))
    for i in range(1, number_of_players + 1):
        players.append(i)
    random.shuffle(players)
    response = input("Is it a team or individual sport? \
                    \nType team or ind: ")
    if response == "team":
        number_of_teams = int(input("How many teams do you need? "))
        for i in range(1, number_of_teams +1):
            teams.append(i)

        if number_of_players % number_of_teams == 0:
            for team in teams:
                print("\nTeam " + str(team) + ":")
                print(players[(number_of_players//number_of_teams)*(team-1):\
                              (number_of_players//number_of_teams)*team])
                print("Team Captain: " + str(random.choice\
                                             (players[(number_of_players//number_of_teams)\
                                                      *(team-1):\
                                                      (number_of_players//number_of_teams)\
                                                      *team])))
        else:
            print("The number of players cannot be divided equally into teams.")
            
    else:
        for i in range(0, number_of_players, 2):
            print(str(players[i]) + " vs " + str(players[i+1]))
            start = random.randrange(i, i+2)
            print(str(players[start]) + " starts\n")
    response = input("\nStart again? Type y or n: ")
    if response == "n":
        break
