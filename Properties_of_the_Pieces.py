from Legal_Moves import Rook, Bishop, Knight, King, Queen, Pawn

# Black Stuff
# Black pieces
Black_RookL = {
    'Name': 'Black_RookL',
    'Piece_No': 1,
    'Piece_colour': 'Black',
    'Piece_Position': 0,
    'Movement': Rook(0, 'Black_RookL'),
    'Points': -5,
    'Can_Be_Captured': True
}

Black_RookR = {
    'Name': 'Black_RookR',
    'Piece_No': 8,
    'Piece_colour': 'Black',
    'Piece_Position': 7,
    'Movement': Rook(7, 'Black_RookR'),
    'Points': -5,
    'Can_Be_Captured': True
}

Black_KnightL = {
    'Name': 'Black_KnightL',
    'Piece_No': 2,
    'Piece_colour': 'Black',
    'Piece_Position': 1,
    'Movement': Knight(1, 'Black_KnightL'),
    'Points': -3,
    'Can_Be_Captured': True
}

Black_KnightR = {
    'Name': 'Black_KnightR',
    'Piece_No': 7,
    'Piece_colour': 'Black',
    'Piece_Position': 6,
    'Movement': Knight(6, 'Black_KnightR'),
    'Points': -3,
    'Can_Be_Captured': True
}

Black_BishopL = {
    'Name': 'Black_BishopL',
    'Piece_No': 3,
    'Piece_colour': 'Black',
    'Piece_Position': 2,
    'Movement': Bishop(2, 'Black_BishopL'),
    'Points': -3,
    'Can_Be_Captured': True
}

Black_BishopR = {
    'Name': 'Black_BishopR',
    'Piece_No': 6,
    'Piece_colour': 'Black',
    'Piece_Position': 5,
    'Movement': Bishop(5, 'Black_BishopR'),
    'Points': -3,
    'Can_Be_Captured': True
}

Black_Queen = {
    'Name': 'Black_Queen',
    'Piece_No': 4,
    'Piece_colour': 'Black',
    'Piece_Position': 3,
    'Movement': Queen(3, 'Black_Queen'),
    'Points': -9,
    'Can_Be_Captured': True
}

Black_King = {
    'Name': 'Black_King',
    'Piece_No': 5,
    'Piece_colour': 'Black',
    'Piece_Position': 4,
    'Movement': King(4, 'Black_King'),
    'Points': -100,
    'Can_Be_Captured': True
}

Black_Pawn1 = {
    'Name': 'Black_Pawn1',
    'Piece_No': 9,
    'Piece_colour': 'Black',
    'Piece_Position': 8,
    'Movement': Pawn(8, 'Black_Pawn1'),
    'Points': -1,
    'Can_Be_Captured': True
}

Black_Pawn2 = {
    'Name': 'Black_Pawn2',
    'Piece_No': 10,
    'Piece_colour': 'Black',
    'Piece_Position': 9,
    'Movement': Pawn(9, 'Black_Pawn2'),
    'Points': -1,
    'Can_Be_Captured': True
}

Black_Pawn3 = {
    'Name': 'Black_Pawn3',
    'Piece_No': 11,
    'Piece_colour': 'Black',
    'Piece_Position': 10,
    'Movement': Pawn(10, 'Black_Pawn3'),
    'Points': -1,
    'Can_Be_Captured': True
}

Black_Pawn4 = {
    'Name': 'Black_Pawn4',
    'Piece_No': 12,
    'Piece_colour': 'Black',
    'Piece_Position': 11,
    'Movement': Pawn(11, 'Black_Pawn4'),
    'Points': -1,
    'Can_Be_Captured': True
}

Black_Pawn5 = {
    'Name': 'Black_Pawn5',
    'Piece_No': 13,
    'Piece_colour': 'Black',
    'Piece_Position': 12,
    'Movement': Pawn(12, 'Black_Pawn5'),
    'Points': -1,
    'Can_Be_Captured': True
}

Black_Pawn6 = {
    'Name': 'Black_Pawn6',
    'Piece_No': 14,
    'Piece_colour': 'Black',
    'Piece_Position': 13,
    'Movement': Pawn(13, 'Black_Pawn6'),
    'Points': -1,
    'Can_Be_Captured': True
}

Black_Pawn7 = {
    'Name': 'Black_Pawn7',
    'Piece_No': 15,
    'Piece_colour': 'Black',
    'Piece_Position': 14,
    'Movement': Pawn(14, 'Black_Pawn7'),
    'Points': -1,
    'Can_Be_Captured': True
}

Black_Pawn8 = {
    'Name': 'Black_Pawn8',
    'Piece_No': 16,
    'Piece_colour': 'Black',
    'Piece_Position': 15,
    'Movement': Pawn(15, 'Black_Pawn8'),
    'Points': -1,
    'Can_Be_Captured': True
}


