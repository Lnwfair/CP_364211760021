# Exception

print('Start')

# x = 100
# print(y)
try:
    x = int(input('Enter an integer:'))
    print(x)
except:
    print('Only integer are allow.')
else: # no errror
    print('user iput: ',x)
finally: # alway excute
    print('finally, process finished.')

print('End')