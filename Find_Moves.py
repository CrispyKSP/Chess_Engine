better ? from Board import *


def Move_Legality_Rook(Moves,Name,Position):

    Legal_Moves_Up = []
    Legal_Moves_Down = []

    Moves_Up = []
    Moves_Down = []

    Main_Rook = One_List_Map.get(Name)

    for i in Moves:
        if i < Position:
            Moves_Up.append(i)

        elif i == Position:
            continue

        else:

            Moves_Down.append(i)

    for A_Move in reversed(Moves_Up):

        Dict_of_Piece_on_That_Place = One_List_Map[A_Move]

        if Dict_of_Piece_on_That_Place['Piece_colour'] == Main_Rook['Piece_colour']:

            break

        elif Dict_of_Piece_on_That_Place['Name'] == 'EMPTY':

            Legal_Moves_Up.append(A_Move)

        else:
            Legal_Moves_Up.append(A_Move)
            break


    for A_Move in Moves_Down:

        Dict_of_Piece_on_That_Place = One_List_Map[A_Move]

        if Dict_of_Piece_on_That_Place['Piece_colour'] == Main_Rook['Piece_colour']:

            break

        elif Dict_of_Piece_on_That_Place['Name'] == 'EMPTY':

            Legal_Moves_Down.append(A_Move)

        else:
            Legal_Moves_Down.append(A_Move)
            break

    Legal_Final = Legal_Moves_Up + Legal_Moves_Down

    return Legal_Final
    
def Move_Legality_Knight(Moves,Name,Position):

    Main_Knight = One_List_Map.get(Name)

    Legal_Move = []

    for A_Move in Moves:

        Dict_of_Piece_on_That_Place = One_List_Map[A_Move]

        if Dict_of_Piece_on_That_Place['Piece_colour'] == Main_Knight['Piece_colour']:

            continue

        else:
            Legal_Move.append(A_Move)


    return Legal_Move


def Move_Legality_Bishop(Moves,Name,Position):

    Moves.sort()

    Legal_Moves_Up = []
    Legal_Moves_Down = []

    Moves_Up = []
    Moves_Down = []

    Main_Bishop = One_List_Map.get(Name)

    for i in Moves:
        if i < Position:
            Moves_Up.append(i)

        elif i == Position:
            continue

        else:

            Moves_Down.append(i)


    for A_Move in reversed(Moves_Up):

        Dict_of_Piece_on_That_Place = One_List_Map[A_Move]

        if Dict_of_Piece_on_That_Place['Piece_colour'] == Main_Bishop['Piece_colour']:

            break

        elif Dict_of_Piece_on_That_Place['Name'] == 'EMPTY':

            Legal_Moves_Up.append(A_Move)

        else:

            Legal_Moves_Up.append(A_Move)
            break

    for A_Move in Moves_Down:

        Dict_of_Piece_on_That_Place = One_List_Map[A_Move]

        if Dict_of_Piece_on_That_Place['Piece_colour'] == Main_Bishop['Piece_colour']:

            break

        elif Dict_of_Piece_on_That_Place['Name'] == 'EMPTY':

            Legal_Moves_Down.append(A_Move)

        else:

            Legal_Moves_Down.append(A_Move)
            break

    Legal_Final = Legal_Moves_Up + Legal_Moves_Down

    return Legal_Final












