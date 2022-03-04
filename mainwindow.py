# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1137, 850)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/school_logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPalette{background:#FFFFFF;}*{outline:0px;color:#57595B;}\n"
"\n"
"QWidget[form=\"true\"],QLabel[frameShape=\"1\"]{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"]{\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"] .QFrame{\n"
"border:1px solid #57595B;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"] QLabel,QWidget[form=\"title\"] QLabel{\n"
"border-radius:0px;\n"
"color:#57595B;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QWidget[form=\"title\"],QWidget[nav=\"left\"],QWidget[nav=\"top\"] QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QWidget[nav=\"top\"] QAbstractButton:hover,QWidget[nav=\"top\"] QAbstractButton:pressed,QWidget[nav=\"top\"] QAbstractButton:checked{\n"
"border-style:solid;\n"
"border-width:0px 0px 2px 0px;\n"
"padding:4px 4px 2px 4px;\n"
"border-color:#00BB9E;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton{\n"
"border-radius:0px;\n"
"color:#57595B;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton:hover{\n"
"color:#FFFFFF;\n"
"background-color:#00BB9E;\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton:checked,QWidget[nav=\"left\"] QAbstractButton:pressed{\n"
"color:#57595B;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 2px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#00BB9E;\n"
"background-color:#FFFFFF;\n"
"}\n"
"\n"
"QWidget[video=\"true\"] QLabel{\n"
"color:#57595B;\n"
"border:1px solid #B6B6B6;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QWidget[video=\"true\"] QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#00BB9E;\n"
"selection-color:#FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{\n"
"border:1px solid #B6B6B6;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"]{\n"
"lineedit-password-character:9679;\n"
"}\n"
"\n"
".QFrame{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:3px;\n"
"}\n"
"\n"
".QGroupBox{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:5px;\n"
"margin-top:3ex;\n"
"}\n"
"\n"
".QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"position:relative;\n"
"left:10px;\n"
"}\n"
"\n"
".QPushButton,.QToolButton{\n"
"border-style:none;\n"
"border:1px solid #B6B6B6;\n"
"color:#57595B;\n"
"padding:5px;\n"
"min-height:15px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
".QPushButton:hover,.QToolButton:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
".QPushButton:pressed,.QToolButton:pressed{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
".QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{\n"
"border-radius:3px;\n"
"color:#57595B;\n"
"padding:3px;\n"
"margin:0px;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{\n"
"color:#FFFFFF;\n"
"margin:1px 1px 2px 1px;\n"
"background-color:rgba(51,127,209,230);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"color:#FFFFFF;\n"
"margin:1px 1px 2px 1px;\n"
"background-color:rgba(238,0,0,128);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"width:15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"image:url(:/qss/flatwhite/radiobutton_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked:disabled{\n"
"image:url(:/qss/flatwhite/radiobutton_unchecked_disable.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image:url(:/qss/flatwhite/radiobutton_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked:disabled{\n"
"image:url(:/qss/flatwhite/radiobutton_checked_disable.png);\n"
"}\n"
"\n"
"QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{\n"
"padding:0px -3px 0px 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{\n"
"image:url(:/qss/flatwhite/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{\n"
"image:url(:/qss/flatwhite/checkbox_unchecked_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{\n"
"image:url(:/qss/flatwhite/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{\n"
"image:url(:/qss/flatwhite/checkbox_checked_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{\n"
"image:url(:/qss/flatwhite/checkbox_parcial.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{\n"
"image:url(:/qss/flatwhite/checkbox_parcial_disable.png);\n"
"}\n"
"\n"
"QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{\n"
"image:url(:/qss/flatwhite/add_top.png);\n"
"width:10px;\n"
"height:10px;\n"
"padding:2px 5px 0px 0px;\n"
"}\n"
"\n"
"QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{\n"
"image:url(:/qss/flatwhite/add_bottom.png);\n"
"width:10px;\n"
"height:10px;\n"
"padding:0px 5px 2px 0px;\n"
"}\n"
"\n"
"QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{\n"
"top:-2px;\n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"bottom:-2px;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit[calendarPopup=\"true\"]::down-arrow,QTimeEdit[calendarPopup=\"true\"]::down-arrow,QDateTimeEdit[calendarPopup=\"true\"]::down-arrow{\n"
"image:url(:/qss/flatwhite/add_bottom.png);\n"
"width:10px;\n"
"height:10px;\n"
"right:2px;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{\n"
"subcontrol-origin:padding;\n"
"subcontrol-position:top right;\n"
"width:15px;\n"
"border-left-width:0px;\n"
"border-left-style:solid;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius:3px;\n"
"border-left-color:#B6B6B6;\n"
"}\n"
"\n"
"QComboBox::drop-down:on{\n"
"top:1px;\n"
"}\n"
"\n"
"QMenuBar::item{\n"
"color:#57595B;\n"
"background-color:#E4E4E4;\n"
"margin:0px;\n"
"padding:3px 10px;\n"
"}\n"
"\n"
"QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{\n"
"color:#57595B;\n"
"background-color:#E4E4E4;\n"
"border:1px solid #B6B6B6;\n"
"margin:0px;\n"
"}\n"
"\n"
"QMenu::item{\n"
"padding:3px 20px;\n"
"}\n"
"\n"
"QMenu::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QMenu::item:selected,QMenuBar::item:selected{\n"
"color:#57595B;\n"
"border:0px solid #B6B6B6;\n"
"background:#F6F6F6;\n"
"}\n"
"\n"
"QMenu::separator{\n"
"height:1px;\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QProgressBar{\n"
"min-height:10px;\n"
"background:#E4E4E4;\n"
"border-radius:5px;\n"
"text-align:center;\n"
"border:1px solid #E4E4E4;\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"border-radius:5px;\n"
"background-color:#B6B6B6;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"background:#E4E4E4;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background:#E4E4E4;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"background:#B6B6B6;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:13px;\n"
"margin-top:-3px;\n"
"margin-bottom:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);\n"
"}\n"
"\n"
"QSlider::groove:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"height:14px;\n"
"margin-left:-3px;\n"
"margin-right:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"background:#E4E4E4;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-height:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"background:#B6B6B6;\n"
"min-width:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"background:#E4E4E4;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background:#B6B6B6;\n"
"min-height:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QTabWidget::pane{\n"
"border:1px solid #B6B6B6;\n"
"selection-background-color:#F6F6F6;\n"
"selection-color:#57595B;\n"
"alternate-background-color:#F6F6F6;\n"
"gridline-color:#B6B6B6;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children{\n"
"margin:4px;\n"
"border-image:url(:/qss/flatwhite/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children{\n"
"margin:4px;\n"
"border-image:url(:/qss/flatwhite/branch_close.png);\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QTableView::item:hover,QListView::item:hover,QTreeView::item:hover,QHeaderView{\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTableView::item,QListView::item,QTreeView::item{\n"
"padding:1px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QHeaderView::section,QTableCornerButton:section{\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#57595B;\n"
"border:1px solid #B6B6B6;\n"
"border-left-width:0px;\n"
"border-right-width:1px;\n"
"border-top-width:0px;\n"
"border-bottom-width:1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"border:1px solid #B6B6B6;\n"
"color:#57595B;\n"
"margin:0px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"border-style:solid;\n"
"border-color:#00BB9E;\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTabBar::tab:top,QTabBar::tab:bottom{\n"
"padding:3px 8px 3px 8px;\n"
"}\n"
"\n"
"QTabBar::tab:left,QTabBar::tab:right{\n"
"padding:8px 3px 8px 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected,QTabBar::tab:top:hover{\n"
"border-width:2px 0px 0px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected,QTabBar::tab:right:hover{\n"
"border-width:0px 0px 0px 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{\n"
"border-width:0px 0px 2px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected,QTabBar::tab:left:hover{\n"
"border-width:0px 2px 0px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{\n"
"border-left-width:1px;\n"
"border-left-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{\n"
"border-top-width:1px;\n"
"border-top-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{\n"
"border-right-width:1px;\n"
"border-right-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{\n"
"border-bottom-width:1px;\n"
"border-bottom-color:#B6B6B6;\n"
"}\n"
"\n"
"QStatusBar::item{\n"
"border:0px solid #E4E4E4;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{\n"
"padding:3px;\n"
"border-radius:5px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QToolTip{\n"
"border:0px solid #57595B;\n"
"padding:1px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QPrintPreviewDialog QToolButton{\n"
"border:0px solid #57595B;\n"
"border-radius:0px;\n"
"margin:0px;\n"
"padding:3px;\n"
"background:none;\n"
"}\n"
"\n"
"QColorDialog QPushButton,QFileDialog QPushButton{\n"
"min-width:80px;\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth{\n"
"icon-size:0px;\n"
"min-width:20px;\n"
"image:url(:/qss/flatwhite/calendar_prevmonth.png);\n"
"}\n"
"\n"
"QToolButton#qt_calendar_nextmonth{\n"
"icon-size:0px;\n"
"min-width:20px;\n"
"image:url(:/qss/flatwhite/calendar_nextmonth.png);\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{\n"
"border:0px solid #57595B;\n"
"border-radius:3px;\n"
"margin:3px 3px 3px 3px;\n"
"padding:3px;\n"
"background:none;\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{\n"
"border:1px solid #B6B6B6;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox#qt_calendar_yearedit{\n"
"margin:2px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QCalendarWidget QTableView{\n"
"border-width:0px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"border:1px solid #B6B6B6;\n"
"border-width:1px 1px 0px 1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"min-height:20px;\n"
"min-width:10px;\n"
"}\n"
"\n"
"QTableView[model=\"true\"]::item{\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTabWidget::pane:top{top:-1px;}\n"
"QTabWidget::pane:bottom{bottom:-1px;}\n"
"QTabWidget::pane:left{right:-1px;}\n"
"QTabWidget::pane:right{left:-1px;}\n"
"\n"
"QDialog {\n"
"background-color:#FFFFFF;\n"
"color:#57595B;\n"
"}\n"
"\n"
"QDialogButtonBox > QPushButton {\n"
"min-width:50px;\n"
"}\n"
"\n"
"*:disabled,QMenu::item:disabled,QTabBar::tab:disabled{\n"
"background:#FFFFFF;\n"
"border-color:#E4E4E4;\n"
"color:#B6B6B6;\n"
"}\n"
"\n"
"/*TextColor:#57595B*/\n"
"/*PanelColor:#FFFFFF*/\n"
"/*BorderColor:#B6B6B6*/\n"
"/*NormalColorStart:#E4E4E4*/\n"
"/*NormalColorEnd:#E4E4E4*/\n"
"/*DarkColorStart:#F6F6F6*/\n"
"/*DarkColorEnd:#F6F6F6*/\n"
"/*HighColor:#00BB9E*/")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 421, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.detect = QtWidgets.QWidget()
        self.detect.setObjectName("detect")
        self.Opendev_comboBox = QtWidgets.QComboBox(self.detect)
        self.Opendev_comboBox.setGeometry(QtCore.QRect(110, 20, 181, 22))
        self.Opendev_comboBox.setObjectName("Opendev_comboBox")
        self.Opendev_comboBox.addItem("")
        self.Opendev_comboBox.addItem("")
        self.StartCapButton = QtWidgets.QPushButton(self.detect)
        self.StartCapButton.setGeometry(QtCore.QRect(10, 150, 93, 28))
        self.StartCapButton.setObjectName("StartCapButton")
        self.ClosedevButton = QtWidgets.QPushButton(self.detect)
        self.ClosedevButton.setGeometry(QtCore.QRect(130, 150, 93, 28))
        self.ClosedevButton.setObjectName("ClosedevButton")
        self.opendev_label = QtWidgets.QLabel(self.detect)
        self.opendev_label.setGeometry(QtCore.QRect(20, 20, 72, 15))
        self.opendev_label.setObjectName("opendev_label")
        self.LoadmodellineEdit = QtWidgets.QLineEdit(self.detect)
        self.LoadmodellineEdit.setGeometry(QtCore.QRect(110, 80, 181, 21))
        self.LoadmodellineEdit.setObjectName("LoadmodellineEdit")
        self.loadmodel_label = QtWidgets.QLabel(self.detect)
        self.loadmodel_label.setGeometry(QtCore.QRect(20, 80, 72, 15))
        self.loadmodel_label.setObjectName("loadmodel_label")
        self.BrowerModelButton = QtWidgets.QPushButton(self.detect)
        self.BrowerModelButton.setGeometry(QtCore.QRect(310, 80, 51, 27))
        self.BrowerModelButton.setObjectName("BrowerModelButton")
        self.detect_checkBox = QtWidgets.QCheckBox(self.detect)
        self.detect_checkBox.setGeometry(QtCore.QRect(260, 200, 101, 19))
        self.detect_checkBox.setObjectName("detect_checkBox")
        self.setconf_label = QtWidgets.QLabel(self.detect)
        self.setconf_label.setGeometry(QtCore.QRect(20, 240, 101, 16))
        self.setconf_label.setObjectName("setconf_label")
        self.mouse_Slider = QtWidgets.QSlider(self.detect)
        self.mouse_Slider.setGeometry(QtCore.QRect(120, 270, 160, 22))
        self.mouse_Slider.setMaximum(100)
        self.mouse_Slider.setSingleStep(1)
        self.mouse_Slider.setPageStep(10)
        self.mouse_Slider.setProperty("value", 0)
        self.mouse_Slider.setSliderPosition(0)
        self.mouse_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.mouse_Slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.mouse_Slider.setObjectName("mouse_Slider")
        self.mouse_label = QtWidgets.QLabel(self.detect)
        self.mouse_label.setGeometry(QtCore.QRect(20, 270, 72, 15))
        self.mouse_label.setObjectName("mouse_label")
        self.cup_label = QtWidgets.QLabel(self.detect)
        self.cup_label.setGeometry(QtCore.QRect(20, 310, 72, 15))
        self.cup_label.setObjectName("cup_label")
        self.cup_Slider = QtWidgets.QSlider(self.detect)
        self.cup_Slider.setGeometry(QtCore.QRect(120, 310, 160, 22))
        self.cup_Slider.setMaximum(100)
        self.cup_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.cup_Slider.setObjectName("cup_Slider")
        self.pencil_label = QtWidgets.QLabel(self.detect)
        self.pencil_label.setGeometry(QtCore.QRect(20, 350, 72, 21))
        self.pencil_label.setObjectName("pencil_label")
        self.pecil_Slider = QtWidgets.QSlider(self.detect)
        self.pecil_Slider.setGeometry(QtCore.QRect(120, 350, 160, 22))
        self.pecil_Slider.setMaximum(100)
        self.pecil_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.pecil_Slider.setObjectName("pecil_Slider")
        self.mouse_confnum_label = QtWidgets.QLabel(self.detect)
        self.mouse_confnum_label.setGeometry(QtCore.QRect(290, 270, 72, 15))
        self.mouse_confnum_label.setObjectName("mouse_confnum_label")
        self.cup_confnum_label = QtWidgets.QLabel(self.detect)
        self.cup_confnum_label.setGeometry(QtCore.QRect(290, 310, 72, 15))
        self.cup_confnum_label.setObjectName("cup_confnum_label")
        self.pencil_confnum_label = QtWidgets.QLabel(self.detect)
        self.pencil_confnum_label.setGeometry(QtCore.QRect(290, 350, 72, 15))
        self.pencil_confnum_label.setObjectName("pencil_confnum_label")
        self.tabWidget.addTab(self.detect, "")
        self.uart = QtWidgets.QWidget()
        self.uart.setObjectName("uart")
        self.Openuart_Button = QtWidgets.QPushButton(self.uart)
        self.Openuart_Button.setGeometry(QtCore.QRect(10, 230, 131, 31))
        self.Openuart_Button.setObjectName("Openuart_Button")
        self.RevSet_label = QtWidgets.QLabel(self.uart)
        self.RevSet_label.setGeometry(QtCore.QRect(0, 280, 72, 15))
        self.RevSet_label.setObjectName("RevSet_label")
        self.Ascii_radioButton = QtWidgets.QRadioButton(self.uart)
        self.Ascii_radioButton.setGeometry(QtCore.QRect(50, 310, 115, 19))
        self.Ascii_radioButton.setObjectName("Ascii_radioButton")
        self.Hex_radioButton = QtWidgets.QRadioButton(self.uart)
        self.Hex_radioButton.setGeometry(QtCore.QRect(210, 310, 115, 19))
        self.Hex_radioButton.setObjectName("Hex_radioButton")
        self.SaveLog_checkBox = QtWidgets.QCheckBox(self.uart)
        self.SaveLog_checkBox.setGeometry(QtCore.QRect(210, 360, 91, 19))
        self.SaveLog_checkBox.setObjectName("SaveLog_checkBox")
        self.layoutWidget = QtWidgets.QWidget(self.uart)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 281, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.com_label = QtWidgets.QLabel(self.layoutWidget)
        self.com_label.setObjectName("com_label")
        self.horizontalLayout.addWidget(self.com_label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.uart)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 61, 281, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.baud_label = QtWidgets.QLabel(self.layoutWidget1)
        self.baud_label.setObjectName("baud_label")
        self.horizontalLayout_2.addWidget(self.baud_label)
        self.baudrate_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baudrate_comboBox.sizePolicy().hasHeightForWidth())
        self.baudrate_comboBox.setSizePolicy(sizePolicy)
        self.baudrate_comboBox.setObjectName("baudrate_comboBox")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.baudrate_comboBox)
        self.layoutWidget2 = QtWidgets.QWidget(self.uart)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 101, 281, 28))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.databit_label = QtWidgets.QLabel(self.layoutWidget2)
        self.databit_label.setObjectName("databit_label")
        self.horizontalLayout_3.addWidget(self.databit_label)
        self.databit_comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.databit_comboBox.sizePolicy().hasHeightForWidth())
        self.databit_comboBox.setSizePolicy(sizePolicy)
        self.databit_comboBox.setObjectName("databit_comboBox")
        self.databit_comboBox.addItem("")
        self.databit_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.databit_comboBox)
        self.layoutWidget3 = QtWidgets.QWidget(self.uart)
        self.layoutWidget3.setGeometry(QtCore.QRect(11, 141, 281, 28))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Verify_label = QtWidgets.QLabel(self.layoutWidget3)
        self.Verify_label.setObjectName("Verify_label")
        self.horizontalLayout_4.addWidget(self.Verify_label)
        self.Verify_comboBox = QtWidgets.QComboBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Verify_comboBox.sizePolicy().hasHeightForWidth())
        self.Verify_comboBox.setSizePolicy(sizePolicy)
        self.Verify_comboBox.setObjectName("Verify_comboBox")
        self.Verify_comboBox.addItem("")
        self.Verify_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.Verify_comboBox)
        self.layoutWidget4 = QtWidgets.QWidget(self.uart)
        self.layoutWidget4.setGeometry(QtCore.QRect(11, 190, 281, 28))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Stopbit_label = QtWidgets.QLabel(self.layoutWidget4)
        self.Stopbit_label.setObjectName("Stopbit_label")
        self.horizontalLayout_5.addWidget(self.Stopbit_label)
        self.Stopbit_comboBox = QtWidgets.QComboBox(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stopbit_comboBox.sizePolicy().hasHeightForWidth())
        self.Stopbit_comboBox.setSizePolicy(sizePolicy)
        self.Stopbit_comboBox.setObjectName("Stopbit_comboBox")
        self.Stopbit_comboBox.addItem("")
        self.Stopbit_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.Stopbit_comboBox)
        self.searchcom_pushButton = QtWidgets.QPushButton(self.uart)
        self.searchcom_pushButton.setGeometry(QtCore.QRect(310, 20, 93, 28))
        self.searchcom_pushButton.setObjectName("searchcom_pushButton")
        self.tabWidget.addTab(self.uart, "")
        self.data = QtWidgets.QWidget()
        self.data.setObjectName("data")
        self.Send_textEdit = QtWidgets.QTextEdit(self.data)
        self.Send_textEdit.setGeometry(QtCore.QRect(20, 30, 341, 71))
        self.Send_textEdit.setObjectName("Send_textEdit")
        self.Rev_textEdit = QtWidgets.QTextEdit(self.data)
        self.Rev_textEdit.setGeometry(QtCore.QRect(20, 170, 341, 221))
        self.Rev_textEdit.setObjectName("Rev_textEdit")
        self.Senddata_label = QtWidgets.QLabel(self.data)
        self.Senddata_label.setGeometry(QtCore.QRect(20, 10, 72, 15))
        self.Senddata_label.setObjectName("Senddata_label")
        self.Revdata_label = QtWidgets.QLabel(self.data)
        self.Revdata_label.setGeometry(QtCore.QRect(20, 140, 72, 15))
        self.Revdata_label.setObjectName("Revdata_label")
        self.RevClear_Button = QtWidgets.QPushButton(self.data)
        self.RevClear_Button.setGeometry(QtCore.QRect(270, 400, 93, 28))
        self.RevClear_Button.setObjectName("RevClear_Button")
        self.Senddata_Button = QtWidgets.QPushButton(self.data)
        self.Senddata_Button.setGeometry(QtCore.QRect(260, 110, 93, 28))
        self.Senddata_Button.setObjectName("Senddata_Button")
        self.tabWidget.addTab(self.data, "")
        self.ImageBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ImageBox.setGeometry(QtCore.QRect(440, 20, 661, 561))
        self.ImageBox.setStyleSheet("")
        self.ImageBox.setObjectName("ImageBox")
        self.showimage = QtWidgets.QLabel(self.ImageBox)
        self.showimage.setGeometry(QtCore.QRect(10, 40, 640, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showimage.sizePolicy().hasHeightForWidth())
        self.showimage.setSizePolicy(sizePolicy)
        self.showimage.setStyleSheet("")
        self.showimage.setObjectName("showimage")
        self.StateBox = QtWidgets.QGroupBox(self.centralwidget)
        self.StateBox.setGeometry(QtCore.QRect(10, 490, 421, 291))
        self.StateBox.setObjectName("StateBox")
        self.State_textEdit = QtWidgets.QTextEdit(self.StateBox)
        self.State_textEdit.setGeometry(QtCore.QRect(20, 30, 371, 231))
        self.State_textEdit.setObjectName("State_textEdit")
        self.StateClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.StateClearButton.setGeometry(QtCore.QRect(450, 720, 93, 28))
        self.StateClearButton.setObjectName("StateClearButton")
        self.cap_imageButton = QtWidgets.QPushButton(self.centralwidget)
        self.cap_imageButton.setGeometry(QtCore.QRect(661, 652, 91, 41))
        self.cap_imageButton.setObjectName("cap_imageButton")
        self.cap_videoButton = QtWidgets.QPushButton(self.centralwidget)
        self.cap_videoButton.setGeometry(QtCore.QRect(820, 652, 91, 41))
        self.cap_videoButton.setObjectName("cap_videoButton")
        self.cap_imagelabel = QtWidgets.QLabel(self.centralwidget)
        self.cap_imagelabel.setGeometry(QtCore.QRect(670, 700, 72, 15))
        self.cap_imagelabel.setText("")
        self.cap_imagelabel.setObjectName("cap_imagelabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1137, 26))
        self.menubar.setObjectName("menubar")
        self.filemenu = QtWidgets.QMenu(self.menubar)
        self.filemenu.setObjectName("filemenu")
        self.settingmenu = QtWidgets.QMenu(self.menubar)
        self.settingmenu.setObjectName("settingmenu")
        self.aboutmenu = QtWidgets.QMenu(self.menubar)
        self.aboutmenu.setObjectName("aboutmenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionfromimage = QtWidgets.QAction(MainWindow)
        self.actionfromimage.setObjectName("actionfromimage")
        self.actionfromvideo = QtWidgets.QAction(MainWindow)
        self.actionfromvideo.setObjectName("actionfromvideo")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actioninstruction = QtWidgets.QAction(MainWindow)
        self.actioninstruction.setObjectName("actioninstruction")
        self.actionsaveasimage = QtWidgets.QAction(MainWindow)
        self.actionsaveasimage.setCheckable(True)
        self.actionsaveasimage.setObjectName("actionsaveasimage")
        self.actionsaveasvideo = QtWidgets.QAction(MainWindow)
        self.actionsaveasvideo.setCheckable(True)
        self.actionsaveasvideo.setObjectName("actionsaveasvideo")
        self.actionsavesetting = QtWidgets.QAction(MainWindow)
        self.actionsavesetting.setCheckable(True)
        self.actionsavesetting.setObjectName("actionsavesetting")
        self.saveimagepath = QtWidgets.QAction(MainWindow)
        self.saveimagepath.setObjectName("saveimagepath")
        self.savevideopath = QtWidgets.QAction(MainWindow)
        self.savevideopath.setObjectName("savevideopath")
        self.filemenu.addAction(self.actionfromimage)
        self.filemenu.addAction(self.actionfromvideo)
        self.settingmenu.addAction(self.actionsavesetting)
        self.settingmenu.addAction(self.saveimagepath)
        self.settingmenu.addAction(self.savevideopath)
        self.aboutmenu.addAction(self.actionabout)
        self.aboutmenu.addAction(self.actioninstruction)
        self.menubar.addAction(self.filemenu.menuAction())
        self.menubar.addAction(self.settingmenu.menuAction())
        self.menubar.addAction(self.aboutmenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.StartCapButton.pressed.connect(MainWindow.startcapture)
        self.StateClearButton.clicked.connect(MainWindow.clear_state)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于通用摄像头的视觉分拣系统-尹文庆"))
        self.Opendev_comboBox.setItemText(0, _translate("MainWindow", "USB摄像头0"))
        self.Opendev_comboBox.setItemText(1, _translate("MainWindow", "USB摄像头1"))
        self.StartCapButton.setText(_translate("MainWindow", "开始采集"))
        self.ClosedevButton.setText(_translate("MainWindow", "关闭相机"))
        self.opendev_label.setText(_translate("MainWindow", "打开设备"))
        self.loadmodel_label.setText(_translate("MainWindow", "导入模型"))
        self.BrowerModelButton.setText(_translate("MainWindow", "浏览"))
        self.detect_checkBox.setText(_translate("MainWindow", "目标检测"))
        self.setconf_label.setText(_translate("MainWindow", "设置置信度"))
        self.mouse_label.setText(_translate("MainWindow", "mouse"))
        self.cup_label.setText(_translate("MainWindow", "cup"))
        self.pencil_label.setText(_translate("MainWindow", "pencil"))
        self.mouse_confnum_label.setText(_translate("MainWindow", "1"))
        self.cup_confnum_label.setText(_translate("MainWindow", "2"))
        self.pencil_confnum_label.setText(_translate("MainWindow", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.detect), _translate("MainWindow", "目标检测"))
        self.Openuart_Button.setText(_translate("MainWindow", "打开串口"))
        self.RevSet_label.setText(_translate("MainWindow", "接受设置"))
        self.Ascii_radioButton.setText(_translate("MainWindow", "ASCII"))
        self.Hex_radioButton.setText(_translate("MainWindow", "HEX"))
        self.SaveLog_checkBox.setText(_translate("MainWindow", "保存日志"))
        self.com_label.setText(_translate("MainWindow", "端口号"))
        self.baud_label.setText(_translate("MainWindow", "波特率"))
        self.baudrate_comboBox.setCurrentText(_translate("MainWindow", "115200"))
        self.baudrate_comboBox.setItemText(0, _translate("MainWindow", "115200"))
        self.baudrate_comboBox.setItemText(1, _translate("MainWindow", "38400"))
        self.baudrate_comboBox.setItemText(2, _translate("MainWindow", "921600"))
        self.baudrate_comboBox.setItemText(3, _translate("MainWindow", "9600"))
        self.databit_label.setText(_translate("MainWindow", "数据位"))
        self.databit_comboBox.setItemText(0, _translate("MainWindow", "8"))
        self.databit_comboBox.setItemText(1, _translate("MainWindow", "6"))
        self.Verify_label.setText(_translate("MainWindow", "校验位"))
        self.Verify_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.Verify_comboBox.setItemText(1, _translate("MainWindow", "NONE"))
        self.Stopbit_label.setText(_translate("MainWindow", "停止位"))
        self.Stopbit_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.Stopbit_comboBox.setItemText(1, _translate("MainWindow", "0"))
        self.searchcom_pushButton.setText(_translate("MainWindow", "检测串口"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uart), _translate("MainWindow", "串口"))
        self.Senddata_label.setText(_translate("MainWindow", "发送数据"))
        self.Revdata_label.setText(_translate("MainWindow", "接受数据"))
        self.RevClear_Button.setText(_translate("MainWindow", "清除"))
        self.Senddata_Button.setText(_translate("MainWindow", "发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data), _translate("MainWindow", "数据"))
        self.ImageBox.setTitle(_translate("MainWindow", "图像显示"))
        self.showimage.setText(_translate("MainWindow", "                                 showimage"))
        self.StateBox.setTitle(_translate("MainWindow", "状态信息"))
        self.StateClearButton.setText(_translate("MainWindow", "清除"))
        self.cap_imageButton.setText(_translate("MainWindow", "捕获图片"))
        self.cap_videoButton.setText(_translate("MainWindow", "捕获视频"))
        self.filemenu.setTitle(_translate("MainWindow", "文件"))
        self.settingmenu.setTitle(_translate("MainWindow", "设置"))
        self.aboutmenu.setTitle(_translate("MainWindow", "帮助"))
        self.actionfromimage.setText(_translate("MainWindow", "从文件中导入图片"))
        self.actionfromvideo.setText(_translate("MainWindow", "从文件中导入视频"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actioninstruction.setText(_translate("MainWindow", "使用说明"))
        self.actionsaveasimage.setText(_translate("MainWindow", "保存为图片"))
        self.actionsaveasvideo.setText(_translate("MainWindow", "保存为视频"))
        self.actionsavesetting.setText(_translate("MainWindow", "自动保存设置"))
        self.saveimagepath.setText(_translate("MainWindow", "设置图片保存路径"))
        self.savevideopath.setText(_translate("MainWindow", "设置视频保存路径"))

import qss
