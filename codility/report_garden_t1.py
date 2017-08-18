# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, S, T):
    ships = S.split(',')
    targets = T.split(' ')
    sea_map = [[0 for i in xrange(26)] for ii in xrange(N)]

    # Populate the sea map with sea locations
    for i in xrange(len(ships)):
        ship_location = ships[i].split(' ')
        t_left = ship_location[0]
        b_right = ship_location[1]

        start_i = int(t_left[0])-1
        end_i = int(b_right[0])-1

        start_j = int(ord(t_left[1])-65)
        end_j = int(ord(b_right[1])-65)

        # print start_i, end_i, start_j, end_j

        for j in xrange(start_i, end_i+1):
            for jj in xrange(start_j, end_j+1):
                sea_map[j][jj] = 1

    # Mark the map with targets 'X' i,e. -1
    for target in targets:
        t_i = int(target[0])-1
        t_j = int(ord(target[1])-65)
        sea_map[t_i][t_j] = -1

    # Validate if a ship has been sunk or just hit.
    ships_hit, ships_sunk = 0, 0
    for l in xrange(len(ships)):
        ship_location = ships[l].split(' ')
        t_left = ship_location[0]
        b_right = ship_location[1]

        start_i = int(t_left[0])-1
        end_i = int(b_right[0])-1

        start_j = int(ord(t_left[1])-65)
        end_j = int(ord(b_right[1])-65)

        ship_sunk, ship_hit = True, False

        for ll in xrange(start_i, end_i+1):
            for lll in xrange(start_j, end_j+1):
                if(sea_map[ll][lll] == -1):
                    ship_hit = True
                else:
                    ship_sunk = False

        if ship_sunk:
            ships_sunk += 1
        elif ship_hit:
            ships_hit += 1

    return str(ships_sunk) + ',' + str(ships_hit)
