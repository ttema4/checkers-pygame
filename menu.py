if self.board_sq[pos[0] + pos[1] * 8][1] == 3:
    self.board_sq[pos[0] + pos[1] * 8] = self.board_sq[is_moving[1]]
    self.board_sq[is_moving[1]] = ["e", 0]
    if SEQUENCE == "w":
        SEQUENCE = "b"
    else:
        SEQUENCE = "w"
    self.clear_board()
elif self.board_sq[pos[0] + pos[1] * 8] == [1, SEQUENCE]:
    self.check_mb_step(pos)
else:
    self.clear_board()