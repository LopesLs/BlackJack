#Modules
from random import choice, randint
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from rich.layout import Layout

#Panel Initial
print(Panel('                                                        WELCOME TO MY BLACKJACK GAME', style='purple'))

#Login System, can be... Guest account, Create a new cccount, existent account.
print('[purple]Hello There, You need to login\n')
while True:
    nickname = Prompt.ask("[purple]Type your name for start")
    question = Prompt.ask('\n[purple]Do you want learn roles?(yes/no)').lower().strip()
    if 'yes' in question:
        print('\n[green]IMPORTANT: Blackjack ou Vinte-e-um é um jogo praticado com cartas em casinos e que pode ser jogado com 1 a 8 baralhos de 52 cartas, em que o objetivo é ter mais pontos do que o adversário, mas sem ultrapassar os 21 (caso em que se perde). O dealer só pode pedir até um máximo de 5 cartas ou até chegar ao número 17')
        question = Prompt.ask('\n[purple]Do you read it? ')
        if 'yes' in question:
            print('\n[red]Good Luckk!!!\n')
            break
        else:
            print('\n[red]Why not, idiot!\n')
            break

    else:
        print('\n[red]All right, Good Luck!!!\n')
        break

#Read the docstrings.
def exibition_with_superiorBar():
    """
    Docstring --> This function can be used for print layouts in your screen.
    Paramater --> None.
    Return --> None.
    """
    layout.split_column(
        Layout(name = 'SubSuperiorBar'),
        Layout(name = 'CardsBar'),
        Layout(name = 'InfoBar')
        )
    layout['CardsBar'].split_row(
        Layout(Panel(f'''   

{nickname} (Player)

Cards - [blue]{UserDeck}[/]

Total - [white]{sum(cards_numbers_usr)}  
    ''', style='purple')),
        Layout(Panel(f'''                         
    
CarloS (Dealer)

Cards - [blue][{DealerDeck[0]}, ?][/]

Total - ?''', style='purple'))
)
    layout['SubSuperiorBar'].size = 3
    layout['InfoBar'].size = 3
    layout['InfoBar'].add_split(
        Layout(Panel('K, Q, J = 10 | A = 11', style='purple'))
    )
    layout['SubSuperiorBar'].add_split(
        Layout(Panel('                                                         BlackJack Game With Python', style='purple'))
    )
    print(layout)
def DealerCards(card):
    """
    Docstring --> Basicaly, this function will get the  dealer cards in string format and transfer to int.
    Paramater --> Card, here card is the cards in string format.
    Return --> None.
    """
    global DealerDeck
    global cards_numbers_dlr
    DealerDeck.append(card)
    if '2' in card: cards_numbers_dlr.append(2)
    elif '3' in card: cards_numbers_dlr.append(3)
    elif '4' in card: cards_numbers_dlr.append(4)
    elif '5' in card: cards_numbers_dlr.append(5)
    elif '6' in card: cards_numbers_dlr.append(6)
    elif '7' in card: cards_numbers_dlr.append(7)
    elif '8' in card: cards_numbers_dlr.append(8)
    elif '9' in card: cards_numbers_dlr.append(9)
    elif '10' in card: cards_numbers_dlr.append(10)
    elif 'K' in card: cards_numbers_dlr.append(10)
    elif 'J' in card: cards_numbers_dlr.append(10)
    elif 'Q' in card: cards_numbers_dlr.append(10)
    elif 'A' in card: cards_numbers_dlr.append(11)
    else: pass
def UserCards(card):
    """
    Docstring --> Basicaly, this function will get the user cards in string format and transfer to int.
    Paramater --> Card, here card is the cards in string format.
    Return --> None.
    """
    global UserDeck
    global cards_numbers_usr
    UserDeck.append(card)
    if '2' in card: cards_numbers_usr.append(2)
    elif '3' in card: cards_numbers_usr.append(3)
    elif '4' in card: cards_numbers_usr.append(4)
    elif '5' in card: cards_numbers_usr.append(5)
    elif '6' in card: cards_numbers_usr.append(6)
    elif '7' in card: cards_numbers_usr.append(7)
    elif '8' in card: cards_numbers_usr.append(8)
    elif '9' in card: cards_numbers_usr.append(9)
    elif '10' in card: cards_numbers_usr.append(10)
    elif 'K' in card: cards_numbers_usr.append(10)
    elif 'J' in card: cards_numbers_usr.append(10)
    elif 'Q' in card: cards_numbers_usr.append(10)
    elif 'A' in card: cards_numbers_usr.append(11)
    else: pass

#Cards with string format and beatifull form. They are a list.
cards = [
'♠ 2', '♠ 3', '♠ 4', '♠ 5', '♠ 6', '♠ 7', '♠ 8', '♠ 9', '♠ 10',
'♣ 2', '♣ 3', '♣ 4', '♣ 5', '♣ 6', '♣ 7', '♣ 8', '♣ 9', '♣ 10',
'♥ 2', '♥ 3', '♥ 4', '♥ 5', '♥ 6', '♥ 7', '♥ 8', '♥ 9', '♥ 10',
'♦ 2', '♦ 3', '♦ 4', '♦ 5', '♦ 6', '♦ 7', '♦ 8', '♦ 9', '♦ 10',
'♠ J', '♠ Q', '♠ K', '♠ A', '♣ J', '♣ Q', '♣ K', '♣ A',
'♥ J', '♥ Q', '♥ K', '♥ A','♦ J', '♦ Q', '♦ K', '♦ A'
]

