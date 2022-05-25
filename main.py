import string
import urllib.request

url_prefix = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def record_word(word):
    url = url_prefix + word
    req = urllib.request.Request(url)

    try:
        url = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        return

    file_name = "ok.txt"
    with open(file_name, "a")as f:
        f.write(word + "\n")


def rec(i, tmp, word_length):
    if i == (word_length - 1):
        record_word(tmp)
        return

    for alphabet in string.ascii_uppercase:
        rec(i+1, tmp+alphabet, word_length)


def main():
    word_length = 5

    for alphabet in string.ascii_uppercase:
        rec(0, alphabet, word_length)


if __name__ == "__main__":
    record_word("test")
    record_word("apple")
    main()
