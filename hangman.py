import sys
from random import randint
from urllib.request import urlopen


hang_dict = {
    0: ' \n \n \n \n ',
    1: ' \n \n \n \n∆',
    2: ' \n \n \n|\n∆',
    3: ' \n \n|\n|\n∆',
    4: ' \n|\n|\n|\n∆',
    5: '____\n|\n|\n|\n∆',
    6: '____\n|  @\n|\n|\n∆',
    7: '____\n|  @\n| /\n|\n∆',
    8: '____\n|  @\n| /0\n|\n∆',
    9: '____\n|  @\n| /0\ \n|\n∆',
    10: '____\n|  @\n| /0\ \n|  ∏  \n∆'
}

word_dict = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9:  [],
    10: [],
    11: [],
    12: [],
    13: []
}
length = 0


def main():
    sort_list()
    counter = 0
    ltrs = ""
    wrd = word()
    to_guess_list = []
    for i in range(len(wrd)):
        to_guess_list.append("_ ")
    solut = len(wrd) * "_ "
    print("Hallo,\nHangman, selbsterklärend!")

    while True:
        if counter == 10:
            print(hang_dict[counter])
            sys.exit(f'Verloren! Das gesuchte Wort war "{wrd}"')
        print(hang_dict[counter])
        print(solut, end=" ")
        if ltrs != "":
            print(f"bisherige Buchstaben: {ltrs}")
        s = ""
        letter = input("Buchstabe? ").upper()
        if len(letter) == 1:
            if letter not in ltrs:
                ltrs += letter
                if letter in wrd:
                    for i in range(len(wrd)):
                        if wrd[i] == letter:
                            to_guess_list[i] = letter + " "
                            solut = s.join(to_guess_list)
                            if solution(wrd) == solut:
                                print(wrd)
                                sys.exit("Hurra!")
                else:
                    counter += 1
            else:
                print("Hattest du schon!")
        else:
            print("Nur EIN Buchstabe bitte!")


def sort_list():
    f = urlopen("http://www.netzmafia.de/software/wordlists/deutsch.txt")
    for line in f:
        if len(line) > 13:
            word_dict[13].append(line.rstrip("\n"))
        else:
            word_dict[len(line) - 1].append(line.rstrip("\n"))
            

def solution(x):
    sol = ""
    for i in range(len(x)):
        sol += x[i] + " "
    return sol

def word():
    level = 7
    index = randint(0, len(word_dict[level]))
    word = ((word_dict[level])[index]).upper()
    return word


if __name__ == "__main__":
    main()
