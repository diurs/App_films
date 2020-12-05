# systemctl start apache2
# systemctl start mysql

from tkinter import *
from tkinter.ttk import Combobox , Radiobutton , Frame, Label, Style
import pymysql, os, random
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button , BOTH, scrolledtext, messagebox
from collections import Counter

class MainApp(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        Window_search.UI(self)
        
        button2 = Button(self, text='Поиск', command=self.window_search)
        button4 = Button(self, text='Самый популярный актер', command=self.most_popular_actor)
        button5 = Button(self, text='Частовстречаемый актер у director', command=self.new_window3)
        button6 = Button(self, text='Все топ 250', command=self.new_window2)
        button7 = Button(self, text='Рандомный фильм', command=self.random_film)
        
        self.geometry('900x600')
        self.title('Выбор фильма')
        #button2.bind('<Double-Button-1>', self.hide)
        label = Label(self, text='Меню', font= ('Arial', 30), bg="#b2bfbb")
        label.place(x=20, y = 50)
        button2.place(x=20,y=250)
        button6.place(x=20,y=300)
        button7.place(x=20,y=350)
        button4.place(x=20,y=400)
        button5.place(x=20,y=450)
        
        #canvas = Canvas(self,width=200,height=99)
        pilImage = Image.open("4.jpg")
        image = ImageTk.PhotoImage(pilImage)
        canvas = Canvas(self, width=490, height=600)
        canvas.place(x=350,y=0)
        a = canvas.create_image(250,300,im = image)
        self.mainloop()
        
    def random_film(self):
    	Window_search.connect(self)
    	film = random.randint(0,len(movie))
    	res = messagebox.showinfo('Фильм на сегодня ', movie[film])
    	return res
    def most_popular_actor(self):
    	Window_search.connect(self)
    	max_actor=str(d.keys()).split("'")
    	res2 = messagebox.showinfo('Самый популярный актер ', max_actor[1])
    	return res2
    def close_window55(self):
    	#import sys
    	#sys.exit()
    	return MainApp.destroy(self)
    def window_search(self):
    	#window.destroy()
    	#self.destroy()
    	Window_search().mainloop()
    	#self.close_window55()
        
        #self.destroy()
        #self.tk.call('wm', 'withdraw',self._w)
    
    def new_window2(self):
    	Window2().mainloop()
    
    def new_window3(self):
    	Director_actor().mainloop()
    	
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

class Director_actor(Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        Window_search.connect(self)
        Window_search.UI(self)	
        self.geometry('900x600')
        self.title('Какой актер чаще всего снимается у режиссера? ')
        self.text_name()
    	
    def search_director_actor(self):
    	zapros = director_actor.get()
    	# тут поиск и запрос в бд
    	#print(zapros)
    	number_actor=[]
    	tmp_act=[]
    	maxx=[]
    	m=[]
    	#search_director = 'Фрэнк Дарабонт'
    	for i in range(len(director)):
    		if director[i].count(zapros) >=1:
    			number_actor.append(i)
    	for ac in number_actor:
    		tmp_act.append(actors[ac])
    	for d in tmp_act:
    		s=d.split(';')
    		for kek in s:
    			maxx.append(kek)

    	# удалить пробелы в maxx
    	for delete in maxx:
    		d =delete.lstrip(' ')
    		m.append(d)
    		
    	answer_db_actors = dict((x, m.count(x)) for x in set(m) if m.count(x) >= 1)
    	print(answer_db_actors)    	
    	key_list = list(answer_db_actors.keys())
    	val_list = list(answer_db_actors.values())
    	maximal_val=max(val_list)
    	list_one_actors=[]
    	if maximal_val == 1:
    		window32.insert(INSERT,'У этого режиссера все актеры снимались по одному разу:')
    		for hw in key_list:
    			#list_one_actors.append(hw)
    			window32.insert(INSERT,'\n')
    			window32.insert(INSERT,hw)
    	else:
    		textt= key_list[val_list.index(maximal_val)]
    		window32.insert(INSERT,textt)
    		
    def for_ok_button(self):
    	window32.delete(1.0,END)
    	self.search_director_actor()

    def text_name(self):
        label = Label(self, text='Выберите имя режиссера :', font= ('Arial', 20), bg="#b2bfbb")
        label.place(x=20,y=70)
        global director_actor
        director_actor = Combobox(self, values = director2 ,  state = "readonly")   
        director_actor.place(x= 30,y=140)
        
        label2 = Label(self, text='Самый популярный актер у', font= ('Arial', 20), bg="#b2bfbb")
        label2.place(x=20, y = 210)
        label3 = Label(self, text='этого режиссера: ', font= ('Arial', 20), bg="#b2bfbb")
        label3.place(x=20, y = 250)
        global window32
        window32 = scrolledtext.ScrolledText(self, width = 35, height = 8, bg =('#dcd2c9'), font = ('Arial', 12))
        window32.place(x=20,y=300)
        
        ok = Button(self, text="OK", bg = '#dcd2c9', activebackground = '#dcd2c9',command=self.for_ok_button)
        ok.place(x=150,y=510)
        
        pilImage1 = Image.open("d.jpg")
        image1 = ImageTk.PhotoImage(pilImage1)
        canvas = Canvas(self,width=460,height=540)
        canvas.place(x=400,y=30)
        imagesprite = canvas.create_image(230,270,im = image1)
        self.mainloop()
         
class Window_search(Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.connect()
        #выбор
        self.type_search()
        self.UI()
        
    def UI(self):
        self.configure(background="#b2bfbb")

    def connect(self):
        connection = pymysql.connect('localhost','root','newpassword','kek')
        
        global year, year_all
        global rating_ball, rating_b_all
        global country, country_all
        global director, director2
        global actors, akter
        global screenwriter, screenw
        
        global rating
        global url_logo
        global movie
        global d
        
        country_all = []
        country=[]
        
        rating_b_all=[]
        rating_ball =[]
        
        year_all=[]
        year = []
        
        screenw = []
        screenwriter=[]

        director=[]
        director2=[]
        actors=[]
        akter=[]
        
        rating=[]
        url_logo=[]
        movie=[]
        
        with connection.cursor() as cursor:
        	sql= "SELECT year, rating_ball, country, director , actors, screenwriter  , rating , url_logo, movie FROM table_name"
        	cursor.execute(sql)
        	
        for row in cursor:
        	year.append(str(row[0]))
        	year_all.append(str(row[0])) #все годы - повторяющиеся данные
        	
        	rating_ball.append(str(row[1]))
        	rating_b_all.append(str(row[1])) # все повторяющиеся данные тоже без сортировки
        	
        	country.append(str(row[2]))
        	country_all.append(str(row[2]))
        	
        	director.append(str(row[3]))	 #все режиссеры
        	actors.append(str(row[4]))	 #все(и повторяющиеся) актеры		
        	
        	screenwriter.append(str(row[5]))
        	rating.append(row[6])
        	url_logo.append(str(row[7]))
        	movie.append(str(row[8]))

        for d in range(len(actors)):
        	xx= actors[d].split(';')
        	for dd in xx:
        		akter.append(dd.lstrip(' '))
        for dire in range(len(director)):
        	x1=director[dire].split(';')
        	for dire2 in x1:
        		director2.append(dire2.lstrip(' '))

        for scre in range(len(screenwriter)):
        	x2=screenwriter[scre].split(';')
        	for scre2 in x2:
        		screenw.append(scre2.lstrip(' '))

        d = dict((x, akter.count(x)) for x in set(akter) if akter.count(x) > 7)
        
        year=list(set(year))
        year.sort()
        rating_ball=list(set(rating_ball))
        rating_ball.sort()
        country=list(set(country))
        
        director2=list(set(director2)) # неповтор режиссеры
        director2.sort()
        
        akter = list(set(akter)) # тут хранятся неповторяющиеся актеры
        akter.sort()
        
        screenw=list(set(screenw))
        screenw.sort()

        connection.close()

    def get(self,b):
    	global da
    	da = b.get()
    	#получение текста
    	text_search.append(da)
    	#print(text_search)
    	messagebox.showinfo('Фильм', da)  
    
    def ok(self, a,b):
    	a.bind("<Double-Button-1>", self.get)
    	self.get(b)
    
    def type_search(self):
    	label = Label(self, text='Расширенный поиск ', font= ('Arial Bold', 25) , bg="#b2bfbb")
    	label.place(x=230, y=10)
    	self.geometry('900x600')
    	self.title('Поиск по критериям')
    	label_choice = Label(self, text='Выберите тип поиска: ', font= ('Arial', 17) , bg="#b2bfbb")
    	label_choice.place(x=20,y=65)
    	global var
    	var= IntVar()
    	rad1 = Radiobutton(self,text='Поиск по одному критерию', value=1, variable=var, command= self.selected_search)  		
    	rad2 = Radiobutton(self,text='Поиск по нескольким критериям', value=2, variable=var, command= self.selected_search) 	
    	rad1.place(x= 20, y = 115)
    	rad2.place(x=20, y = 140)
    	
    def selected_search(self):
    	r = var.get()
    	global db_search
    	db_search=[]  
    	if r == 1:
    		print('1!')
    		self.text()
    		for i in db_search:
    			if i != '':
    				db_search.append(i)
    		print(db_search)
    	elif r == 2:
    		print('2!')
    		self.text()
    		for i in db_search:
    			if i != '':
    				db_search.append(i)
    		print(db_search)
      
    def ap(self):
        global db_search, year_all_tmp
        keka=[]
        keka.append(combo2.get())
        keka.append(combo3.get())
        keka.append(combo4.get())
        keka.append(combo5.get())
        keka.append(combo6.get())
        keka.append(combo7.get())
        db_search=[]
        if var.get()==2:
        	for n in keka:
        		#if n !='':
        		db_search.append(n)
        	self.advanced_search()
        elif var.get() == 1:
        	for n in keka:
        		if n !='':
        			db_search.append(n)
        		
        	self.single_search()
 	
        print(db_search)
        #self.advanced_search()
        
        #тут расширенный поиск
    def advanced_search(self):
    	#print('для отладки-----')
    	global year_tmp, year_all_tmp, rating_tmp, country_tmp, director_tmp, actor_tmp, screenwr_tmp, tmp_text_search
    	actor_tmp=[]
    	screenwr_tmp=[]
    	director_tmp=[]
    	country_tmp=[]
    	rating_tmp=[]
    	year_all_tmp=[]
    	tmp_text_search = [year_all_tmp, rating_tmp, country_tmp, director_tmp, actor_tmp,screenwr_tmp]
    	eh= [year_all, rating_b_all, country_all, director, actors, screenwriter]
    	for sea in range(len(db_search)):
    		#print('sea  ',sea)
    		if db_search[sea] != '':
    			m = tmp_text_search[sea]
    			find=db_search[sea]
    			print(find, sea)
    			count = eh[sea].count(find)
    			ann=eh[sea]
    			for g in range(len(eh[sea])):
    				if ann[g].count(find) == 1:
    					print('count', count, ' , № совпадающего элемента с искомым префиксом', g)
    					m.append(g)
    		if db_search[sea] == '':
    			sea+=1
    	elements=[]
    	for i in year_all_tmp:
    		if i == '':
    			print('переход к след эдементу')
    		for i2 in rating_tmp:
    			if i != i2:
    				messagebox.showinfo('Найденный фильм', 'Не найдено фильма по Вашему запросу')
    				break
    			elif i==i2:
    				# если всего столько непустых параметров то ищем фильм и break
    				for element in db_search:
    					if element !='':
    						elements.append(element)
    				if len(elements)==2:
    					messagebox.showinfo('Найденный фильм' , movie[i2])
   
    				elements.clear()
    				
    				for i3 in country_tmp:
    					if i2 !=i3:
    						messagebox.showinfo('Найденный фильм', 'Не найдено фильма по Вашему запросу')
    						break
    					elif i2==i3:
    						for element in db_search:
		    					if element !='':
		    						elements.append(element)
		    				if len(elements)==3:
		    					messagebox.showinfo('Найденный фильм' , movie[i3])
		    				break
    						elements.clear()
    						print(len(db_search))
    						
    						for i4 in director_tmp:
    							if i3 !=i4:
    								messagebox.showinfo('Найденный фильм', 'Не найдено фильма по Вашему запросу')
    								break
    							elif i3==i4:
    								for element in db_search:
				    					if element !='':
				    						elements.append(element)
				    				if len(elements)==4:
				    					messagebox.showinfo('Найденный фильм' , movie[i4])
				    				break
				    				elements.clear()
    								print(len(db_search))
    								for i5 in actor_tmp:
    									if i4 !=i5:
    										messagebox.showinfo('Найденный фильм', 'Не найдено фильма по Вашему запросу')
    										break
    									elif i4==i5:
	    									for element in db_search:
						    					if element !='':
						    						elements.append(element)
						    				if len(elements)==5:
						    					messagebox.showinfo('Найденный фильм' , movie[i5])
						    				break
						    				elenemts.clear()
    										for i6 in screenwr_tmp:
    											if i5 !=i6:
    												messagebox.showinfo('Найденный фильм', 'Не найдено фильма по Вашему запросу')
    												break
    											elif i5==i6:
    												messagebox.showinfo('Найденный фильм', movie[i6])
    												break
    def clear(self):
    	self.withdraw()
    	second_window=tk.Toplewel()
    	second_window.protocol("WM_DELETE_WINDOW", lambda: self.destroy())	
    								
    def single_search(self):
    	print(db_search)
    	m_rand=[] 
    	find = db_search[0]
    	tt=[year_all,rating_b_all,country_all,director,actors,screenwriter]
    	   	# оиск значения в каждой строчке рейтинг год и тд
    	for t in range(len(tt)):
    		if tt[t].count(find) > 0:
    			# поиск в массиве совпад
    			massivchik = tt[t]
    			for f in range(len(massivchik)):
    				if massivchik[f].count(find) > 0:
    					m_rand.append(f)
    					print(f, movie[f])
    				f+=1
    		t+=1
    	film = random.choice(m_rand)
    	messagebox.showinfo('Найденный фильм', movie[random.choice(m_rand)])									
							
    def text(self):
        label2 = Label(self, text='Год', font= ('Arial', 17), bg="#b2bfbb")
        label2.place(x=20,y=200)
        global combo2, combo3, combo4, combo5, combo6, combo7
        combo2 = Combobox(self, values = year,  state = "readonly",)   
        combo2.place(x= 150,y=205)
        
        label3 = Label(self, text='Рейтинг', font= ('Arial', 17), bg="#b2bfbb")
        label3.place(x=20,y=250)
        combo3 = Combobox(self, values = rating_ball , state = "readonly")  
        combo3.place(x= 150,y=255)

        label4 = Label(self, text='Страна', font= ('Arial', 17), bg="#b2bfbb")
        label4.place(x=20,y=300)
        combo4 = Combobox(self, values = country, state = "readonly")  
        combo4.place(x= 150,y=305)
        
        global text_search
        text_search=[] 
        
        label5 = Label(self, text='Режиссер', font= ('Arial', 17), bg="#b2bfbb")
        label5.place(x=20,y=350)
        
        combo5 = Combobox(self, values = director2, state = "readonly")  
        combo5.place(x= 150,y=355)

        label6 = Label(self, text='Актер', font= ('Arial', 17), bg="#b2bfbb").place(x=20,y=405)
        combo6 = Combobox(self, values = akter, state = "readonly")   
        combo6.place(x= 150,y=400)
        
        label7 = Label(self, text='Сценарист', font= ('Arial', 17), bg="#b2bfbb")
        label7.place(x=20,y=450)
        combo7 = Combobox(self, values = screenw, state = "readonly")  
        combo7.place(x= 150,y=455)      

        btn_ok = Button(self, text="OK", bg = '#dcd2c9', activebackground = '#dcd2c9',command=self.ap)
        btn_ok.place(x=150,y=510)
        
        canvas = Canvas(self,width=470,height=470)
        canvas.place(x=380,y=80)
        pilImage2 = Image.open("searchhh.jpg")
        image2 = ImageTk.PhotoImage(pilImage2)
        imagesprite2 = canvas.create_image(235,235,im = image2)
        self.mainloop()

if __name__ == '__main__':
    MainApp().mainloop()
