grade = int(input('Enter your grade(0-100):'))
print('-'*3 , 'Result' , '-'*3)
print('Numerical Grade:' , grade)
a = 51-grade
b = 61-grade
c = 76-grade
d = 87-grade
grade<=50 and print('Letter grade: D', 'Status: Failed' , 'Points to F:', a )  
51<grade<=60 and print('Letter grade: F' ,'\nStatus: Failed', '\nPoints to C:', b) 
61<grade<=75 and print('Letter grade: C', '\nStatus: Passed', '\nPoints to B:', c) 
76<grade<=86 and print('Letter grade: B', '\nStatus: Passed', '\nPoints to A:', d ) 
87<grade<=100 and print('Letter grade: A','\nStatus: Passed' )