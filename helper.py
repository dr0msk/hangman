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

with open("deutsch.txt", 'r') as f:
    for line in f:
        if len(line) > 13:
            word_dict[13].append(line.rstrip("\n"))
        else:
            word_dict[len(line) - 1].append(line.rstrip("\n"))
