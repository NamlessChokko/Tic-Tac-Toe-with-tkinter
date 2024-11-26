import tkinter as tk
# You need to have tkinter library installed in your Python environment for this program.

"""
This program creates a simple Tic-Tac-Toe game using tkinter library.
It was Created by Osmany Leyva -> "NamlessChokko"

Features:
1. Two players can play simultaneously.
2. Adjustable grid size (3x3, 4x4, 5x5, etc.)
3. The game board is displayed in interface screen.

Requirements:
- Python 3.x
- tkinter installed in your Python environment.
- A computer with the capacity of turn on.
- 128kb RAM.
- Screen resolution of 174 x 168 or higher.
- 7 kB of free disk space.

Instructions:
- Adjust the format variable to adjust the grid size.
- Adjust the bottoms_size_multiplier variable to change the scaling size of buttons.
- Change the last_turn variable to start with 'O' as the first turn.

Problems:
1. The game does not calculate correctly the screen geometry on different button sizes.
2. The game have some problems detecting draws and wins on different formats.
3. The game does not have an ia to play with, so if you don't have friends this will be a big problem. 

"""


# Grid configuration
format: int = 3  # Grid size (3x3 for Tic-Tac-Toe)
assert format > 2, "Grid size must be greater than 2"
bottoms_size_multiplier: int = 1  # Size multiplier for buttons (only integer values)
assert bottoms_size_multiplier >= 1, "Size multiplier must be greater than 1"
last_turn: bool = True  # Initial turn (Change this to False to start with 'O' as the first turn)


# This variable store the main screen configuration and the grid size.
main_screen_geometry = f"{58 * format * bottoms_size_multiplier}x{56 * format * bottoms_size_multiplier}"


# Create main window
root = tk.Tk()
root.title("XOXO")  # Title of the window
root.geometry(f'{main_screen_geometry}')  # Set window size
root.resizable(False, False)  # Prevent resizing the window

# Function that executes every time a button is clicked
def button_click(button, row: int = format, col: int = format) -> None:
    """Handle button click events."""
    turn_grid(button, row, col)  # Update the grid with the current turn

    winner = check_winner()
    
    if check_draw():  # Check for a draw
        show_exit_dialog("It's a draw!")
        return

    if winner:  
        # Show dialog with winner message
        show_exit_dialog(f"The winner is {winner}!")
        return

    
# Function that changes the button text based on the current turn.
def turn_grid(button, row: int = format, col: int = format) -> None:
    """Update the button text based on the current turn."""
    global last_turn
    if button["text"] == " ":  # Only modify buttons that are empty
        button["text"] = "X" if last_turn else "O" # Use last_turn to switch buttons text
        button["fg"] = "red" if last_turn else "blue"  # Change button color based on the current turn
        print(f"Button pressed: Row {row}, Column {col}, Turn: {'X' if last_turn else 'O'}")
        last_turn = not last_turn  # Toggle turn


#Function that checks for a winner in rows, columns, or diagonals.
def check_winner():
    """Check for a winner in rows, columns, or diagonals."""
    for i in range(format):
        # Check rows
        if (button_matrix[i][0]["text"] != " " and 
            all(button_matrix[i][j]["text"] == button_matrix[i][0]["text"] for j in range(format))):
            return button_matrix[i][0]["text"]

        # Check columns
        if (button_matrix[0][i]["text"] != " " and 
            all(button_matrix[j][i]["text"] == button_matrix[0][i]["text"] for j in range(format))):
            return button_matrix[0][i]["text"]

    # Check diagonal (top-left to bottom-right)
    if (button_matrix[0][0]["text"] != " " and  # Ensure the first button in the diagonal is not empty.
        all(button_matrix[i][i]["text"] == button_matrix[0][0]["text"] for i in range(format))):  
        # `all()` checks if every button in the main diagonal has the same text as the first button (0, 0).
        return button_matrix[0][0]["text"]  # Return the winner's text.

    # Check diagonal (top-right to bottom-left)
    if (button_matrix[0][format - 1]["text"] != " " and  # Ensure the first button in the diagonal is not empty.
        all(button_matrix[i][format - 1 - i]["text"] == button_matrix[0][format - 1]["text"] for i in range(format))):  
        # `all()` checks if every button in the secondary diagonal has the same text as the first button (0, format - 1).
        return button_matrix[0][format - 1]["text"]  # Return the winner's text.

    return None


# Function that checks for a draw.
def check_draw():
    """Check if the game is a draw (no empty spaces left)."""
    for row in button_matrix:
        for button in row:
            if button["text"] == " ":
                return False  # Still empty spaces, not a draw
    return True  # No empty spaces, it's a draw


# Function that displays an exit dialog with winner/draw message and options to restart or exit.
def show_exit_dialog(message: str):
    """Display an exit dialog with winner/draw message and options to restart or exit."""
    dialog = tk.Toplevel(root)
    dialog.title("Game Over")
    dialog.geometry("250x150")
    dialog.resizable(False, False)

    # Display message (winner or draw)
    tk.Label(dialog, text=message, font=("Helvetica", 14)).pack(pady=10)

    # Restart button
    def restart_game():
        dialog.destroy()  # Close the dialog
        reset_game()  # Reset the game board

    tk.Button(dialog, text="Restart", font=("Helvetica", 12), command=restart_game).pack(pady=5)

    # Exit button
    tk.Button(dialog, text="Exit", font=("Helvetica", 12), command=root.destroy).pack(pady=5)


# Function that resets the game board.
def reset_game():
    """Reset the game board to its initial state."""
    global last_turn
    last_turn = True  # Reset turn to X
    for row in button_matrix:
        for button in row:
            button["text"] = " "  # Clear button text
            button["state"] = tk.NORMAL  # Re-enable the button


# Create a matrix to store button references
button_matrix = []


# Create grid
for row in range(format):
    button_row = []
    for col in range(format):
        button = tk.Button(
            root,
            width=3 * bottoms_size_multiplier,
            height=1 * bottoms_size_multiplier,
            font=("Helvetica", 20),
            text=" ",  # Initial empty text
            command=lambda r=row, c=col: button_click(button_matrix[r][c], r, c)
        )
        button.grid(row=row, column=col)
        button_row.append(button)
    button_matrix.append(button_row)


# Start the Tkinter event loop
root.mainloop()