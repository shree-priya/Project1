# write a python program for hand cricket
print("welcome to hand cricket game")
import random 
over=int(input("enter a over:"))
ball=over*6
team1_total=0
team2_total=0
print("1:single player mode")
print("2:multi player mode ")
game=int(input("enter a number:"))
if game==1:
 player_name=input("enter a name:")
 total1=0    
 comp=random.randint(1,6)
 choice_user=input("enter a even or odd:")
 user_num=int(input("enter a number for odd or even:"))
 num=user_num+comp
 print("total for odd or even number:",num)
 if num%2==0:
  print("your are batting") 
  while (1,ball):
    comp=random.randint(1,6)
    user=int(input('enter a number:'))
    if (comp==user):
     print("you are out")
     break
    else:
     total1=total1+user
     print("computer entered:",comp)
  print("SCORE of MATCH:",total1)
  print("your are bowling")
  total2=0
  while(1,ball):
    comp=random.randint(1,6)
    user=int(input("enter a number:"))
    if (comp==user):
     print("comp out")
     break
    else:
     total2=total2+comp
     print("comp enter:",comp)
  print("score of match:",total2)
  if total1>total2:
    print("you are won the match by",total1-total2)
  else:
    print("you lose the match by:",total2-total1)
 else:
     total2=0
     if num%2==1:
      while (1,ball):
       comp=random.randint(1,6)
       user=int(input("enter a number:"))
       if (comp==user):
        print("comp is out")
        break
       else:
        total2=total2+comp
        print("comp enter:",comp)
      print("score of match:",total2)
      print("your are batting")
      total1=0
      while(1,ball):
        comp=random.randint(1,6)
        user=int(input("enter a number:"))
        print("Computer entered:",comp)
        if (comp==user):
         print("you are out")
         break
        else:
         total1=total1+user
      print("score of match:",total1)
      if total1>total2:
        print("you won the match by:",total1-total2)
      else:
        print("you lose the match by:",total2-total1)
else:
 if game==2:
  team1_meb=input("enter a name (members team1):")
  team2_meb=input("enter a name (members team2):")
  print("the game participent",team1_meb,team2_meb)
  members1=len(team1_meb)
  members2=len(team2_meb)
  total_members=members1+members2
  print("FIRST MATCH TEAM1(BATING),TEAM2(BOWLING)")
  from getpass import getpass 
  for a in range(members1):
   while (1,ball):
    team1=getpass("enter a number between 1to6(team1)")
    team2=getpass('enter a number between 1to6(team2):')
    print("team1 enter",team1)
    print("team2 enter",team2)
    if (team1==team2):
     print("team1 lost a wicket",team1_total)
     break
    else:
     team1_total=team1 
     print("team1 present total:",team1_total)
    print("team1 score is",team1_total)
  print("SECOND MATCH TEAM1(BOWLING),TEAM2(BATING)")
  from getpass import getpass
  for b in range(members2):
   while(1,ball):
    team1=getpass("enter a number 1to6(team1):")
    team2=getpass("enter a number 1to6(team2):")
    print("team1 enter",team1)
    print("team2 enter",team2)
    if (team1==team2):
      print("team2 lost a wicket",team2_total)
      break
    else:
      team2_total=team2
      print("team2 present total:",team2_total)
    print("team2 score is",team2_total)
print("thanking you for playing this game")     
