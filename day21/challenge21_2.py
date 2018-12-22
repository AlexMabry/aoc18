three, four, previous = 0, 0, 0
answers = set()
while True:
    three = four | 0x10000
    four = 0xA1068B

    while True:
        four = (four + (three % 0x100)) % 0x1000000
        four = (four * 0x1016B) % 0x1000000

        if three < 256:
            break
        else:
            three = three // 256

    if four in answers:
        print(previous)
        exit()
    else:
        previous = four
        answers.add(four)
