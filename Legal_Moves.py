import Board
import Properties_of_the_Pieces

def Row_Column(Board_Index):

    Row = Board_Index // 10
    Column = Board_Index % 10

    return Row,Column


def Rook(Board_Index):

    Row,Column = Row_Column(Board_Index)

    Moves = []

    for i in range(,7):

        Moves.append([i,Column])
        Moves.append([Row,i])

    return Moves

def Bishop(Board_Index):

    Row,Column = Row_Column(Board_Index)

    Moves = []

    Goes_in_Negative_Row = Goes_in_Positive_Row = Row
    Goes_in_Negative_Column = Goes_in_Positive_Column = Column

    while Goes_in_Negative_Column >= 0 and Goes_in_Negative_Row >= 0:

        Moves.append([Goes_in_Negative_Row,Goes_in_Negative_Column])
        Goes_in_Negative_Row -= 1
        Goes_in_Negative_Column -= 1

    Goes_in_Negative_Row = Goes_in_Positive_Row = Row
    Goes_in_Negative_Column = Goes_in_Positive_Column = Column

    while Goes_in_Positive_Column < 8 and Goes_in_Negative_Row >= 0:

        if Goes_in_Positive_Column == Column and Goes_in_Negative_Row == Row :
            Goes_in_Negative_Row -= 1
            Goes_in_Positive_Column += 1
            continue

        Moves.append([Goes_in_Negative_Row,Goes_in_Positive_Column])
        Goes_in_Negative_Row -= 1
        Goes_in_Positive_Column += 1

    Goes_in_Negative_Row = Goes_in_Positive_Row = Row
    Goes_in_Negative_Column = Goes_in_Positive_Column = Column

    while Goes_in_Positive_Column < 8 and Goes_in_Positive_Row < 8:

        if Goes_in_Positive_Column == Column and Goes_in_Positive_Row == Row :
            Goes_in_Positive_Row += 1
            Goes_in_Positive_Column += 1
            continue

        Moves.append([Goes_in_Positive_Row,Goes_in_Positive_Column])
        Goes_in_Positive_Row += 1
        Goes_in_Positive_Column += 1

    Goes_in_Negative_Row = Goes_in_Positive_Row = Row
    Goes_in_Negative_Column = Goes_in_Positive_Column = Column

    while Goes_in_Negative_Column >= 0 and Goes_in_Positive_Row < 8:

        if Goes_in_Negative_Column == Column and Goes_in_Positive_Row == Row :
            Goes_in_Positive_Row += 1
            Goes_in_Negative_Column -= 1
            continue

        Moves.append([Goes_in_Positive_Row,Goes_in_Negative_Column])
        Goes_in_Positive_Row += 1
        Goes_in_Negative_Column -= 1

    return Moves

def Knight(Board_Index): 

    Row,Column = Row_Column(Board_Index)

    Move = [] 

    Up_Right = [Row - 2 ,Column + 1]
    Up_Left = [Row - 2 ,Column - 1]

    Down_Left = [Row + 2 ,Column + 1] 
    Down_Right = [Row + 2 ,Column - 1]

    Left_Up = [Row + 1 ,Column - 2]
    Left_Down = [Row - 1 ,Column - 2] 

    Right_Up = [Row + 1 ,Column + 2]
    Right_Down = [Row - 1 ,Column + 2] 

    All_moves = [Up_Right,Up_Left,Down_Left,Down_Right,Left_Up,Left_Down,Right_Up,Right_Down]

    for A_Move in All_moves:

        if (A_Move[0] < 8 and A_Move[0] >= 0) and (A_Move[1] < 8 and A_Move[1] >= 0 ):
            Move.append(A_move)

    return Move

    '''

  #Longer part of the L shape 
    Up_Row = Row - 2 
    Up_Column = Column - 2 

    # Basically upwards which is lower in value


    Down_Row = Row + 2 
    Down_Column = Column + 2 
    # Downwards as higher in value 

    #Shorter Part of the L Shape 
    Short_Up_Column = Column - 1 
    Short_Up_Row = Row - 1 

    Short_Down_Column = Column + 1 
    Short_Down_Row = Row + 1 
    if Up_Row >= 2: 

        if Short_Up_Column >= 1:

            Move.append([Up_Row,Short_Up_Column])

        if Short_Down_Column < 9: 

            Move.append([Up_Row,Short_Down_Column]) 

    if Down_Row <= 9 : 

        if Short_Up_Column >= 1: 

            Move.append([Down_Row,Short_Up_Column]) 

        if Short_Down_Column < 9: 

            Move.append([Down_Row,Short_Down_Column]) 

    if Up_Column >= 1: 

        if Short_Up_Row >=2: 

            Move.append([Short_Up_Row,Up_Column]) 

        if Short_Down_Row <=9: 
            Move.append([Short_Down_Row,Up_Column]) 

    if Down_Column < 9: 

        if Short_Up_Row >=2: 

            Move.append([Short_Up_Row,Down_Column]) 

        if Short_Down_Row <=9: 

            Move.append([Short_Down_Row,Down_Column]) 

    '''

def King(Board_Index):

    Row,Column = Row_Column(Board_Index)

    Move = []

    Up = [ Row - 1, Column]
    Down = [ Row + 1, Column ]
    Left = [ Row, Column - 1]
    Right = [ Row, Column + 1]
    Up_Right = [ Row - 1, Column + 1]
    Down_Right = [ Row + 1, Column + 1]
    Up_Left = [ Row - 1 , Column - 1 ]
    Down_Left = [ Row + 1, Column - 1]

    All_moves = [Up,Down,Left,Right,Up_Left,Up_Right,Down_Left,Down_Right]

    for A_Move in All_moves:

        if (A_Move[0] < 8 and A_Move[0] >= 0) and (A_Move[1] < 8 and A_Move[1] >= 0 ):
            Move.append(A_move)


    return Move


def Queen(Board_Index):

    Move = []

    Rook_Moves = Rook(Board_Index)
    Bishop_Moves = Bishop(Board_Index)

    Move = Rook_Moves + Bishop_Moves

    return Move


def Pawn(Board_Index):

    Row,Column = Row_Column(Board_Index)

    Move = [Row+1,Column]

    return Move


def Check_Legality(Moves):

    One_Number_Move = []
    Can_Be_Placed_At = []

    for A_Move in Moves:

        One_Number_Move.append(A_Move[0]*10 + A_Move[1] )


    for i in One_Number_Move:

        Position  = One_List_Map[i]

        if Position == 'EMPTY':

            Can_Be_Placed_At.append(i)

        elif Position






