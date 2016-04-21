

PlyrEle = []
z = 0
while z < 5:
    PlyrEle.append([])
    z=z+1
x = 0
y = 0
PlayersHp = ""
class Character:
    'Hp System For Players, this Session'
    playercount = 0

    def __init__(self, Name, MaxHp, x):
            self.name = Name
            self.MaxHp = int(MaxHp)
            self.Hp = 0
            PlyrEle[x].append(self.name)
            PlyrEle[x].append(int(self.MaxHp))
            PlyrEle[x].append(int(self.Hp))
            self.x = x

    def update(self, hp):
        PlyrEle[self.x][2] = hp
        print(PlyrEle[self.x])

    def SessionBegins(self):
        self.Hp = self.MaxHp
        PlyrEle[self.x][1] = self.MaxHp
        PlyrEle[self.x][2] = self.MaxHp
        self.update(self.Hp)


    def ShortRest(self):
        self.Hp = self.MaxHp
        self.update(self.Hp)

    def Healing(self, Heal):
        self.Hp = self.Hp + Heal
        if (self.Hp > self.MaxHp) :
            self.Hp = self.MaxHp
        self.update(self.Hp)

    def Damage(self, Damage):
        self.Hp = int(self.Hp) - int(Damage)
        if (self.Hp <= ((self.MaxHp/2)*-1)) :
            print("Player Is Kill")
        elif (self.Hp <= 0) :
            print("Player Is Down")
        self.update(self.Hp)
#while y < x:
#    PlayersHp = (PlayersHp, PlyrEle[y][0], ":", PlyrEle[y][1],":",PlyrEle[y][2])
#    y= y+1
#x=x+1

k=0
print("Welcome To the Menu")
while k < len(PlyrEle):
    print(PlyrEle[k])
    k=k+1

z=1
def checkplayerID(who):
    x=0
    CLAUSE = false
    while x < len(PlyrEle):
        y = 0
        if who == PlyrEle[x][0]:
            print("Ah, them.")
            print(x)
            y=x
            CLAUSE = true
        x=x+1
    if (y==0 and CLAUSE == true):
        return y
    elif y > 0:
        return y
    else :
        y = 69
        return y
command = input("Hey, watcha wanna do?: ")
if command == "Addplayer":
    Addname = input("What's their name?: ")
    AddMaxHp = input("What's their MaxHp?: ")
    g = 1
    if g == 1:
        p1 = Character(Addname,AddMaxHp,g)
        g = g+1
    elif g ==2:
        p2 = Character(Addname,AddMaxHp,g)
        g = g+1
    elif g ==3:
        p3 = Character(Addname,AddMaxHp,g)
        g = g+1
    elif g ==4:
        p4 = Character(Addname,AddMaxHp,g)
        g = g+1
    elif g ==5:
        p5 = Character(Addname,AddMaxHp,g)
        g = g+1
    else:
        print("hmmm. you've got too many characters...")
elif command == "help":
    print("Help")

elif command == "damage":
        i = checkplayerID(MYNAMEIS)
        dmg = input("How Much Damage: ")
        if i == 1:
            p1.Damage(dmg)
        elif i == 2:
            p2.Damage(dmg)
        elif i ==3:
            p3.Damage(dmg)
        elif i ==4:
            p4.Damage(dmg)
        elif i ==5:
            p5.Damage(dmg)
        else:
            print("Thats not a correct Id...")
elif command == "heal":
    print("ty")
    helt = input("How Much Heal: ")
    i = checkplayerID(MYNAMEIS)
    if i == 1:
        p1.Healing(helt)
    elif i ==2:
        p2.Healing(helt)
    elif i ==3:
        p3.Healing(helt)
    elif i ==4:
        p4.Healing(helt)
    elif i ==5:
        p5.Healing(helt)
    else:
        print("Thats not a correct Id...")
    #check through the dict for the correct number for the player then go through an if statement
    #make func.
else:
    print("Thats not a thing.")
