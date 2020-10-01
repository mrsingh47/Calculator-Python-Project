# This Project is Made by Abhishek
# Main File of Calculator

from PyQt5 import QtWidgets, uic
import sys

memory = 0
state = 0


def clear():
    Form.screen.setText("")


def check_blank():
    if Form.screen.text() == "" or Form.screen.text() == "Invalid Input":
        return True
    else:
        return False


def check_callback():
    global state
    if state == 1:
        clear()
        state = 0


def check_action():
    global state
    if state == 1:
        state = 0
    elif state == 2:
        Form.screen.setText("")
        state = 0


def endswith_operation(inp):
    arr = ["+", "-", "*", "/", "**"]
    try:
        if inp[-1] in arr:
            return True
        else:
            return False
    except:
        False


def push_0():
    check_callback()
    if Form.screen.text() == '':
        pass
    else:
        inp = Form.screen.text() + "0"
        Form.screen.setText(inp)


def push_1():
    check_callback()
    inp = Form.screen.text() + "1"
    Form.screen.setText(inp)


def push_2():
    check_callback()
    inp = Form.screen.text() + "2"
    Form.screen.setText(inp)


def push_3():
    check_callback()
    inp = Form.screen.text() + "3"
    Form.screen.setText(inp)


def push_4():
    check_callback()
    inp = Form.screen.text() + "4"
    Form.screen.setText(inp)


def push_5():
    check_callback()
    inp = Form.screen.text() + "5"
    Form.screen.setText(inp)


def push_6():
    check_callback()
    inp = Form.screen.text() + "6"
    Form.screen.setText(inp)


def push_7():
    check_callback()
    inp = Form.screen.text() + "7"
    Form.screen.setText(inp)


def push_8():
    check_callback()
    inp = Form.screen.text() + "8"
    Form.screen.setText(inp)


def push_9():
    check_callback()
    inp = Form.screen.text() + "9"
    Form.screen.setText(inp)


def push_sqrt():
    check_action()
    if Form.screen.text() == "" or Form.screen.text() == "Invalid Input":
        Form.screen.setText("Invalid Input")
    else:
        inp = float(eval(Form.screen.text()) ** 0.5)
        value = str(inp)
        if len(value) > 17:
            exp_value = "{:.2e}".format(float(value))
            Form.screen.setText(exp_value)
        else:
            Form.screen.setText(value)


def push_square():
    check_action()
    if Form.screen.text() == "" or Form.screen.text() == "Invalid Input":
        Form.screen.setText("Invalid Input")
    else:
        inp = float(eval(Form.screen.text()) ** 2)
        value = str(inp)
        if len(value) > 17:
            exp_value = "{:.2e}".format(float(value))
            Form.screen.setText(exp_value)
        else:
            Form.screen.setText(value)


def push_power():
    check_action()
    if check_blank():
        return
    if endswith_operation(Form.screen.text()):
        inp = Form.screen.text()[:-1] + "**"
        Form.screen.setText(inp)
    else:
        inp = Form.screen.text() + "**"
        Form.screen.setText(inp)


def push_divide():
    check_action()
    # if check_blank():
    #     return
    if endswith_operation(Form.screen.text()):
        inp = Form.screen.text()[:-1] + "/"
        Form.screen.setText(inp)
    else:
        inp = Form.screen.text() + "/"
        Form.screen.setText(inp)


def push_multiply():
    check_action()
    # if check_blank():
    #     return
    if endswith_operation(Form.screen.text()):
        inp = Form.screen.text()[:-1] + "*"
        Form.screen.setText(inp)
    else:
        inp = Form.screen.text() + "*"
        Form.screen.setText(inp)


def push_minus():
    check_action()
    # if check_blank():
    #     return
    if endswith_operation(Form.screen.text()):
        inp = Form.screen.text()[:-1] + "-"
        Form.screen.setText(inp)
    else:
        inp = Form.screen.text() + "-"
        Form.screen.setText(inp)


