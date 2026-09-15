
import random
computer =random.choice([-1,0,1])
user=(input("enter your choice : "))

mydict={
  "stone":-1,
  "paper":1,
  "scissor":0
}

reversedict={ -1:"stone",1:"paper",0:"scissor"}
younum=mydict[user]

print(f"you chose {reversedict[younum]}\n computer chose {reversedict[computer]}")

if(younum==computer):
  print("its a draw!")
elif (younum==1 and computer ==-1 ):
  print("congrats u won!")
elif (younum==1 and computer ==0 ):
  print("bad luck try again next time !")

  
elif (younum==0 and computer ==1):
  print("congrats u won!")
elif(younum==0 and computer == -1 ):
  print("bad luck try again next time !")

elif (younum==-1 and computer == 0 ):
  print("congrats u won!")
elif(younum==-1 and computer ==1 ):
  print("bad luck try again next time !")
else:
  print("something went wrong ,please try again")p