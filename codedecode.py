import random
key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
       'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
       'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = input("This code maker only works for a single word message!!!\nEnter the word: \n")
wor = list(word)
if (len(wor) > 3):
    first = wor[0]
    wor.remove(first)
    wor.append(first)
    for R in range(0, 3):
        wor.append(random.choice(key))
        wor.insert(0,random.choice(key))
    final = ("".join(wor))
    print(final)
else:
    wor.reverse()
    final = ("".join(wor))
    print(final)

dec = list(final)


decode = input("Do you want the code decoded for yes press: y for no press: n: \n")
if (decode == "n"):
    print("Thanks the program is over !!!")
elif (decode == "y"):
    if (len(dec) > 3):
        for e in range (0,3):
          e = dec[-1]
          dec.remove(e)
        for s in range(0,3):
          s = dec[0]
          dec.remove(s)
        last = dec[-1]
        dec.remove(last)
        dec.insert(0, last)

        fin = ("".join(dec))
        print(fin)
    else:
        dec.reverse()
        fin = ("".join(dec))
        print(fin)
else:
    print("Thanks the program is over !!!!!")