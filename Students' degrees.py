from sqlite3 import *

start_message = '''Please select the process you want
 1- Create a table of students degrees (c)
2- See one or more of students degrees (s)
3- Delete one of them (d)
4- edit one of them (e)
5- Calculate the mean of it (a):'''
db_filename_s = """Enter the file name(must be existed):"""
student_name_s = """Enter the student's name(if you want to skip it press enter):"""
student_id_s = """Enter the student's id(if you want to skip it press enter):"""

try:
    while True:

        a = input(start_message).strip().lower()
        if a in ['c', 's', 'd', 'e', 'a']:
            print(f'You have selected the process {a}')
            if a == 'c':
                def c(db_filename=input('Enter the file name:'), no_of_std=int(input('Enter the students number:'))):
                    x = connect(f"{db_filename}.db")
                    x.execute(
                        'create table if not exists school_data(student_id INTEGER,student_name TEXT,student_degree INTEGER)')
                    for i in range(no_of_std):
                        k = input("enter the student name:").strip().capitalize()
                        z = int(input("enter the student degree:"))
                        q = int(input("Enter the student's id:"))
                        x.execute(
                            f"insert into school_data(student_id,student_name,student_degree) values({q},'{k}',{z})")
                        x.commit()


                c()
            elif a == 's':
                def s(db_filename=input(db_filename_s),
                      method=input('select the method (name or id):').strip().lower()):
                    x = connect(f"{db_filename}.db")
                    if method == 'name':
                        print('The name method is used')
                        cr = x.cursor()
                        q = input("Enter the student's name:").strip().capitalize()
                        y = cr.execute(f"select * from school_data where student_name = '{q}'")
                        k = y.fetchone()
                        print(f"student's name is : {k[1]} , his id: {k[0]} and his degree: {k[2]}")
                    elif method == 'id':
                        print('The id method is used')
                        cr = x.cursor()
                        z = int(input("Enter the student's id:"))
                        y = cr.execute(f'select * from school_data where student_id = {z}')
                        k = y.fetchone()
                        print(f"student's name is : {k[1]} , his id: {k[0]} and his degree: {k[2]}")
                    else:
                        print("You have entered the method wrong")
                        print("Please restart the programme")


                s()
            elif a == 'd':

                def d(db_filename=input(db_filename_s),
                      method=input('select the method (name or id):').strip().lower()):
                    x = connect(f"{db_filename}.db")
                    if method == 'id':
                        cr = x.cursor()
                        print('The id method is used')
                        z = int(input("Enter the student's id:"))
                        y = cr.execute(f'select * from school_data where student_id = {z}')
                        k = y.fetchone()
                        cr.execute(f"delete from school_data where student_id = {z}")
                        print(f"Student {k[1]} with id {k[0]} has been removed")
                        x.commit()
                    elif method == 'name':
                        cr = x.cursor()
                        print('The name method is used')
                        z = input("Enter the student's name:").strip().capitalize()
                        y = cr.execute(f"select * from school_data where student_name = '{z}'")
                        k = y.fetchone()
                        cr.execute(f"delete from school_data where student_name = '{z}'")
                        print(f"Student {k[1]} with id {k[0]} has been removed")
                        x.commit()
                    else:
                        print("You have entered the method wrong")
                        print("Please restart the programme")


                d()
            elif a == 'e':
                def e(db_filename=input(db_filename_s),
                      method=input('select the method (name or id):').strip().lower()):
                    x = connect(f"{db_filename}.db")
                    if method == 'id':
                        cr = x.cursor()
                        print('The id method is used')
                        z = int(input("Enter the student's id:"))
                        r = input("Enter the student's new name:").strip().capitalize()
                        q = int(input("Enter the student's new degree:"))
                        y = cr.execute(f'select * from school_data where student_id = {z}')
                        k = y.fetchone()
                        cr.execute(
                            f"update school_data set student_name = '{r}' where student_id = {z}")
                        cr.execute(f"update school_data set student_degree = {q} where student_id = {z}")
                        print(f"Student {k[1]} with id {k[0]} has been changed to {r} and now his degree is: {q} ")
                        x.commit()
                    elif method == 'name':
                        cr = x.cursor()
                        print('The name method is used')
                        z = input("Enter the student's name:").strip().capitalize()
                        r = input("Enter the student's new name:").strip().capitalize()
                        q = int(input("Enter the student's new degree:"))
                        y = cr.execute(f"select * from school_data where student_name = '{z}'")
                        k = y.fetchone()
                        cr.execute(f"update school_data set student_name = '{r}' where student_name = '{z}'")
                        cr.execute(f"update school_data set student_degree = {q} where student_name = '{r}'")
                        x.commit()
                        print(f"Student {k[1]} with id {k[0]} has been changed to {r} and now his degree is: {q}")


                e()
            elif a == 'a':
                def a(db_filename=input(db_filename_s)):
                    x = connect(f"{db_filename}.db")
                    x.execute("select student_degree from school_data")
                    cr = x.cursor()
                    cr.execute("select student_degree from school_data")
                    total = int(
                        input(
                            "Enter the total number of students\n(the students' number mustn't exceed the max. number):"))
                    q = 0
                    loops = 0
                    for i in range(total):
                        y = cr.fetchone()
                        k = y[0]
                        q += k
                        loops += 1
                    mean = q / total
                    if int(mean) == mean:
                        print(int(mean))
                    else:
                        print(mean)


                a()
        else:
            print("""The method you selected isn't in the program
                Please start it again""")
        q1 = input("Do you want to start programme again? (Y/N)").strip().capitalize()
        if q1[0] == 'Y':
            continue
        elif q1[0] == 'N':
            break
    print('The programme has been stopped')
except ValueError:
    print("You have enter a wrong value.\nRestart the programme again.")