def push_plus():
    check_action()
    # if check_blank():
    #     return
    if endswith_operation(Form.screen.text()):
        inp = Form.screen.text()[:-1] + "+"
        Form.screen.setText(inp)
    else:
        inp = Form.screen.text() + "+"
        Form.screen.setText(inp)


def push_point():
    check_action()
    check = str(Form.screen.text())
    if "." in check:
        pass
    elif check[-1].isnumeric():
        Form.screen.setText(check + ".")
    else:
        pass


def push_equal():
    global state
    state = 1
    inp = Form.screen.text()

    try:
        value = str(eval(inp))
        if len(value) > 17:
            exp_value = "{:.2e}".format(int(value))
            Form.screen.setText(exp_value)
        else:
            Form.screen.setText(value)
    except:
        Form.screen.setText("Invalid Input")
        state = 2


def push_del():
    check_action()
    if Form.Forscreen.text() == "Invalid Input":
        clear()
    else:
        inp = Form.screen.text()
        Form.screen.setText(inp[: len(inp) - 1])


def push_c():
    check_action()
    Form.screen.setText("")


def push_pandm():
    check_action()
    check = str(Form.screen.text())
    if check[0] == "-":
        Form.screen.setText(check[1:])
    else:
        inp = "-" + Form.screen.text()
        Form.screen.setText(inp)


def push_byX():
    check_action()
    inp = eval("1/" + Form.screen.text())
    value = str(inp)
    if len(value) > 17:
        exp_value = "{:.2e}".format(int(value))
        Form.screen.setText(exp_value)
    else:
        Form.screen.setText(value)


def push_percent():
    check_action()
    inp = Form.screen.text()
    try:
        value = str(eval(inp + "/100"))
        Form.screen.setText(value)
    except:
        Form.screen.setText("")


def pushM_plus():  # M+
    global memory
    memory += int(Form.screen.text())


def pushM_minus():  # M-
    global memory
    memory -= int(Form.screen.text())


def pushM_read():  # MR-MEMORY READ
    global memory
    Form.screen.setText(str(memory))


def pushM_clear():  # MC - MEMORY CLEAR  (ALSO DELETE THE TXT FILE AFTER CLOSING OF CALCULTOR)
    global memory
    memory = 0


app = QtWidgets.QApplication([])
Form = uic.loadUi("main.ui")
Form.show()
Form.push0.clicked.connect(push_0)
Form.push1.clicked.connect(push_1)
Form.push2.clicked.connect(push_2)
Form.push3.clicked.connect(push_3)
Form.push4.clicked.connect(push_4)
Form.push5.clicked.connect(push_5)
Form.push6.clicked.connect(push_6)
Form.push7.clicked.connect(push_7)
Form.push8.clicked.connect(push_8)
Form.push9.clicked.connect(push_9)
Form.pushPercent.clicked.connect(push_percent)
Form.pushSqrt.clicked.connect(push_sqrt)
Form.pushDel.clicked.connect(push_del)
Form.pushByX.clicked.connect(push_byX)
Form.pushSquare.clicked.connect(push_square)
Form.pushPower.clicked.connect(push_power)
Form.pushDivide.clicked.connect(push_divide)
Form.pushMultiply.clicked.connect(push_multiply)
Form.pushMinus.clicked.connect(push_minus)
Form.pushPlus.clicked.connect(push_plus)
Form.pushEqual.clicked.connect(push_equal)
Form.pushPandM.clicked.connect(push_pandm)
Form.pushPoint.clicked.connect(push_point)
Form.pushC.clicked.connect(push_c)
Form.pushMp.clicked.connect(pushM_plus)
Form.pushMm.clicked.connect(pushM_minus)
Form.pushMR.clicked.connect(pushM_read)
Form.pushMC.clicked.connect(pushM_clear)

sys.exit(app.exec_())
