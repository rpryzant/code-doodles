

# is matrix mutable?
#   no 


# for each point
#   if water and not covered
#      get and record size of that pond
# return all ponds

WATER = 0


def compute_pond_sizes(m):
    def get_neighbors(r, c):
        r_offsets = [0]
        if r > 0:
            r_offsets += [-1]
        if r < len(m[0])-1:
            r_offsets += [1]

        c_offsets = [0]
        if c > 0:
            c_offsets += [-1]
        if c < len(m)-1:
            c_offsets += [1]

        for roff in r_offsets:
            for coff in c_offsets:
                if roff == 0 and coff == 0:
                    continue
                yield roff, coff

    def get_size(r, c, visited):
        size = 0

        if m[r][c] != WATER or (r, c) in visited:
            return size

        visited[r,c] = True
        size += 1

        for r_off, c_off in get_neighbors(r, c):
            if r == 1 and c == 2:
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
