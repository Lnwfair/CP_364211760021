# lab 8

""""
จงกำหนดฟังก์ชัน ชื่อ "getNumber()" เพื่อรับข้อมูลจำนวนเต็มจากผู้ใช้
5 จำนวน และแสดงผลทางจอภาพ จากนั้นให้กำหนดังก์ชันต่อไปนี้
และ กำหนดฟังก์ชัน  "totalValue()" เพื่อหาผลรวมของตัวเลขทั้งหมด
แสดงผลทางจอภาพ
"""

def getNumber():
    mynumber = []
    for x in range(5):
            mynumber.append(int(input(f'E:{x+1}')))
        return mynumber

def totalValue(var):
    total = 0
    for x in var:
        total+=x
    return total

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The summation of thoese integer user: {mynum}')

