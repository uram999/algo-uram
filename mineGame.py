import random


class MineGame:
    ROW = 10    # ROW 수
    COL = 10    # COLUMN 수
    MINE = 0    # 지뢰 갯수
    MATRIX = [[0] * 10 for i in range(10)]  # 10X10 배열 초기화

    def __init__(self):
        pass

    def game_main(self):
        print("시작합니다 !!!")

        self.set_mine()

        self.game_result()
        self.print_matrix()

    # 지뢰 심기 함수 : 자동으로 지뢰를 10개 만든다
    def set_mine(self):

        while self.MINE < 10:
            ran_row = random.randrange(0, 9)
            ran_col = random.randrange(0, 9)

            if self.MATRIX[ran_row][ran_col] == 0:
                self.MATRIX[ran_row][ran_col] = 9
                self.MINE += 1

    # 지뢰 판별 함수 : 주변 1칸내 지뢰를 판별한다.
    def exist_mine(self, row, col):

        if row < 0 or row >= self.ROW or col < 0 or col >= self.COL:
            return False

        return self.MATRIX[row][col] == 9

    # 지뢰 숫자 계산 함수 : 총 사방 칸의 지뢰를 반별하여 숫자를 반환한다.
    def get_mine_number(self, row, col):
        count = 0
        if self.exist_mine(row - 1, col - 1):
            count += 1
        if self.exist_mine(row - 1, col):
            count += 1
        if self.exist_mine(row - 1, col + 1):
            count += 1
        if self.exist_mine(row, col - 1):
            count += 1
        if self.exist_mine(row, col + 1):
            count += 1
        if self.exist_mine(row + 1, col - 1):
            count += 1
        if self.exist_mine(row + 1, col):
            count += 1
        if self.exist_mine(row + 1, col + 1):
            count += 1

        return count

    # 게임 진행 함수 : 배열을 차례대로 누르는 게임을 진행
    def game_result(self):
        for idx_i, val_i in enumerate(self.MATRIX):

            for idx_j, val_j in enumerate(val_i):
                if self.MATRIX[idx_i][idx_j] != 9:
                    self.MATRIX[idx_i][idx_j] = self.get_mine_number(idx_i, idx_j)

    # 결과 출력 함수 : 진행 된 게임의 결과를 출력한다.
    def print_matrix(self):
        for idx_i, val_i in enumerate(self.MATRIX):
            row_data = ''

            for idx_j, val_j in enumerate(val_i):
                if  val_j == 9:
                    row_data = row_data + ' *'
                else:
                    row_data = row_data + ' ' + str(val_j)

            print(row_data)


if __name__ == '__main__':
    e = MineGame()
    e.game_main()


