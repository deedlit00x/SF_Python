from random import randint


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за пределы игрового поля"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"


class BoardWrongShipException(BoardException):
    pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y
            if self.o == 0:
                cur_x += i
            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hide=False, size=8):
        self.size = size
        self.hide = hide
        self.count = 0
        self.field = [["0"] * size for _ in range(size)]
        self.busy = []
        self.ships = []

    def __str__(self):
        res = ""
        res += "   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1}  | " + " | ".join(row) + " |"
        if self.hide:
            res = res.replace("■", "0")
        return res

    def sym_act(self):
        global miss_shoot, not_shooted, shrapnel, wounded
        miss_shoot = " "
        not_shooted = "■"
        shrapnel = "."
        wounded = "X"

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contour(self, ship, verb=False):
        self.sym_act()
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = shrapnel
                    self.busy.append(cur)

    def add_ship(self, ship):
        self.sym_act()
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = not_shooted
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        self.sym_act()
        if self.out(d):
            raise BoardOutException()
        if d in self.busy:
            raise BoardUsedException()
        self.busy.append(d)
        for ship in self.ships:
            if ship.shooten(d):
                ship.lives -= 1
                self.field[d.x][d.y] = wounded
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль повреждён!")
                    return True
        self.field[d.x][d.y] = miss_shoot
        print("Промах!")
        return False

    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count == len(self.ships)


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"{user_turn} {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    def ask(self):
        while True:
            coords = input("Ваш ход: ").split()
            if len(coords) != 2:
                print("Введите 2 координаты! Только числа!")
                continue
            x, y = coords
            if not (x.isdigit()) or not (y.isdigit()):
                print("Введите числа! ")
                continue
            x, y = int(x), int(y)
            return Dot(x - 1, y - 1)


class Game:
    def __init__(self, size=8):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hide = True
        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def message(self):
        global user_win, user_turn, user_desk, ai_turn, ai_win, ai_desk, tilde
        user_win = "Пользователь выиграл!"
        user_turn = 'Ход пользователя!'
        user_desk = "Доска пользователя: "
        ai_turn = 'Ход компьютерa!'
        ai_win = "Компьютер выиграл!"
        ai_desk = "Доска компьютера: "
        tilde = '-' * 40

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        self.message()
        greeting = (
            tilde, "        Приветствуем вас в игре   ", "             Mорской бой      ", tilde,
            "        формат ввода: x y   ",
            "        x - номер строки    ", "        y - номер столбца   ", tilde)
        for el in greeting:
            print(el)

    def print_boards(self):
        board = (user_desk, self.us.board, tilde, ai_desk, self.ai.board, tilde)
        print(el for el in board)

    def loop(self):
        num = 0
        while True:
            set_list = (
                tilde, user_desk, self.us.board, tilde, ai_desk, self.ai.board, tilde)
            for el in set_list:
                print(el)
            if num % 2 == 0:
                print(user_turn)
                repeat = self.us.move()
            else:
                print(ai_turn)
                repeat = self.ai.move()
            if repeat:
                num -= 1
            if self.ai.board.defeat():
                self.print_boards()
                print(tilde, '\n', user_win)
                break
            if self.us.board.defeat():
                self.print_boards()
                print(tilde, '\n', ai_win)
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()