# White pieces
White_RookL = {
    'Name': 'White_RookL',
    'Piece_No': 49,
    'Piece_colour': 'White',
    'Piece_Position': 48,
    'Movement': Rook(48, 'White_RookL'),
    'Points': 5,
    'Can_Be_Captured': True
}

White_RookR = {
    'Name': 'White_RookR',
    'Piece_No': 56,
    'Piece_colour': 'White',
    'Piece_Position': 55,
    'Movement': Rook(55, 'White_RookR'),
    'Points': 5,
    'Can_Be_Captured': True
}

White_KnightL = {
    'Name': 'White_KnightL',
    'Piece_No': 50,
    'Piece_colour': 'White',
    'Piece_Position': 49,
    'Movement': Knight(49, 'White_KnightL'),
    'Points': 3,
    'Can_Be_Captured': True
}

White_KnightR = {
    'Name': 'White_KnightR',
    'Piece_No': 55,
    'Piece_colour': 'White',
    'Piece_Position': 54,
    'Movement': Knight(54, 'White_KnightR'),
    'Points': 3,
    'Can_Be_Captured': True
}

White_BishopL = {
    'Name': 'White_BishopL',
    'Piece_No': 51,
    'Piece_colour': 'White',
    'Piece_Position': 50,
    'Movement': Bishop(50, 'White_BishopL'),
    'Points': 3,
    'Can_Be_Captured': True
}

White_BishopR = {
    'Name': 'White_BishopR',
    'Piece_No': 54,
    'Piece_colour': 'White',
    'Piece_Position': 53,
    'Movement': Bishop(53, 'White_BishopR'),
    'Points': 3,
    'Can_Be_Captured': True
}

White_Queen = {
    'Name': 'White_Queen',
    'Piece_No': 52,
    'Piece_colour': 'White',
    'Piece_Position': 51,
    'Movement': Queen(51, 'White_Queen'),
    'Points': 9,
    'Can_Be_Captured': True
}

White_King = {
    'Name': 'White_King',
    'Piece_No': 53,
    'Piece_colour': 'White',
    'Piece_Position': 52,
    'Movement': King(52, 'White_King'),
    'Points': 100,
    'Can_Be_Captured': True
}

White_Pawn1 = {
    'Name': 'White_Pawn1',
    'Piece_No': 57,
    'Piece_colour': 'White',
    'Piece_Position': 56,
    'Movement': Pawn(56, 'White_Pawn1'),
    'Points': 1,
    'Can_Be_Captured': True
}

White_Pawn2 = {
    'Name': 'White_Pawn2',
    'Piece_No': 58,
    'Piece_colour': 'White',
    'Piece_Position': 57,
    'Movement': Pawn(57, 'White_Pawn2'),
    'Points': 1,
    'Can_Be_Captured': True
}

White_Pawn3 = {
    'Name': 'White_Pawn3',
    'Piece_No': 59,
    'Piece_colour': 'White',
    'Piece_Position': 58,
    'Movement': Pawn(58, 'White_Pawn3'),
    'Points': 1,
    'Can_Be_Captured': True
}

White_Pawn4 = {
    'Name': 'White_Pawn4',
    'Piece_No': 60,
    'Piece_colour': 'White',
    'Piece_Position': 59,
    'Movement': Pawn(59, 'White_Pawn4'),
    'Points': 1,
    'Can_Be_Captured': True
}

White_Pawn5 = {
    'Name': 'White_Pawn5',
    'Piece_No': 61,
    'Piece_colour': 'White',
    'Piece_Position': 60,
    'Movement': Pawn(60, 'White_Pawn5'),
    'Points': 1,
    'Can_Be_Captured': True
}

White_Pawn6 = {
    'Name': 'White_Pawn6',
    'Piece_No': 62,
    'Piece_colour': 'White',
    'Piece_Position': 61,
    'Movement': Pawn(61, 'White_Pawn6'),
    'Points': 1,
    'Can_Be_Captured': True
}

White_Pawn7 = {
    'Name': 'White_Pawn7',
    'Piece_No': 63,
    'Piece_colour': 'White',
    'Piece_Position': 62,
    'Movement': Pawn(62, 'White_Pawn7'),
    'Points': 1,
    'Can_Be_Captured': True
}

White_Pawn8 = {
    'Name': 'White_Pawn8',
    'Piece_No': 64,
    'Piece_colour': 'White',
    'Piece_Position': 63,
    'Movement': Pawn(63, 'White_Pawn8'),
    'Points': 1,
    'Can_Be_Captured': True
}


# Empty square
EMPTY = {
    'Name': 'EMPTY',
    'Piece_No': None,
    'Piece_colour': None,
    'Movement': None,
    'Points': 0,
    'Can_Be_Captured': True
}
