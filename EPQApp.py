
cardname = []
cardcolour = []
cardcost = []
cardtext = []
cardstren = []
cardtough = []
cardtype = []
#^sets all the variables
z=0
splitoutput = []
lst = open('mtgcardsfile.txt').readlines()
while z < 2:
	splitoutput = lst[z].split(",")
	cardname.append(splitoutput[0])
	cardcolour.append(splitoutput[1])
	cardcost.append(splitoutput[2])
	cardtext.append(splitoutput[3])
	cardtype.append(splitoutput[4])
	cardstren.append(splitoutput[5])
	cardtough.append(splitoutput[6])
	z=z+1
def CheckByPicture(photo):
	import pytesseract
	from PIL import Image
	Imagewords = str(pytesseract.image_to_string(Image.open(photo))).lower() #this actually converts the image into text.
#below is file handling and attempts to split the file and put said pieces into the right place
	#I said they were attempts...
	cardname = []
	cardcolour = []
	cardcost = []
	cardtext = []
	cardstren = []
	cardtough = []
	cardtype = []
	#^sets all the variables
	z=0
	splitoutput = []
	lst = open('mtgcardsfile.txt').readlines()
	while z < 2:
		splitoutput = lst[z].split(",")
		cardname.append(splitoutput[0])
		cardcolour.append(splitoutput[1])
		cardcost.append(splitoutput[2])
		cardtext.append(splitoutput[3])
		cardtype.append(splitoutput[4])
		cardstren.append(splitoutput[5])
		cardtough.append(splitoutput[6])
		z=z+1
	x = len(cardname)
#this stuff checks whether the imagewords are the same as any of the cards. This is the basic functionality that should be working soon. Then ill make it poss to edit your collection.
	n=0
	while (n < x):

		if Imagewords == cardname[n] :
			print("Theres a Match! We've Put it into a file for you.")
			mcards = open("MyCards.txt", "a")
			mcards.write(Imagewords + ",")
		n=n + 1
#CheckByPicture("twelver.jpg")
def NamSer(serch):
	k=0
	retvalnam = ""
	x = len(cardname)
	while k < x :
		if (serch == cardname[k]):
			retvalnam = cardname[k]
			cardno = k
		k=k+1
	if (retvalnam != ""):
		print(cardname[cardno], "Is a ", cardcost[cardno], " cost ", cardcolour[cardno]," ", cardtype[cardno])
		if (cardtype[cardno] == "creature"):
			print(" and it has ", cardstren, " strength and ", cardtough, " toughness, it's text is: ", cardtext)
		else:
			print(" and it does the following: ", cardtext)
def ColSer(serch):
	k=0
	retvalcol = []
	x = len(cardcolour)
	while k < x :
		if (serch == cardcolour[k]):
			retvalcol.append(cardname[k])
		k=k+1
	if (retvalcol != ""):
		print("Cards with colour ",serch," = ",retvalcol)
def TypSer(serch):
	k=0
	retvalcol = []
	x = len(cardtype)
	while k < x :
		if (serch.lower() == cardtype[k]):
			retvalcol.append(cardname[k])
		k=k+1
	if (retvalcol != ""):
		print("Cards with type ",serch.lower()," = ",retvalcol)
