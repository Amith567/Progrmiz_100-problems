import random as r
num=int(input('enter no of cards you want : '))
card_type=['diamond','clover','heart','leaf']
card_num=[1,2,3,4,5,6,7,8,9,'k','j','q']

for i in range (num):
    print(card_type[r.randint(0,3)],card_num[r.randint(0,11)])
    