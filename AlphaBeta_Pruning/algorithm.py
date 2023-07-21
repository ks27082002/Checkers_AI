from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)

def alpha_beta_pruning(possible_board, depth, max_player, game, alpha, beta):#position->board


    if depth == 0 or possible_board.winner() == WHITE or possible_board== RED:
        return possible_board.evaluate(),possible_board#returns tuple of evaluaion value and current position/board
    
    if max_player: #maximize evaluate
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(possible_board, WHITE, game):#here move stores all new boards possible by moving any white piece
            evaluation = alpha_beta_pruning(move, depth-1, False, game, alpha, beta)[0]#only evaluation value for each possible move/board
            maxEval = max(maxEval, evaluation)#chainging eval
            alpha = max(alpha,maxEval)#changing alpha
            if maxEval == evaluation:
                best_move = move#storing best move
            if beta <= alpha:#ACTUAL PRUNING
                break#BREAK ON PRUNING
        return maxEval, best_move
    
    else:#min player minimize evaluate
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(possible_board, RED, game):#here move stores all new boards possible by moving any red piece
            evaluation = alpha_beta_pruning(move, depth-1, True, game, alpha, beta)[0]#only evaluation value for each possible move/board
            minEval = min(minEval, evaluation)#chainging eval
            beta = min(beta, minEval)#changing beta
            if minEval == evaluation:
                best_move = move#storing best move
                if beta <= alpha:#ACTUAL PRUNING
                    break #BREAK ON PRUNING
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            #draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


# def draw_moves(game, board, piece):
#     valid_moves = board.get_valid_moves(piece)
#     board.draw(game.win)
#     pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
#     game.draw_valid_moves(valid_moves.keys())
#     pygame.display.update()
    #pygame.time.delay(100)

