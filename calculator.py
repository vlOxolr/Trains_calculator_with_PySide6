from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QCoreApplication
from calculator_ui import Ui_Form
import re

class basic_calculator(QWidget):
    def __init__(self):
        # init ui
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.b1.clicked.connect(self.b1)
        self.ui.b2.clicked.connect(self.b2)
        self.ui.b3.clicked.connect(self.b3)
        self.ui.b4.clicked.connect(self.b4)
        self.ui.b5.clicked.connect(self.b5)
        self.ui.b6.clicked.connect(self.b6)
        self.ui.b7.clicked.connect(self.b7)
        self.ui.b8.clicked.connect(self.b8)
        self.ui.b9.clicked.connect(self.b9)
        self.ui.b0.clicked.connect(self.b0)
        self.ui.bdot.clicked.connect(self.bdot)
        self.ui.bAC.clicked.connect(self.bAC)
        self.ui.bplus.clicked.connect(self.bplus)
        self.ui.bminus.clicked.connect(self.bminus)
        self.ui.btimes.clicked.connect(self.btimes)
        self.ui.bdiv.clicked.connect(self.bdiv)
        self.ui.bdel.clicked.connect(self.bdel)
        self.ui.bequ.clicked.connect(self.bequ)
        self.ui.blbracket.clicked.connect(self.blbracket)
        self.ui.brbracket.clicked.connect(self.brbracket)
        
        self.equation = ''
        self.result = ''

    def calc(self):
        nums = re.split('\+|-|x|/',self.equation)

        if len(nums) != 2:
            pass

        if '+' in self.equation:
            rlt = float(nums[0])+float(nums[1])
        elif '-' in self.equation:
            rlt = float(nums[0])-float(nums[1])
        elif '*' in self.equation:
            rlt = float(nums[0])*float(nums[1])
        elif '/' in self.equation:
            rlt = float(nums[0])/float(nums[1])
        else:
            rlt = self.equation

        self.result = str(rlt)
    
    def calc1(self):
        try:
            self.result = str(eval(self.equation))
        except:
            self.result = '你在干神魔？'

    def display_update(self):
        self.ui.lblequ.setText(QCoreApplication.translate("Form", self.equation, None))
        self.ui.lblans.setText(QCoreApplication.translate("Form", self.result, None))  

    def equ_update(self,oper):
        # 保存操作
        self.equation += oper

        # 计算更新
        #self.calc()
        #self.calc1()

        # 更新显示
        self.display_update()

    def b1(self):
        self.equ_update('1')

    def b2(self):
        self.equ_update('2')

    def b3(self):
        self.equ_update('3')

    def b4(self):
        self.equ_update('4')

    def b5(self):
        self.equ_update('5')

    def b6(self):
        self.equ_update('6')

    def b7(self):
        self.equ_update('7')

    def b8(self):
        self.equ_update('8')

    def b9(self):
        self.equ_update('9')

    def b0(self):
        self.equ_update('0')

    def bdot(self):
        self.equ_update('.')    

    def bAC(self):
        self.equation = ''
        self.result = ''

        self.display_update()

    def bplus(self):
        self.equ_update('+')

    def bminus(self):
        self.equ_update('-')

    def btimes(self):
        self.equ_update('*')

    def bdiv(self):
        self.equ_update('/')
    
    def bdel(self):
        self.equation = self.equation[:-1]

        self.display_update()

    def bequ(self):
        self.calc1()
        self.display_update()

    def blbracket(self):
        self.equ_update('(')

    def brbracket(self):
        self.equ_update(')')

class basic_calc_with_another_way_to_init(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = basic_calculator()
    #window = basic_calc_with_another_way_to_init()
    window.show()
    app.exec()