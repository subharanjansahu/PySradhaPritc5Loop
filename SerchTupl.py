nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# normal
# j = int(input("enter a no. from above tuple:"))
# i = nums.index(j)
# print("index of",j,"is",i,"and no. is",nums[i])

x = int(input("enter a no. from above tuple:"))
i = 0
while(i< len(nums)):
  if(x == nums[i]):
    print("Found the no. in index",i)
    break
  i+=1
else:
  print("not found")