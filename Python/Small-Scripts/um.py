import re


def main():
    print(count(input("Text: ")))


def count(s):
    word = r"((?:^|[^a-zA-Z])um(?:[^a-zA-Z]|$))"
    matches = re.findall(word, s.lower())
    return len(matches)


if __name__ == "__main__":
    main()