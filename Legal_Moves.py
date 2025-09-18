import Board
import Properties_of_the_Pieces

def Row_Column(Board_Index):

    Row = Board_Index // 8
    Column = Board_Index % 8

    return Row,Column

def Anti_Row_Column(Moves_in_Row_Column, Name):

    Moves_in_one_Number = []

    for i in Moves_in_Row_Column:
        if type(i) == int:

            print(i)
            print(Name)
            continue

        Num = i[0]*8 + i[1]

        Moves_in_one_Number.append(Num)

    return Moves_in_one_Number

def Rook(Board_Index,Name):

    Row,Column = Row_Column(Board_Index)

    Moves_In_Same_Row = []
    Moves_In_Same_Column = []

    for i in range(7):

        Moves_In_Same_Column.append([i,Column])
        Moves_In_Same_Row.append([Row,i])


    Moves_Horizontal = Move_Legality_Rook(Anti_Row_Column(Moves_In_Same_Row,'Rook'),Name,Board_Index)

    Moves_Vertical = Move_Legality_Rook(Anti_Row_Column(Moves_In_Same_Column,'Rook'),Name)

    return Moves_Vertical + Moves_Horizontal


def Bishop(Board_Index,Name):

    Row,Column = Row_Column(Board_Index)

    Left_Up_Right_Down_Moves = []
    Right_up_Left_Down_Moves = []

    Goes_in_Negative_Row = Goes_in_Positive_Row = Row
    Goes_in_Negative_Column = Goes_in_Positive_Column = Column

    while Goes_in_Negative_Column >= 0 and Goes_in_Negative_Row >= 0:

        Right_Up_Left_Down_Moves.append([Goes_in_Negative_Row,Goes_in_Negative_Column])
        Goes_in_Negative_Row -= 1 
        Goes_in_Negative_Column -= 1

    Goes_in_Negative_Row = Goes_in_Positive_Row = Row
    Goes_in_Negative_Column = Goes_in_Positive_Column = Column

    while Goes_in_Positive_Column < 8 and Goes_in_Negative_Row >= 0:

        if Goes_in_Positive_Column == Column and Goes_in_Negative_Row == Row :
            Goes_in_Negative_Row -= 1
            Goes_in_Positive_Column += 1
            continue

        Left_Up_Right_Down_Moves.append([Goes_in_Negative_Row,Goes_in_Positive_Column])
        Goes_in_Negative_Row -= 1
        Goes_in_Positive_Column += 1

    Goes_in_Negative_Row = Goes_in_Positive_Row = Row
    Goes_in_Negative_Column = Goes_in_Positive_Column = Column

    while Goes_in_Positive_Column < 8 and Goes_in_Positive_Row < 8:

        if Goes_in_Positive_Column == Column and Goes_in_Positive_Row == Row :
            Goes_in_Positive_Row += 1
            Goes_in_Positive_Column += 1
            continue

        Right_up_Left_Down_Moves.append([Goes_in_Positive_Row,Goes_in_Positive_Column])
        Goes_in_Positive_Row += 1
        Goes_in_Positive_Column += 1

    Goes_in_Negative_Row = Goes_in_Positive_Row = Row
    Goes_in_Negative_Column = Goes_in_Positive_Column = Column

    while Goes_in_Negative_Column >= 0 and Goes_in_Positive_Row < 8:

        if Goes_in_Negative_Column == Column and Goes_in_Positive_Row == Row :
            Goes_in_Positive_Row += 1
            Goes_in_Negative_Column -= 1
            continue

        Left_Up_Right_Down_Moves.append([Goes_in_Positive_Row,Goes_in_Negative_Column])
        Goes_in_Positive_Row += 1
        Goes_in_Negative_Column -= 1

    Left_Up_Right_Down_Moves = Move_Legality_Bishop(Anti_Row_Column(Left_Up_Right_Down_Moves,"Bishop"),Name,Board_Index)
    Right_up_Left_Down_Moves = Move_Legality_Bishop(Anti_Row_Column(Right_up_Left_Down_Moves,"Bishop"),Name,Board_Index)


    return Moves

def Knight(Board_Index,Name): 

    Row,Column = Row_Column(Board_Index)

    Moves = [] 

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
            Moves.append(A_Move)

    Moves = Anti_Row_Column(Moves,"Knight")

    return Moves

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

def King(Board_Index,Name):

    Row,Column = Row_Column(Board_Index)

    Moves = []

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
            Moves.append(A_Move)

    Moves = Anti_Row_Column(Moves,"King")

    return Moves

def Queen(Board_Index,Name):

    Moves = []

    Rook_Moves = Rook(Board_Index,Name)
    Bishop_Moves = Bishop(Board_Index,Name)

    Moves = Rook_Moves + Bishop_Moves

    return Moves

def Pawn(Board_Index,Name):



    return [Board_Index+1]






