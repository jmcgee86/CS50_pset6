import cs50


while True:
   print("Height: ", end="")
   height = cs50.get_int()
   if height<23 and height>0:
       break

for i in range(height):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i+1):
        print("#", end="")
    print()
