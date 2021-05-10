import argparse

with open("words_alpha.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def solve_old(pool, word_len, clue=None):
    # fix up clue
    if clue is None:
        clue = '_' * word_len
    clue = clue.lower()

    # start with words of correct length
    words = [w for w in english_words if len(w) == word_len]

    # filter out words with letters not in the pool
    words = [w for w in words if all(l in pool for l in w)]

    # filter out words that have more letters than available in the pool
    words = [w for w in words if all(w.count(l) <= pool.count(l) for l in w)]

    # filter out words that dont match the clue
    words = [w for w in words if all(h in ('_', l) for h, l in zip(clue, w))]

    # done. return sorted results
    return sorted(words)

def get_combs(comblen, pool, start=''):
    if comblen == 1:
        combs = []
        for letter in pool:
            combs.append(start + letter)
        return combs

    combs = []
    for i, e in enumerate(pool):
        nustart = start + e
        nupool = [x for j, x in enumerate(pool) if i != j]
        combs += get_combs(comblen - 1, nupool, nustart)

    return combs

def solve_new(pool, word_len, clue=None):
    # fix up clue
    if clue is None:
        clue = '_' * word_len
    clue = clue.lower()

    # find all letter combinations of desired length
    words = get_combs(word_len, pool)

    # filter out words that arent english
    words = [w for w in words if w in english_words]

    # filter out words that dont match the clue
    words = [w for w in words if all(h in ('_', l) for h, l in zip(clue, w))]

    # return sorted words
    return sorted(words)

def solve(pool, word_len, clue=None):
    #return solve_old(pool, word_len, clue)
    return solve_new(pool, word_len, clue)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--letter-pool', required=True, type=str)
    parser.add_argument('-l', '--word-length', required=True, type=int)
    parser.add_argument('-c', '--clue', type=str)
    args = parser.parse_args()

    matches = solve(args.letter_pool, args.word_length, args.clue)
    print('matches: {}'.format(matches))

