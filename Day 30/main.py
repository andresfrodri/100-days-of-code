#File not found exception


try:
    file= open('file.txt') #There's no file.txt so it will probably cause an error
except FileNotFoundError as error_message:
    file=open('file.txt','w') #It will create the file 
    file.write('It was an strange and lovely night')
else:
    text=file.read()
    print(text)
finally:
    file.close()
    print('file was closed')

#Making our own exceptions

height=float(input('Height in meters: '))
weight = float(input('Weight in kg: '))

if height > 3:
    raise ValueError('Humans should not be over 3 meters')

bmi= weight / height**2
print(bmi)

