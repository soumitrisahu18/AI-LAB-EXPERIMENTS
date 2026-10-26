def print_board(board):
  for row in board:
    print("|".join(row))
    print("-"*5) # Adjusted for visual consistency with a 3x3 board
def check_winner(board):
  # Check rows
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return True

  # Check columns
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
      return True

  # Check main diagonal
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
    return True

  # Check anti-diagonal
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
    return True

  return False # Only return False if no winner is found after all checks


board = [[" " for _ in range(3)] for _ in range(3)] # Corrected list comprehension syntax
player = "X"

for turn in range(9):
  print("\nCurrent Board:")
  print_board(board) # Corrected function call

  print(f"Player {player}'s Turn")

  row = int(input("Enter the row (0-2):"))
  col = int(input("Enter the column (0-2):"))

  if board[row][col] == " ":
    board[row][col] = player

    if check_winner(board):
        print("\nFinal Board:")
        print_board(board) # Corrected function call
        print(f"Player {player} Wins!") # Corrected string formatting
        break

    player = "O" if player == "X" else "X" # Changed '0' to 'O'
  else:
      print("Cell already occupied. Try again.")
else:
  print("\nFinal Board:")
  print_board(board) # Corrected function call
  print("Game Draw!")
