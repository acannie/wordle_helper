import string


def rec(i, tmp, word_length):
    if i == (word_length - 1):
        print(tmp)
        return

    for alphabet in string.ascii_uppercase:
        rec(i+1, tmp+alphabet, word_length)


def main():
    word_length = 5

    for alphabet in string.ascii_uppercase:
        rec(0, alphabet, word_length)


if __name__ == "__main__":
    main()
