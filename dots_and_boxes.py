class Game:
    def __init__(self, board):
        self.board = board
        self.boxes = self.get_boxes(self.board)
        self.results = []

    @staticmethod
    def get_boxes(board):
        boxes = []
        start = 1
        for i in range(board):
            for j in range(board):
                # draw the four lines to make up a complete box
                top = start + j
                left = top + board
                right = left + 1
                bot = right + board
                # keep a list of all possible boxes
                boxes.append([top, left, right, bot])
            start += 2 * board + 1
        return boxes

    def play(self, lines):
        return self.test_boxes(self.boxes, lines)

    def test_boxes(self, boxes, lines):
        for box in boxes:
            line_in, line_out = [], []
            # check how many lines have been drawn for each box
            for i in box:
                line_in.append(i) if i in lines else line_out.append(i)
            if len(line_in) == 3:
                # only need one line - add last line needed
                line_in = line_in + line_out
                self.results.extend(line_in)
                # add new lines as they're drawn
                lines = list(set(lines + self.results))
                # re-check connected boxes if adding lines
                new_boxes = self.update_boxes(sorted(line_in), self.boxes)
                if new_boxes:
                    self.test_boxes(new_boxes, lines)
            elif len(line_in) == 4:
                self.results.extend(line_in)
                lines = list(set(lines + self.results))
        return sorted(list(set(self.results + lines)))

    def update_boxes(self, completed, boxes):
        box_num = boxes.index(completed)
        connected = []
        connections = [-self.board, -1]
        for connection in connections:
            try:
                connected.append(boxes[box_num + connection])
            except IndexError:
                pass
        return connected

original = [5, 6, 12, 13, 19, 20, 23]
game = Game(3)
print(game.play(original))
