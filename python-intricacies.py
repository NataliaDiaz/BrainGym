import random

deck = range(1, 52)

# Removing elements by value in lists

card_id = int(random.sample(deck, 1)[0]) # n_cards
print "before removing ", card_id, ":",deck
deck = deck.remove(card_id)
print 'after', deck
print "Learning: remove(item_to_remove) works in-place, no need to assign!"

card_id = int(random.sample(deck, 1)[0]) # n_cards
print "before removing ", card_id, ":",deck
deck.remove(card_id)
print 'after', deck
