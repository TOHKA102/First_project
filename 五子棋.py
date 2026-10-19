import os


def create_board():
  # 初始化 15x15 的棋盘，用 '.' 代表空位
  return [["." for _ in range(15)] for _ in range(15)]


def print_board(board):
  # 打印顶部的列号标尺（1 到 15）
  header = "   " + " ".join([str(i).zif if False else str(i) for i in range(1, 16)])
  # 为了对齐好看，给双位数和单位数做一点间距调整
  header_list = []
  for i in range(1, 16):
    header_list.append(f"{i:2d}")
  print("    " + " ".join(header_list))

  # 打印每一行以及左侧的行号（1 到 15）
  for idx, row in enumerate(board):
    row_str = " ".join([f" {cell} " for cell in row])
    print(f"{idx + 1:2d} |{row_str}|")


def check_win(board, row, col, player):
  # 检查刚刚落子的位置 (row, col) 是否构成了五子连珠
  # 四个方向：(水平), (垂直), (左斜), (右斜)
  directions = [
      (0, 1),  # 水平方向 (右)
      (1, 0),  # 垂直方向 (下)
      (1, 1),  # 右下对角线
      (1, -1),  # 左下对角线
  ]

  for dr, dc in directions:
    count = 1  # 包含刚落的这一子

    # 1. 向正方向检查连续相同的棋子
    r, c = row + dr, col + dc
    while 0 <= r < 15 and 0 <= c < 15 and board[r][c] == player:
      count += 1
      r += dr
      c += dc

    # 2. 向反方向检查连续相同的棋子
    r, c = row - dr, col - dc
    while 0 <= r < 15 and 0 <= c < 15 and board[r][c] == player:
      count += 1
      r -= dr
      c -= dc

    # 如果任意一个方向达到了 5 个或以上，说明获胜
    if count >= 5:
      return True

  return False


def main():
  board = create_board()
  current_player = "X"  # X 代表黑棋，O 代表白棋

  while True:
    os.system("cls" if os.name == "nt" else "clear")  # 自动清屏
    print(f"当前轮到【 {'黑棋 (X)' if current_player == 'X' else '白棋 (O)'} 】落子")
    print_board(board)

    try:
      # 获取输入并把 1-15 转换为 0-14 的列表索引
      input_row = int(input("请输入行 (1-15): ")) - 1
      input_col = int(input("请输入列 (1-15): ")) - 1
    except ValueError:
      print("输入无效，请输入数字！")
      input("按回车键继续...")
      continue

    # 检查坐标是否在棋盘范围内
    if not (0 <= input_row < 15 and 0 <= input_col < 15):
      print("坐标超出范围，请输入 1 到 15 之间的数字！")
      input("按回车键继续...")
      continue

    # 检查该位置是否已经被占用
    if board[input_row][input_col] != ".":
      print("该位置已经有棋子了，不能重复落子！")
      input("按回车键继续...")
      continue

    # 落子
    board[input_row][input_col] = current_player

    # 检查是否获胜
    if check_win(board, input_row, input_col, current_player):
      os.system("cls" if os.name == "nt" else "clear")
      print_board(board)
      print(f"\n🎉 恭喜！【 {current_player} 】 获胜！🎉")
      break

    # 切换玩家
    current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
  main()