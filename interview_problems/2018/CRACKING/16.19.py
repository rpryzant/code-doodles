

# is matrix mutable?
#   no 


# for each point
#   if water and not covered
#      get and record size of that pond
# return all ponds

WATER = 0

OFFSETS = [(1, 0),
           (1, -1),
           (1, 1),
           (0, 1),
           (0, -1),
           (-1, 0),
           (-1, 1),
           (-1, -1)]


def compute_pond_sizes(m):
    def valid(r, c):
        if r < 0 or c < 0:
            return False
        if r >= len(m) or c >= len(m[0]):
            return False
        return True

    def get_neighbors(r, c):
        for rof, cof in OFFSETS:
            if valid(r+rof, c+cof):
                yield rof, cof

    def get_size(r, c, visited):
        size = 0

        if m[r][c] != WATER or (r, c) in visited:
            return size

        visited[r,c] = True
        size += 1

        for r_off, c_off in get_neighbors(r, c):
            if m[r+r_off][c+c_off] == WATER:  # north
                size += get_size(r+r_off, c+c_off, visited)

        return size


    visited = {}
    pond_sizes = []
    for r, row in enumerate(m):
        for c, col in enumerate(row):
            if m[r][c] == 0 and (r, c) not in visited:
                size = get_size(r, c, visited)
                pond_sizes.append(size)
    return pond_sizes

test = [
    [0,2,1,0],
    [0,1,0,1],
    [1,1,0,1],
    [0,1,0,1]]

print compute_pond_sizes(test)
