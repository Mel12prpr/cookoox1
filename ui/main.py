from PyQt5 import QtWidgets, QtCore
import sys
import sqlite3
from pirvelii import Ui_MainWindow
import kerdzebisgverdi, desertebisgverdi, snekebisgverdi, iaponiiisgverdi, italiisgverdi, truketisgverdii, meqsikisgverdi, sakartveloo, safrangetisgverdi, modzebna, checkboxx

# base klasi categoriebisTvis
class CategoryWindow(QtWidgets.QWidget):
    def __init__(self, ui_class, filter_type, filter_value):
        super().__init__()
        self.ui = ui_class()
        self.ui.setupUi(self)
        self.filter_type = filter_type
        self.filter_value = filter_value
        self.load_recipes()
# receptebis filtracia da daloudeba
    def load_recipes(self):
        conn = sqlite3.connect("D:/Python_II/cookbox/database/cookbox.db")
        cursor = conn.cursor()

        if self.filter_type == "category":
            cursor.execute("SELECT dish_name, ingredient_details, prep_time FROM recipes WHERE category = ?", (self.filter_value,))
        elif self.filter_type == "country":
            cursor.execute("SELECT dish_name, ingredient_details, prep_time FROM recipes WHERE country = ?", (self.filter_value,))

        recipes = cursor.fetchall()
        conn.close()

        for recipe in recipes:
            recipe_text = f"🍽 <b>{recipe[0]}</b><br>📌 <b>ინგრედიენტები:</b> {recipe[1]}<br>⏳ <b>მომზადების დრო:</b> {recipe[2]} წუთი"
            label = QtWidgets.QLabel(recipe_text)
            label.setWordWrap(True)
            label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(300, 120))

            self.ui.recipesList.addItem(item)
            self.ui.recipesList.setItemWidget(item, label)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui_checkboxx = None
        self.checkboxx_window = None
        self.setupUi(self)

        self.windows = {}

        # kategorebis ghilakebi
        self.kerdzebi.clicked.connect(lambda: self.open_category("category", "კერძი", kerdzebisgverdi.Ui_Form))
        self.wasaxemsebeli.clicked.connect(lambda: self.open_category("category", "წასახემსებელი",  snekebisgverdi.Ui_Form  ))
        self.desertebi.clicked.connect(lambda: self.open_category("category", "დესერტი", desertebisgverdi.Ui_Form  ))

        # qveynebis ghilakebi
        self.japan.clicked.connect(lambda: self.open_category("country", "იაპონია", iaponiiisgverdi.Ui_Form))
        self.italy.clicked.connect(lambda: self.open_category("country", "იტალია", italiisgverdi.Ui_Form))
        self.turkey.clicked.connect(lambda: self.open_category("country", "თურქეთი", truketisgverdii.Ui_Form))
        self.mexico.clicked.connect(lambda: self.open_category("country", "მექსიკა", meqsikisgverdi.Ui_Form))
        self.georgia.clicked.connect(lambda: self.open_category("country", "საქართველო", sakartveloo.Ui_Form))
        self.france.clicked.connect(lambda: self.open_category("country", "საფრანგეთი", safrangetisgverdi.Ui_Form))

        # dzebnis ghilaki
        self.pushButton_11.clicked.connect(self.search_recipes)

        # ingredientiT dzebnis ghilaki
        self.pushButton.clicked.connect(self.open_checkbox)

    def open_category(self, filter_type, filter_value, ui_class):
        key = f"{filter_type}_{filter_value}"
        if key not in self.windows:
            self.windows[key] = CategoryWindow(ui_class, filter_type, filter_value)
        self.windows[key].show()
        self.windows[key].load_recipes()

    def search_recipes(self):
        search_query = self.lineEdit.text()
        if search_query:
            results = self.perform_search(search_query)
            self.open_modzebna_window(results)
        else:
            self.open_modzebna_window()

    def perform_search(self, search_query):
        conn = sqlite3.connect("D:/Python_II/cookbox/database/cookbox.db")
        cursor = conn.cursor()
        cursor.execute("SELECT dish_name, ingredient_details, instructions, prep_time FROM recipes WHERE dish_name LIKE ?",
                       ('%' + search_query + '%',))
        results = cursor.fetchall()
        conn.close()
        return results

    def open_modzebna_window(self, results=None):
        self.modzebna_window = QtWidgets.QMainWindow()
        self.ui_modzebna = modzebna.Ui_Form()
        self.ui_modzebna.setupUi(self.modzebna_window)

        if results:
            self.ui_modzebna.display_results(results)

        self.modzebna_window.show()

    def open_checkbox(self):
        self.checkboxx_window = QtWidgets.QWidget()
        self.ui_checkboxx = checkboxx.Ui_Form()
        self.ui_checkboxx.setupUi(self.checkboxx_window)
        self.checkboxx_window.show()

        self.ui_checkboxx.pushButton.clicked.connect(self.get_selected_ingredients)

        self.checkboxx_window.show()

    def get_selected_ingredients(self):
        selected_ingredients = []

        for checkbox_name in dir(self.ui_checkboxx):
            if checkbox_name.startswith("checkBox") and getattr(self.ui_checkboxx, checkbox_name).isChecked():
                selected_ingredients.append(getattr(self.ui_checkboxx, checkbox_name).text())

        if selected_ingredients:
            results_text = self.filter_recipes_by_ingredients(selected_ingredients)
            self.ui_checkboxx.label_2.setText(results_text)

    def filter_recipes_by_ingredients(self, ingredients):
        conn = sqlite3.connect("D:/Python_II/cookbox/database/cookbox.db")
        cursor = conn.cursor()

        placeholders = " AND ".join(["ingredient_details LIKE ?" for _ in ingredients])
        query = f"SELECT dish_name FROM recipes WHERE {placeholders}"
        params = ["%" + ingredient + "%" for ingredient in ingredients]

        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()

        if results:
            return ",".join([f"🍽 {recipe[0]}" for recipe in results])
        else:
            return "რეცეპტი არ მოიძებნა"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
