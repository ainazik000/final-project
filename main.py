import tkinter as tk
from tkinter import ttk
from errors import ChoiceError
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from images_convert import change_contrast

class Window:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('900x300')
        self.root.title('My program')
        self.files = []
        self.tree = ttk.Treeview(self.root)
        

    def choose_file(self):
        try:
            filename = askopenfilename()
            if filename in self.files:
                raise RecursionError()
            self.files.append(filename)
            self.refrash_tree()
        except RecursionError:
            messagebox.showerror('Repetition Error', 'You can select file only once')


    def save(self):
        try:
            option = self.varF2.get()
            messagebox.showinfo('OK!', 'OK!')
            change_contrast(img_pathes=self.files, option=option)
            print(self.files)
            self.clear()
        except ChoiceError:
            messagebox.showerror('Choice Error', 'Make choice!')


    def refrash_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.files:
            self.tree.insert(parent='', index='end', iid=row,text='', values=(row,), tag='orow')
        self.tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
        self.tree.grid(row=0, column=4, columnspan=5, rowspan=11, padx=10, pady=20)
        

    def clear(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.files.clear()


    def delete(self):
        
        try:
            row = self.tree.selection()[0]
            self.tree.delete(row)
            self.files.remove(row)


        except IndexError:
            messagebox.showerror('Error', 'Select file for delete')


    def main_loop(self):

        button_choose = Button(self.root, text='Choose file', command=self.choose_file)
        button_choose.grid(row=0, column=0)

        button_save = Button(self.root, text='Run', command=self.save)
        button_save.grid(row=4, column=0)

        button_clear = Button(self.root, text='Clear', command=self.clear)
        button_clear.grid(row=6, column=0)

        button_delete = Button(self.root, text='Delete', command=self.delete)
        button_delete.grid(row=8, column=0)

        self.varF2 = StringVar(self.root)
        self.option_text = 'Choose option'
        self.varF2.set(self.option_text)
        sidesF2 = ['Contrast', "Black and white"]
        sideF2 = OptionMenu(self.root, self.varF2, *sidesF2)        
        sideF2.grid(row=2, column=0, columnspan=1, padx=25, pady=5)

        self.tree['columns'] = ('dir',)
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('dir', anchor=W, width=600)
        self.tree.heading("dir", text="dir", anchor=W)
        self.refrash_tree()
        self.root.mainloop()


if __name__ == '__main__':
    window = Window()
    window.main_loop()

