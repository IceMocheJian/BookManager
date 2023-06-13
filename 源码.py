import tkinter
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap import Style
import pymysql

class Root_system_func():

    def login(self): # 登录
        username = username_input.get()
        password = password_input.get()
        # 创建数据库连接
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='H1394830398h',
            port=3306,
            db='library',
            charset='utf8'
        )
        cursor = conn.cursor()
        sql = "select * from user_table"
        cursor.execute(sql)
        results = cursor.fetchall()
        f = 0
        for row in results:
            if username == row[0]:
                f = 1
                if password == row[1]:
                    messagebox.showinfo(title='提示', message='登录成功！')
                    window.destroy()
                    system(username)
                else:
                    messagebox.showinfo(title='提示', message='用户名或密码错误，请重新输入。')
        if f == 0:
            messagebox.showinfo(title='提示', message='用户名不存在，请重新输入。')
        username_input.delete(0, 'end')
        password_input.delete(0, 'end')
        cursor.close()
        conn.close()  # 关闭连接

    def register(self): # 注册
        username = username_input.get()
        password = password_input.get()
        # 创建数据库连接
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='H1394830398h',
            port=3306,
            db='library',
            charset='utf8'
        )
        cursor = conn.cursor()
        sql = "select * from user_table"
        cursor.execute(sql)
        results = cursor.fetchall()
        f = 0
        for row in results:
            if username == row[0]:
                f = 1
                break
        if f == 1:
            messagebox.showinfo(title='提示', message='该用户名已存在，请重新输入。')
        else:
            sql = 'insert into user_table(username,password) values(%s, %s)'
            cursor.execute(sql, (username, password))
            conn.commit()
            messagebox.showinfo(title='提示', message='注册成功！请登录')
        username_input.delete(0, 'end')
        password_input.delete(0, 'end')
        cursor.close()
        conn.close()  # 关闭连接

    def exit_system(self): # 退出
        response = tkinter.messagebox.askquestion("提示", "是否退出图书管理系统？")
        if response == 'yes':
            messagebox.showinfo(title='提示', message="感谢使用图书管理系统，再见！")
            window.destroy()
            exit()

class System_func():

    def add_book(self, a, b, c, d, e): # 添加书籍
        name = a.get()
        author = b.get()
        publisher = c.get()
        isbn = d.get()
        price = e.get()
        # 创建数据库连接
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='H1394830398h',
            port=3306,
            db='library',
            charset='utf8'
        )
        cursor = conn.cursor()
        sql = "select * from book_table"
        cursor.execute(sql)
        results = cursor.fetchall()
        books = [row[0] for row in results]
        if name in books:
            response = tkinter.messagebox.askquestion("提示", "该书籍已存在，是否更新该书籍信息？")
            if response == 'yes':
                self.update_book(a, a, b, c, d, e)
        else:
            sql = 'insert into book_table(name, author, publisher, ISBN, price) \
                  values(%s, %s, %s, %s, %s)'
            cursor.execute(sql, (name, author, publisher, isbn, price))
            conn.commit()
            messagebox.showinfo(title='提示', message='添加成功')
        a.delete(0, 'end')
        b.delete(0, 'end')
        c.delete(0, 'end')
        d.delete(0, 'end')
        e.delete(0, 'end')
        cursor.close()
        conn.close()  # 关闭连接

    def remove_book(self, a): # 删除书籍
        name = a.get()
        # 创建数据库连接
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='H1394830398h',
            port=3306,
            db='library',
            charset='utf8'
        )
        cursor = conn.cursor()
        sql = "select * from book_table"
        cursor.execute(sql)
        results = cursor.fetchall()
        books = [row[0] for row in results]
        if name in books:
            response = tkinter.messagebox.askquestion("提示", "删除操作无法撤销，是否确认删除？")
            if response == 'yes':
                sql = 'delete from book_table where name = %s'
                cursor.execute(sql, name)
                conn.commit()
                messagebox.showinfo(title='提示', message="删除成功")
        else:
            messagebox.showinfo(title='提示', message="未找到该书籍")
        a.delete(0, 'end')
        cursor.close()
        conn.close()  # 关闭连接

    def update_book(self, a1, a, b, c, d, e): # 修改信息
        oldname = a1.get()
        name = a.get()
        author = b.get()
        publisher = c.get()
        isbn = d.get()
        price = e.get()
        # 创建数据库连接
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='H1394830398h',
            port=3306,
            db='library',
            charset='utf8'
        )
        cursor = conn.cursor()
        sql = "select * from book_table"
        cursor.execute(sql)
        results = cursor.fetchall()
        books = [row[0] for row in results]
        if oldname in books:
            response = tkinter.messagebox.askquestion("提示", "更新后原信息将被覆盖，是否确认更新？")
            if response == 'yes':
                sql = 'update book_table set name = %s, author = %s, publisher = %s, ISBN = %s, price = %s where name = %s'
                cursor.execute(sql, (name, author, publisher, isbn, price, oldname))
                conn.commit()
                messagebox.showinfo(title='提示', message="修改成功")
        else:
            messagebox.showinfo(title='提示', message="未找到书籍")
        a1.delete(0, 'end')
        a.delete(0, 'end')
        b.delete(0, 'end')
        c.delete(0, 'end')
        d.delete(0, 'end')
        e.delete(0, 'end')
        cursor.close()
        conn.close()  # 关闭连接

    def search_book(self, a): # 查找书籍
        name = a.get()
        # 创建数据库连接
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='H1394830398h',
            port=3306,
            db='library',
            charset='utf8'
        )
        cursor = conn.cursor()
        sql = "select * from book_table"
        cursor.execute(sql)
        results = cursor.fetchall()
        books = [row[0] for row in results]
        if name in books:
            for row in results:
                if name == row[0]:
                    author = row[1]
                    publisher = row[2]
                    ISBN = row[3]
                    price = row[4]
            self.book_window(name, author, publisher, ISBN, price)
        else:
            messagebox.showinfo(title='提示', message="未找到书籍")
        a.delete(0, 'end')
        cursor.close()
        conn.close()  # 关闭连接

    def book_window(self, name, author, publisher, ISBN, price): # 书籍信息页面
        global my_book
        my_book = tkinter.Tk()
        my_book.title("书籍详情")
        my_book.geometry('250x250')
        my_book.geometry('+400+300')
        book_text = tkinter.Label(my_book,
                                  text="您查询的书籍详细信息如下:\n\n 书名: %s\n\n 作者: %s\n\n 出版社: %s\n\n ISBN: %s\n\n 价格: %s\n\n"
                                       % (name, author, publisher, ISBN, price),
                                  justify=tkinter.LEFT)
        book_text.place(x=10, y=10)
        button = tkinter.Button(my_book, text='返回', command=my_book.destroy, width=3, height=1)
        button.place(x=200, y=200)

    def exit_user_system(self): # 退出系统
        response = tkinter.messagebox.askquestion("提示", "是否退出图书管理系统？")
        if response == 'yes':
            messagebox.showinfo(title='提示', message="感谢使用图书管理系统，再见！")
            user_system.destroy()
            exit()


