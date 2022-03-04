import numpy
from cv2 import imwrite,imread,VideoCapture,COLOR_BGR2RGB,resize,cvtColor,COLOR_GRAY2BGR,imshow
import cv2
from PyQt5.QtCore import QTimer,QSettings
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QLabel
import sys
import serial
import serial.tools.list_ports
from detect_ywq import detectapi
from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow
import time
from threading import Thread
import torch
# -*- coding:utf-8 -*-
#coding: unicode_escape
settings = QSettings("config.ini", QSettings.IniFormat)
ui = mainwindow.Ui_MainWindow()
cap=VideoCapture()

ser = serial.Serial()


class Stop_Threads(object):
    Uart_stop_threads = False
    Image_stop_threads = False
    Uart_start_flag=False
    Image_start_flag=False
stop_ths=Stop_Threads()


class Mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # ui = mainwindow.Ui_MainWindow()
        ui.setupUi(self)
        self.timer_camera = QtCore.QTimer()
        # self.cap=VideoCapture()
        # self.CAM_NUM=0
        # ser = serial.Serial()
        self.slot_init()
        self.init()
        self.image = imread('./camera.jpg', 1)
        show = resize(self.image, (640, 480))
        show = cvtColor(show, COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.show_icon=showImage
        ui.showimage.setPixmap(QtGui.QPixmap.fromImage(showImage))
        ui.State_textEdit.setText('开始运行！！！' + '\n')
        # self.image_th = Image_Thread('image')
        # self.uart_th=Uart_Thread('uart')
    def slot_init(self):
        #摄像头定时捕捉
        # self.timer_camera.timeout.connect(self.show_camera)
            # 串口检测按钮
        # ui.searchcom_pushButton.clicked.connect(self.port_check)
        #     # 打开关闭串口按钮
        # ui.Openuart_Button.clicked.connect(self.port_open_close)
        #     # 发送数据按钮
        # ui.Senddata_Button.clicked.connect(self.data_send)
        # # 清除接收窗口
        # ui.RevClear_Button.clicked.connect(self.receive_data_clear)
        ui.BrowerModelButton.clicked.connect(self.showDialog)
        # 定时器接收数据
        self.Rev_timer = QTimer(self)
        # self.Rev_timer.timeout.connect(self.data_receive)
        ui.searchcom_pushButton.clicked.connect(lambda: self.Uartfunc(ui.searchcom_pushButton))
        ui.Openuart_Button.clicked.connect(lambda: self.Uartfunc(ui.Openuart_Button))
        ui.Senddata_Button.clicked.connect(lambda: self.Uartfunc(ui.Senddata_Button))
        ui.RevClear_Button.clicked.connect(lambda: self.Uartfunc(ui.RevClear_Button))
        # self.Rev_timer.timeout.connect(lambda: self.Uartfunc(self.Rev_timer))
        # 滑动条信号
        ui.mouse_Slider.valueChanged.connect(lambda: self.on_change_func(ui.mouse_Slider))
        ui.cup_Slider.valueChanged.connect(lambda: self.on_change_func(ui.cup_Slider))
        ui.pecil_Slider.valueChanged.connect(lambda: self.on_change_func(ui.pecil_Slider))


        #menubar信号
        ui.saveimagepath.triggered.connect(lambda: self.processtrigger(ui.saveimagepath))
        ui.savevideopath.triggered.connect(lambda: self.processtrigger(ui.savevideopath))
        ui.actionabout.triggered.connect(lambda: self.processtrigger(ui.actionabout))
        ui.actionsavesetting.triggered.connect(lambda: self.processtrigger(ui.actionsavesetting))
        #捕获图像和视频信号
        ui.cap_imageButton.clicked.connect(lambda: self.saveimage_video(ui.cap_imageButton))
        ui.cap_videoButton.clicked.connect(lambda: self.saveimage_video(ui.cap_videoButton))
# 打开摄像头
    def startcapture(self):
        print('* startcapture')
        if self.timer_camera.isActive() == False:
            if ui.Opendev_comboBox.currentText()=='USB摄像头0':
                self.CAM_NUM=0
            else:
                self.CAM_NUM=1
            flag = cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"warning", u"请检测相机与电脑连接", buttons=QtWidgets.QMessageBox.ok,
                                                    defaultButton=QtWidgets.QMessageBox.ok)
            else:
                self.timer_camera.start(30)
                ui.StartCapButton.setText('关闭采集')
                ui.State_textEdit.append('相机已打开！！！'+'\n')
                stop_ths.Image_stop_threads=False
                stop_ths.Image_start_flag=True
                self.image_th = Image_Thread('image')
                self.image_th.start()
                # a.opt.conf_thres=0.25
        else:
            self.timer_camera.stop()
            cap.release()
            ui.showimage.clear()
            ui.StartCapButton.setText('开始采集')
            ui.showimage.setPixmap(QtGui.QPixmap.fromImage(self.show_icon))
            ui.State_textEdit.append('相机已关闭！！！'+'\n')
            stop_ths.Image_stop_threads=True
            self.image_th.join()
            #显示图像
    def show_camera(self):
        flag, self.image = cap.read()
        # self.image = imread('./1.jpg',1)
        self.image = resize(self.image, (640, 480))
        show = cvtColor(self.image, COLOR_BGR2RGB)
        if(ui.detect_checkBox.isChecked() and self.model_loaded):
            result, names = self.yolov5.detect([show],self.conf1,self.conf2)
            show = result[0][0]  # 第一张图片的处理结果图片
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        ui.showimage.setPixmap(QtGui.QPixmap.fromImage(showImage))

        #关闭摄像头
    def stopcapture(self):
        if self.cap.isOpened():
            self.cap.release()
        if self.timer_camera.isActive():
            self.timer_camera.stop()
        ui.showimage.clear()
        ui.State_textEdit.append('相机已关闭！！！'+'\n')
        print('* stopcapture  ')
    def init(self):

        self.port_check()
        self.cap_image_num=0
        # settings = QSettings("config.ini", QSettings.IniFormat)
        #HEX发送

            # 定时发送数据
        # self.timer_send = QTimer()
        # self.timer_send.timeout.connect(self.data_send)
        # self.timer_send_cb.stateChanged.connect(self.data_send_timer)


        # ui.mouse_Slider.setValue(self.conf1*100)
        # # self.conf1=0.5
        # ui.mouse_confnum_label.setText(str(ui.mouse_Slider.value()/100.0))
        # ui.cup_Slider.setValue(self.conf2*100)
        # # self.conf2 = 0.5
        # ui.cup_confnum_label.setText(str(ui.cup_Slider.value()/100.0))
        # ui.pecil_Slider.setValue(self.conf3*100)
        # # self.conf3 = 0.5
        # ui.pencil_confnum_label.setText(str(ui.pecil_Slider.value()/100.0))


        # 串口检测
    def port_check(self):
            # 检测所有存在的串口，将信息存储在字典中
            self.Com_Dict = {}
            port_list = list(serial.tools.list_ports.comports())
            ui.comboBox.clear()
            for port in port_list:
                self.Com_Dict["%s" % port[0]] = "%s" % port[1]
                ui.comboBox.addItem(port[0])
            if len(self.Com_Dict) == 0:
                ui.comboBox.addItem(" 无串口")
