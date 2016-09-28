def mutateSentences(sentence):
    """
    High-level idea: generate sentences similar to a given sentence.
    Given a sentence (sequence of words), return a list of all possible
    alternative sentences of the same length, where each pair of adjacent words
    also occurs in the original sentence. (The words within each pair should appear 
    in the same order in the output sentence as they did in the orignal sentence.)
    Notes:
    - The order of the sentences you output doesn't matter.
    - You must not output duplicates.
    - Your generated sentence can use a word in the original sentence more than
      once.
    """
    def dfs(result, sofar, bigrams, depth):
        if depth > len(bigrams):
            result.append(' '.join(w for w in sofar))
            return
        for bigram in bigrams:
            if len(sofar) == 0:
                sofar = bigram
                dfs(result, sofar, bigrams, depth + 1)
                sofar = []
            elif sofar[-1] == bigram[0]:
                sofar.append(bigram[1])
                dfs(result, sofar, bigrams, depth + 1)
                sofar.pop()
        return result
    chunks = sentence.split(' ')
    bigrams = [chunks[i:i+2] for i in range(len(chunks) - 1)]
    mutations = dfs([], [], bigrams, 1)
    return list(set(mutations))



print mutateSentences('the cat and the mouse')
print mutateSentences('a a a a a')
print mutateSentences('the cat')
