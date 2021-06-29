import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout,QVBoxLayout,QApplication

class application(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        OkButton = QPushButton("ok")
        CancerButton = QPushButton("Cancel")

        OkButton0 = QPushButton("ok0")
        CancerButton0 = QPushButton("Cancel0")

        # 使用HBoxLayout和QVBoxLayout并添加伸展因子，在窗口的右下角显示两个按钮
        # 我们创建一个水平布局和添加一个伸展因子和两个按钮。两个按钮前的伸展增加了一个可伸缩的空间。这将推动他们靠右显示。
        hbox = QHBoxLayout()
        hbox.addWidget(OkButton)
        hbox.addStretch(3)
        hbox.addWidget(CancerButton)

        hbox_1 = QHBoxLayout()
        hbox_1.addStretch(1)
        hbox_1.addWidget(OkButton0)
        hbox_1.addWidget(CancerButton0)

        # 创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(2)
        vbox.addLayout(hbox_1)
        vbox.addStretch(0)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('ButtonsExample')
        self.show()



app = QApplication(sys.argv)
ex = application()
sys.exit(app.exec_())