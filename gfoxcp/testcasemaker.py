def generate_500x500_test(filename="test500.in"):
    R, C = 500, 500
    # Initialize a 500x500 grid of empty space
    grid = [["." for _ in range(C)] for _ in range(R)]

    # 1. Create Bedrock Borders
    for i in range(R):
        grid[i][0] = grid[i][C-1] = "#"
    for j in range(C):
        grid[0][j] = grid[R-1][j] = "#"

    # 2. Place Critical Points
    # S = Steve, E = Exit, L = Lava
    grid[1][1] = "S"
    grid[R-2][C-2] = "E"
    grid[1][C-2] = "L"
    grid[R-2][1] = "L"

    # 3. Write to File
    with open(filename, "w") as f:
        f.write("1\n") # Number of test cases
        f.write(f"{R} {C}\n") # Rows and Columns
        for row in grid:
            f.write("".join(row) + "\n")
    
    print(f"Success! Generated {filename}")

generate_500x500_test()
