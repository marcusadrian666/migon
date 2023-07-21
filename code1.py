def print_maze(maze, current_pos):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == current_pos:
                print("O", end=" ")  # 当前位置用O表示
            else:
                print(maze[row][col], end=" ")
        print()

def is_valid_move(maze, row, col):
    rows = len(maze)
    cols = len(maze[0])
    return 0 <= row < rows and 0 <= col < cols and maze[row][col] == "."

def find_exit(maze, row, col):
    if not is_valid_move(maze, row, col):
        return False

    if maze[row][col] == "E":  # 找到出口
        print("恭喜你，成功找到出口！")
        return True

    maze[row][col] = "V"  # 标记当前位置为已访问

    # 尝试向四个方向移动
    if find_exit(maze, row - 1, col):
        return True
    if find_exit(maze, row + 1, col):
        return True
    if find_exit(maze, row, col - 1):
        return True
    if find_exit(maze, row, col + 1):
        return True

    maze[row][col] = "."  # 若当前位置没有通路，则将标记重置
    return False

def main():
    # 迷宫地图示例，用"."表示通路，"#"表示墙壁，"E"表示出口
    maze = [
        ["#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", ".", ".", "#"],
        ["#", ".", ".", "#", "#", ".", "#"],
        ["#", "#", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#"],
    ]

    start_row, start_col = 1, 1  # 起始位置
    print("迷宫地图：")
    print_maze(maze, (start_row, start_col))

    if not find_exit(maze, start_row, start_col):
        print("很抱歉，没有找到出口。")

if __name__ == "__main__":
    main()
