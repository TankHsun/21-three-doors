import random
times= int(input('您要隨機的次數:'))
x = 0
win = 0
lose = 0
while x < times:
	doors = ['car','sheep','sheep']
	random.shuffle(doors)

	#select = random.randint(1, 3) #隨機選門

	select = input('有1~3道門，請選擇一個門:')
	if select != '1' and select != '2' and select != '3':
		print('請輸入1~3')
		break

	del doors[int(select) - 1]
	doors.remove('sheep')
	if doors == ['car']:
		win += 1
	else:
		lose += 1
	x += 1
print('win=', win)
print('lose=', lose)