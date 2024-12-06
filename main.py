from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtWidgets import (
    QApplication, QLineEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QWidget
)
import sys
import random

# Ensure that EqualizerBar is imported or defined appropriately
from equalizer_bar import EqualizerBar

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Asisten Virtual Rina")
        self.resize(1920, 900)
        self.layout = QVBoxLayout()  # Mengubah ke QVBoxLayout untuk penyelarasan vertikal
        self.setGeometry(100, 100, 600, 400) 

        # Membuat tiga tombol titik
        self.button1 = QPushButton("")
        self.button2 = QPushButton("")
        self.button3 = QPushButton("")

        # Menghubungkan tombol ke slot yang sama
        self.button1.clicked.connect(self.button_clicked)
        self.button2.clicked.connect(self.button_clicked)
        self.button3.clicked.connect(self.button_clicked)
        
        # Mengatur gaya untuk tombol agar berbentuk lingkaran
        button_style = """
            background-color: blue; 
            text-align: center;
            text-decoration: none;
            color: white; 
            font-size: 30px; 
            min-width: 60px; 
            min-height: 60px; 
            max-width: 60px; 
            max-height: 60px; 
            margin: 0;
            padding: 0;
            
            border-radius: 30px;  /* Setengah dari lebar/tinggi untuk membuatnya berbentuk lingkaran */
        """
        self.button1.setStyleSheet(button_style)
        self.button2.setStyleSheet(button_style)
        self.button3.setStyleSheet(button_style)

        # Menambahkan tombol ke tata letak dengan jarak minimal
        self.layout.setSpacing(10)  # Memberi sedikit jarak antara tombol dan equalizer
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        # Membuat tata letak horizontal untuk tombol
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(10)  # Memberi jarak antar tombol
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.addWidget(self.button1)
        self.button_layout.addWidget(self.button2)
        self.button_layout.addWidget(self.button3)
        
        # Menambahkan tata letak tombol ke tata letak utama
        self.layout.addLayout(self.button_layout)
        
        # Inisialisasi Equalizer
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
        self.equalizer.setBarSolidXPercent(0.4)
        self.equalizer.hide()  # Sembunyikan equalizer awalnya
        self.layout.addWidget(self.equalizer)

        # Mengisi elemen kosong dengan input teks
        self.text_input = QLineEdit()
        self.text_input.setText("")  # Mulai dengan teks kosong
        self.fade_text = "Halo Saya Adalah Rina , Asisten Virtual Anda"
        self.fade_index = 0

        def update_text():
            if self.fade_index < len(self.fade_text):
                self.text_input.setText(self.text_input.text() + self.fade_text[self.fade_index])
                self.fade_index += 1
                QTimer.singleShot(150, update_text)  # Delay 150ms untuk efek fade
            else:
                # Matikan equalizer ketika teks telah dirender sepenuhnya
                self.equalizer.hide()
                self.button1.show()
                self.button2.show()
                self.button3.show()

        update_text()
        
        # Menambahkan gaya untuk input teks
        text_input_style = """
            margin-top: -5px;  /* Mengurangi margin atas untuk mendekatkan teks ke tombol */
            font-size: 20px;
            padding: 5px;  /* Mengurangi padding untuk mengurangi tinggi teks */
            text-align: center;
            background-color: transparent;
            border: none;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            color: #333;
        """
        self.text_input.setStyleSheet(text_input_style)
        
        # Mengatur teks input agar dimulai dari tengah
        self.text_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.layout.addWidget(self.text_input)
        
        self.setLayout(self.layout)

        # Set up QTimer to periodically check the text input
        self._timer = QTimer()
        self._timer.setInterval(100)  # Check every 100ms for faster response
        self._timer.timeout.connect(self.update_values_based_on_text)
        self._timer.start()

    def button_clicked(self):
        print("Tombol diklik")

    def update_values_based_on_text(self):
        text = self.text_input.text().strip()
        if text and self.fade_index < len(self.fade_text):
            # Jika ada teks input dan teks belum sepenuhnya dirender, tampilkan equalizer dan sembunyikan tombol
            self.equalizer.show()
            self.button1.hide()
            self.button2.hide()
            self.button3.hide()

            # Update equalizer values based on text
            values = [min(100, len(text) * random.randint(1, 3)) for _ in range(15)]
            self.equalizer.setValues(values)
        else:
            # Jika tidak ada teks input atau teks telah sepenuhnya dirender, tampilkan tombol dan sembunyikan equalizer
            self.equalizer.hide()
            self.button1.show()
            self.button2.show()
            self.button3.show()
            
          

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()