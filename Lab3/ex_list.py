# List

x = 100
print(x)
x = 200
print(x)

mylist = ['apple', 'banana', 'cherry']
print(mylist, type(mylist))
print(f'Length fo mylist = {len(mylist)}')

# access data in list
# index
print(mylist[0])  # apple
print(mylist[1])  # banana
print(mylist[2])  # cherry
# negative index
print(mylist[-1])  # cherry
print(mylist[-2])  # cherry
print(mylist[-3])  # cherry
# range index
mynum = [10, 20, 30, 40, 50, 60, 70]
print(mynum)
print(mynum[2:5]) # คือตำแหน่งที่ 2-4
print(mynum[1:6]) # 1-5
print(mynum[:5]) # 0-4
print(mynum[3:]) # 3-end
# negative range index
print(mynum[-5:-1]) # 30,40,50,60

# loop
# for
for x in mynum:
    print(x,type(x))
for x in range(len(mynum)):
    print(mynum[x])

# while
i = 0
while i < len(mynum):
    print(mynum[i])
    i+=1

# chang data in list
mynum[-1] = 80
print(mynum)
mynum[-7] = 100
print(mynum)
mynum[0:3] = [100,200] # 0,1,2
print(mynum)
mynum[3:5] = [400,500,600]
print(mynum)

# add data
mynum.append(10)
print(mynum)
#insert () -- add data at specifis=c index
# add 5 at 0 index
mynum.insert(0,5)
print(mynum)

# remove data in list
# remove() ถ้าซ้ำจะลบตัวแรก
mynum.remove(10)
print(mynum)
mynum.remove(100)
print(mynum)
# pop()
mynum.pop(3) # ลบตำแหน่งที่3
print(mynum)
mynum.insert(0,100)
print(mynum)
mynum.pop(-1)
print(mynum)
# del
del mynum[1]
print(mynum)
# del mynum
# print(mynum)

# clear()
print(f'All data in mynum = {mynum}')
mynum.clear()
print(mynum)
