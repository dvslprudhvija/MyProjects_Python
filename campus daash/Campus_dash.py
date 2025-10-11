import random
from art import header
print(header)
print("WELCOME!! Are you ready for the day?")
friends =0
timeline=30
crashed = False
reached=False
while reached!=True and crashed!=True and timeline>0:
    route1=int(input("Which way are you taking to campus? 1.Through the Main Road 2.Through the Shortcut 3.Through the highway "))
    if route1==1:
        print("You have chosen to go through the Main Road")
        traffic=int(input("There is a traffic jam ahead. Do you want to wait or take a detour? 1.Wait 2.Detour "))
        if traffic==1:
            timeline-=10
            print("You waited in traffic and lost 10 minutes")
        else:
            timeline-=3
            print("You took a detour and lost 3 minutes")
        print("You see a Yellow Light")
        light=int(input("Do you want to stop or go? 1.Stop 2.Speed up "))
        if light==1:
            timeline-=5
            print("You stopped at the light and lost 5 minutes")
        else:
            timeline+=2
            print("You went through the yellow light and gained 2 minutes")
        if timeline>0:
            reached=True
            print("You have reached your campus safely!")
        else:
            reachesd=False
            print("You ran out of time and couldn't reach your campus.")

        

    elif route1==2:
        print("You have chosen to go through the Shortcut")
        obstacle=int(input("You encounter a construction site. Do you want to go through it or take a longer route? 1.Go through 2.Long route "))
        if obstacle==1:
            timeline-=10
            print("You went through the construction site and lost 7 minutes")
        else:
            timeline-=12
            print("You took the longer route and lost 12 minutes")
            print("Your friend is on the way to campus too")
        pickup_friend=int(input("Do you want to pick him up? 1.Pick up 2.Ignore "))
        if pickup_friend==1:
            friends+=1
            timeline-=5
            print("You met your friends and lost 5 minutes")
            friend_late=int(input("Your friend is late. Do you want to wait or leave? 1.Wait 2.Leave "))
            if friend_late==1:
                timeline-=5
                print("You waited for your friend and lost 5 minutes")
            else:
                timeline+=5
                friends-=1
                print("You chose not to wait for your friend and saved 5 minutes")
        else:
            print("You chose not to meet your friends and saved 5 minutes")
        if timeline>0 :
            reached=True
            if friends>0:
                print(f"Perfect !! You guys made it to Campus in time with {friends} friends")
            else:
                print("Perfect !! You made it to Campus in time")
        else:
            reachesd=False
            print("You ran out of time and couldn't reach your campus.")
        


    else:
        print("You have choosen to go through the Highway")
        speed=int(input("The highway is clear. Do you want to speed up or maintain speed? 1.Speed up 2.Maintain speed "))
        if speed==1:
            timeline+=5
            print("You sped up and gained 5 minutes")
        else:
            timeline-=2
            print("You maintained speed and lost 2 minutes")
        cow_cross=int(input("You see a cow crossing the highway. Do you want to stop or swerve? 1.Stop 2.Swerve "))
        if cow_cross==1:
            timeline-=6
            print("You stopped for the cow and lost 6 minutes")
        else:
            crash_chance=random.randint(1,10)
            if crash_chance<=3:
                crashed=True
                print("You swerved and crashed into a tree. Game Over.")
            else:
                timeline+=3
                print("You swerved successfully and gained 3 minutes")
        if timeline>0 and crashed!=True:
            reached=True
            print("You have reached your campus safely!")
        elif crashed!=True and timeline<=0:
            reachesd=False
            print("You ran out of time and couldn't reach your campus.")


