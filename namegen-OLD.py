import random
from random import randint
import math
# first we need to import the random shit that let's us generate random things

#now we're going to ask the user for some inputs and define a few things
times = input('How many Cities? ')
citySize = input('input city size. 1-7. put 0 for random. ')

#this makes the size of the cities they want to generate an integer so we can use it
k = int(citySize)


for i in range(0,int(times)):

	if k == 1:
		j = random.randint(40,200)
		foo2 = ['VILLE', ' THORP' , 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
		secondPart = random.choice(foo2)
	elif k == 2:
		j = random.randint(200,500)
		foo2 = [' TOWN', 'VILLE', ' THORP' , 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
		secondPart = random.choice(foo2)
	elif k == 3:
		j = random.randint(500,1000)
		foo2 = [' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
		secondPart = random.choice(foo2)
	elif k == 4:
		j = random.randint(1000,5000)
		foo2 = [' CITY', ' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
		secondPart = random.choice(foo2)
	elif k == 5:
		j = random.randint(5000,10000)
		foo2 = [' CITY', ' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
		secondPart = random.choice(foo2)
	elif k == 6:
		j = random.randint(10000,75000)
		foo2 = [' CITY', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
		secondPart = random.choice(foo2)
	elif k == 7:
		j = random.randint(75000,160000)
		foo2 = [' CITY', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
		secondPart = random.choice(foo2)
	else:
		k0 = random.randint(1,7)
		if k0 == 1:
			j = random.randint(40,200)
			foo2 = ['VILLE', ' THORP' , 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
			secondPart = random.choice(foo2)
		elif k0 == 2:
			j = random.randint(200,500)
			foo2 = [' TOWN', 'VILLE', ' THORP' , 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
			secondPart = random.choice(foo2)
		elif k0 == 3:
			j = random.randint(500,1000)
			foo2 = [' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
			secondPart = random.choice(foo2)
		elif k0 == 4:
			j = random.randint(1000,5000)
			foo2 = [' CITY', ' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
			secondPart = random.choice(foo2)
		elif k0 == 5:
			j = random.randint(5000,10000)
			foo2 = [' CITY', ' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
			secondPart = random.choice(foo2)
		elif k0 == 6:
			j = random.randint(10000,75000)
			foo2 = [' CITY', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
			secondPart = random.choice(foo2)
		elif k0 == 7:
			j = random.randint(75000,160000)
			foo2 = [' CITY', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
			secondPart = random.choice(foo2)
		else:
			j = random.randint(40,160000)
			foo2 = [' CITY', ' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
			secondPart = random.choice(foo2)
	#this generates a random population
	# this is the part where we generate a name based on word parts instead of letters
	x = random.randint(1,5)
	#similar to above, this determines how long the name will be. 20% of the time the name will have 4 parts instead of 3 and a 20% for a two part
	foo1 = ['AGHA', 'ARD' ,'ATH', 'BALLY', 'BELLA', 'BANE', 'BEGG', 'BELL', 'BEL', 'BEN', 'BIN', 'BOY', 'BRACK', 'BUN', 'CASHEL', 
	'CAPPAGH', 'CARN', 'CARROW', 'CARRY', 'CARRIG', 'CARRACK', 'CRAI', 'CAHIR', 'CLARE', 'CLOGH', 'CLON', 'COM', 'COR', 'CORRY',
	 'CROUGH', 'CUL', 'BREAK', 'DERRY', 'DONAGH', 'DROHID', 'DROGHED', 'DRUM', 'DUFF', 'DUN', 'DOON', 'ENIS', 'ESK', 'FINN', 'FIN',
 	 'FREAGH', 'FRACK', 'GARF', 'GLASS', 'GLEN', 'GLAN', 'GORM', 'GORT', 'ILIAN', 'INISH', 'KIN', 'KNOCK', 'LEA', 'LETTER', 'LIS', 
	  'LOUGH', 'LURGAN', 'MAUM', 'MAY', 'MONA', 'MULLA', 'MORE', 'POLL', 'PORT', 'RATH', 'ROE', 'ROS', 'RUS', 'SALL', 'SHAN', 
	  'SHESKIN', 'SKE', 'STRA', 'SLIEVE', 'TERMON', 'TYR', 'TUBBER', 'TRA', 'TAUM', 'TULLY', 'URLAR',
	  'AR', 'ART', 'ARK', 'JONS', 'SOT', 'ICE', 'WIND', 'SHINING', 'GLEAM', 'GLEAMING', 'RED', 'JAMES', 'ERIK', 'BOST', 'BOULDER', 'RAPIDS',
	  'CLIFF', 'BREAK']

	zerothPart = random.choice(foo1)
	firstPart = random.choice(foo1)
	#the generator always generates 2 variables but can choose to only use some
	if x == 1:
		name = firstPart + secondPart
	else:
		name = zerothPart + firstPart + secondPart

	# this part of the code lays out what random aspects a city could have
	foo3 = ['The city grew up around a coastal harbor.', 'The city grew up around a calm, coastal bay.', 'The city grew up around a large freshwater lake.', 'The city grew up around a wide navigable river.', 'The city grew up around a river navigable by small craft.', 'The city grew up around where two rivers met.', 'The city grew up around a river delta.', 'The city grew up around a series of natural springs.', 'The city grew up around a well traveled crossroads.', 'The city grew up around a water source on a well traveled road.']
	foo4 = ['The city is near a region known for its prominent amounts of iron ore.', 'The city is near a region known for its prominent amounts of copper ore.', 'The city is near a region known for its prominent amounts of gold.', 'The city is near a region known for its prominent amounts of silver.', 'The city is near a region known for its prominent amounts of platinum.', 'The city is near a region known for its prominent amounts of electrum.', 'The city is near a region known for its prominent amounts of tin.', 'The city is near a region known for its prominent amounts of spices.', 'The city is near a region known for its prominent amounts of clay.', 'The city is near a region known for its prominent amounts of granite.', 'The city is near a region known for its prominent amounts of quarts.', 'The city is near a region known for its prominent amounts of salt.', 'The city is near a region known for its prominent amounts of peat.', 'The city is near a region known for its prominent amounts of bituminous coal.', 'The city is near a region known for its prominent amounts of anthracite coal.', 'The city is near a region known for its prominent amounts of pine trees.', 'The city is near a region known for its prominent amounts of oak trees.', 'The city is near a region known for its prominent amounts of birch trees.', 'The city is near a region known for its prominent amounts of hardwood lumber.', 'The city is near a region known for its prominent amounts of barley.', 'The city is near a region known for its prominent amounts of oats.', 'The city is near a region known for its prominent amounts of beans.', 'The city is near a region known for its prominent amounts of corn.', 'The city is near a region known for its prominent amounts of squash.', 'The city is near a region known for its prominent amounts of nuts.', 'The city is near a region known for its prominent amounts of olives.', 'The city is near a region known for its prominent amounts of rice.', 'The city is near a region known for its prominent amounts of wheat.', 'The city is near a region known for its prominent amounts of potatoes.', 'The city is near a region known for its prominent amounts of leaks.', 'The city is near a region known for its prominent amounts of sugar cane.', 'The city is near a region known for its prominent amounts of tobacco.', 'The city is near a region known for its prominent amounts of cotton.', 'The city is near a region known for its prominent amounts of grapes.', 'The city is near a region known for its prominent amounts of apples.', 'The city is near a region known for its prominent amounts of citrus fruits.', 'The city is near a region known for its prominent amounts of pears.', 'The city is near a region known for its prominent amounts of plums.', 'The city is near a region known for its prominent amounts of peaches.', 'The city is near a region known for its prominent amounts of fruit trees.', 'The city is near a region known for its prominent amounts of berries.', 'The city is near a region known for its prominent amounts of cabbage.', 'The city is near a region known for its prominent amounts of beets.', 'The city is near a region known for its prominent amounts of cattle.', 'The city is near a region known for its prominent amounts of sheep.', 'The city is near a region known for its prominent amounts of dairy cows']
	foo5 = ['The city is known for it architectural style.', 'The city is known for it architectural feats.', 'The city is known for it artists and poets.', 'The city is known for it cuisine.', 'The city is known for it suggestive dancing.', 'The city is known for it gladitorial games.', 'The city is known for it horse races.', 'The city is known for it scholars.', 'The city is known for it sages.', 'The city is known for it music.', 'The city is known for it romance.', 'The city is known for it jousting.', 'The city is known for it superior soldiers.', 'The city is known for it street festivals.', 'The city is known for it religious feasts.', 'The city is known for it reiligous fervor.', 'The city is known for it traditional dress.', 'The city is known for it theater.', 'The city is known for it wine.', 'The city is known for it ale']
	foo6 = ['The city is ruled by the head of a noble family.', 'The city is ruled by a concil of distinguished nobles.', 'The city is ruled by a council of wealthy merchants.', 'The city is ruled by a council of elected officials.', 'The city is ruled by an elected mayor.', 'The city is ruled by a benevolent sovereign.', 'The city is ruled by a wicked tyrant.', 'The city is ruled by a brutal warlord.', 'The city is ruled by a cabal of witches and wizards.', 'The city is ruled by the leaders of a religious order']
	foo7 = ['The city has experienced mass conversions.', 'The city has experienced an earthquake.', 'The city has experienced an age of exploration.', 'The city has experienced a terrible famine.', 'The city has experienced a disastrous flood.', 'The city has experienced a legendary storm.', 'The city has experienced an assassination.', 'The city has experienced a series of riots.', 'The city has experienced a serial killer.', 'The city has experienced a great discovery.', 'The city has experienced a vermin infestation.', 'The city has experienced a destructive fire.', 'The city has experienced a deadly plague.', 'The city has experienced a bloody rebellion.', 'The city has experienced a lengthy seige.', 'The city has experienced religious wars.', 'The city has experienced territorial wars.', 'The city has experienced a foreigh occupation.', 'The city has experienced an economic boom.', 'The city has experienced a great depression.', 'The city has experienced a dragon attack']
	foo8 = ['The people of the city are fearful of bandits and outlaws.', 'The people of the city are fearful of barbarian invasions.', 'The people of the city are fearful of a crime lord.', 'The people of the city are fearful of disease outbreaks.', 'The people of the city are fearful of a dragon or legendary beast.', 'The people of the city are fearful of destructive flooding.', 'The people of the city are fearful of food shortages.', 'The people of the city are fearful of occupation by a foreign empire.', 'The people of the city are fearful of the wrath of a vengeful god.', 'The people of the city are fearful of magic.', 'The people of the city are fearful of new inventions.', 'The people of the city are fearful of pirates.', 'The people of the city are fearful of smugglers.', 'The people of the city are fearful of a new religion.', 'The people of the city are fearful of a rival city']
	foo9 = ['The city is defended by a disciplined military guard.', 'The city is defended by a standing army of devoted soldiers.', 'The city is defended by a company of sellswords and knaves.', 'The city is defended by an order of holy knights.', 'The city is defended by little; the city has been sacked many times.', 'The city is defended by a huge fortress within the city.', 'The city is defended by a series of watch towers and forts throughout the region.', 'The city is defended by thick stone walls.', 'The city is defended by high stone walls.', 'The city is defended by catapults, scorpions.', 'The city is defended by a powerful magical ward']
	foo10 = ['The laws are enforced by a strict, orderly city watch.', 'The laws are enforced by a corrupt roguish city watch.', 'The laws are not enforced among wealthy elite.', 'The laws are enforced in a haphazard fashion, incomrehensible to visitors.', 'The laws are not enforced by those who pay bribes.', 'The laws are more like guidelines.', 'The laws are enforced by a secret society of assassins, mages, and priests.', 'The laws are enforced by a company of mercenaries.', 'The laws are simple easy to learn and follow.', 'The laws are extensive and complicated.', 'The laws are nonsensical.', 'The laws are enforced by a cheery drunken sheriff.', 'The laws are enforced by a rigid soldier-turned sheriff']
	foo11 = ['Outside the government, power is heald by a ruthless assassin guild.', 'Outside the government, power is heald by a populist demagogue.', 'Outside the government, power is heald by a captain of a mercenary company.', 'Outside the government, power is heald by a champion knight or arena figher.', 'Outside the government, power is heald by one or more crafting guilds.', 'Outside the government, power is heald by a dangerous crime boss.', 'Outside the government, power is heald by one or more criminal gangs.', 'Outside the government, power is heald by a charismatic cult leader.', 'Outside the government, power is heald by one or more merchant guilds.', 'Outside the government, power is heald by a scheming noble lord or lady.', 'Outside the government, power is heald by an outspoken philosopher or scholar.', 'Outside the government, power is heald by a celebrated poet and playwright.', 'Outside the government, power is heald by a popular priest or priestess.', 'Outside the government, power is heald by a secret societty of lore keepers.', 'Outside the government, power is heald by smugglers and black market dealers.', 'Outside the government, power is heald by the son or daughter of a deposed foriegn ruler.', 'Outside the government, power is heald by a wealthy trader of exotic goods.', 'Outside the government, power is heald by a conniving vampire or fiend.', 'Outside the government, power is heald by a bold war hero.', 'Outside the government, power is heald by a clever witch or wizard']
	foo12 = ['dry winters', 'wet winters', 'dark winters', 'cool winters', 'cold winters', 'frigid winters', 'windy winters', 'long winters', 'short winters', 'no winterts']
	foo13 = ['dry summers', 'wet summers', 'cool summers', 'warm summers', 'hot summers', 'blistering summers', 'windy summers', 'long summers', 'short summers', 'no summers']
	foo99 = ['The Aurora are visible from the city.', 'insert other interesting miscellaineous facts here.']

	#this part of the code chooses from those and assigns them to the appropriate variables
	x0 = random.choice(foo3)
	x1 = random.choice(foo4)
	x2 = random.choice(foo5)
	x3 = random.choice(foo6)
	x4 = random.choice(foo7)
	x5 = random.choice(foo8)
	x6 = random.choice(foo9)
	x7 = random.choice(foo10)
	x8 = random.choice(foo11)
	x9 = random.choice(foo12)
	x10 = random.choice(foo13)

	#this is where i want to generate random percentages for the races that inhabit the city
	humans = random.randint(30,70)
	gothes = random.randint(12,40)
	dwarves = random.randint(1,25)
	elves = random.randint(1,15)
	kobolds = random.randint(1,3)

	#now i'm totaling thing
	totalInhabitants = (humans + gothes + dwarves + elves + kobolds)

	#now i'm finding the percentages
	f0 = humans/totalInhabitants*100
	g0 = gothes/totalInhabitants*100
	h0 = dwarves/totalInhabitants*100
	i0 = elves/totalInhabitants*100
	j0 = kobolds/totalInhabitants*100

	#now i'm finding the raw number for each race within the city
	f1 = humans/totalInhabitants*j
	g1 = gothes/totalInhabitants*j
	h1 = dwarves/totalInhabitants*j
	i1 = elves/totalInhabitants*j
	j1 = kobolds/totalInhabitants*j

	#this is where it chooses how many facts to give about the city
	z = random.randint(2,6)

	foo14 = [x0, x1, x2, x3, x4, x5, x6, x7, x8]
	if z == 2:
		fact0, fact1 = random.sample(foo14, 2)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + '\n' 'Humans {}%'.format(round(f0,1)), ' Gothes {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' Gothes:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)

	elif z == 3:
		fact0, fact1, fact2 = random.sample(foo14, 3)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, fact2, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + '\n' 'Humans {}%'.format(round(f0,1)), ' Gothes {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' Gothes:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)

	elif z == 4:
		fact0, fact1, fact2, fact3 = random.sample(foo14, 4)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, fact2, fact3, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + '\n' 'Humans {}%'.format(round(f0,1)), ' Gothes {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' Gothes:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)

	elif z == 5:
		fact0, fact1, fact2, fact3, fact4 = random.sample(foo14, 5)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, fact2, fact3, fact4, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + '\n' 'Humans {}%'.format(round(f0,1)), ' Gothes {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' Gothes:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)

	else:
		fact0, fact1, fact2, fact3, fact4, fact5 = random.sample(foo14, 6)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, fact2, fact3, fact4, fact5, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + '\n' 'Humans {}%'.format(round(f0,1)), ' Gothes {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' Gothes:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)
