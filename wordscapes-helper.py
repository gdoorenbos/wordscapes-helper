import sys

with open("words_alpha.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english_word(word):
    return word.lower() in english_words
    
def main():
    while True:
        word_pool = input('word pool: ')
        word_len = int(input('length of word: '))
        word_hint = input('word hints: ').lower()
        matches = []
        for word in english_words:
            if len(word) == word_len:
                word_fits = True
                for i in range(word_len):
                    if word[i] not in word_pool:
                        word_fits = False
                        break
                    if word_hint[i] != '_' and word_hint[i] != word[i]:
                        word_fits = False
                        break

                if word_fits:
                    for letter in word:
                        letter_count = len([x for x in word if x == letter])
                        pool_count = len([x for x in word_pool if x == letter])
                        if letter_count > pool_count:
                            word_fits = False
                            break

                    if word_fits:
                        matches.append(word)

        print('matches: {}'.format(matches))

if __name__ == '__main__':
    main()