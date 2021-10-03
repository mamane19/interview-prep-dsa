def labyrinthEscape2(n, m, obstacles, teleports):
    obs = set()
    for x, y in obstacles:
        obs.add((x, y))
    t = {}
    for sx, sy, ex, ey in teleports:
        t[(sx, sy)] = (ex, ey)
    cur_x = cur_y = 0
    visited = set()
    moves = n * m
    while moves > 0:
        if cur_y >= m:
            cur_y -= 1
            cur_x += 1
        if cur_x >= n or (cur_x, cur_y) in visited:
            return False
        elif cur_x == n - 1 and cur_y == m - 1:
            return True
        visited.add((cur_x, cur_y))
        if (cur_x, cur_y + 1) in obs:
            if (cur_x + 1, cur_y) in obs:
                return False
            else:
                if (cur_x + 1, cur_y) in t:
                    cur_x, cur_y = t[(cur_x + 1, cur_y)]
                else:
                    cur_x += 1
        else:
            if (cur_x, cur_y + 1) in t:
                cur_x, cur_y = t[(cur_x, cur_y + 1)]
            else:
                cur_y += 1
        moves -= 1
    return False
