class Board:
  def __init__(self, dim = 3):
    self.cells = [' '] * dim**2 # flat array
    self.dim = dim
    self.history = []

  def __str__(self):
    rows = []
    for i in range(self.dim):
      row_start = i*self.dim
      rows.append('|'.join(self.cells[row_start:row_start + self.dim]))
    separator = '\n' + '+'.join(['-']*self.dim) + '\n'
    return separator.join(rows)

  def has_horizontal_tris(self, player):
    if player not in ['X', 'O']:
      raise ValueError(f'Player should be one of "X" or "O", received {player}')
    
    for i in range(self.dim):
      for j in range(self.dim):
        if self.cells[i*self.dim + j] != player:
          break
      else:
        return True
    return False

  def has_vertical_tris(self, player):
    if player not in ['X', 'O']:
      raise ValueError(f'Player should be one of "X" or "O", received {player}')

    for j in range(self.dim):
      for i in range(self.dim):
        if self.cells[i*self.dim + j] != player:
          break
      else:
        return True
    return False

  def has_diagonal_tris(self, player):
    if player not in ['X', 'O']:
      raise ValueError(f'Player should be one of "X" or "O", received {player}')

    # Main diagonal
    for i in range(self.dim):
      if self.cells[i*self.dim + i] != player:
        break
    else:
      return True

    # Secondary diagonal
    for i in range(self.dim):
      if self.cells[i*self.dim + self.dim-1-i] != player:
        break
    else:
      return True

    return False

  def has_tris(self, player):
    return self.has_horizontal_tris(player) or self.has_vertical_tris(player) or \
           self.has_diagonal_tris(player)

  def is_in_terminal_state(self):
    # Check if the board is full
    for cell in self.cells:
      if cell == ' ':
        break
    else:
      return True

    return self.has_tris('X') or self.has_tris('O')

  def apply_move(self, player, row, col):
    if self.is_in_terminal_state():
      raise RuntimeError("Can't apply new moves to board in terminal state")
    if player not in ['X', 'O']:
      raise ValueError(f'Player should be one of "X" or "O", received {player}')
    if self.cells[row*self.dim + col] != ' ':
      raise ValueError(f'The cell {row}, {col} is already occupied')

    self.cells[row*self.dim + col] = player
    self.history.append((player, row, col))

  def revert_last_move(self):
    player, row, col = self.history.pop()
    self.cells[row*self.dim + col] = ' '

  def get_empty_cells(self):
    empty_cells = []
    for i in range(self.dim):
      for j in range(self.dim):
        if self.cells[i*self.dim + j] == ' ':
          empty_cells.append((i, j))
    return empty_cells