style = Style()
root_system_func = Root_system_func()
system_func = System_func()

def root_system():

    global username_input, password_input, window
    window = style.master
    window.title("欢迎使用图书管理系统")
    window.geometry('400x400')
    username_input = tkinter.Entry(window, width=15)
    username_input.place(x=195, y=100)
    password_input = tkinter.Entry(window, width=15, show='*')
    password_input.place(x=195, y=150)

    button1 = tkinter.Button(window, text='登录', command=root_system_func.login, width=3, height=1)
    button2 = tkinter.Button(window, text='注册', command=lambda: root_system_func.register(), width=3, height=1)
    button3 = tkinter.Button(window, text='退出', command=root_system_func.exit_system, width=3, height=1)
    button1.place(x=150, y=200)
    button2.place(x=200, y=200)
    button3.place(x=250, y=200)

    text1 = tkinter.Label(window, bd=4, fg='black', text='用户名')
    text2 = tkinter.Label(window, bd=4, fg='black', text='密码')
    text1.place(x=130, y=100)
    text2.place(x=130, y=150)
    window.mainloop()

def system(username):

    global user_system
    user_system = tkinter.Tk()
    user_system.title("欢迎进入%s的秘密小窝" % str(username))
    user_system.geometry('800x800')
    note = ttk.Notebook()
    note.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    #添加
    frame1 = tkinter.Frame()
    note.add(frame1, text='添加书籍')
    name = tkinter.Entry(frame1, width=15)
    name.place(relx=0.4, rely=0.3)
    text111 = tkinter.Label(frame1, bd=2, fg='black', bg='white', text='请输入书籍的相关信息')
    text111.place(relx=0.35, rely=0.21)
    text11 = tkinter.Label(frame1, bd=4, fg='black', bg='white', text='书名')
    text11.place(relx=0.3, rely=0.3)
    author = tkinter.Entry(frame1, width=15)
    author.place(relx=0.4, rely=0.35)
    text12 = tkinter.Label(frame1, bd=4, fg='black', bg='white', text='作者')
    text12.place(relx=0.3, rely=0.35)
    publisher = tkinter.Entry(frame1, width=15)
    publisher.place(relx=0.4, rely=0.4)
    text13 = tkinter.Label(frame1, bd=4, fg='black', bg='white', text='出版社')
    text13.place(relx=0.3, rely=0.4)
    isbn = tkinter.Entry(frame1, width=15)
    isbn.place(relx=0.4, rely=0.45)
    text14 = tkinter.Label(frame1, bd=4, fg='black', bg='white', text='ISBN')
    text14.place(relx=0.3, rely=0.45)
    price = tkinter.Entry(frame1, width=15)
    price.place(relx=0.4, rely=0.5)
    text15 = tkinter.Label(frame1, bd=4, fg='black', bg='white', text='价格')
    text15.place(relx=0.3, rely=0.5)
    add = tkinter.Button(frame1, text='添加',
                         command=lambda: system_func.add_book(name, author, publisher, isbn, price),
                         width=5, height=2)
    add.place(relx=0.5, rely=0.6)
    leave = tkinter.Button(frame1, text='退出', command=system_func.exit_user_system, width=5, height=2)
    leave.place(relx=0.9, rely=0.9)
    # 删除
    frame2 = tkinter.Frame()
    note.add(frame2, text='删除书籍')
    text211 = tkinter.Label(frame2, bd=2, fg='black', bg='white', text='请输入要删除的书')
    text211.place(relx=0.35, rely=0.33)
    name2 = tkinter.Entry(frame2, width=15)
    name2.place(relx=0.4, rely=0.4)
    text21 = tkinter.Label(frame2, bd=4, fg='black', bg='white', text='书名')
    text21.place(relx=0.3, rely=0.4)
    remove = tkinter.Button(frame2, text='删除', command=lambda: system_func.remove_book(name2), width=5, height=2)
    remove.place(relx=0.5, rely=0.6)
    leave = tkinter.Button(frame2, text='退出', command=system_func.exit_user_system, width=5, height=2)
    leave.place(relx=0.9, rely=0.9)
    # 更新
    frame3 = tkinter.Frame()
    note.add(frame3, text='修改信息')
    text311 = tkinter.Label(frame3, bd=2, fg='black', bg='white', text='请输入要修改的书')
    text311.place(relx=0.35, rely=0.14)
    name3 = tkinter.Entry(frame3, width=15)
    name3.place(relx=0.4, rely=0.21)
    text31 = tkinter.Label(frame3, bd=4, fg='black', bg='white', text='书名')
    text31.place(relx=0.3, rely=0.21)
    text311 = tkinter.Label(frame3, bd=4, fg='black', bg='white', text='请输入新的书籍信息')
    text311.place(relx=0.35, rely=0.28)
    namen = tkinter.Entry(frame3, width=15)
    namen.place(relx=0.4, rely=0.35)
    text31n = tkinter.Label(frame3, bd=4, fg='black', bg='white', text='书名')
    text31n.place(relx=0.3, rely=0.35)
    author3 = tkinter.Entry(frame3, width=15)
    author3.place(relx=0.4, rely=0.4)
    text32 = tkinter.Label(frame3, bd=4, fg='black', bg='white', text='作者')
    text32.place(relx=0.3, rely=0.4)
    publisher3 = tkinter.Entry(frame3, width=15)
    publisher3.place(relx=0.4, rely=0.45)
    text33 = tkinter.Label(frame3, bd=4, fg='black', bg='white', text='出版社')
    text33.place(relx=0.3, rely=0.45)
    isbn3 = tkinter.Entry(frame3, width=15)
    isbn3.place(relx=0.4, rely=0.5)
    text34 = tkinter.Label(frame3, bd=4, fg='black', bg='white', text='ISBN')
    text34.place(relx=0.3, rely=0.5)
    price3 = tkinter.Entry(frame3, width=15)
    price3.place(relx=0.4, rely=0.55)
    text35 = tkinter.Label(frame3, bd=4, fg='black', bg='white', text='价格')
    text35.place(relx=0.3, rely=0.55)
    update = tkinter.Button(frame3, text='更新',
                         command=lambda: system_func.update_book(name3, namen, author3, publisher3, isbn3, price3),
                         width=5, height=2)
    update.place(relx=0.5, rely=0.65)
    leave = tkinter.Button(frame3, text='退出', command=system_func.exit_user_system, width=5, height=2)
    leave.place(relx=0.9, rely=0.9)
    #查询
    frame4 = tkinter.Frame()
    note.add(frame4, text='查询书籍')
    text211 = tkinter.Label(frame4, bd=2, fg='black', bg='white', text='请输入要查询的书')
    text211.place(relx=0.35, rely=0.33)
    name4 = tkinter.Entry(frame4, width=15)
    name4.place(relx=0.4, rely=0.4)
    text41 = tkinter.Label(frame4, bd=4, fg='black', bg='white', text='书名')
    text41.place(relx=0.3, rely=0.4)
    search = tkinter.Button(frame4, text='查询', command=lambda: system_func.search_book(name4), width=5, height=2)
    search.place(relx=0.5, rely=0.6)
    leave = tkinter.Button(frame4, text='退出', command=system_func.exit_user_system, width=5, height=2)
    leave.place(relx=0.9, rely=0.9)

if __name__ == '__main__':
    root_system()


