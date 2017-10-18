from PyQt5.Qt import *


class GameField(QWidget):

    def __init__(self, player, x, y, game_speed):
        super().__init__()
        self.player = player

        self.init_ui(x, y)
        self.start()

        self.game_speed = game_speed
        self.timer = self.startTimer(self.game_speed)

    def init_ui(self, x, y):

        self.resize(x, y)
        self.setWindowTitle("TNTD")
        self.center()
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def start(self):
        pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.player.x, self.player.y, self.player)

    def timerEvent(self, event):
        self.player.update()
        self.repaint()

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Up:
            self.player.move(0, -1)
        elif event.key() == Qt.Key_Down:
            self.player.move(0, 1)
        elif event.key() == Qt.Key_Left:
            self.player.move(-1, -0)
        elif event.key() == Qt.Key_Right:
            self.player.move(1, 0)

    def keyReleaseEvent(self, event):

        if event.key() == Qt.Key_Up:
            self.player.move(0, 0)
        elif event.key() == Qt.Key_Down:
            self.player.move(0, 0)
        elif event.key() == Qt.Key_Left:
            self.player.move(0, -0)
        elif event.key() == Qt.Key_Right:
            self.player.move(0, 0)
