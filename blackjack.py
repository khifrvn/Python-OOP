
import random, sys

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is 'â™¥'.
DIAMONDS = chr(9830) # Character 9830 is 'â™¦'.
SPADES   = chr(9824) # Character 9824 is 'â™ '.
CLUBS    = chr(9827) # Character 9827 is 'â™£'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

# main program
def main():
    print('''Blackjack, tqtq al sweigart

    Rules:
      Cobalah untuk mendekati 21 tanpa melampaui batas.
      Kings, Queens, dan Jacks bernilai 10 poin.
      As bernilai 1 atau 11 poin.
      Kartu 2 hingga 10 sebanding dengan nilai nominalnya.
      (H) untuk mengambil kartu lain.
      (S) untuk berhenti mengambil kartu.
      Pada permainan pertama Anda, Anda dapat (D) turun untuk meningkatkan taruhan Anda
      tetapi harus memukul tepat sekali lagi sebelum berdiri.
      Jika terjadi seri, taruhan dikembalikan ke pemain.
      Dealer berhenti memukul pukul 17.\n''')

    print("======Blackjack=======\n")

    money = 5000
    while True:  # Main game loop.
        # Check jika player uangnya abis:
        if money <= 0:
            print("POKE LU!")
            print("Untung bukan uang asli!")
            print('Makasi udah main!')
            sys.exit()

        # Player taruhan untuk round pertama:
        print('Uang:', money)
        bet = getBet(money)

        # Berikan player dan dealer 2 kartu:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Player actions:
        print('Taruhan:', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            # check jika player punya bust:
            if getHandValue(playerHand) > 21:
                break

            # Player move, antara H, S, or D:
            # player moving
            move = getMove(playerHand, money - bet)

            # Handle untuk player actions:
            if move == 'D':
                # Player jika doubling down, mereka gabisa nambah bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Taruhan bertambah ke {}.'.format(bet))
                print('Taruhan:', bet)

            if move in ('H', 'D'):
                # Hit/doubling ambil kartu lain.
                newCard = deck.pop()
                rank, suit = newCard
                print('Kamu dapat a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # Player dapet busted:
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops giliran player.
                break

        # Dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # Dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # Dealer busted.
                input('Tekan enter untuk melanjutkan...')
                print('\n\n')

        # Final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue > 21:
            print('Dealer busts! Kamu menang ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('Kamu kalah!')
            money -= bet
        elif playerValue > dealerValue:
            print('Kamu menang ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('Imbang, bet dikembalikan.')

        input('Tekan enter untuk melanjutkan...')
        print('\n\n')


def getBet(maxBet):
    """Tanya player di round ini mau bet berapa"""
    while True:  # Keep asking until they enter a valid amount.
        print('Isi taruhan/bet? (1-{}, atau KELUAR)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'KELUAR':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue  # jika player tidak memasuki nomer

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # Player mengisi bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]  # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):  # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank)  # Numbered cards are worth their number.

    # Add the value for the aces:
    value += numberOfAces  # Add 1 per ace.
    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so:
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    rows = ['', '', '', '', '']  # The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Print the top line of the card.
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card  # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:  # Keep looping until the player enters a correct move.
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move  # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move  # Player has entered a valid move.


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
