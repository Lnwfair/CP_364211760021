# Function

print('Start')

# define function
def functionA():
    print('Hello from function A.')

def functionB(var):
    print('Hello from function B.',var)

def functionC(var1,var2):
    print('Hello from function C.',var1,var2)

def functionF(**var): # var--> dictionary
    print('Hello from function F.')
    print(var)

# calling function
functionA()
functionB('Saiyai')
functionC('Saiyai','Campus')
functionF(fname='Puriwat',lname='lertkrai'major='MIT')



print('End')




