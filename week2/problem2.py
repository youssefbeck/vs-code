a = float(input(' enter the price:'))
b = int(input('enter the quantity:'))
c = a * b 
print (c)
print('-'*3 , 'Reciept' , '-'*3)
print(f'Item price:' , '$',a)
print(f'Quantity' , '$',b)
c=c/12.5
print('Tax:' ,c)
if c > 100 :
    c-=c/10
    
    print('Subtotal', '$',c)