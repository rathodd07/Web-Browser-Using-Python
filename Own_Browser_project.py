import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self ):
        super(MainWindow, self).__init__()
        self.showMaximized()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)

        # navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        #back button
        back_button = QAction('Back',self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        #forward button
        forward_button = QAction("Forward",self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        #refresh or reload button 
        refresh_button = QAction("Reload",self)
        refresh_button.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_button)

        #Home Button
        home_button = QAction("Home",self)
        home_button.triggered.connect(self.navget_home)
        navbar.addAction(home_button)

        #url editing bar
        self.url_edit_bar=QLineEdit("")
        self.url_edit_bar.returnPressed.connect(self.navget_to_url)
        navbar.addWidget(self.url_edit_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navget_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    def navget_to_url(self):
        url = self.url_edit_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_edit_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("My Own Browser -> Rathore Prashanth Rajput...!")
window = MainWindow()
app.exec_()


