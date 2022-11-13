import sys
import os
from PyQt6.QtWidgets import   QFrame, QWidget,QVBoxLayout,QFileDialog ,QPushButton,  QMainWindow, QApplication, QLabel, QCheckBox, QComboBox,QLineEdit,QLineEdit, QSpinBox, QDoubleSpinBox, QSlider

from PyQt6.QtCore import Qt, QUrl, QSize

from PyQt6.QtGui import QPixmap, QImage

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("App")

        self.setFixedSize(QSize(900, 600))

        #кнопка открытия файла
        btn = QPushButton('Откройте файл')
        self.setCentralWidget(btn)
        btn.setGeometry(430, 10, 120, 60)
        btn.clicked.connect(self.evt_btn_clicked)
        
        layout = QVBoxLayout(self)
        layout.addWidget(btn)

        #кнопка анализа картинок
        btn2 = QPushButton('Использовать ИИ')
        self.setCentralWidget(btn2)
        btn2.setGeometry(300, 10, 120, 60)

        layout.addWidget(btn2)
        

        filepath = None
        probability = 98
        probability_label = QLabel(f'Вероятность {probability}')
        self.setCentralWidget(probability_label)

        probability_label.setGeometry(390, 400, 300, 330)

        layout.addWidget(probability_label)

       
        ''' label = QLabel(filepath)
        pixmap = QPixmap.fromImage(QImage(self.filePATH(result)))
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label.setGeometry(200, 150, 300, 100)
        label.resize(pixmap.width(),
                         pixmap.height())
        label.setPixmap(pixmap)'''
        
        
    '''def filePATH(self, result):
        if len(result()) > 1:
            for i in range(len(result)):
                if 'jpg' in result[i]:
                    filepath = result[i] 
            if filepath == None:
                filepath = result[0]
        else:
            filepath = result[0]
        return filepath 
    def location(self):
        return self.evt_btn_clicked()[0]'''
    

        

    def evt_btn_clicked(self): #Открытие проводника по кнопке
        res = QFileDialog.getOpenFileNames(
            self, 'Откройте файл', '/Users')
        print(res)
        return res[0]



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()