#打开关闭串口
    def port_open_close(self):
        # if ser.serialEngine is None:
            ser.port = ui.comboBox.currentText()
            ser.baudrate = int(ui.baudrate_comboBox.currentText())
            ser.bytesize = int(ui.databit_comboBox.currentText())
            ser.stopbits = int(ui.Stopbit_comboBox.currentText())
            # ser.parity = ui.Verify_comboBox.currentText()
            ser.parity = 'N'
            if ser.isOpen() == True:
                ser.close()
                ui.Openuart_Button.setText('打开串口')
                ui.State_textEdit.append('串口已关闭！！！')
                stop_ths.Uart_stop_threads = True
                self.uart_th.join()
            else:
                ser.open()
                # self.Rev_timer.start(2)
                ui.Openuart_Button.setText('关闭串口')
                ui.State_textEdit.append('串口已打开！！！')
                stop_ths.Uart_stop_threads=False
                stop_ths.Uart_start_flag=True
                self.uart_th = Uart_Thread('uart')
                self.uart_th.start()

    def data_send(self):
            if ser.isOpen():
                input_s = ui.Send_textEdit.toPlainText()
                if input_s != "":
                    # 非空字符串
                    if ui.Hex_radioButton.isChecked():
                        # hex发送
                        input_s = input_s.strip()
                        send_list = []
                        while input_s != '':
                            try:
                                num = int(input_s[0:2], 16)
                            except ValueError:
                                QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                                return None
                            input_s = input_s[2:].strip()
                            send_list.append(num)
                        input_s = bytes(send_list)
                    else:
                        # ascii发送
                        input_s = (input_s + '\r\n').encode('utf-8')
                        ser.write(input_s)
                    # self.data_num_sended += num
                    # self.lineEdit_2.setText(str(self.data_num_sended))
            else:
                pass

            # 接收数据
    def data_receive(self):
        if ser.is_open == True:
            self.RC_data = ser.read_all()
            # if self.RC_data != b'':
            # print('receive',self.RC_data.decode("gbk"))
            ui.Rev_textEdit.insertPlainText(self.RC_data.decode('utf-8'))
            ui.Rev_textEdit.moveCursor(ui.Rev_textEdit.textCursor().End)  # 文本框显示到底部
            # try:
            #     num = ser.inWaiting()
            # except:
            #     self.port_close()
            #     return None
            # if num > 0:
            #     data = ser.read(num)
            #     num = len(data)
            #     # hex显示
            #     if ui.Hex_radioButton.checkState():
            #         out_s = ''
            #         for i in range(0, len(data)):
            #             out_s = out_s + '{:02X}'.format(data[i]) + ' '
            #         ui.Rev_textEdit.insertPlainText(out_s)
            #     else:
            #         # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
            #         ui.Rev_textEdit.insertPlainText(data.decode('utf-8'))
            #
            #     # 统计接收字符的数量
            #     self.data_num_received += num
            #     # self.lineEdit.setText(str(self.data_num_received))
            #
            #     # 获取到text光标
            #     textCursor = ui.Rev_textEdit.textCursor()
            #     # 滚动到底部
            #     textCursor.movePosition(textCursor.End)
            #     # 设置光标到text中去
            #     ui.Rev_textEdit.setTextCursor(textCursor)
            # else:
            #     pass


            # 定时发送数据
    # def data_send_timer(self):
    #         if self.timer_send_cb.isChecked():
    #             self.timer_send.start(int(self.lineEdit_3.text()))
    #             self.lineEdit_3.setEnabled(False)
    #         else:
    #             self.timer_send.stop()
    #             self.lineEdit_3.setEnabled(True)
    #
    #         # 清除显示
    # def Data_Send(self):
    #     if ser.isOpen() == True:
    #         str=ui.Send_textEdit.toPlainText();
    #         ser.write((str+'\r\n').encode('utf-8'))
    #         # ser.write(str(binascii.b2a_hex(self.textEdit.toPlainText()))) #尝试编写HEX发送—失败
