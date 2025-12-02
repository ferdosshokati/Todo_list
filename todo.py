from PyQt5.QtWidgets import QTextEdit,QListWidget,QLabel,QPushButton,QMainWindow,QApplication
from PyQt5 import uic
import sys,os


class Task:
    def __init__(self,title):
        self.title = title
    def __str__(self):
        return self.title

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self,title):
        if title.strip():
           self.tasks.append(Task(title))
    def delete_task(self,index):
        if 0<=index <len(self.tasks):
            self.tasks.pop(index)

    def clear_tasks(self):
        self.tasks.clear()

    def get_all_tasks(self):
        return [str(task) for task in self.tasks]


class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("todo.ui",self)

        # define widget
        self.label = self.findChild(QLabel,"label1")
        self.list_widget = self.findChild(QListWidget,"listWidget")
        self.add_item = self.findChild(QTextEdit,"textEdit_additem")
        # pushbutton
        # self.save = self.findChild(QPushButton,"save_Pushbutton")
        self.add_task = self.findChild(QPushButton,"add_task")
        self.delete = self.findChild(QPushButton,"delete_pushButton")
        self.clear = self.findChild(QPushButton,"clear_pushButton")
        self.show()

        self.todo = TodoList()

        self.add_task.clicked.connect(self.handle_add)
        self.delete.clicked.connect(self.handle_delete)
        self.clear.clicked.connect(self.handle_clear)
        # self.save.clicked.connect(self.handle_save)

    def handle_add(self):
        text = self.add_item.toPlainText()
        self.todo.add_task(text)
        self.add_item.clear()
        self.update_display()

    def handle_delete(self):
        row = self.list_widget.currentRow()
        if row >= 0:
            self.todo.delete_task(row)
            self.update_display()
        # else:
        #     self.label.setText("⚠ Choose one!")

    def handle_clear(self):
        self.todo.clear_tasks()
        self.update_display()

    # def handle_save(self):
    #     with open("tasks.txt", "w", encoding="utf-8") as f:
    #         f.write(self.todo.get_all_tasks())
    #     self.label.setText("✅ Save list!")

    def update_display(self):
        self.list_widget.clear()
        for task in self.todo.tasks:
            self.list_widget.addItem(task.title)


os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"F:\aferdos\پایتون\GUI\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


