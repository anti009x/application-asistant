import random
import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow

from equalizer_bar import EqualizerBar


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.equalizer = EqualizerBar(
            15,
            [
                "#0C0786",
                "#1A1A9C",
                "#3333B3",
                "#4D4DCC",
                "#6666E6",
                "#8080FF",
            ],
        )
        self.equalizer.setBarSolidYPercent(0.4)
        self.equalizer.setBarSolidXPercent(0.4)  # Uncommented to set X percent
        self.setCentralWidget(self.equalizer)

        self._timer = QTimer()
        self._timer.setInterval(100)
        self._timer.timeout.connect(self.update_values_based_on_text)  # Corrected to connect to the right method
        self._timer.start()

    def update_values_based_on_text(self):
        text = "Halo Saya Adalah Asisten Virtual Anda"
        print(text)
        # Example logic to update equalizer based on text length
        values = [min(100, len(text) * random.randint(1, 3)) for _ in range(15)]
        self.equalizer.setValues(values)
        QTimer.singleShot(100000, self.update_values_based_on_text)  # Corrected to 1000ms (1 second)


app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()