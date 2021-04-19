import string

if __name__ == '__main__':
    with open('/tmp/p022_names.txt', 'r', encoding='utf8') as f:
        names = [z.lower().strip('"') for z in f.read().strip().split(",")]

    names.sort()
    char_score = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}


    def score(w):
        return sum(map(char_score.get, w))


    total = sum(i * score(word) for i, word in enumerate(names, start=1))

    print(score('colin'))
    print(names.index('colin'))
    print(total)