#numbers of cards of user in int format, before pass for function UserCards.
cards_numbers_usr = []

#numbers of cards of dealer in int format, before pass for function DealerCards.
cards_numbers_dlr = []

#UserDeck, number of cards of user in string format for make print beatifull for user.
UserDeck = []

#DealerDeck, number of cards of dealer in string format for make print beatiful for user.
DealerDeck = []

#count, this variable can know which is the turn correct, because she add 1 for each while runned.
count = 0

#Config, config variable is a variable of testing, the dealer only will get cards if this config be true.
config_ = True

#Layout, just made mention because i'll use after.
layout = Layout()

#Stop, is a variable of stopped, if this value was different of 0, the user dont'll get any card.
stop = 0

#This while is very important because is responsable for all the game, get cards, turns, layouts, sums, appends, this while is only basical.
while True:
    count += 1
    if count == 1:
        for User in range(2):
            card = choice(cards)
            UserCards(card)
            cards.remove(card)
        for Dlr in range(2):
            card = choice(cards)
            DealerCards(card)
            cards.remove(card)
    if count % 2 == 0:
        while config_ == True:
            value = sum(cards_numbers_dlr)
            if value > 21:
                layout.split_column(
                    Layout(name = 'SuperiorBar'),
                    Layout(name = 'CardsBar'),
                )
                layout['SuperiorBar'].add_split(
                    Layout(Panel(('                                                     [green]Info: You Win! , The Dealer went over 21 and busted.'), style='green'))
                )
                stop += 1
                break
            elif value == 21:
                layout.split_column(
                    Layout(name = 'SuperiorBar'),
                    Layout(name = 'CardsBar'),
                )
                layout['SuperiorBar'].add_split(
                    Layout(Panel((f'                                                            [red]Info: You lost ):, The Dealer got 21.'), style='red'))
                )
                stop += 1
                break
            elif value < 21:
                number = randint(1, 2)
            if number == 2:
                card = choice(cards)
                DealerCards(card)
                cards.remove(card)
            else:
                config_ = False
        if stop == 1:
            break
        else:
            pass
    else:   
        value = sum(cards_numbers_usr)
        if value > 21:
            layout.split_column(
                Layout(name = 'SuperiorBar'),
                Layout(name = 'CardsBar'),
            )
            layout['SuperiorBar'].add_split(
                Layout(Panel((f'                                                       [red]Info: You lost ); You went over 21 and busted.'), style='red'))
            )

            break
        elif value == 21:
            layout.split_column(
                Layout(name = 'SuperiorBar'),
                Layout(name = 'CardsBar'),
            )
            layout['SuperiorBar'].add_split(
                Layout(Panel(f'                                                              [green]Info: You Won!, You got to 21.', style='green'))
            )
            break
        elif value < 21:
            pass
        exibition_with_superiorBar()
        escolha = int(Prompt.ask('\n1 - [blue]Hit[/]       2 - [green]Stand[/]      3 - [purple]Forfeit: '))
        if escolha == 1:
            card = choice(cards)
            UserCards(card)
            cards.remove(card)
        elif escolha == 2:
            if sum(cards_numbers_dlr) > sum(cards_numbers_usr):
                layout.split_column(
                    Layout(name = 'SuperiorBar'),
                    Layout(name = 'CardsBar'),
                )
                layout['SuperiorBar'].add_split(
                    Layout(Panel(f'                                          [red]Info: You lost ); You stood with a lower score[/] ({sum(cards_numbers_usr)}) [red]than the Dealer[/] ({sum(cards_numbers_dlr)}).', style='red'))
                )
                break
            elif sum(cards_numbers_usr) > sum(cards_numbers_dlr):
                layout.split_column(
                    Layout(name = 'SuperiorBar'),
                    Layout(name = 'CardsBar'),
                )
                layout['SuperiorBar'].add_split(
                    Layout(Panel(f'                                          [green]Info: You Win!, You stood with a higler score[/] ({sum(cards_numbers_usr)}) [green]than the Dealer[/] ({sum(cards_numbers_dlr)}).', style='green'))
                )
                break
            elif sum(cards_numbers_dlr) == sum(cards_numbers_usr):
                layout.split_column(
                    Layout(name = 'SuperiorBar'),
                    Layout(name = 'CardsBar'),
                )
                layout['SuperiorBar'].add_split(
                    Layout(Panel('[yellow]Info: You tied, You tied with the Dealer')))
                break
        elif escolha == 3:
            layout.split_column(
                Layout(name = 'SuperiorBar'),
                Layout(name = 'CardsBar'),
            )
            layout['SuperiorBar'].add_split(
                Layout(Panel(('[red]Info: You ended the game.')))
            )
            break



layout['CardsBar'].split_row(
        Layout(Panel(f'''        


{nickname} (Player)


Cards - [blue]{UserDeck}[/]


Total - [white]{sum(cards_numbers_usr)}  
    ''', style='purple')),
        Layout(Panel(f'''                          
    

CarloS (Dealer)


Cards - [blue]{DealerDeck}[/]


Total - [white]{sum(cards_numbers_dlr)}''', style='purple'))
)
layout['SuperiorBar'].size = 3
print(layout)

#Progam by Carlos Ofc