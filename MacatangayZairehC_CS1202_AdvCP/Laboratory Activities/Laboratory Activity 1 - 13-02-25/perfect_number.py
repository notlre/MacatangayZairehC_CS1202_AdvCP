number = int(input('Enter a number: '))
divisor_sum = 0

for i in range(1, number):   
    if number% i == 0:
        divisor_sum += i
if divisor_sum == number:
    print(number, 'is a perfect number.')
else:
    print(number, 'is not a perfect number.')
    
    
  
    
        
        