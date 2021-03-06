from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate
from chen import Chen

NB_SIMULATION = 1000

class ChenPlayer(BasePokerPlayer):



    def declare_action(self, valid_actions, hole_card, round_state):
        ch=Chen()
        (top_card,bottom_card,suited)=ch.convert_chen(hole_card)
        chen_score = ch.chen_calc(top_card,bottom_card,suited)
        street = round_state['street']
        community_cards = round_state['community_card']
        print('Round State' + str(round_state) + str(community_cards))
        if chen_score > 8 and street == 'preflop':
            action = valid_actions[1]  # fetch CALL action info
        else:
            action = valid_actions[0]  # fetch FOLD action info
        return action['action'], action['amount']

    def receive_game_start_message(self, game_info):
        self.nb_player = game_info['player_num']

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass