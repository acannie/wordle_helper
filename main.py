def rec(word, i, tmp, word_length):
    if i == (word_length - 1):
        print(tmp)
        return

    for c in word:
        if tmp.count(c) >= word.count(c):
            continue
        rec(word, i+1, tmp+c, word_length)


def main():
    word = input()
    word_length = len(word)

    for c in word:
        rec(word, 0, c, word_length)


if __name__ == "__main__":
    main()
