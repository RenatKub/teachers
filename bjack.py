import random
suits=('Черва','Буба','Пика','Крест')
ranks=('две','три','четыре','пять','шесть','семь','восемь','девять','десять',
'Валет','Королева','Король','Туз')
values={'две':2, 'три':3, 'четыре':4, 'пять':5, 'шесть':6, 'семь':7, 'восемь':8,
'девять':9, 'десять':10, 'Валет':10, 'Королева':10, 'Король':10, 'Туз':11,}
playing=True

class card():
  def __init__(self,suit,rank):
    self.suit=suit
    self.rank=rank

def __str__(self):
  return self.rank+" из "+self.suit

class deck():
  def __init__(self):
    self.deck=[]
    for suit in suits:
      for rank in ranks:
        self.deck.append(card(suit, rank))
  def __str__(self):
    deck_comp=''
    for card in self.deck:
      deck_comp+='\n'+card.__str__()
    return("В колоде находятся: "+deck_comp)
  def shuffle(self):
    random.shuffle(self.deck)
  def deal(self):
    single_card=self.deck.pop()
    return single_card