import cs50

while True:
   print("How much change is owed? ", end="")
   changeOwed = cs50.get_float()
   if changeOwed>0:
       break
changeOwed=changeOwed*100
coins = 0
while changeOwed>=25:
    changeOwed -=25
    coins+=1
while changeOwed>=10:
    changeOwed -=10
    coins+=1
while changeOwed>=5:
    changeOwed -=5
    coins+=1
while changeOwed>=1:
    changeOwed -=1
    coins+=1

print(coins)
