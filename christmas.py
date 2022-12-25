from termcolor import cprint, colored

#r=int(input("Ho,ho.ho! input your rows").strip())
r=15
i=1


for i in range(r):
    cprint((" "*r + ("*"+" ")*i + " "*r),"red",)
    i=i+1
    r=r-1

print("\n")

cprint("Wishing all of you a Merry Christmas and Happy New Year from Vectra,Asia team"+ "\n", "blue","on_green")



