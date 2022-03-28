from cProfile import label
from otree.api import *
import random

doc = """
In today's experiment, two randomly chosen participants will form a 2-person group to work on a joint project. In each group, there will be two roles A and B. A and B will make their decisions independently. However, their decisions will determine not only their own but also each other's payoff from the joint project. Pairs are independent, so whatever happens in one pair will not affect any other pair in any way.
There will be multiple rounds in the experiment, and each round will proceed in the same way. For two participants, they will NOT be in the same group for more than one round. In each round, both A and B will receive XX tokens (10 tokens = S$1). They will both decide 1) whether to carry out the joint project; and 2) how much to invest in the joint project. All the decisions and answers are recorded on the decision sheet.
"""


class C(BaseConstants):
    NAME_IN_URL = 'experiment2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 19
    INSTRUCTIONS_TEMPLATE = 'experiment/instructions.html'
    INSTRUCTION_TEMPLATE = 'experiment/instruction.html'
    # Initial amount allocated to each player
    ENDOWMENT = cu(100)
    MULTIPLIER = 1.2
    BONUS_PAYOFF = cu(50)

    A_ROLE = 'A'
    B_ROLE = 'B'

class Subsession(BaseSubsession):
    #group and types are defined in the Subsession class
    def creating_session(self):
    #to set initial values in the subsession
        self.group_randomly(fixed_id_in_group=False)
        #group_randomly() -> built-in function that  shuffles players
        rdm=random.randint(0, 1)
       
        # assign a random value, either 0 or 1, to variable rdm
        for g in self.get_groups():
        #get_groups() -> returns a list of all the groups in the subsession.
        # loop through the groups in the subsession
            for p in g.get_players():
            # get_players() -> returns a list of all the players in the subsession.
            # loop through the players in the subsession (p is a player)
#***************************************************************************
# matching and types when random is 1 - > even = B, odd= A
#***************************************************************************
                if rdm==0:
                # the following code is executed if rdm is 1
                    p.id._in_group  = 1
                    # id_in_group -> player's attribute (unique identifier)
                    # if the id is even (via modulo operator)
                    p.participant.vars['type'] = 'B'
                        # the participant is assigned to type "B"
                        # participant.vars is a dictionary that can store any data.
                        # information stored participant.vars persists across apps
                        # this piece of information is not saved in the data exported, do not store here info you need for your analysis
                    
                    # if the participant id is odd
                    # p.participant.vars['type'] = 'A'
                        # the participant is assigned to type "A"
                    p.type = p.participant.vars['type']
                    # "copy" the value to variable "type" in players space
                    # the variable type must be defined in class Player (see below)
#***************************************************************************
# matching and types when random is 1 - > even = A, odd= B
#***************************************************************************
                else:
                # the following code is executed if rdm is 0
                    p.id_in_group  = 2
                    # see comment above
                    p.participant.vars['type'] = 'A'
                        # see comment above
                    
                    # see comment above
                    # p.participant.vars['type'] = 'B'
                        # see comment above
                p.type = p.participant.vars['type']



    #  def creating_session(self):
    #      self.group_randomly() # The method with the argument, group_randomly(fixed_id_in_group=True) shuffles players in a way that each player is in the same id as before.¶



        #  print("== Round " , self.round_number, " == ")
        #  print("  Matching: ", self.get_group_matrix())


        # for p in self.get_players():
        #     p.random_value = random.random() # Returns a value between 0 and 1
# for p in get_players():
#     p.random_value = random.random()


class Group(BaseGroup):
    # Write the message to be sent fro A to B.
        # Define a method to determine guesses.
    sent_message = models.StringField(
        label = "A has sent you the following message: "
    )
    write_message = models.StringField(
        label = "Write down the message you picked."
    )
    write_words = models.StringField(
        label = "You will receive 70% of the revenue and I will receive 30% of the revenue."
    )
    choose_message = models.IntegerField(
        choices=[[1, 'Yes'],[2, 'No']],
        widget=widgets.RadioSelect,
    )
    guess_investment = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Enter an amount from 0 to 100:",
    )
    guess_investment_b = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Enter an amount from 0 to 100:",
    )
    investment_amount = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Enter an investment amount from 0 to 100:",
    )
    investment_amount_b = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Enter an investment amount from 0 to 100:",
    )
    confident_b = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )

    

