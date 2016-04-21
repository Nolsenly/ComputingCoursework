dict = [(name1,hpm1,hp1),(name2,hpm2,hp2),(name3,hpm3,hp3)]
z=1
def checkplayerID(who):
    x=0
    while x < len(dict):
        y = 0
        if who == dict[x][0]:
            print("Ah, them.")
            y=x+1
        x=x+1
        if y = 0
        return y
command = input("Hey, watcha wanna do?: ")
if command == "Addplayer":
    MYNAMEIS = input("HIS NAME IS A WHAT?: ")
    g = checkplayerID(MYNAMEIS)
    if g == 1:
        #1.FUNCTION()
    elif g ==2:
        #2.FUNCTION()
    elif g ==3:
        #3.FUNCTION()
    #e.t.c
elif command == "help":
elif command == "damage":
elif command == "heal":
    #check through the dict for the correct number for the player then go through an if statement
    #make func.
else:
    print("Thats not a thing.")
