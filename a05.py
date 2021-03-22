'''Simple application to compare the average scores of boys and girls
Created by Fernando Ames
2/11/2019'''


name = input("Please enter your name")
print("Hello,", name + ' ' "!!! Welcome to my Fifth Python program!")


bscore = 0
gscore = 0
gtotal = 0
btotal = 0
baverage = 0
gaverage = 0
bcount = 0
gcount = 0

gen = input("Boy(b), Girl(g) or Quit(q): ")

while(gen != "q"):

    if(gen == "b"):
        bscore = int(input("Boy score: "))
        bcount += 1
        btotal = btotal + bscore

    elif(gen == "g"):
        gscore = int(input("Girl score: "))
        gcount += 1
        gtotal = gtotal + gscore

    gen = input("Boy (b), Girl (g) or Quit (q): ")

baverage = btotal/float(bcount)
gaverage = gtotal/float(gcount)

print("Boy average is: ", baverage)
print("Girl average is: ", gaverage)
       

                