#接受数据
    # def Data_Recive(self):
    #     while True:
    #         if ser.is_open == True:
    #             self.RC_data = ser.read_all()
    #             # if self.RC_data != b'':
    #                 # print('receive',self.RC_data.decode("gbk"))
    #             ui.Rev_textEdit.insertPlainText(self.RC_data.decode("gbk"))
    #             ui.Rev_textEdit.moveCursor(ui.Rev_textEdit.textCursor().End)  # 文本框显示到底部
#清除发送数据
    def send_data_clear(self):
            ui.Send_textEdit.setText("")
#清除接收数据
    def receive_data_clear(self):
        ui.Rev_textEdit.setText("")
#清除状态信息
    def clear_state(self):
        ui.State_textEdit.setText("")
#滑动条函数信号处理
    def on_change_func(self,slider):
        if slider == ui.mouse_Slider:
            self.conf1=ui.mouse_Slider.value()/100.0
            ui.mouse_confnum_label.setText(str(self.conf1))
        elif slider == ui.cup_Slider:
            self.conf2 = ui.cup_Slider.value() / 100.0
            ui.cup_confnum_label.setText(str(self.conf2))
        else:
            self.conf3 = ui.pecil_Slider.value() / 100.0
            ui.pencil_confnum_label.setText(str(self.conf3))
