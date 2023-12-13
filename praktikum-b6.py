import os
os.system("clear")

a = True
i = 0
limit = 5

while a:
    i +=1  # i = i + 1
    if i <= limit:
        print("Selamat bergabung",limit-i+1)
    else:
        a = False 
