matrix = [0]*13
j = 11
q = 12
k = 13
a = 14
def formatInput():
    with open('file.txt') as f:
        lines = f.read().splitlines()
        
        for line in lines:
            hand = line.split(' ')
            values = []
            for card in hand:
                if not card.isdigit():
                    if card == 'J':
                        values.append(j)
                    elif card == 'Q':
                        values.append(q)
                    elif card == 'K':
                        values.append(k)
                    elif card == 'A':
                        values.append(a)
                else:
                    values.append(int(card))

            matrix[lines.index(line)] = values
    
    return matrix

def play(matrix):
    played = []
    for player in matrix: 
            print(len(played), min(player))
            if len(played)==0:
                played.append(min(player))
            else:
                played.append(checkPlay(played, player))

    return played

def checkPlay(played, cards):
    if min(cards) in played:
        return max(cards)
    else:
        return min(cards)
    
if __name__ == '__main__':
    matrix = formatInput()
    print(matrix)
    played = play(matrix)
    print(played)
