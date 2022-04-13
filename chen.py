import random
import math

class Chen:
    card_values={'A':10,'K':8,'Q':7,'J':6,'T':5,'9':4.5,'8':4,'7':3.5,'6':3,'5':2.5,'4':2,'3':1.5,'2':1}

    card_order=['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    gap_lookup=[0,0,-1,-2,-4,-5]

    def gap_score(self,high_card,low_card):
        high_idx=self.card_order.index(high_card)
        low_idx=self.card_order.index(low_card)
        if high_idx == low_idx:
            return 0 #pair
        dist=abs(high_idx-low_idx)
        gap_offset=min(dist,5)
        gap_bonus = 0
        if high_idx >2 and gap_offset <=2:
            gap_bonus=1
        return self.gap_lookup[gap_offset]+gap_bonus

    def chen_calc(self,high_card,low_card,suited):
        val=self.card_values[high_card]
        if (high_card == low_card):
            val = val * 2
            return val
        gap_bonus=self.gap_score(high_card,low_card)
        suit_bonus=0
        if suited:
            suit_bonus=2
        return math.ceil(val + gap_bonus + suit_bonus)

    def convert_chen(self,hole_cards):
        suited=hole_cards[0][0]==hole_cards[1][0]
        c1=hole_cards[0][1]
        c2=hole_cards[1][1]
        if self.card_order.index(c2) < self.card_order.index(c1):
            return (c2,c1,suited)
        else:
            return(c1,c2,suited)
        
    # def calculator(self):
    #     while True:
    #         hand=input ("Enter Hand: ")
    #         first_card=hand[0]
    #         second_card=hand[1]
    #         if (first_card == second_card):
    #             suited=False
    #         else: 
    #             suited=hand[2]=='s'
        
    #         print(first_card)
    #         print(second_card)
    #         print(suited)
    #         result=chen(first_card,second_card,suited)
    #         print(result)

def generate_hand():
    a=random.randint(0,12) 
    b=random.randint(0,12) 
    c=random.randint(0,1) 
    hand='' 

    if b<a: 
        hand=ch.card_order[b]+ch.card_order[a] 
    else:
        hand=ch.card_order[a]+ch.card_order[b] 
    if c==1: 
        hand=hand+'s' 
    else: 
        hand=hand+'o'
    return hand


def flash_cards():
    passes=0
    fails=0
    cn=Chen()
    while True:
        hand=generate_hand()
        my_chen=input("score "+hand+": ")
        calc_chen=ch.chen_calc(hand[0],hand[1],hand[2]=='s')
        if (int(calc_chen)==int(my_chen)):
            passes+=1
            print("RIGHT!")
        else:
            fails+=1
            print("Wrong! should have been: " + str(calc_chen))
        print("Current_score:"+str(passes) + " / " + str(passes + fails)) 

#calculator()
if __name__ == "__main__":
    ch=Chen()
    hole_cards=['DK','CA']
    converted=ch.convert_chen(hole_cards)
    print(converted)
    value=ch.chen_calc(converted[0],converted[1],converted[2])
    print(value)
    # ch=Chen()
    # flash_cards()
