import requests
from tkinter import *


# root class
class QuoteGenerator:
    __QUOTE_API  = 'http://api.quotable.io/random'
    
    def __init__(self, root):
        self.root = root
        self.initUI()
        
        
    # create initial widgets
    def initUI(self):
        self.quote_label=Label(self.root, wraplength=500, width=200, height=10, font=('Times new romans', 14, 'bold'), background='lightgray', foreground='blue')
        self.quote_label.pack(ipadx=20, ipady=20, padx=20, pady=(20, 5))

        self.generate_quote_button=Button(self.root, text='Generate quote', width=15, cursor='hand2', relief='flat', font=('Times new romans', 12, 'bold'), bg='#0c20f7', activebackground='#2839f7', fg='white', activeforeground='white', command=self.generate_quote)
        self.generate_quote_button.pack(side=RIGHT, padx=20)
    
    # call api and read quote as json format
    def generate_quote(self):
        self.quote_label.configure(text="")
        try:
            quote_json = requests.get(self.__QUOTE_API).json()
            quote_text = '{}\n\n__{}'.format(quote_json['content'], quote_json['author'])
        except:
            quote_text = "Error:\nThere was a problem generating the quote.\nPlease check your internet connection or API key."
        self.quote_label.configure(text=quote_text)


# root
if __name__ == '__main__':
    root=Tk()
    root.title('Quote Generator')
    root.geometry('600x355')
    root.resizable(False, False)
    QuoteGenerator(root)
    root.mainloop()