def get_valid_moves(board, row, col,color,ignore_king=False):
    piece = board[row][col]
    if piece.upper() == "P":
        color = "white" if piece.isupper() else "black"
        return valid_moves_pawn(board, row, col, color)
    if piece.upper() == "K" and not ignore_king:
        color = "white" if piece.isupper() else "black"
        return valid_moves_king(board, row, col,color)
    if piece.upper() == "N":
        color = "white" if piece.isupper() else "black"
        return valid_moves_knight(board, row, col, color)
    if piece.upper() == "B":
        color = "white" if piece.isupper() else "black"
        return valid_moves_bishop(board, row, col, color)
    if piece.upper() == "Q":
        color = "white" if piece.isupper() else "black"
        return valid_moves_queen(board, row, col, color)
    if piece.upper() == "R":
        color = "white" if piece.isupper() else "black"
        return valid_moves_rock(board, row, col, color)
    return []
