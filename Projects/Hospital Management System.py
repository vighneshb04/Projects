from sys import exit
import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='', database='project')

if conn.is_connected():
    print('Successfully connected')
    c1 = conn.cursor()
    print('---------------------------------------------')
    print("HOSPITAL MANAGEMENT SYSTEM")
    print('---------------------------------------------')
    print('"GOD WISHES YOU"')
    print("1. LOGIN")
    print("2. EXIT")
    choice = int(input("ENTER YOUR CHOICE:"))

    if choice == 1:
        u1 = input("enter user name:")
        pwd1 = input("enter the password:")

        while u1 == 'vasu' and pwd1 == 'vasu6072':
            print('Connected')
            print("WELCOME TO HOSPITAL")
            print("Successfully connected")
            print('1. Registering Patient details')
            print('2. Registering Doctor details')
            print('3. Registering Worker details')
            print("4. Total patient details")
            print("5. Total doctor details")
            print("6. Total worker details")
            print('7. Patient detail')
            print('8. Doctor detail')
            print('9. Worker detail')
            print('10. Exit')
            choice = int(input('ENTER YOUR CHOICE:'))

            if choice == 1:
                p_name = input('Enter Patient Name:')
                p_age = int(input('Enter Age:'))
                p_problems = input('Enter the Problem/Disease:')
                p_phono = int(input('Enter Phone number:'))
                sql_insert = "insert into patient_details values('{}', {}, '{}', {})".format(p_name, p_age, p_problems, p_phono)
                c1.execute(sql_insert)
                print('SUCCESSFULLY REGISTERED')
                conn.commit()
                
            elif choice == 2:
                d_name = input('Enter Doctor Name:')
                d_age = int(input('Enter Age:'))
                d_department = input('Enter the Department:')
                d_phono = int(input('Enter Phone number:'))
                sql_insert = "insert into doctor_details values('{}', {}, '{}', {})".format(d_name, d_age, d_department, d_phono)
                c1.execute(sql_insert)
                print('successfully registered')
                conn.commit()

            elif choice == 3:
                w_name = input('Enter Worker Name:')
                w_age = int(input('Enter Age:'))
                w_workname = input('Enter type of work:')
                w_phono = int(input('Enter Phone number:'))
                sql_insert = "insert into worker_details values('{}', {}, '{}', {})".format(w_name, w_age, w_workname, w_phono)
                c1.execute(sql_insert)
                print('successfully registered')
                conn.commit()

            elif choice == 4:
                sql_w = 'select * from patient_details'
                c1.execute(sql_w)
                r = c1.fetchall()
                for i in r:
                    print(i)

            elif choice == 5:
                sql_x = "select * from doctor_details"
                c1.execute(sql_x)
                s = c1.fetchall()
                for i in s:
                    print(i)

            elif choice == 6:
                sql_y = "select * from worker_details"
                c1.execute(sql_y)
                t = c1.fetchall()
                for i in t:
                    print(i)

            elif choice == 7:
                h = input("Enter the name:")
                sql_w = 'select * from patient_details where p_name="{}"'.format(h)
                c1.execute(sql_w)
                u = c1.fetchall()
                for i in u:
                    print(i)

            elif choice == 8:
                d = input("Enter the name:")
                sql_d = 'select * from doctor_details where p_name="{}"'.format(d)
                c1.execute(sql_d)
                v = c1.fetchall()
                for i in v:
                    print(i)

            elif choice == 9:
                f = input("Enter the name:")
                sql_f = 'select * from worker_details where p_name="{}"'.format(f)
                c1.execute(sql_f)
                w = c1.fetchall()
                for i in w:
                    print(i)

            elif choice == 10:
                exit()
                break

            else:
                print('Wrong username & password')

    if choice == 2:
        exit()
