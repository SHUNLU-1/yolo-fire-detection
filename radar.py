
from PyQt5.QtGui import QPainter, QPen, QPolygon
import cv2
from PyQt5.QtCore import  Qt, QPoint
import sys
import serial
import serial.tools.list_ports
from detect_ywq import detectapi
from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow
import time
from threading import Thread
import torch
import traceback
point=QPoint(100,100)
location=[]
label_name=[]
# -*- coding:utf-8 -*-
#coding: unicode_escape

# ui = mainwindow.Ui_MainWindow()
cap=cv2.VideoCapture()

ser = serial.Serial()

class Stop_Threads(object):
    Uart_stop_threads = False
    Image_stop_threads = False
    Uart_start_flag=False
    Image_start_flag=False
stop_ths=Stop_Threads()

class Uart_Thread(Thread):
    def __init__(self,threadname):
        Thread.__init__(self, name=threadname)
    def run(self):
        while True:
            if (stop_ths.Uart_stop_threads):
                break
            elif (ser.is_open == True):
                self.RC_data = ser.read_all()
                # if self.RC_data != b'':
                # print('receive',self.RC_data.decode("gbk"))
                # ui.Rev_textEdit.insertPlainText(self.RC_data.decode('ISO-8859-1'))
                # ui.Rev_textEdit.insertPlainText(self.RC_data.decode('utf-8'))
                # ui.Rev_textEdit.moveCursor(ui.Rev_textEdit.textCursor().End)  # 文本框显示到底部

            time.sleep(0.003)  # 休眠
            # 定时发送数据

class Image_Thread(Thread):  # 线程2
    def __init__(self,threadname):
        Thread.__init__(self,name=threadname)
    def run(self):
        while True:
            if (stop_ths.Image_stop_threads):
                break
            else:
                flag, self.image = cap.read()
                self.image = cv2.flip(self.image, 180)
                global location
                global point
                global label_name
                show= cv2.resize(self.image, (640, 480))

                # show = cvtColor(self.image, COLOR_BGR2RGB)
                # if (ui.detect_checkBox.isChecked()):
                result, names,location,label_name= yolo.detect([show], 0.5, 0.5)
                show = result[0][0]  # 第一张图片的处理结果图片
                ex.repaint()
                cv2.imshow("detect",show);
                cv2.waitKey(2)
                # showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
                # ui.showimage.setPixmap(QtGui.QPixmap.fromImage(showImage))
            time.sleep(0.003)

class Example(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(640,480)
        self.setWindowTitle('Points')
        self.init()
        self.show()
    def init(self):
        self.CAM_NUM=0
        flag = cap.open(self.CAM_NUM)
        ser.port = 'COM7'
        ser.baudrate = 115200
        ser.bytesize = 8
        ser.stopbits = 1
        ser.parity = 'N'
        try:
            ser.open()
        except:
            traceback.print_exc()
        if ser.isOpen() == False:
            QtWidgets.QMessageBox.warning(self, u"warning", u"请检测串口与电脑连接")
        else:
            stop_ths.Uart_stop_threads = False
            stop_ths.Uart_start_flag = True
            self.uart_th = Uart_Thread('uart')
            self.uart_th.start()
        if flag == False:
             QtWidgets.QMessageBox.warning(self, u"warning", u"请检测相机与电脑连接")
        else:
            stop_ths.Image_stop_threads = False
            stop_ths.Image_start_flag = True
            self.image_th = Image_Thread('image')
            self.image_th.start()

    def paintEvent(self, e):
        self.qp = QPainter()
        self.qp.begin(self)
        # if (ui.detect_checkBox.isChecked()):
        for index in range(len(location)):
            points = location[index]
            ex.DrawPoints(points)
            self.qp.drawText(points,label_name[index])
        # else:
        #     self.DrawPoints(point)
        self.qp.end()

    def closeEvent(self, event):
        if (stop_ths.Uart_start_flag):
            stop_ths.Uart_stop_threads = True
            self.uart_th.join()
        if (stop_ths.Image_start_flag):
            stop_ths.Image_stop_threads = True
            self.image_th.join()

    def DrawPoints(self,point):
        pen = QPen(Qt.black, 6, Qt.SolidLine)
        self.qp.setPen(pen)
        self.qp.drawPoints(point)

    def data_send(self):
            if ser.isOpen():
                input_s = ui.Send_textEdit.toPlainText()
                # ascii发送
                input_s = (input_s + '\r\n').encode('utf-8')
                ser.write(input_s)
            else:
                 pass

            # 接收数据
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if (torch.cuda.is_available()):
        yolo = detectapi(weights='./bus.pt', conf_thres=0.5, iou_thres=0.5, device='')
    else:
        yolo = detectapi(weights='./bus.pt', conf_thres=0.5, iou_thres=0.5, device='cpu')
    ex = Example()
    sys.exit(app.exec_())


