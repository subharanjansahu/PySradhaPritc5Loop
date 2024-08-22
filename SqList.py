# insert
sq = []
count = 1
while(count <= 10):
  # random no. input from user
  # x = int(input("Enter no.="))
  # n = x*x
  n=count**2
  sq.append(n)
  count+=1
print(sq)

# retrive/travers
i = 0
while i < len(sq):
  print(sq[i])
  i += 1

# for i in sq:
#   print(i,end=',')