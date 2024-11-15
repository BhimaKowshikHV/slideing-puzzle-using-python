import random
import copy
goal_state = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 0]]  

class SlidingPuzzle:
    def __init__(self, board=None):
        if board:
            self.board = board
        else:
            self.board = [[(i + j * 4 + 1) % 16 for i in range(4)] for j in range(4)]
        self.empty_pos = self.find_empty_position()
        
    def display(self):
        """Display the puzzle board."""
        for row in self.board:
            print(' '.join(str(x) if x != 0 else ' ' for x in row))
        print()
    
    def find_empty_position(self):
        """Find the position of the empty space (0)."""
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return (i, j)

    def is_goal_state(self):
        """Check if the current board is in the goal state."""
        return self.board == goal_state

    def manhattan_distance(self):
        """Calculate the total Manhattan Distance of the current board."""
        distance = 0
        for r in range(4):
            for c in range(4):
                if self.board[r][c] != 0:
                    goal_r, goal_c = divmod(self.board[r][c] - 1, 4)
                    distance += abs(goal_r - r) + abs(goal_c - c)
        return distance

    def valid_moves(self):
        """Return a list of valid moves based on the position of the empty space."""
        row, col = self.empty_pos
        moves = []
        if row > 0: moves.append('up')  
        if row < 3: moves.append('down')  
        if col > 0: moves.append('left')  
        if col < 3: moves.append('right')  
        return moves
    
    def make_move(self, move):
        """Make a move by swapping the empty space with the neighboring tile."""
        row, col = self.empty_pos
        new_board = copy.deepcopy(self.board)
        
        if move == 'up':
            new_board[row][col], new_board[row - 1][col] = new_board[row - 1][col], new_board[row][col]
            new_empty_pos = (row - 1, col)
        elif move == 'down':
            new_board[row][col], new_board[row + 1][col] = new_board[row + 1][col], new_board[row][col]
            new_empty_pos = (row + 1, col)
        elif move == 'left':
            new_board[row][col], new_board[row][col - 1] = new_board[row][col - 1], new_board[row][col]
            new_empty_pos = (row, col - 1)
        elif move == 'right':
            new_board[row][col], new_board[row][col + 1] = new_board[row][col + 1], new_board[row][col]
            new_empty_pos = (row, col + 1)
        
        return SlidingPuzzle(new_board), new_empty_pos
    
    def hill_climb(self):
        """Hill climbing algorithm to solve the puzzle."""
        current_puzzle = self
        print("Starting Hill Climbing Algorithm:")
        
        while not current_puzzle.is_goal_state():
            print(f"Current Manhattan Distance: {current_puzzle.manhattan_distance()}")
            moves = current_puzzle.valid_moves()
            next_puzzle = None
            next_manhattan = float('inf')
            
    
            for move in moves:
                neighbor, _ = current_puzzle.make_move(move)
                dist = neighbor.manhattan_distance()
                
                if dist < next_manhattan:
                    next_manhattan = dist
                    next_puzzle = neighbor
            
            if next_puzzle.manhattan_distance() >= current_puzzle.manhattan_distance():
                print("Stuck in local optimum, no better moves available.")
                break  
            current_puzzle = next_puzzle
        
        current_puzzle.display()
        return current_puzzle.is_goal_state()

def play_game():
    """Play the sliding puzzle using Hill Climbing."""
    puzzle = SlidingPuzzle()
    
    puzzle.display()

    if puzzle.hill_climb():
        print("Puzzle Solved!")
    else:
        print("Unable to solve the puzzle using Hill Climbing.")

if __name__ == "__main__":
    play_game()
