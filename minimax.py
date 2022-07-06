from math import inf
from board import Board

def minimax(board: Board, player, depth):
  return maximize(board, player, depth)[0]

def maximize(board: Board, player, depth):
  """
  Given a board configuration, find a move that
  maximizes the value of the player
  """
  if board.is_in_terminal_state() or depth == 0:
    return None, eval(board, player)

  opponent = 'X' if player == 'O' else 'O'
  best_move = None
  max_value = -inf
  for row, col in board.get_empty_cells():
    board.apply_move(player, row, col)
    value = minimize(board, opponent, depth-1)[1]
    if value > max_value:
      max_value = value
      best_move = (row, col)
    board.revert_last_move()
  return best_move, max_value

def minimize(board: Board, player, depth):
  """
  Given a board configuration, find a move that
  minimizes the value of the opponent
  """
  opponent = 'X' if player == 'O' else 'O'
  if board.is_in_terminal_state() or depth == 0:
    return None, eval(board, opponent)

  best_move = None
  min_value = inf
  for row, col in board.get_empty_cells():
    board.apply_move(player, row, col)
    value = maximize(board, opponent, depth-1)[1]
    if value < min_value:
      min_value = value
      best_move = (row, col)
    board.revert_last_move()
  return best_move, min_value

def eval(board: Board, player):
  """
  Evaluates the status of the board according to the player's perspective.
  The board is assumed to be in a terminal state.
  """
  if board.has_tris(player): # win
    return 1
  opponent = 'X' if player == 'O' else 'O'
  if board.has_tris(opponent): # loss
    return -1
  return 0 #draw
