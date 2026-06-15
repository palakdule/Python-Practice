nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 64

i = 0
while i< len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
        break
    else:
        print("finding...")
    i+= 1
print("end of loop")
