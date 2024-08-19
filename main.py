import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QScrollArea
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt

class PromptTemplate(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('GPT-4 Prompt Template')
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()
        
        # Create scrollable area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        self.text_boxes = []
        self.roles = ['system', 'user', 'assistant', 'user', 'assistant', 'user', 'assistant']
        
        for role in self.roles:
            box_layout = QHBoxLayout()
            label = QLabel(f"{role}:")
            text_box = QTextEdit()
            text_box.textChanged.connect(self.updateFormat)
            box_layout.addWidget(label)
            box_layout.addWidget(text_box)
            scroll_layout.addLayout(box_layout)
            self.text_boxes.append(text_box)
        
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        
        # Add button
        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.addTextBox)
        layout.addWidget(self.add_button)
        
        # Format display
        self.format_display = QTextEdit()
        self.format_display.setReadOnly(True)
        layout.addWidget(self.format_display)
        
        # Copy button
        copy_button = QPushButton('Copy Format')
        copy_button.clicked.connect(self.copyFormat)
        layout.addWidget(copy_button)
        
        self.setLayout(layout)
        self.updateFormat()
        
    def updateFormat(self):
        messages = []
        for i, text_box in enumerate(self.text_boxes):
            content = text_box.toPlainText()
            if content:
                messages.append({"role": self.roles[i], "content": content})
        
        format_dict = {"messages": messages}
        format_json = json.dumps(format_dict)
        self.format_display.setText(format_json)
        
    def addTextBox(self):
        new_role = 'assistant' if self.roles[-1] == 'user' else 'user'
        self.roles.append(new_role)
        
        box_layout = QHBoxLayout()
        label = QLabel(f"{new_role}:")
        text_box = QTextEdit()
        text_box.textChanged.connect(self.updateFormat)
        box_layout.addWidget(label)
        box_layout.addWidget(text_box)
        
        scroll_content = self.findChild(QScrollArea).widget()
        scroll_content.layout().addLayout(box_layout)
        
        self.text_boxes.append(text_box)
        self.updateFormat()
        
    def copyFormat(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.format_display.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PromptTemplate()
    ex.show()
    sys.exit(app.exec_())
