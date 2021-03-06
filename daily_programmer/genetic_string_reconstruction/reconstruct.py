import sys
import random
import string

# returns random char
def random_char():
    return random.choice(string.printable)

# returns a random string with length equal to param
def random_str(length):
    return ''.join(random_char() for _ in range(length))


# returns fitness of str w/r/t target (negative hamming distance of str & target)
def fitness(str, target):
    return sum(a == b for a, b in zip(str, target))

# mixes the material of two strings to produce a recombinatnt/mutated offspring
# TODO: use proper crossover masks for crossing over...make point mutations seperate
def mate(a, b):
    mutation_rate = 1.0 / len(a) 
    child = ''
    # uniform crossover / point mutationish type thing 
    for c1, c2 in zip(a, b):
        if random.random() < mutation_rate:
            child += random_char()
        else:
            child += random.choice([c1, c2])
    return child

target = sys.argv[1]
# pop size conditional on target size b/c complex hypothesis spaces (e.g. large targets)
# benefit from more initial search points, -  we're more likely to end up with better 
# starting guesses. 
population_size = len(target) * 50
population = [random_str(len(target)) for _ in range(population_size)]

# since hamming distance is fitness metric, am negating fitness so that the "max" fitness is still maximal
max_fitness = -1e10
gen = 1
while max_fitness < len(target):
    # 66% of progeny come from top 2 parents
    

    parent_1 = max(population, key = lambda x: fitness(x, target))
    max_fitness = fitness(parent_1, target)
    population.remove(parent_1)
    parent_2 = max(population, key = lambda x: fitness(x, target))
    population = [mate(parent_1, parent_2) for _ in range(population_size * 2 / 3 )]

    print "Generation: %s | Fitness: %s | %s" % (gen, max_fitness, parent_1)
    gen += 1

