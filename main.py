from random import randint

END_GAME = 2001


def dice():
    result = 0
    for _ in range(2):
        result += randint(1, 6)
    return result


def throw():
    player_1 = dice()
    computer = dice()
    print(f'Twój rzut: {player_1}')
    print(f'Rzut przeciwnika: {computer}')
    return player_1, computer


def game():
    P1_SCORE = 0
    CPU_SCORE = 0
    ROUND = 0

    print("Naciśnij 'enter', by rzucić lub 'q', aby zakończyć")
    while P1_SCORE <= END_GAME and CPU_SCORE <= END_GAME:
        start = input()
        if start == 'q':
            break
        p1_score, cpu_score = throw()
        if ROUND > 0:
            if p1_score == 7:
                P1_SCORE = int(P1_SCORE / 7)
            elif p1_score == 11:
                P1_SCORE = P1_SCORE * 11
            else:
                P1_SCORE += p1_score
            if cpu_score == 7:
                CPU_SCORE = int(CPU_SCORE / 7)
            elif p1_score == 11:
                CPU_SCORE = CPU_SCORE * 11
            else:
                CPU_SCORE += cpu_score
        else:
            P1_SCORE += p1_score
            CPU_SCORE += cpu_score
        ROUND += 1
        print('-----')
        print(f'Twój wynik: {P1_SCORE}')
        print(f'Wynik przeciwnika: {CPU_SCORE}')
        print()

    if P1_SCORE > CPU_SCORE:
        print('Wygrywasz!')
    else:
        print('Przeciwnik wygrywa!')


if __name__ == '__main__':
    game()
