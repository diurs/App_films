# systemctl start apache2
# systemctl start mysql


from tkinter import *
from tkinter.ttk import Combobox , Radiobutton , Frame, Label, Style
import pymysql
import os
import random
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button , BOTH, scrolledtext, messagebox
import os

class MainApp(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        Window_search.UI(self)
        
        button2 = Button(self, text='Поиск', command=self.window_search)
        button4 = Button(self, text='Самый популярный актер', command=self.new_window2)
        button5 = Button(self, text='Частовстречаемый актер у director', command=self.new_window2)
        button6 = Button(self, text='Все топ 250', command=self.new_window2)
        button7 = Button(self, text='Рандомный фильм', command=self.random_film)
        
        self.geometry('900x600')
        self.title('Выбор фильма')
        #button2.bind('<Double-Button-1>', self.hide)
        button2.pack()
        button6.pack()
        button7.pack()
        button4.pack()
        button5.pack()
    def random_film(self):
    	Window_search.connect(self)
    	film = random.randint(0,len(movie))
    	res = messagebox.showinfo('Фильм на сегодня ', movie[film])
    	return res

    def window_search(self):
        Window_search().mainloop()
        self.destroy()
        self.tk.call('wm', 'withdraw',self._w)
    
    def new_window2(self):
    	Window2().mainloop()
    	'''
    def hide(self):
    	#self.withdraw()
    	return MainApp().deinconfity()
    	
    def wm_withdraw(self):
    	return MainApp().destroy()
    	#return self.tk.call('wm', 'withdraw',self._w)
    	'''
    def director(self):
    	#поиск upper lower в базе данных с таким именем если нет то так и писать else
    	messagebox.showinfo('Ошибка', 'Введенного режиссера не существует в бд. Попробуйте ввести снова')
    
    	
class Window2(Tk):
	def __init__(self, *arg, **kwarg):
		super().__init__(*arg, **kwarg)
		label = Label(self, text='Печерень всех фильмов: ', font = ('Arial Bold', 17), bg="#b2bfbb")
		# тут с бд вывод текста
		label.pack()
		self.geometry('900x600')
		self.title('Топ 250 фильмов')
		Window_search.connect(self)
		Window_search.UI(self)
		self.all_films()
	def all_films(self):
		window = scrolledtext.ScrolledText(self, width = 88, height = 25, bg =('#dcd2c9'), font = ('Arial', 12))
		window.place(x=20,y=50)
		for i in range(len(movie)):
			window.insert(INSERT,i+1)
			window.insert(INSERT,' 	 ')
			window.insert(INSERT,movie[i])
			window.insert(INSERT,'\n')
		
		
class Window_search(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.connect()
        self.text()
        self.UI()
        
    def UI(self):
        
        #img = ImageTk.PhotoImage(Image.open('1.jpg'))
        #panel = Label(self, image = img)
        #panel.place(x=150,y=300)
        self.configure(background="#b2bfbb")
        
        
    def connect(self):
        connection = pymysql.connect('localhost','root','newpassword','kek')
        global year
        global rating_ball
        global country
        global director
        global actors
        global screenwriter
        global rating
        global url_logo
        global movie
        year = []
        rating_ball =[]
        country=[]
        director=[]
        actors=[]
        screenwriter=[]
        rating=[]
        url_logo=[]
        movie=[]
        
        with connection.cursor() as cursor:
        	sql= "SELECT year, rating_ball, country, director , actors, screenwriter  , rating , url_logo, movie FROM table_name"
        	cursor.execute(sql)
        for row in cursor:
        	year.append(row[0])
        	rating_ball.append(str(row[1]))
        	country.append(str(row[2]))
        	director.append(str(row[3]))
        	actors.append(str(row[4]))			#с ними что-то сделать отсортировать надо
        	screenwriter.append(str(row[5]))
        	rating.append(row[6])
        	url_logo.append(str(row[7]))
        	movie.append(str(row[8]))
        	
        year=list(set(year))
        year.sort()
        rating_ball=list(set(rating_ball))
        rating_ball.sort()
        country=list(set(country))
        director=list(set(director))
        movie.sort()
        connection.close()
		#actors=list(set(actors))
        #Style().configure("TFrame", background="#333")
    def get(self,b):
    	global da
    	da = b.get()
    	#получение текста
    	#tt = b.get()
    	text_search.append(da)
    	print(text_search)
    	
    	messagebox.showinfo('Фильм', da)
    
   
    
    def ok(self, a,b):
    	a.bind("<Double-Button-1>", self.get)
    	self.get(b)
    	
    	   
    
    def text(self):
    	#self.connect()
        #self.connect()
        label = Label(self, text='Расширенный поиск ', font= ('Arial Bold', 25) , bg="#b2bfbb")
        label.place(x=230, y=10)
        self.geometry('900x600')
        self.title('Поиск по критериям')
        label_choice = Label(self, text='Выберите тип поиска: ', font= ('Arial', 17) , bg="#b2bfbb")
        label_choice.place(x=20,y=65)
        
        label2 = Label(self, text='Год :', font= ('Arial', 17), bg="#b2bfbb")
        label2.place(x=20,y=200)
        combo2 = Combobox(self, values = year,  state = "readonly",)   
        combo2.current(0)  
        combo2.place(x= 150,y=205)
        #rk = messagebox.showinfo('Фильм на сегодня ', combo2.get())
        #combo2.get()
        
        label3 = Label(self, text='Рейтинг :', font= ('Arial', 17), bg="#b2bfbb")
        label3.place(x=20,y=250)
        combo3 = Combobox(self, values = rating_ball , state = "readonly",)  
        combo3.current(0)  
        combo3.place(x= 150,y=255)
        #combo3.get()
        
        label4 = Label(self, text='Страна :', font= ('Arial', 17), bg="#b2bfbb")
        label4.place(x=20,y=300)
        combo4 = Combobox(self, values = country, state = "readonly")  
        combo4.current(0)  
        combo4.place(x= 150,y=305)
        global text_search
        text_search=[]   
        
        label5 = Label(self, text='Режиссер :', font= ('Arial', 17), bg="#b2bfbb")
        label5.place(x=20,y=350)
        txt = Entry(self,width=30, bg = '#dcd2c9')
        txt.place(x=150, y=355)
        btn_ok_director = Button(self, text="OK", bg = '#dcd2c9', activebackground = '#dcd2c9', command =lambda: self.ok(btn_ok_director, txt))
        btn_ok_director.place(x=400,y=355)
        text_label5=Label(self, text='Например : '+director[0] + director[1], font= ('Arial', 8), bg="#b2bfbb")
        text_label5.place(x=20,y=380)
        #text_search.append(txt.get())
        #print(text_search)
        
 		
        label6 = Label(self, text='Актер :', font= ('Arial', 17), bg="#b2bfbb").place(x=20,y=430)
        txt_actor = Entry(self,width=30,bg = '#dcd2c9')
        txt_actor.place(x=150, y=435)
        btn_ok_actor = Button(self, text="OK",bg = '#dcd2c9', activebackground = '#dcd2c9',command =lambda: self.ok(btn_ok_actor, txt_actor) )
        btn_ok_actor.place(x=400,y=435)
        text_label6=Label(self, text='Например : '+actors[218], font= ('Arial', 8), bg="#b2bfbb").place(x=20,y=460)
        #text_search.append(txt_actor.get())
        #print(text_search) 

        
        label7 = Label(self, text='Сценарист :', font= ('Arial', 17), bg="#b2bfbb")
        label7.place(x=20,y=505)
        txt_screenwriter = Entry(self,width=30, bg = '#dcd2c9')
        txt_screenwriter.place(x=150, y=510)
        btn_ok_screenwriter = Button(self, text="OK", bg = '#dcd2c9', activebackground = '#dcd2c9', command =lambda: self.ok(btn_ok_screenwriter, txt_screenwriter))
       	btn_ok_screenwriter.place(x=400,y=510)
        text_label7=Label(self, text='Например : '+screenwriter[0], font= ('Arial', 8), bg="#b2bfbb")
        text_label7.place(x=20,y=535)
        #text_search.append(self.da)
        print(text_search) 
          
          
          
        selected= IntVar()
        rad1 = Radiobutton(self,text='Поиск по одному критерию', value=1, variable=selected)  
        rad2 = Radiobutton(self,text='Поиск по нескольким критериям', value=2, variable=selected) 
        rad1.place(x= 60, y = 115)
        rad2.place(x=60, y = 140)
        
        #combo2.get()
        #combo3.get()
        
        
        #imga = ImageTk.PhotoImage(file="ha.png")
        #labeli = Label(self, image=imga)
        #labeli.image_ref = img
        #labeli.place(x=400,y=300)
       
    
    #combo.get() 
    #def ok(self):
     #   name = self.btn_ok_director.get()
    	#оиск в массиве имен. upper и тд
    	# имя есть :
    	# имени нет
        
	

 


if __name__ == '__main__':



    MainApp().mainloop()
