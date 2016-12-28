import random
from random import randint
import math
# first we need to import the random shit that let's us generate random things

k = random.randint(1,7)
if k == 1:
	j = random.randint(40,200)
	foo2 = ['VILLE', ' THORP' , 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
	secondPart = random.choice(foo2)
elif k == 2:
	j = random.randint(150,600)
	foo2 = [' TOWN', 'VILLE', ' THORP' , 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
	secondPart = random.choice(foo2)
elif k == 3:
	j = random.randint(400,800)
	foo2 = [' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
	secondPart = random.choice(foo2)
elif k == 4:
	j = random.randint(1000,7500)
	foo2 = [' CITY', ' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
	secondPart = random.choice(foo2)
elif k == 5:
	j = random.randint(5000,10000)
	foo2 = [' CITY', ' TOWN', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
	secondPart = random.choice(foo2)
elif k == 7:
	j = random.randint(8000,75000)
	foo2 = [' CITY', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
	secondPart = random.choice(foo2)
else:
	j = random.randint(50000,160000)
	foo2 = [' CITY', 'VILLE', 'TON', 'BUR', 'PORT', 'Y', 'DALE', ' BEACH', 'HILL', 'ROCK', 'STONE', 'BOROUGH', 'RAPIDS', 'ON']
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
foo3 = ['A COASTAL HARBOR', 'A CALM, COASTAL BAY', 'A LARGE FRESHWATER LAKE', 'A WIDE NAVIGABLE RIVER', 'A RIVER NAVIGABLE BY SMALL CRAFT', 'WHERE TWO RIVERS MET', 'A RIVER DELTA', 'A SERIES OF NATURAL SPRINGS', 'A WELL TRAVELED CROSSROADS', 'A WATER SOURCE ON A WELL TRAVELED ROAD']
foo4 = ['IRON ORE', 'COPPER ORE', 'GOLD', 'SILVER', 'PLATINUM', 'ELECTRUM', 'TIN', 'SPICES', 'CLAY', 'GRANITE', 'QUARTS', 'SALT', 'PEAT', 'BITUMINOUS COAL', 'ANTHRACITE COAL', 'PINE TREES', 'OAK TREES', 'BIRCH TREES', 'HARDWOOD LUMBER', 'BARLEY', 'OATS', 'BEANS', 'CORN', 'SQUASH', 'NUTS', 'OLIVES', 'RICE', 'WHEAT', 'POTATOES', 'LEAKS', 'SUGAR CANE', 'TOBACCO', 'COTTON', 'GRAPES', 'APPLES', 'CITRUS FRUITS', 'PEARS', 'PLUMS', 'PEACHES', 'FRUIT TREES', 'BERRIES', 'CABBAGE', 'BEETS', 'CATTLE', 'SHEEP', 'DAIRY COWS']
foo5 = ['ARCHITECTURAL STYLE', 'ARCHITECTURAL FEATS', 'ARTISTS AND POETS', 'CUISINE', 'SUGGESTIVE DANCING', 'GLADITORIAL GAMES', 'HORSE RACES', 'SCHOLARS', 'SAGES', 'MUSIC', 'ROMANCE', 'JOUSTING', 'SUPERIOR SOLDIERS', 'STREET FESTIVALS', 'RELIGIOUS FEASTS', 'REILIGOUS FERVOR', 'TRADITIONAL DRESS', 'THEATER', 'WINE', 'ALE']
foo6 = ['THE HEAD OF A NOBLE FAMILY', 'A CONCIL OF DISTINGUISHED NOBLES', 'A COUNCIL OF WEALTHY MERCHANTS', 'A COUNCIL OF ELECTED OFFICIALS', 'AN ELECTED MAYOR', 'A BENEVOLENT SOVEREIGN', 'A WICKED TYRANT', 'A BRUTAL WARLORD', 'A CABAL OF WITCHES AND WIZARDS', 'THE LEADERS OF A RELIGIOUS ORDER']
foo7 = ['MASS CONVERSIONS', 'AN EARTHQUAKE', 'AN AGE OF EXPLORATION', 'A TERRIBLE FAMINE', 'A DISASTROUS FLOOD', 'A LEGENDARY STORM', 'AN ASSASSINATION', 'A SERIES OF RIOTS', 'A SERIAL KILLER', 'A GREAT DISCOVERY', 'A VERMIN INFESTATION', 'A DESTRUCTIVE FIRE', 'A DEADLY PLAGUE', 'A BLOODY REBELLION', 'A LENGTHY SEIGE', 'RELIGIOUS WARS', 'TERRITORIAL WARS', 'A FOREIGH OCCUPATION', 'AN ECONOMIC BOOM', 'A GREAT DEPRESSION', 'A DRAGON ATTACK']
foo8 = ['BANDITS AND OUTLAWS', 'BARBARIAN INVASIONS', 'A CRIME LORD', 'DISEASE OUTBREAKS', 'A DRAGON OR LEGENDARY BEAST', 'DESTRUCTIVE FLOODING', 'FOOD SHORTAGES', 'OCCUPATION BY A FOREIGN EMPIRE', 'THE WRATH OF A VENGEFUL GOD', 'MAGIC', 'NEW INVENTIONS', 'PIRATES', 'SMUGGLERS', 'A NEW RELIGION', 'A RIVAL CITY']
foo9 = ['A DISCIPLINED MILITARY GUARD', 'A STANDING ARMY OF DEVOTED SOLDIERS', 'A COMPANY OF SELLSWORDS AND KNAVES', 'AN ORDER OF HOLY KNIGHTS', 'LITTLE; THE CITY HAS BEEN SACKED MANY TIMES', 'A HUGE FORTRESS WITHIN THE CITY', 'A SERIES OF WATCH TOWERS AND FORTS THROUGHOUT THE REGION', 'THICK STONE WALLS', 'HIGH STONE WALLS', 'CATAPULTS, SCORPIONS', 'A POWERFUL MAGICAL WARD']
foo10 = ['ENFORCED BY A STRICT, ORDERLY CITY WATCH', 'ENFORCED BY A CORRUPT ROGUISH CITY WATCH', 'NOT ENFORCED AMONG WEALTHY ELITE', 'ENFORCED IN A HAPHAZARD FASHION, INCOMREHENSIBLE TO VISITORS', 'NOT ENFORCED BY THOSE WHO PAY BRIBES', 'MORE LIKE GUIDELINES', 'ENFORCED BY A SECRET SOCIETY OF ASSASSINS, MAGES, AND PRIESTS', 'ENFORCED BY A COMPANY OF MERCENARIES', 'SIMPLE EASY TO LEARN AND FOLLOW', 'EXTENSIVE AND COMPLICATED', 'NONSENSICAL', 'ENFORCED BY A CHEERY DRUNKEN SHERIFF', 'ENFORCED BY A RIGID SOLDIER-TURNED SHERIFF']
foo11 = ['A RUTHLESS ASSASSIN GUILD', 'A POPULIST DEMAGOGUE', 'A CAPTAIN OF A MERCENARY COMPANY', 'A CHAMPION KNIGHT OR ARENA FIGHER', 'ONE OR MORE CRAFTING GUILDS', 'A DANGEROUS CRIME BOSS', 'ONE OR MORE CRIMINAL GANGS', 'A CHARISMATIC CULT LEADER', 'ONE OR MORE MERCHANT GUILDS', 'A SCHEMING NOBLE LORD OR LADY', 'AN OUTSPOKEN PHILOSOPHER OR SCHOL;AR', 'A CELEBRATED POET AND PLAYWRIGHT', 'A POPULAR PRIEST OR PRIESTESS', 'A SECRET SOCIETTY OF LORE KEEPERS', 'SMUGGLERS AND BLACK MARKET DEALERS', 'THE SON OR DAUGHTER OF A DEPOSED FORIEGN RULER', 'A WEALTHY TRADER PF EXOTIC GOODS', 'A CONNIVING VAMPIRE OR FIEND', 'A BOLD WAR HERO', 'A CLEVER WITH OR WIZARD']
foo12 = ['dry winters', 'wet winters', 'cool winters', 'cold winters', 'frigid winters', 'windy winters', 'long winters', 'short winters', 'no winterts']
foo13 = ['dry summers', 'wet summers', 'cool summers', 'warm summers', 'hot summers', 'blistering summers', 'windy summers', 'long summers', 'short summers', 'no summers']

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

#now time to print everything out

with open("Cities.txt", "a") as text_file:
	print(name, ' Pop:',j, file=text_file)
	print("-----------------------------", file=text_file)
	print('The city grew up around',x0 + 
		'\n' 'The city is near a region known for its prominent amounts of',x1 +
		'\n' 'The city is known for its',x2 +
		'\n' 'The city is ruled by',x3 +
		'\n' 'The city has experienced',x4 +
		'\n' 'The people of the city are fearful of',x5 +
		'\n' 'The city is defended by',x6 +
		'\n' 'The laws are',x7 +
		'\n' 'Outside the government, power is heald by',x8 +
		'\n' '-----------------------------' +
		'\n' 'It has' ,x10 + ' and' ,x9 + '\n' 'Humans {}%'.format(round(f0,1)), ' Gothes {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' Gothes:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)