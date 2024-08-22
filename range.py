# seq = range(5)
# for i in seq:
#   print(i)
'''
range(start?,stop,step?)
start and step are optional by default step incriment by 1
'''
# for i in range(10): #range(stop)
#   print(i)

# for i in range(5,10): #range(start,stop)
#   print(i)

# for i in range(4,15,3): #range(start,stop,step)
#   print(i)

'''print all odd no.s btween 1 to 100'''
# for i in range(1,101,2):
#   print(i)

'''print reverse 100 to 1'''
# for i in range(100,0,-1):
#   print(i)

'''multiplication table'''
x = int(input("Ent the no.:"))
for i in range(1,11):
  print(x,'X',i,'=',x*i)