



def numPaths(n, t):
    def countSumPaths(n, l, sofar):
        if n == None:
            return sofar

        l_cp = [x+n.data for x in l] + [n.data]
        num_left = countSumPaths(n.left, l_cp, sofar + sum(1 if x == t else 0 for x in l_cp))

        r_cp = [x+n.data for x in l] + [n.data]
        num_right = countSumPaths(n.right, r_cp, sofar + sum(1 if x == t else 0 for x in r_cp))

        return num_left + num_right


    return countSumPaths(n, [], 0)



# TODO the beter way of doing it
