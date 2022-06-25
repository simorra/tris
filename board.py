class Board:
  def __init__(self, dim = 3):
    self.cells = [' '] * dim**2 # flat array
    self.dim = dim

  def __str__(self):
    rows = []
    for i in range(self.dim):
      row_start = i*self.dim
      rows.append('|'.join(self.cells[row_start:row_start + self.dim]))
    separator = '\n' + '+'.join(['-']*self.dim) + '\n'
    return separator.join(rows)

  def is_in_terminal_state(self):
    # Check if the board is full
    for cell in self.cells:
      if cell == ' ':
        break
    else:
      return True

    # Check for horizontal "tris"
    for i in range(self.dim):
      if self.cells[i*self.dim] == ' ':
        continue
      for j in range(1, self.dim):
        # All the cells in the row must contain the same value as the first
        if self.cells[i*self.dim + j] != self.cells[i*self.dim]:
          break
      else:
        return True

    # Check for vertical "tris"
    for j in range(self.dim):
      if self.cells[j] == ' ':
        continue
      for i in range(1, self.dim):
        # All the cells in the column must contain the same value as the first
        if self.cells[i*self.dim + j] != self.cells[j]:
          break
      else:
        return True

    # Check for diagonal "tris"
    if self.cells[0] != ' ':
      for i in range(1, self.dim):
        if self.cells[i*self.dim + i] != self.cells[0]:
          break
      else:
        return True

    if self.cells[self.dim-1] != ' ':
      for i in range(1, self.dim):
        if self.cells[i*self.dim + self.dim-1-i] != self.cells[self.dim-1]:
          break
      else:
        return True

    return False

  def apply_move(self, player, row, col):
    if self.is_in_terminal_state():
      raise RuntimeError("Can't apply new moves to board in terminal state")

    # Check input arguments
    if player not in 'XO':
      raise ValueError(f'Player should be one of "X" or "O", received {player}')
    if self.cells[row*self.dim + col] != ' ':
      raise ValueError(f'The cell {row}, {col} is already occupied')

    self.cells[row*self.dim + col] = player
