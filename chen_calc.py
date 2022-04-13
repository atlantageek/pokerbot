
card_values={'A':10,'K':8,'Q':7,'J':6,'T':5,'9':4.5,'8':4,'7':3.5,'6':3,'5':2.5,'4':2,'3':1.5,'2':1}

card_order=['A','K','Q','J','T','9','8','7','6','5','4','3','2']

def gap_score(high_card,low_card):
    high_idx=card_order.index(high_card)
    low_idx=card_order.index(low_card)
    if high_idx == low_idx:
        return 0 #pair
    dist=(abs(high_idx-low_idx)-1) * -1
    gap_offset=max(dist,-5)
    gap_bonus = 0
    if high_idx >2 and gap_offset >=-1:
        gap_bonus=1
    return gap_offset+gap_bonus

def chen(high_card,low_card,suited):
    val=card_values[high_card]
    if (high_card == low_card):
        val = val * 2
    gap_bonus=gap_score(high_card,low_card)
    suit_bonus=0
    if suited:
        suit_bonus=2
    return val + gap_bonus + suit_bonus

while True:
    hand=input ("Enter Hand: ")
    first_card=hand[0]
    second_card=hand[1]
    if (first_card == second_card):
        suited=False
    else: 
        suited=hand[2]=='s'

    print(first_card)
    print(second_card)
    print(suited)
    result=chen(first_card,second_card,suited)
    print(result)


