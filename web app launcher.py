from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys
class MainWindow(QMainWindow):
	"""docstring for MainWindow"""
	def __init__(self, *args,**kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("nonstopjaguar")
		self.setFixedWidth(1200)
		self.browser=QWebEngineView()
		self.browser.setUrl(QUrl("the website you want to run"))
		self.setCentralWidget(self.browser)


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()		 
