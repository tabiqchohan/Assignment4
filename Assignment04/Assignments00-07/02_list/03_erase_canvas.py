import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40

grid = []  # Declare grid globally so it's accessible in the erase function

def create_grid(canvas):
    cells = []
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        row_cells = []
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
            row_cells.append(rect)
        cells.append(row_cells)
    return cells

def erase(event):
    x, y = event.x, event.y
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        canvas.itemconfig(grid[row][col], fill="white")

def main():
    global canvas, grid
    root = tk.Tk()  # Capital "T" in Tk()
    root.title("Grid Example")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.bind("<B1-Motion>", erase)
    canvas.pack()

    grid = create_grid(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
