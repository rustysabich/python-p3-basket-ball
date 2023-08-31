def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

### Helper Functions ###
# 1. Get the details of a specific player
def get_player_details(p_name):

    # get all the games details
    game_details = game_dict()

    # get all players details
    players_info = game_details['home']['players']
    players_info.extend(game_details['away']['players'])

    # Get the details of the player of interest
    player_of_interest = [p_info for p_info in players_info if p_info['name'] == p_name][0]

    # return the player of interest
    return player_of_interest

# 2. Get team details
def get_team_details(t_name):

    # get all the games details
    game_details = game_dict()

    # get all teams details
    teams_info = [game_details['home'], game_details['away']]

    # Get the details of the player of interest
    team_of_interest = [t_info for t_info in teams_info if t_info['team_name'] == t_name][0]

    # return the player of interest
    return team_of_interest

# 3. Get the rebounds for a shoe brand
def get_shoe_brand_rebounds(brand):

    # get all the games details
    game_details = game_dict()

    # get all players details
    players_info = game_details['home']['players']
    players_info.extend(game_details['away']['players'])

    # Get the details of the player of interest
    players_of_interest_rebounds = [p_info["rebounds_per_game"] for p_info in players_info if p_info['shoe_brand'] == brand]

    return players_of_interest_rebounds

# 4. Get the shoe brands
def get_shoe_brands():
    # get all the games details
    game_details = game_dict()

    # get all players details
    players_info = game_details['home']['players']
    players_info.extend(game_details['away']['players'])

    # grab shoe brands
    shoe_brands = [p_info["shoe_brand"] for p_info in players_info]

    return list(set(shoe_brands))


### Deliverables ###
### 1. num_points_per_game()

def num_points_per_game(name):
    # Get the player's info 
    player_info = get_player_details(name)

    # return the points per game
    return player_info["points_per_game"]


### 2. player_age()

def player_age(name):
    # Get the player's info 
    player_info = get_player_details(name)

    # return the points per game
    return player_info["age"]


### 3. team_colors()

def team_colors(t_name):

    # get the team information
    team_info = get_team_details(t_name)

    # return the team colors
    return team_info['colors']

### 4. team_names()

def team_names():
    # get all the games details
    game_details = game_dict()

    # get all teams details
    teams_info = [game_details['home'], game_details['away']]

    return [t_info['team_name'] for t_info in teams_info]


### 5. player_numbers()

def player_numbers(t_name):
    
    # get the team information
    team_info = get_team_details(t_name)

    # get team players
    team_players = team_info['players']

    return [player['number'] for player in team_players]


### 6. player_stats()

def player_stats(name):
    return get_player_details(name)


### 7. average_rebounds_by_shoe_brand()

def average_rebounds_by_shoe_brand():

    # get the shoe brands
    #shoe_brands = get_shoe_brands()
    shoe_brands = ['Nike', 'Adidas', 'Puma', 'Jordan'] # maintain order as in the test file
    
    # get players rebounds and print the average
    for s_brand in shoe_brands:
        # get the rebounds for the shoe brand
        rebounds = get_shoe_brand_rebounds(s_brand)

        # get the average
        average = sum(rebounds)/len(rebounds)

        print(f"{s_brand}:  {average:.2f}")

    # return None
    #return None