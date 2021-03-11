import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from program2_ui import Ui_Dialog

class myUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()
        
        def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()


    def mouseMoveEvent(self, event):
        if(event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()



    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False


    def paintEvent(self, event):
        canvasPainter  = QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image, self.image.rect() )
        
    def accept(self):
        self.image.fill(Qt.white)
        self.update()
    
    def reject(self):
        print("ho")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myUI()
    w.show()
    sys.exit(app.exec_())

    
