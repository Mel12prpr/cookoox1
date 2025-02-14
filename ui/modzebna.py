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
        Form.setWindowTitle(_translate("Form", "ძიების შედეგი"))


    def display_results(self, results):
        """Display the search results with selected information (name, ingredient details, and prep time)."""
        result_text = ""

        if results:
            for recipe in results:
                # Extracting the required data from the recipe tuple
                dish_name = recipe[0]  # Dish name
                ingredient_details = recipe[1]  # Ingredient details
                prep_time = recipe[3]  # Preparation time
                instructions = recipe[2]  # Instructions

                # Formatting the result text
                result_text += f"🍽 <b>{dish_name}</b>\n"
                result_text += f"🔍 <b>ინგრედიენტები:</b>\n{ingredient_details}\n\n"
                result_text += f"⏳ <b>მომზადების დრო:</b> {prep_time} წუთი\n\n"
                result_text += f"📜 <b>ინსტრუქცია:</b>\n{instructions}\n\n"
                result_text += "<hr>"  # Divider between recipes

            result_text = result_text.replace("\n",
                                              "<br>")  # Converting new lines to HTML line breaks for better display
        else:
            result_text = "No recipes found."

        # Set the result text in the QTextEdit (multiline widget)
        self.resultDisplay.setText(result_text)

