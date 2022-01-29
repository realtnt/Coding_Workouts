'''
    
codewars

7 kyu

Triple Crown

'''


def triple_crown(players):
    yards, touchdowns, receptions = 0, 0, 0
    plr_yards, plr_touchdowns, plr_receptions = '', '', ''
    for player in players.keys():
        tmp_yards = players[player]['Receiving yards']
        if tmp_yards > yards:
            yards = tmp_yards
            plr_yards = player
        elif tmp_yards == yards:
            return('None of them')

        tmp_touchdowns = players[player]['Receiving touchdowns']
        if tmp_touchdowns > touchdowns:
            touchdowns = tmp_touchdowns
            plr_touchdowns = player
        elif tmp_touchdowns == touchdowns:
            return('None of them')

        tmp_receptions = players[player]['Receptions']
        if tmp_receptions > receptions:
            receptions = tmp_receptions
            plr_receptions = player
        elif tmp_receptions == receptions:
            return('None of them')

    if plr_yards == plr_touchdowns == plr_receptions:
        return(plr_yards)
    else:
        return('None of them')
