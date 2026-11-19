x=int(input('Enter the number of seconds:'))
h=x//3600
remaining_h=x%3600
m=remaining_h//60
s=remaining_h%60
print('hours=',h,'minutes=',m,'seconds=',s)
