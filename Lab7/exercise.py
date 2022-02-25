""""
เขียนโปรแกรม login โดยรับ input จากผู้ใช้
คือ username และ password หากผู้ใช้กรอกข้อมูล
ถูกต้องแสดงข้อความ "welcome {name}"
แต่ถ้าไม่ถูก ให้กรอกใหม่
หากผิด3ครั้ง ให้แสดงข้อความ
"your accont has been locked, please contact admin."

"""

username = 'admin'
passwod = '1234'

cont = 0
while cont < 3:
    u = input('username')
    p = input('password')
    if u == username and p == passwod:
        print(f'hello, {u}')
        break
    else:
        print(f'username or password is not correct.')
        print(f'password, login again.')
        cont+=1
else:
    print('your accont has been locked, please contact admin')