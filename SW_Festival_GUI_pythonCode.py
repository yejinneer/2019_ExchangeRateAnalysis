import sys, random, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):
    btnlist = list()

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        global btnlist

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        nameList = list()
        for path, temp, files in os.walk("countries")  :
            for file in files :
                nameList.append(path + "/" + file)

        i = 0; k = 0; x = 0; y = 0 ; 

        for element in nameList :
            pixmap = QPixmap(element)
            pixmap = pixmap.scaled(200, 200) 
            lbl_img = QLabel()
            lbl_img.setPixmap(pixmap)
            lbl_img.move(100,100)
            grid_layout.addWidget(lbl_img, x,y)

            btn = QPushButton(element.split(".")[0].split("/")[1], self)
            self.btnlist.append(btn)
            btn.setStyleSheet("font: bold; background-color:#fff0b3; font-size: 30px")
            btn.setMinimumSize(170,100)
            btn.setMaximumSize(170,100)
            btn.move(250 + k * 600, 80 + i * 250)
            btn.toggle()
            if(btn.text() == 'Australia'):
                btn.clicked.connect(self.openSecondDialog_Australia)
            if(btn.text() == 'China'):
                btn.clicked.connect(self.openSecondDialog_China)
            if(btn.text() == 'Europe'):
                btn.clicked.connect(self.openSecondDialog_China)
            if(btn.text() == 'HongKong'):
                btn.clicked.connect(self.openSecondDialog_HongKong)
            if(btn.text() == 'Japan'):
                btn.clicked.connect(self.openSecondDialog_Japan)
            if(btn.text() == 'Philippines'):
                btn.clicked.connect(self.openSecondDialog_Philippines)
            if(btn.text() == 'Singapore'):
                btn.clicked.connect(self.openSecondDialog_Singapore)
            if(btn.text() == 'Taiwan'):
                btn.clicked.connect(self.openSecondDialog_Taiwan)
            if(btn.text() == 'Thailand'):
                btn.clicked.connect(self.openSecondDialog_Thailand)
            if(btn.text() == 'UK'):
                btn.clicked.connect(self.openSecondDialog_UK)
            if(btn.text() == 'USA'):
                btn.clicked.connect(self.openSecondDialog_USA)
            if(btn.text() == 'Vietnam'):
                btn.clicked.connect(self.openSecondDialog_Vietnam)
    
   
            i+=1; x+=1
            if i%4==0 :
                k+=1; i=0; y+=1; x=0

        self.setWindowTitle('   <<  Prediction  of  World\'s  Exchange  Rate  >>   2019 KyungHee SW festival __ 서예진, 이효순, 성예지')
        self.setGeometry(300, 300, 300, 200)
        self.setStyleSheet("background-color: #ffcc00;")
        self.resize(1800, 1000)
        self.show()


    def openSecondDialog_Australia(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of Australia")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("Australia_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec()

    def openSecondDialog_China(Self):
        mydialog = QDialog()
        mydialog.setModal(True)
        mydialog.setWindowTitle("Our Prediction of China")

        grid_layout = QGridLayout()
        mydialog.setLayout(grid_layout)


        graphList = list()
        for path, temp, files in os.walk("china_graph")  :
            for file in files :
                graphList.append(path + "/" + file)

        x = 2; y = 1 ;

        for element in graphList :
            pixmap = QPixmap(element)
            pixmap = pixmap.scaled(600, 400) 
            lbl_img = QLabel()
            lbl_img.setPixmap(pixmap)
            lbl_img.move(100,100)
            grid_layout.addWidget(lbl_img, x,y)
            x+=2; 

        lbl_01 = QLabel()
        lbl_01.setText("<<최근 6개월 변화추이>>\n")
        lbl_01.setStyleSheet("font: bold;font-size: 30px")
        lbl_02 = QLabel()
        lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
        lbl_02.setStyleSheet("font: bold;font-size: 30px")

        grid_layout.addWidget(lbl_01,1,1)
        grid_layout.addWidget(lbl_02,3,1)

        
        mydialog.setStyleSheet("background-color: #ffcc00;")
        mydialog.exec()


    def openSecondDialog_Europe(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of Europe")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("Europe_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec()


    def openSecondDialog_HongKong(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of HongKong")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("HongKong_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec() 

    def openSecondDialog_Japan(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of Japan")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("Japan_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec() 

    def openSecondDialog_Philippines(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of Philippines")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("Philippines_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec() 

    def openSecondDialog_Singapore(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of Singapore")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("Singapore_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec() 

    def openSecondDialog_Taiwan(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of Taiwan")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("Taiwan_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec() 

    def openSecondDialog_Thailand(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of Thailand")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("Thailand_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec()

    def openSecondDialog_UK(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of United Kingdom")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("UK_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec() 

    def openSecondDialog_USA(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of USA")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("USA_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec() 

    def openSecondDialog_Vietnam(Self):
            mydialog = QDialog()
            mydialog.setModal(True)
            mydialog.setWindowTitle("Our Prediction of Vietnam")

            grid_layout = QGridLayout()
            mydialog.setLayout(grid_layout)


            graphList = list()
            for path, temp, files in os.walk("Vietnam_graph")  :
                for file in files :
                    graphList.append(path + "/" + file)

            x = 2; y = 1 ;

            for element in graphList :
                pixmap = QPixmap(element)
                pixmap = pixmap.scaled(600, 400) 
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap)
                lbl_img.move(100,100)
                grid_layout.addWidget(lbl_img, x,y)
                x+=2; 

            lbl_01 = QLabel()
            lbl_01.setText("<<최근 6개월 변화추이>>\n")
            lbl_01.setStyleSheet("font: bold;font-size: 30px")
            lbl_02 = QLabel()
            lbl_02.setText("\n\n<<최근 2주 변화추이>>\n")
            lbl_02.setStyleSheet("font: bold;font-size: 30px")

            grid_layout.addWidget(lbl_01,1,1)
            grid_layout.addWidget(lbl_02,3,1)

            mydialog.setStyleSheet("background-color: #ffcc00;")
            mydialog.exec() 


    def closeEvent(self, QcloseEvent):
        ans = QMessageBox.question(self,"종료 확인", "종료하시겠습니까?", 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes :
            QcloseEvent.accept()
        else:
            QcloseEvent.ignore()
                       
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())