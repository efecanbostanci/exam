def valid_moves_knight(board, row, col, selected_color):
    moves = []
    color = selected_color

    if 0 <= col - 2 < 8 and 0 <= row - 1 < 8:  # sol yukarı
        if board[row - 1][col - 2] != " ":
            new_row = row - 1
            new_col = col - 2
            target_piece = board[new_row][new_col]
            if (color == "white" and target_piece.islower()) or \
               (color == "black" and target_piece.isupper()):
                moves.append((new_row, new_col))
        else:
            moves.append((row - 1, col - 2))

    if 0 <= col - 2 < 8 and 0 <= row + 1 < 8:  # sol aşağı
        if board[row + 1][col - 2] != " ":
            new_row = row + 1
            new_col = col - 2
            target_piece = board[new_row][new_col]
            if (color == "white" and target_piece.islower()) or \
               (color == "black" and target_piece.isupper()):
                moves.append((new_row, new_col))
        else:
            moves.append((row + 1, col - 2))

    if 0 <= col + 2 < 8 and 0 <= row - 1 < 8:  # sağ yukarı
        if board[row - 1][col + 2] != " ":
            new_row = row - 1
            new_col = col + 2
            target_piece = board[new_row][new_col]
            if (color == "white" and target_piece.islower()) or \
               (color == "black" and target_piece.isupper()):
                moves.append((new_row, new_col))
        else:
            moves.append((row - 1, col + 2))

    if 0 <= col + 2 < 8 and 0 <= row + 1 < 8:  # sağ aşağı
        if board[row + 1][col + 2] != " ":
            new_row = row + 1
            new_col = col + 2
            target_piece = board[new_row][new_col]
            if (color == "white" and target_piece.islower()) or \
               (color == "black" and target_piece.isupper()):
                moves.append((new_row, new_col))
        else:
            moves.append((row + 1, col + 2))

    if 0 <= row + 2 < 8 and 0 <= col - 1 < 8:  # aşağı sol
        if board[row + 2][col - 1] != " ":
            new_row = row + 2
            new_col = col - 1
            target_piece = board[new_row][new_col]
            if (color == "white" and target_piece.islower()) or \
               (color == "black" and target_piece.isupper()):
                moves.append((new_row, new_col))
        else:
            moves.append((row + 2, col - 1))

    if 0 <= row + 2 < 8 and 0 <= col + 1 < 8:  # aşağı sağ
        if board[row + 2][col + 1] != " ":
            new_row = row + 2
            new_col = col + 1
            target_piece = board[new_row][new_col]
            if (color == "white" and target_piece.islower()) or \
               (color == "black" and target_piece.isupper()):
                moves.append((new_row, new_col))
        else:
            moves.append((row + 2, col + 1))

    if 0 <= row - 2 < 8 and 0 <= col - 1 < 8:  # yukarı sol
        if board[row - 2][col - 1] != " ":
            new_row = row - 2
            new_col = col - 1
            target_piece = board[new_row][new_col]
            if (color == "white" and target_piece.islower()) or \
               (color == "black" and target_piece.isupper()):
                moves.append((new_row, new_col))
        else:
            moves.append((row - 2, col - 1))

    if 0 <= row - 2 < 8 and 0 <= col + 1 < 8:  # yukarı sağ
        if board[row - 2][col + 1] != " ":
            new_row = row - 2
            new_col = col + 1
            target_piece = board[new_row][new_col]
            if (color == "white" and target_piece.islower()) or \
               (color == "black" and target_piece.isupper()):
                moves.append((new_row, new_col))
        else:
            moves.append((row - 2, col + 1))

    return moves
