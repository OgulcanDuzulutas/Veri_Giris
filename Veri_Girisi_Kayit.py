import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def enter_data():
    accepted = accept_var.get()
    
    if accepted == "Accepted":
        
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()


            
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
                    registration_status TEXT, num_courses INT, num_semesters INT)
            '''
            conn.execute(table_create_query)

           
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, title, 
            age, nationality, registration_status, num_courses, num_semesters) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title,
                                  age, nationality, registration_status, numcourses, numsemesters)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
            messagebox.showwarning(title="Basarılı", message="Kayıt Başarılı")
        else:
            messagebox.showwarning(title="Error", message="İsim ve soyisim alanlarını giriniz.")
    else:
        messagebox.showwarning(title="Error", message="Kullancı sözleşmesini kabul etmeniz lazım.")

def list_data():
    pass

window = tk.Tk()
window.title("Veri Giriş Tablosu")

frame = tk.Frame(window)
frame.pack()


user_info_frame = tk.LabelFrame(frame, text="Kullanıcı Bilgileri")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tk.Label(user_info_frame, text="İsim")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="Soyisim")
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Cinsiyet")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Erkek", "Kadın"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Yaş")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(user_info_frame, text="Ülke")
nationality_combobox = ttk.Combobox(user_info_frame,
                                    values=["Turkiye", "Almanya", "İngiltere", "İtalya", "Mısır"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


courses_frame = tk.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tk.Label(courses_frame, text="Kayıt Durumu")

reg_status_var = tk.StringVar(value="Kayıtlı Değil")
registered_check = tk.Checkbutton(courses_frame, text="Kayıtlı",
                                  variable=reg_status_var, onvalue="Kayıtlı", offvalue="Kayıtlı Değil")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(courses_frame, text="Tamamlanmış Dersler")
numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(courses_frame, text="Dönem")
numsemesters_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


terms_frame = tk.LabelFrame(frame, text="Kullanıcı Sözleşmesi")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text="Kullanıcı sözleşmesini kabul ediyorum.",
                             variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)


enter_button = tk.Button(frame, text="Kayıt ol", command=enter_data)
enter_button.grid(row=3, column=0, sticky="news", padx=5, pady=5)

list_button = tk.Button(frame, text="Kayıtlı listesi", command=list_data)
list_button.grid(row=4, column=0, sticky="news", padx=5, pady=5)
window.mainloop()