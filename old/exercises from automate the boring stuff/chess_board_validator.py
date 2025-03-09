player_types=['W','B']
piece_types=['king','queen','knight','bishop','rook','pawn']
valid_board_requirement={'W':16, 'Wking':1, 'Wqueen':1, 'Wbishop':2,
                        'Wknight':2, 'Wrook':2, 'Wpawn':8,
                        'B':16, 'Bking':1, 'Bqueen':1, 'Bbishop':2,
                        'Bknight':2, 'Brook':2, 'Bpawn':8,}

#This does everything except deal with promotion.
#this also is sort of cheating since I capitalized the first letter.

def count_all_pieces(board):
    piece_count={}
    for color in player_types:
        count_particular_pieces(board, color, piece_count)
        for piece in piece_types:
            count_particular_pieces(board, color+piece, piece_count)
    return piece_count


def count_particular_pieces(board, name, current_count):
    for position in board:
        current_count.setdefault(name, 0)
        if name in board[position]:
            current_count[name]+=1
    return current_count

def check_valid_positions(board):
    for position in board.keys():
        if int(position[0])-1 not in range(8):
            print(f'The board is invalid because of position {position}.')
            return False
        elif position[1] not in 'abcdefgh':
            print(f'The board is invalid because of position {position}.')
            return False
    print('The board is valid with respect to positions.')
    return True

def check_valid_pieces(count_dict):
    result = 0
    for name, count in count_dict.items():
        if count> valid_board_requirement[name]:
            print(f'This board is invalid because there are too many {name} pieces.')
            return False
        elif 'king' in name:
            if count!=1:
                print('There are not the right number of kings.')
                return False
        #print(f'The number of {name} present is {count}, which is ok.')
    print('The board is valid with respect to the number of pieces.')
    return True

def validate_board(board):
    count_dict = count_all_pieces(board)
    pieces = check_valid_pieces(count_dict)
    positions = check_valid_positions(board)
    if pieces and positions:
        print('This board is indeed valid')
        return True
    else:
        print('This board is not valid.')
        return False

print(validate_board({"1h": "Bking", "6c": "Wqueen", "2g": "Bbishop", "5h": "Bqueen",
                      "3e": "Wking"}))  # True
print(validate_board({"1a": "Bpawn", "2a": "Wking"}))  # False: no bking
print(validate_board({"1a": "Wking", "2a": "Wking", "3c": "Bbishop"}))  # False: cannot have 2 white kings, no bking
print(validate_board({"1a": "Bking", "9z": "Wking"}))  # False: 9z is an invalid position

check_valid_positions({"1a": "Bking", "9z": "Wking"})