class Player(BasePlayer):
    type = models.StringField()# this is a string variable that will be filled with player's type (see above)

    # rand_number = models.IntegerField(random.random())
    # random_number = round(random.uniform(0, 1), 1)
    # rand_number = models.IntegerField(random.random())
    # print(random_number)


    # def role(self):
    #     if self.random_number > 0.5:
    #         return 'A'
    #     if self.id_in_group <= 0.5:
    #         return 'B'
    

    # def role(self):
    #     if self.id_in_group == 2:
    #         return 'A'
    #     if self.id_in_group == 1:
    #         return 'B'
        

    message_list = models.IntegerField(
        choices = [[1, 'Hi'], [2, 'No']],
        # widget=widgets.RadioSelect,
        label="I choose:",
    )
    

    choose_message = models.IntegerField(
        choices=[[1, 'Yes'],[2, 'No']],
        widget=widgets.RadioSelect,
        label="Will you choose the message you selected?",
    
    )
    

    most_popular_message = models.IntegerField(
        choices=[[1, 'Hi'],[2, 'No']],
        widget=widgets.RadioSelect,
        label="The most popular message is:",
    )
    # is_player = models.BooleanField()
    
# FUNCTIONS
# def creating_session(subsession: Subsession):
#     session = subsession.session
#     import random

#     if subsession.round_number == 1:
#         paying_round = random.randint(1, C.NUM_ROUNDS)
#         session.vars['paying_round'] = paying_round
#     if subsession.round_number == 3:
#         # reverse the roles
#         matrix = subsession.get_group_matrix()
#         for row in matrix:
#             row.reverse()
#         subsession.set_group_matrix(matrix)
#     if subsession.round_number > 3:
#         subsession.group_like_round(3)
# Group players randomly each round
# def creating_session(subsession):
#     subsession.group_randomly()

# Assign random id 
# def creating_session(subsession):
#     subsession.group_randomly(fixed_id_in_group=False)

# def set_payoffs(group: Group):
#     subsession = group.subsession
#     session = group.session

#     p1 = group.get_player_by_id(1)
#     p2 = group.get_player_by_id(2)
#     for p in [p1, p2]:
#         is_matcher = p.role == C.A_ROLE
#         p.is_player = (p1.message_list == p2.message_list) == is_matcher
#         if subsession.round_number == session.vars and p.is_player:
#             p.payoff = C.STAKES
#         else:
#             p.payoff = cu(0)

