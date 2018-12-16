from Stat import Stat

teams_arr = []
teams_map = {}


def count_scores(wins, draws):
    return 3 * wins + draws


def fill_team_map():
    for team in teams_arr:
        if team[0] not in teams_map:
            teams_map[team[0]] = Stat(0, 0, 0, 0, 0)

        if team[2] not in teams_map:
            teams_map[team[2]] = Stat(0, 0, 0, 0, 0)


number_of_teams = int(input())

while number_of_teams > 0:
    line = input().split(";")
    line[1] = int(line[1])
    line[3] = int(line[3])
    teams_arr.append(line)
    number_of_teams -= 1

fill_team_map()

for team in teams_arr:

    first_win = 0
    first_lost = 0

    second_win = 0
    second_lost = 0

    draw = 0

    if team[1] > team[3]:
        first_win = 1
        second_lost = 1

    elif team[1] < team[3]:
        first_lost = 1
        second_win = 1

    elif team[1] == team[3]:
        draw = 1

    first_stat = teams_map[team[0]]
    second_stat = teams_map[team[2]]

    first_stat.games += 1
    first_stat.wins += first_win
    first_stat.draw += draw
    first_stat.loses += first_lost
    first_stat.scores = count_scores(first_stat.wins, first_stat.draw)

    second_stat.games += 1
    second_stat.wins += second_win
    second_stat.draw += draw
    second_stat.loses += second_lost
    second_stat.scores = count_scores(second_stat.wins, second_stat.draw)

for team, stat in teams_map.items():
    print(team, ":", end='', sep='')
    print(stat.games, stat.wins, stat.draw, stat.loses, stat.scores)
