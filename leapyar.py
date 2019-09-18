#print('enter year:')
#y=int(input("enter year:"))
#if 1900<=y<=100000:
 #   print("valid consyraint")
  #  if y%400==0 and y%100==0:
   #     print("year is leap")
    #elif y%100!=0 and y%4==0:
     #   print ("valid leap year")
    #else:
     #   print (" not leap year")
#else:
 #   print (" invalid constrint")

#n=y=int(input("enter year:"))
def is_leap(n):
    if n % 400 == 0:
        return True           # leap year program by function
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_leap(int(input())))