def set_payoffs(group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = C.BONUS_PAYOFF
    p2.payoff = C.BONUS_PAYOFF

# PAGES
class Introduction(Page):
    pass

class ListMessage(Page):
    form_model = 'player'
    form_fields = ['message_list']

    # @staticmethod
    # def error_message(player, values):
    #     print('values is', values)
    #     if values['message_list'] == message_list:
    #         return 'The messages must be similar.'
    
    
class PopularMessage(Page):
    form_model = 'player'
    form_fields = ['most_popular_message']

class Choice(Page):
    form_model = 'group'
    form_fields = ['write_message']
    # , 'write_words'

    

    # @staticmethod
    # def get_form_fields(player):
    #     if player.id_in_group == 1:
    #         return ['write_message']
    #     else:
    #         return ['']

    # This page is only shown to player 1.
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

    @staticmethod
    def vars_for_template(player: Player):
        return dict(player_in_previous_rounds=player.in_previous_rounds())


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    


class Results(Page):
    # @staticmethod
    # def vars_for_template(player):
    #     group = player.group

    #     return dict(
    #         total_revenue = group.investment_amount * C.MULTIPLIER
    #     )
    pass

class ChooseMessage(Page):
    form_model = 'group'
    form_fields = ['write_words']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1
    
class PickedMessage(Page):
    form_model = 'player'
    form_fields = ['choose_message']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

class SecondChoice(Page):


    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2

class SentMessage(Page):
    form_model = 'group'
    form_fields = ['choose_message']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2

class GuessA(Page):
    form_model = 'group'
    form_fields = ['guess_investment']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

class GuessB(Page):
    form_model = 'group'
    form_fields = ['guess_investment_b']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2


class InvestmentA(Page):
    form_model = 'group'
    form_fields = ['investment_amount']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

class InvestmentB(Page):
    form_model = 'group'
    form_fields = ['investment_amount_b']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2
    

class ChoiceAConfidence(Page):
    form_model = 'group'
    form_fields =['confident']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

class ChoiceBConfidence(Page):
    form_model = 'group'
    form_fields = ['confident_b']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2


page_sequence = [
    Introduction, 
    ListMessage, 
    ResultsWaitPage,
    PopularMessage,
    ResultsWaitPage,
    Choice,
    ResultsWaitPage,
    PickedMessage,
    ResultsWaitPage,
    ChooseMessage,
    ResultsWaitPage,
    SecondChoice,
    ResultsWaitPage,
    SentMessage,
    ResultsWaitPage,
    GuessA,
    ResultsWaitPage,
    GuessB,
    ResultsWaitPage,
    ChoiceAConfidence,
    ResultsWaitPage,
    ChoiceBConfidence,
    ResultsWaitPage,
    InvestmentA,
    ResultsWaitPage,
    InvestmentB,
    ResultsWaitPage,

    
    
    
]


# from otree.api import *




# doc = """
# This is a standard 2-player trust game where the amount sent by player 1 gets
# tripled. The trust game was first proposed by
# <a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
#     Berg, Dickhaut, and McCabe (1995)
# </a>.
# """


# class C(BaseConstants):
#     NAME_IN_URL = 'trust'
#     PLAYERS_PER_GROUP = 2
#     NUM_ROUNDS = 1
#     INSTRUCTIONS_TEMPLATE = 'trust/instructions.html'
#     # Initial amount allocated to each player
#     ENDOWMENT = cu(100)
#     MULTIPLIER = 3


# class Subsession(BaseSubsession):
#     pass


# class Group(BaseGroup):
#     sent_amount = models.CurrencyField(
#         min=0,
#         max=C.ENDOWMENT,
#         doc="""Amount sent by P1""",
#         label="Please enter an amount from 0 to 100:",
#     )
#     sent_back_amount = models.CurrencyField(doc="""Amount sent back by P2""", min=cu(0))


# class Player(BasePlayer):
#     pass


# # FUNCTIONS
# def sent_back_amount_max(group: Group):
#     return group.sent_amount * C.MULTIPLIER


# def set_payoffs(group: Group):
#     p1 = group.get_player_by_id(1)
#     p2 = group.get_player_by_id(2)
#     p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
#     p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount


# # PAGES
# class Introduction(Page):
#     pass


# class Send(Page):
#     """This page is only for P1
#     P1 sends amount (all, some, or none) to P2
#     This amount is tripled by experimenter,
#     i.e if sent amount by P1 is 5, amount received by P2 is 15"""

#     form_model = 'group'
#     form_fields = ['sent_amount']

#     @staticmethod
#     def is_displayed(player: Player):
#         return player.id_in_group == 1


# class SendBackWaitPage(WaitPage):
#     pass


# class SendBack(Page):
#     """This page is only for P2
#     P2 sends back some amount (of the tripled amount received) to P1"""

#     form_model = 'group'
#     form_fields = ['sent_back_amount']

#     @staticmethod
#     def is_displayed(player: Player):
#         return player.id_in_group == 2

#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group

#         tripled_amount = group.sent_amount * C.MULTIPLIER
#         return dict(tripled_amount=tripled_amount)


# class ResultsWaitPage(WaitPage):
#     after_all_players_arrive = set_payoffs


# class Results(Page):
#     """This page displays the earnings of each player"""

#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group

#         return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


# page_sequence = [
#     Introduction,
#     Send,
#     SendBackWaitPage,
#     SendBack,
#     ResultsWaitPage,
#     Results,
# ]
