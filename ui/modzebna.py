from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1404, 834)

        # Background image
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1411, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1978203.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")


        self.resultDisplay = QtWidgets.QTextEdit(Form)
        self.resultDisplay.setGeometry(QtCore.QRect(0, 370, 1411, 461))
        self.resultDisplay.setObjectName("resultDisplay")
        self.resultDisplay.setReadOnly(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "result"))


    def display_results(self, results):
        result_text = ""

        if results:
            for recipe in results:
                dish_name = recipe[0]
                ingredient_details = recipe[1]
                prep_time = recipe[3]
                instructions = recipe[2]

                result_text += f"🍽 <b>{dish_name}</b>\n"
                result_text += f"🔍 <b>ინგრედიენტები:</b>\n{ingredient_details}\n\n"
                result_text += f"⏳ <b>მომზადების დრო:</b> {prep_time} წუთი\n\n"
                result_text += f"📜 <b>ინსტრუქცია:</b>\n{instructions}\n\n"
                result_text += "<hr>"

            result_text = result_text.replace("\n",
                                              "<br>")
        else:
            result_text = "რეცეპტი არ მოიძებნა"

        self.resultDisplay.setText(result_text)

