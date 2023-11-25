import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import sys

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui1.ui', self)
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()

        cur.execute(f'''SELECT id, variety, roasting, ground_beans, taste, price, volume FROM coffee''')
        dates = cur.fetchall()
        if bool(dates):
            # Устнавливаем количество строк и столбцов в таблице
            self.table_widget.setRowCount(len(dates))
            self.table_widget.setColumnCount(len(dates[0]))

            # Устанавливаем название столбцов
            self.table_widget.setHorizontalHeaderLabels(["id", "название сорта", "степень обжарки", "молотый/в зернах",
                                                         "Описание вкуса", "Цена", "Объем упаковки"])

            # Заполняем таблицу данными из базы данных
            for i, elem in enumerate(dates):
                for j, val in enumerate(elem):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(val)))
        else:
            self.table_widget.setRowCount(len(dates))
            self.table_widget.setHorizontalHeaderLabels(["id", "Запись", "День недели", "Время", "Дата"])
        con.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())