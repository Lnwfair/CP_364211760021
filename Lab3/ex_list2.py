# list comprehension

mylist = [12, 34, 65, 33, 78, 56, 34, 12, 67, 89, ]
print(mylist,len(mylist))

# เลือกข้อมูลจาก mylist
# โดยเลือกเฉพาะ >= 50
newlist = [x for x in mylist if x >= 50]
print(newlist)

# เลือกข้อมูลจาก mylist
# โดยเลือกเฉพาะ >= 50 และ < 80
newlist = [x for x in  mylist if x >= 50 and x < 80 ]
print(newlist)

# จากข้อมูลใน mylist
# ให้เปลี่ยนข้อมูลที่มีค่า  >50 เป็น 50 ทั้งหมด
print(mylist)
newlist = [x if x < 50 else 50 for x in mylist]
print(newlist)

# reverse data in list
mylist.reverse()
print(mylist)

# sort list
# low to high
mylist.sort()
print(f'Sort Low to High: {mylist}')
# high to low
mylist.sort(reverse=True)
print(f'Sort High to Low:{mylist}')

# join list
x = [10,20,30]
y = ['a','b','c']

z = x+y
print(z)

x.extend(y)
print(x)