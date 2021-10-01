# Two teams were playing a football (soccer) match and the record of events for each team is available.
# There are 4 possible events, Goal (G), Yellow Card (Y), Red Card (R) and Substitution (S).
# The first three events (G, Y, R) are represented as player-name time event-name
#  whereas the last event (S) is represented as player-name time event-name second-player-name.
# . The time is represented in minutes from the start of the game. A football game is divided into two halves of 45 minutes each,
#  and sometimes a little extra time is given at the end of each half, which is represented in the time as
# time+extra-time. . So, there can be two types of times, for example, 32 and 45 + 2. . The extra time is always considered to have
# occurred before the events of the next half, so, 45 + 2 happened earlier than 46.

# Merge the events for each team into a single game event with teams name in front and sorted by time and event in order of G, Y, R, S.
# In the case of the same event happening at the same time, output should be sorted lexicographically based on teams name and players name.

import re


def getEventsOrder(team1, team2, events1, events2):
    # Write your code here
    football = list()
    football.append({"team": team1, "event": events1})
    football.append({"team": team2, "event": events2})

    game_details_list = list()
    original_event = list()
    event_priority = ["G", "Y", "R", "S"]

    for f in football:
        for event in f["event"]:
            original_event.append(f["team"] + " " + event)

            # split events string to get details
            pattern = re.compile("([a-zA-Z\s]*)(\d+)[+]?(\d*).([G,Y,R,S])([a-zA-Z\s]*)")
            split_event = pattern.search(event)

            # create a list of format ["team name", "player name", "time", "extra time", "event", "second player name"]
            record = list()
            record.append(f["team"])  # team name
            if split_event:
                record.append(split_event.group(1).strip())  # player name
                record.append(int(split_event.group(2).strip()))  # time
                record.append(
                    int(split_event.group(3).strip())
                    if len(split_event.group(3).strip()) > 0
                    else 0
                )  # extra time
                record.append(
                    event_priority.index(split_event.group(4).strip())
                )  # event
                record.append(split_event.group(5).strip())  # second player
            game_details_list.append(record)

    # sorting the list to return index position of the sorted list
    new_num_index_sorted = sorted(
        range(len(game_details_list)),
        key=lambda k: (
            game_details_list[k][2],  # time
            game_details_list[k][3],  # extra time
            game_details_list[k][4],  # event
            game_details_list[k][0],  # team name
            game_details_list[k][1],  # player name
            game_details_list[k][5],
        ),
    )

    # based on the index position, fetching result from original event list and appending in answer
    answer = list()
    for i in new_num_index_sorted:
        answer.append(original_event[i])
    return answer


if __name__ == "__main__":
    print(
        getEventsOrder(
            "Team1",
            "Team2",
            ["Team1 1+0 G", "Team1 1+0 Y", "Team1 1+0 R", "Team1 1+0 S", "Team1 1+0 G"],
            ["Team2 1+0 G", "Team2 1+0 Y", "Team2 1+0 R", "Team2 1+0 S", "Team2 1+0 G"],
        )
    )