###########################文件操作###############################
    #定义打开文件夹目录的函数
    def showDialog(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选取文件","./", "All Files (*);;Text Files (*.pt)")
        if (fileName):
            ui.State_textEdit.append('已导入模型')
            ui.LoadmodellineEdit.setText(fileName)
            self.model_file=fileName
            self.model_loaded=True
            global yolo
            yolo = detectapi(weights=self.model_file, conf_thres=0.5, iou_thres=0.5)
        else:
            self.model_loaded=False
    #menubar信号处理
    def processtrigger(self,action):
        if(action==ui.saveimagepath):
            fileName = QFileDialog.getExistingDirectory(self, "设置图片保存路径")
            self.save_image_path=fileName
            ui.State_textEdit.append('图片保存路径'+fileName)
        elif(action==ui.savevideopath):
            fileName = QFileDialog.getExistingDirectory(self, "设置视频保存路径")
            self.save_video_path=fileName
            ui.State_textEdit.append('视频保存路径'+fileName)
        elif(action==ui.actionabout):
            # ui.State_textEdit.append('版本1.0')
            self.About_UI()
        elif (action == ui.actionsavesetting):
            if(ui.actionsavesetting.isChecked()):
                ui.State_textEdit.append('自动保存设置已生效！！！')
                self.autosetting=True
                settings.setValue('autosetting',self.autosetting)
            else:
                ui.State_textEdit.append('已取消自动保存设置！！！')
                self.autosetting=False
                settings.setValue('autosetting', self.autosetting)
    #加载配置文件及开机动画
    def load_data(self, sp):
        # settings = QSettings("config.ini", QSettings.IniFormat)
        # settings = QSettings('Mysoft', 'yolo')
        if (settings.value('autosetting')):
            ui.actionsavesetting.setChecked(True)
            self.conf1 = float(settings.value('conf'))
            self.conf2 = float(settings.value('iou'))
            self.save_image_path = settings.value('save_image_file')
            self.save_video_path = settings.value('save_video_file')
            self.model_file = settings.value('model_file')
            ui.State_textEdit.append('已导入模型')
            self.model_loaded=True
            ui.LoadmodellineEdit.setText(self.model_file)
            ui.mouse_Slider.setValue(int(self.conf1*100))
            ui.cup_Slider.setValue(int(self.conf2 * 100))
            # self.yolov5 = detect_ywq.detectapi(weights=self.model_file, conf_thres=self.conf1, iou_thres=self.conf2)
        else:
            ui.actionsavesetting.setChecked(False)
        ui.mouse_confnum_label.setText(str(ui.mouse_Slider.value()/100.0))
        ui.cup_confnum_label.setText(str(ui.cup_Slider.value()/100.0))
        # ui.pecil_Slider.setValue(self.conf3*100)
        ui.pencil_confnum_label.setText(str(ui.pecil_Slider.value()/100.0))
        for i in range(1,11):  # 模拟主程序加载过程
            time.sleep(0.3)  # 加载数据
            sp.showMessage("加载... {0}%".format(i * 10), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.blue)
            QtWidgets.qApp.processEvents()  # 允许主进程处理事件
 # 添加中文的确认退出提示框1
    def closeEvent(self, event):
        # 创建一个消息盒子（提示框）
        quitMsgBox = QMessageBox()
        # 设置提示框的标题
        quitMsgBox.setWindowTitle('确认提示')
        # 设置提示框的内容
        if (ui.actionsavesetting.isChecked()):
            quitMsgBox.setText('你确认退出吗,将自动保存本次设置？')
        else:
            quitMsgBox.setText('你确认退出吗？')
        # 设置按钮标准，一个yes一个no
        quitMsgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # 获取两个按钮并且修改显示文本
        buttonY = quitMsgBox.button(QMessageBox.Yes)
        buttonY.setText('确定')
        buttonN = quitMsgBox.button(QMessageBox.No)
        buttonN.setText('取消')
        quitMsgBox.exec_()
        # 判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否则就忽略关闭事件
        if quitMsgBox.clickedButton() == buttonY:
            settings.setValue("model_file", self.model_file)
            settings.setValue("save_image_file", self.save_image_path)
            settings.setValue("save_video_file", self.save_video_path)
            settings.setValue("conf", self.conf1)
            settings.setValue("iou", self.conf2)
            if(stop_ths.Uart_start_flag):
                stop_ths.Uart_stop_threads=True
                self.uart_th.join()
            if(stop_ths.Image_start_flag):
                stop_ths.Image_stop_threads=True
                self.image_th.join()
            event.accept()
        else:
            event.ignore()
    #图片及视频保存信号处理
    def saveimage_video(self,type):
        if (type==ui.cap_imageButton):
            flag, self.image = cap.read()
            self.cap_image_num += 1
            imwrite(self.save_image_path+'/'+str(self.cap_image_num)+'.jpg', self.image)
            ui.cap_imagelabel.setText('已捕获：'+str(self.cap_image_num)+' 张')
        # elif type==ui.cap_videoButton:
#串口信号处理
    def Uartfunc(self,type):
        if(type==ui.searchcom_pushButton):
            self.port_check()
        elif(type==ui.Openuart_Button):
            self.port_open_close()
        elif(type==ui.Senddata_Button):
            self.data_send()
        elif(type==ui.RevClear_Button):
            self.receive_data_clear()
        # elif(type==self.Rev_timer):
        #     self.data_receive()

    def About_UI(self):
         QMessageBox.information(self, "关于", "版本：V1.5\n"+'图片视频保存路径不能有中文！！！\n'+'使用GPU加速请使用NVIDIA显卡并配置CUDA环境', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
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
                ui.Rev_textEdit.insertPlainText(self.RC_data.decode('ISO-8859-1'))
                # ui.Rev_textEdit.insertPlainText(self.RC_data.decode('utf-8'))
                ui.Rev_textEdit.moveCursor(ui.Rev_textEdit.textCursor().End)  # 文本框显示到底部

            time.sleep(0.003)  # 休眠
    def data_receive(self):
        if ser.is_open == True:
            self.RC_data = ser.read_all()
            # if self.RC_data != b'':
            # print('receive',self.RC_data.decode("gbk"))
            ui.Rev_textEdit.insertPlainText(self.RC_data.decode('utf-8'))
            ui.Rev_textEdit.moveCursor(ui.Rev_textEdit.textCursor().End)  # 文本框显示到底部

            # 定时发送数据
class Image_Thread(Thread):  # 线程2
    def __init__(self,threadname):
        Thread.__init__(self,name=threadname)
        self.map=numpy.zeros((480,480),dtype=numpy.uint8)
        self.map=cvtColor(self.map,COLOR_GRAY2BGR)
    def run(self):
        while True:
            if (stop_ths.Image_stop_threads):
                break
            else:
                flag, self.image = cap.read()
                self.image = resize(self.image, (640, 480))
                show = cvtColor(self.image, COLOR_BGR2RGB)
                if (ui.detect_checkBox.isChecked()):
                    result, names,c1,c2 = yolo.detect([show], ui.mouse_Slider.value() / 100.0, ui.cup_Slider.value() / 100.0)
                    show = result[0][0]  # 第一张图片的处理结果图片
                showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
                ui.showimage.setPixmap(QtGui.QPixmap.fromImage(showImage))
                imshow('map',self.map)
                cv2.waitKey(1)
            time.sleep(0.003)

if __name__ == "__main__":
    # # _thread.start_new_thread(win.Data_Recive, ())
    # QApplication专为QGuiApplication提供基于QWidget的应用程序所需的一些功能。 它处理小部件特定的初始化，完成
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("camera.jpg"))
    splash.showMessage("加载... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.blue)
    splash.show()                           # 显示启动界面
    QtWidgets.qApp.processEvents()          # 处理主进程事件
    window = Mainwindow()
    window.load_data(splash)                # 加载数据
    if (not settings.value('model_file')):
        if (torch.cuda.is_available()):
            ui.State_textEdit.append('已检测到GPU和CUDA环境，启用GPU加速！！！')
            yolo = detectapi(weights='./bus.pt', conf_thres=0.5, iou_thres=0.5, device='')
        else:
            ui.State_textEdit.append('未检测到GPU和CUDA环境，使用CPU！！！')
            yolo = detectapi(weights='./bus.pt', conf_thres=0.5, iou_thres=0.5, device='cpu')
    else:
        if (torch.cuda.is_available()):
            ui.State_textEdit.append('已检测到GPU和CUDA环境，启用GPU加速！！！')
            yolo = detectapi(weights=settings.value('model_file'), conf_thres=0.5, iou_thres=0.5, device='')
        else:
            ui.State_textEdit.append('未检测到GPU和CUDA环境，使用CPU！！！')
            yolo = detectapi(weights=settings.value('model_file'), conf_thres=0.5, iou_thres=0.5, device='cpu')
    window.show()
    splash.finish(window)  # 隐藏启动界面
    sys.exit(app.exec_())


