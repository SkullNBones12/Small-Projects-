import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

turns = 0


player_wins = 0
computer_wins = 0

while True:
	print('Best of 3, 5, or 7 games?')
	turns = int(input())
	if turns == 3 or turns == 5 or turns == 7:
		break
	continue

necessary_wins = int(turns/2) + 1	
	

while True:
	print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
	
	
	
	while True:
		print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
		playerMove = input()
		if playerMove == 'q':
			sys.exit()
		if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
			break
		print('Type one of r , p , s, or q')
	
		if playerMove == 'r':
			print('ROCK versus...')
		if playerMove == 'p':
			print('PAPER versus...')
		if playerMove == 's':
			print('SCISSORS versus...')
		


	randomNumber = random.randint(1, 3)
	if randomNumber == 1:
		computerMove = 'r'
		print('ROCK')
	elif randomNumber == 2:
		computerMove = 'p'
		print('PAPER')
	elif randomNumber == 3:
		computerMove = 's'
		print('SCISSORS')

	if playerMove == computerMove:
		print('It is a tie!')
		ties = ties + 1
	elif playerMove == 'r' and computerMove == 's':
		print('You win!')
		wins = wins + 1
	elif playerMove == 'p' and computerMove == 'r':
		print('You win!')
		wins = wins + 1
	elif playerMove == 's' and computerMove == 'p':
		print('You win!')
		wins = wins + 1
	elif computerMove == 'r' and playerMove == 's':
		print('You lost!')
		losses = losses + 1
	elif computerMove == 'p' and playerMove == 'r':
		print('You lost!')
		losses = losses + 1
	elif computerMove == 's' and playerMove == 'p':
		print('You lost!')
		losses = losses + 1
	
	if wins == necessary_wins or losses == necessary_wins:
        	break

