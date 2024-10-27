# Determine if provided argument for board is valid, meaning each player can only have at most 1 king, 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'
board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking'}

# Define all valid chessboard positions
validPositions = {f"{rank}{file}" for rank in range(1,9) for file in 'abcdefgh'}

def isValidChessBoard(board):
    # Initialize counters for the pieces
    wKingCount = 0
    bKingCount = 0
    totalPieces = 0
    pawnCount = 0
    

    for position, piece in board.items(): # position is the key, piece is the value 
        # Count Kings
        if piece == 'wking': 
            wKingCount += 1
        elif piece == 'bking': 
            bKingCount += 1

        # Count total pieces
        totalPieces += 1

        # Count pawns
        if piece.startswith('wpawn'):
            pawnCount += 1
        elif piece.startswith('bpawn'):
            pawnCount += 1

        # Check if position is valid
        if position not in validPositions: 
            return False
        
    # Check the counts
    if wKingCount == 1 and bKingCount == 1 and totalPieces <= 16 and pawnCount <= 8:
        return True
    else:
        return False
    
# Test the function
print(isValidChessBoard(board))