import random

def playrpc(): 
    #take input
    computer_make=random.choice(['r', 'p', 's'])
    user=input(' choose (r) for rock , (p) for scissor, (s) for scissor: ').lower()
    #compare those input
    if(computer_make==user):
        print('ohh its a tie')
        return 0
    if computer_make=='r' and user=='p' or computer_make=='p' and user=='s' or computer_make=='s' and user=='r':
        print(f"user made {user} and computer make {computer_make} user wins")
        return 'user'
    if computer_make=='p' and user=='r' or computer_make=='s' and user=='p' or  computer_make=='r' and user=='s':
        print(f"user made {user} and computer make {computer_make} computer wins")
        return 'computer'
        
    
computer=user=0
max_score=input('how many points u want to play to take a win: ')
while computer!=max_score or user!=max_score: 
    out=playrpc()
    print(out)
    if(out=="computer"):
        computer=computer+1
    if(out=="user"):
        user=user+1
if user==5: 
    print('game ends user wins')
if computer==5:
    print('game ends computer wins')
# out=playrpc()
# print(out)