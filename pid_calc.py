from tkinter import *

class Gediminas():
    def __init__(self, root):
        self.root = root
        self.root.title("PID Generator")
        self.root.geometry("230x150")
        self.root.iconbitmap('images/binary.ico')
        self.choice = StringVar()
        self.choice.set("Female")
        self.dropdown = OptionMenu(root, self.choice, "Male", "Female")
        self.input_birthdate = StringVar()
        self.birthdate = self.input_birthdate.get()
        self.input_queue = StringVar()
        self.queue = self.input_queue.get()

        self.u_gender = Label(root, text="Gender:", border=5)
        self.u_birthdate = Label(root, text="Birthdate:\n(YYYY-MM-DD)", border=5)
        self.input_birthdate = Entry(root, textvariable=self.input_birthdate)
        self.u_queue = Label(root, text="Queue number:", border=5)
        self.e_queue = Entry(root, textvariable=self.input_queue)
        self.b_confirm = Button(root, text="Confirm", command=self.full_check)
        self.full_info = Label(root, text="Input required data", relief=SUNKEN, border=1)
        self.root.bind('<Return>', self.full_check) # ENTER mygtuko funkcija

        self.dropdown.grid(row=0, column=1, columnspan=2)
        self.u_gender.grid(row=0, column=0, sticky=E)
        self.u_birthdate.grid(row=1, column=0, sticky=E)
        self.input_birthdate.grid(row=1, column=1)
        self.u_queue.grid(row=2, column=0, sticky=E)
        self.e_queue.grid(row=2, column=1)
        self.b_confirm.grid(row=5, column=0, columnspan=2)
        self.full_info.grid(row=3, column=0, columnspan=2, sticky=W+E)

        self.root.mainloop()

    def print_selected(self):
        return self.choice.get()

    def print_selected2(self):
        return self.input_birthdate.get()

    def print_selected3(self):
        return self.input_queue.get()

    def first_number(self):
        self.slicing = str(self.print_selected2())
        if self.print_selected() == "Male" and self.slicing[0:2] == "19":
            return 3
        elif self.print_selected() == "Male" and self.slicing[0:2] == "20":
            return 5
        elif self.print_selected() == "Female" and self.slicing[0:2] == "19":
            return 4
        elif self.print_selected() == "Female" and self.slicing[0:2] == "20":
            return 6
        else:
            print("Something's wrong")

    def year_numbers(self):
        year_numbers = str(self.print_selected2())
        return year_numbers[2:4]

    def month_numbers(self):
        month_numbers = str(self.print_selected2())
        return month_numbers[5:7]

    def day_numbers(self):
        day_numbers = str(self.print_selected2())
        return day_numbers[8:10]

    def queue_numbers(self):
        other_numbers = str(self.print_selected3())
        return other_numbers

    def last_number(self):
        list = [self.first_number(), self.year_numbers(), self.month_numbers(), self.day_numbers(), self.queue_numbers()]
        new_list = []
        conversion = [str(integer) for integer in list]
        nosep = "".join(conversion)
        result = int(nosep)
        for x in str(result):
            new_list.append(int(x))

        sk1 = new_list[0]
        sk2 = new_list[1]
        sk3 = new_list[2]
        sk4 = new_list[3]
        sk5 = new_list[4]
        sk6 = new_list[5]
        sk7 = new_list[6]
        sk8 = new_list[7]
        sk9 = new_list[8]
        sk10 = new_list[9]

        sk11 = sk1 * 1 + sk2 * 2 + sk3 * 3 + sk4 * 4 + sk5 * 5 + sk6 * 6 + sk7 * 7 + sk8 * 8 + sk9 * 9 + sk10 * 1
        if sk11 % 11 != 10:
            return sk11 % 11
        else:
            sk11 = sk1 * 3 + sk2 * 4 + sk3 * 5 + sk4 * 6 + sk5 * 7 + sk6 * 8 + sk7 * 9 + sk8 * 1 + sk9 * 2 + sk10 * 3
            if sk11 % 11 != 10:
                return sk11 % 11
            else:
                return 0

    def full_check(self):
        self.full_info['text'] = f"Generated: {self.first_number()}{self.year_numbers()}{self.month_numbers()}{self.day_numbers()}{self.queue_numbers()}{self.last_number()}"

if __name__ == "__main__":
    root = Tk()
    app = Gediminas(root)
    app.mainloop()