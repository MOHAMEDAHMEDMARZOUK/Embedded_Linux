import sys
import math

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        QWidget.__init__(self)                 #super().__init__()
        self.setWindowTitle("GUI_Calculator")

        # Create the display widget
        self.display = QLineEdit()
        #self.display.setReadOnly(True)  #user can only view the contents of the display but cannot directly edit or modify it .

        # Create buttons
        self.buttons = []
        button_labels = [
            '7', '8', '9', '/','|',
            '4', '5', '6', '*',"&",
            '1', '2', '3', '-','~',
            '0', '.', '=', '+','^',
            '(', ')', 'AC','**','%',
            
               
        ]

        grid_layout = QGridLayout()   #used to arrange the calculator buttons in a grid structure.
        for row in range(5):
            for col in range(5):
                button = QPushButton(button_labels[row * 5 + col])
                grid_layout.addWidget(button, row, col)
                self.buttons.append(button)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid_layout)
        self.setLayout(layout)

        # Connect button signals to slots
        for button in self.buttons:
            button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        clicked_button = self.sender()
        current_text = self.display.text()

        if clicked_button.text() == '=':
            try:
                result = eval(current_text)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
                
        elif clicked_button.text() == 'AC' : 
            self.display.setText("")
        
        else:
            new_text = current_text + clicked_button.text()
            self.display.setText(new_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
