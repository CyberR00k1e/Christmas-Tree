from termcolor import cprint, colored
import time


r=int(input("Ho,ho.ho! input your rows").strip())
i=1
print("\n"*2)
cprint("Wishing all of you a Merry Christmas and Happy New Year"+ "\n", "green",)
for i in range(r):
    cprint((" "*r + ("*"+" ")*i + " "*r),"red",)
    i=i+1
    r=r-1
    time.sleep(0.3)

print("\n")
time.sleep(0.2)
cprint("Merry Christmas and Happy New Year !", "green")
print("\n"*2)



