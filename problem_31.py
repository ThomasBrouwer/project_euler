def greedy_fill(coin,money_left,stack):
	while coin <= money_left:
		stack.append(coin)
		money_left -= coin
	return money_left

def coins_lower_than(coins,value):
	return [coin for coin in coins if coin < value]

coins = [1,2,5,10,20,50,100,200]

coins_left = coins[:]
stack = []
money_left = 200
number_ways = 0
while True:
	if money_left == 0:
		number_ways += 1
		coin_popped = stack.pop()
		money_left += coin_popped
	else:
		if not coins_left:
			if not stack:
				break
			else:
				coin_popped = stack.pop()
				money_left += coin_popped
				coins_left = coins_lower_than(coins,coin_popped)
		else:
			coin = coins_left.pop()
			money_left = greedy_fill(coin,money_left,stack)

print number_ways