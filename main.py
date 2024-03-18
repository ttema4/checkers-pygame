import pygame

SEQUENCE = "w"


class Menu:
    def __init__(self):
        pass

    def main(self):
        pass


class Board:
    def __init__(self):
        # Список фигур
        self.board_sq = []
        for i in range(64):
            self.board_sq.append(["e", 0])
        # e - empty | w - white | b - black
        """
        Клетки: 0 - пусто 1 - шашка  2 - шашка взята  3 - подсвет как возможный ход 
                4 - ход должен быть сделан этой шашкой  5 - ход должен быть совершен на эту клетку
        """
        # Заполнение
        for k in range(0, 7, 2):
            self.board_sq[k] = ["w", 1]
            self.board_sq[k + 9] = ["w", 1]
            self.board_sq[k + 16] = ["w", 1]
            self.board_sq[k + 41] = ["b", 1]
            self.board_sq[k + 48] = ["b", 1]
            self.board_sq[k + 57] = ["b", 1]
        # Стандартные значения графики
        self.width = 8
        self.height = 8
        self.left = 10
        self.top = 10
        self.cell_size = 85

    def clear_board(self):
        for i in range(len(self.board_sq)):
            if self.board_sq[i][1] == 2:
                self.board_sq[i][1] = 1
            elif self.board_sq[i][1] == 3:
                self.board_sq[i][1] = 0
            elif self.board_sq[i][1] == 4:
                self.board_sq[i][1] = 1
            elif self.board_sq[i][1] == 5:
                self.board_sq[i][1] = 0

    # Рендер поля
    def render(self):
        # Фон
        screen.fill(pygame.Color("grey"))
        # Проход по всем клеткам и их отрисовка
        for j in range(self.height):
            for i in range(self.width):
                pygame.draw.rect(screen, pygame.Color("white"), (i * self.cell_size + self.top,
                                                                 j * self.cell_size + self.left,
                                                                 self.cell_size,
                                                                 self.cell_size), 1)

        for i in range(len(self.board_sq)):
            if self.board_sq[i][1] == 2:
                pygame.draw.rect(screen, pygame.Color("blue"), ((i % 8) * self.cell_size + self.top + 1,
                                                                i // 8 * self.cell_size + self.left + 1,
                                                                self.cell_size - 2,
                                                                self.cell_size - 2))
            elif self.board_sq[i][1] == 3:
                pygame.draw.circle(screen, pygame.Color("blue"), ((i % 8) * self.cell_size +
                                                                  self.top + self.cell_size // 2,
                                                                  i // 8 * self.cell_size +
                                                                  self.left + self.cell_size // 2), self.cell_size // 4)
            elif self.board_sq[i][1] == 4:
                pygame.draw.rect(screen, pygame.Color("green"), ((i % 8) * self.cell_size + self.top + 1,
                                                                 i // 8 * self.cell_size + self.left + 1,
                                                                 self.cell_size - 2,
                                                                 self.cell_size - 2))
            elif self.board_sq[i][1] == 5:
                pygame.draw.circle(screen, pygame.Color("green"), ((i % 8) * self.cell_size +
                                                                   self.top + self.cell_size // 2,
                                                                   i // 8 * self.cell_size +
                                                                   self.left + self.cell_size // 2),
                                   self.cell_size // 4)

        # Отрисовка фигур
        for i in range(len(self.board_sq)):
            if self.board_sq[i][1] in [1, 2, 4]:
                if self.board_sq[i][0] == "w":
                    r = "white"
                else:
                    r = "black"
                pygame.draw.circle(screen, pygame.Color(r), ((i % 8) * self.cell_size +
                                                             self.top + self.cell_size // 2,
                                                             i // 8 * self.cell_size +
                                                             self.left + self.cell_size // 2),
                                   self.cell_size // 2 - 3)

    def check_beat_checker(self, color):
        for i in range(len(self.board_sq)):
            if color == self.board_sq[i][0]:
                if self.check_beat_checker_rec_helper(i, color):
                    self.board_sq[i][1] = 4

    def check_beat_checker_rec_helper(self, index=0, color="w"):
        s = False
        reversed_color = "w"
        if color == "w":
            reversed_color = "b"
        if index < 48:
            if index % 8 > 2 and self.board_sq[index + 7] == [reversed_color, 1]:
                if self.board_sq[index + 14][1] == 0:
                    self.board_sq[index + 14] = ["e", 5]
                    self.check_beat_checker_rec_helper(index + 14, color)
                    s = True
            if index % 8 < 6 and self.board_sq[index + 9] == [reversed_color, 1]:
                if index < 46:
                    if self.board_sq[index + 18][1] == 0:
                        self.board_sq[index + 18] = [reversed_color, 5]
                        self.check_beat_checker_rec_helper(index + 18, color)
                        s = True
        if index > 15:
            if index % 8 < 6 and self.board_sq[index - 7] == [reversed_color, 1]:
                if self.board_sq[index - 14][1] == 0:
                    self.board_sq[index - 14] = ["e", 5]
                    self.check_beat_checker_rec_helper(index - 14, color)
                    s = True
            if index % 8 > 2 and self.board_sq[index - 9] == [reversed_color, 1]:
                if index > 17:
                    if self.board_sq[index - 18][1] == 0:
                        self.board_sq[index - 18] = ["e", 5]
                        self.check_beat_checker_rec_helper(index - 18, color)
                        s = True
        return s

    def check_mb_step(self, pos):
        self.board_sq[pos[0] + pos[1] * 8][1] = 2
        if self.board_sq[pos[0] + pos[1] * 8][0] == "w":
            if pos[0] != 7 and self.board_sq[pos[0] + pos[1] * 8 + 9][1] != 1:
                self.board_sq[pos[0] + pos[1] * 8 + 9] = ["e", 3]
            if pos[0] != 0 and self.board_sq[pos[0] + pos[1] * 8 + 7][1] != 1:
                self.board_sq[pos[0] + pos[1] * 8 + 7] = ["e", 3]
        else:
            if pos[0] != 7 and self.board_sq[pos[0] + pos[1] * 8 - 7][1] != 1:
                self.board_sq[pos[0] + pos[1] * 8 - 7] = ["e", 3]
            if pos[0] != 0 and self.board_sq[pos[0] + pos[1] * 8 - 9][1] != 1:
                self.board_sq[pos[0] + pos[1] * 8 - 9] = ["e", 3]

    # Обработка нажатия на поле
    def sq_coor(self, pos):
        global SEQUENCE
        pos = [(pos[0] - self.top) // self.cell_size, (pos[1] - self.left) // self.cell_size]
        if pos[0] > self.width - 1 or pos[1] > self.height - 1 or 0 > pos[0] or 0 > pos[1]:
            print("None")
        else:
            if self.board_sq[pos[0] + pos[1] * 8][1] != 0 and self.board_sq[pos[0] + pos[1] * 8][0] in [SEQUENCE, "e"]:
                is_moving = [False, 0]
                for i in range(len(self.board_sq)):
                    if self.board_sq[i][1] == 2:
                        is_moving = [True, i]
                        break
                if is_moving[0]:
                    if self.board_sq[pos[0] + pos[1] * 8][1] == 5:
                        self.board_sq[pos[0] + pos[1] * 8] = self.board_sq[is_moving[1]]
                        self.board_sq[is_moving[1]] = []
                    else:
                        if self.board_sq[pos[0] + pos[1] * 8] == [SEQUENCE, 1]:
                            self.clear_board()
                            self.check_mb_step(pos)
                        else:
                            if self.board_sq[pos[0] + pos[1] * 8][1] == 3:
                                self.board_sq[pos[0] + pos[1] * 8] = self.board_sq[is_moving[1]]
                                self.board_sq[is_moving[1]] = ["e", 0]
                                if SEQUENCE == "w":
                                    SEQUENCE = "b"
                                else:
                                    SEQUENCE = "w"
                            self.clear_board()
                elif self.board_sq[pos[0] + pos[1] * 8][1] == 5:
                    self.clear_board()
                else:
                    self.check_mb_step(pos)
            else:
                self.clear_board()
            print(pos)
        self.check_beat_checker(SEQUENCE)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Checkers")
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    board = Board()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                board.sq_coor(event.pos)
        board.render()
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
