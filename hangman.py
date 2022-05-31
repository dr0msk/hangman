import helper
import sys
from random import randint

def main():
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
            print(helper.hang_dict[counter])
            sys.exit(f'Verloren! Das gesuchte Wort war "{wrd}"')
        print(helper.hang_dict[counter])
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


def solution(x):
    sol = ""
    for i in range(len(x)):
        sol += x[i] + " "
    return sol

def word():
    level = 7
    index = randint(0, len(helper.word_dict[level]))
    word = ((helper.word_dict[level])[index]).upper()
    return word

if __name__ == "__main__":
    main()
