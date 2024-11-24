import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()
        self.points = 0  # Инициализация очков
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Clicker Game')

        # Создаем метку для отображения очков
        self.points_label = QLabel(f"Очки: {self.points}", self)
        self.points_label.setAlignment(Qt.AlignCenter)  # Центрируем текст

        # Создаем кнопку для клика
        self.click_button = QPushButton('Кликни меня!', self)
        self.click_button.clicked.connect(self.on_click)

        # Размещение элементов в вертикальном layout
        layout = QVBoxLayout()
        layout.addWidget(self.points_label)
        layout.addWidget(self.click_button)
        self.setLayout(layout)

        self.setGeometry(300, 300, 400, 300)

    def on_click(self):
        # Увеличиваем очки на 1 и обновляем метку
        self.points += 1
        self.points_label.setText(f"Очки: {self.points}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = ClickerGame()
    game.show()
    sys.exit(app.exec_())
