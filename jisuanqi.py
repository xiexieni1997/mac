from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("计算器")

        self.result = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.display = Entry(master, font=("Arial", 16), width=15, justify=RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+"
        ]

        row = 1
        col = 0
        for button_text in button_list:
            button = Button(master, text=button_text, font=("Arial", 16), width=3, height=2)
            button.grid(row=row, column=col, padx=3, pady=3)
            button.bind("<Button-1>", self.button_click)
            col += 1
            if col > 3:
                col = 0
                row += 1

        equals_button = Button(master, text="=", font=("Arial", 16), width=3, height=2)
        equals_button.grid(row=5, column=2, padx=3, pady=3)
        equals_button.bind("<Button-1>", self.calculate)

    def button_click(self, event):
        text = event.widget.cget("text")
        if text.isdigit() or text == ".":
            if self.new_num:
                self.display.delete(0, END)
                self.new_num = False
            self.display.insert(END, text)
        else:
            if not self.new_num:
                self.calculate()
            self.op = text
            self.result = float(self.display.get())
            self.new_num = True
            self.op_pending = True

    def calculate(self, event=None):
        if self.op_pending:
            if self.op == "+":
                self.result += float(self.display.get())
            elif self.op == "-":
                self.result -= float(self.display.get())
            elif self.op == "*":
                self.result *= float(self.display.get())
            elif self.op == "/":
                self.result /= float(self.display.get())
            self.op_pending = False
            self.display.delete(0, END)
            self.display.insert(END, self.result)
            self.new_num = True

root = Tk()
calc = Calculator(root)
root.mainloop()