import config
import requests
import random
import trending

world_citys = {'Vienna': '48.2082,16.3738', 'New York': '40.7128,-74.0060', 'BARCELONA': '41.390205,2.154007', 'Rio De Janeiro': '-22.9068,-43.1729', 'Bangkok': '13.736717,100.523186', 'Sydney': '-33.865143,151.209900', 'Dubrovnik': '42.6507,18.0944', 'Cape Town': '-33.9249,18.4241', 'Los Angeles': '34.052235,-118.243683', 'Orlando': '28.538336,-81.379234', 
'Mexico City': '19.432608,-99.133209', 'Athens': '37.983810,23.727539', 'Istanbul': '41.015137,28.979530', 'Tel Aviv': '32.109333,34.855499', 'Moscow': '55.751244,37.618423', 'ABUDHABI': '24.46667,54.36667', 'Amsterdam': '52.37403,4.88969', 'Ankara': '39.91987,32.85427', 'BAGHDAD': '33.34058,44.40088', 'BAKU': '40.37767,49.89201', 
'Beijing': '39.9075,116.39723', 'Belgrade': '44.80401,20.46513', 'Berlin': '52.52437,13.41053', 'Budapest': '47.49801,19.03991', 'Buenos Aires': '-34.61315,-58.37723', 'Cairo': '30.06263,31.24967', 'CARACAS': '10.5,-66.91667', 'Copenhagen': '55.67594,12.56553', 'DAMASCUS': '33.5102,36.29128', 'Dhaka': '23.7104,90.40744', 'Gibralta': '36.14474,-5.35257',
'GUATAMALA': '14.64072,-90.51327', 'Havana': '23.13302,-82.38304', 'Hong Kong': '22.28552,114.15769', 'JAKARATA': '-6.21462,106.84513', 'KABUL': '34.52813,69.17233', 'Kathmandu': '27.70169,85.3206', 'Kiev': '50.45466,30.5238', 'Kuala Lumper': '3.1412,101.68653', 'KUWAIT': '29.36972,47.97833', 'Lisbon': '38.71667,-9.13333', 'MADRID': '40.4165,-3.70256', 
'Manila': '14.6042,120.9822', 'Monaco': '43.73333,7.41667', 'NAIROBI': '-1.28333,36.81667', 'New Delhi': '28.63576,77.22445', 'Singapore': '1.28967,103.85007', 'TOKYO': '35.61488,139.5813', 'Zagreb': '45.81444,15.97798'}


uk_city_list = {'Brighton': '50.8225,0.1372', 'London': '51.5074,0.1278', 'Liverpool': '53.41058,-2.97794', 'Edinburgh': '55.9533,3.1883', 'Leicester': '52.6369,1.1398', 'Plymouth': '50.3755,-4.1427', 'Porthmadog': '52.9278,-4.1334',
 'Aberdeen': '57.14369,-2.09814', 'Belfast': '54.58333,-5.93333', 'Bexley': '51.44162,0.14866', 'Birmingham': '52.48142,-1.89983', 'Blackpool': '53.81667,-3.05', 'Bolton': '53.58333,-2.43333', 'Bournmouth': '50.72048,-1.8795',
  'Bradford': '53.79391,-1.75206', 'Bristol': '51.45523,-2.59665','Cardiff': '51.48,-3.18', 'Snowdonia': '52.9180,-3.8912'}

def uk_city_checker():
	max_temp = -9999
	for city in uk_city_list:
		response = requests.get('https://api.darksky.net/forecast/'+ config.key+'/'+uk_city_list[city]+'?exclude=minutely,hourly,alerts,flags&units=si')
		print('This is the temp for ', city)
		data = response.json()
		current_temp = data['currently']['temperature']
		daily = data['daily']['data']
		daily_high = daily[0]['temperatureHigh']
		daily_high_round = int(round(daily_high,0))
		print(daily_high_round)
		if daily_high_round > max_temp:
			max_temp = daily_high_round
			hottest_city = city
	print("The hottest city in the uk is "+str(hottest_city)+" with a temperature of "+ str(max_temp))
	return [hottest_city,max_temp]


def world_temps(uk_temps):
	i = 0
	colder_citys = []
	colder_temps = []
	for city in world_citys:
		response = requests.get('https://api.darksky.net/forecast/'+ config.key+'/'+world_citys[city]+'?exclude=minutely,hourly,alerts,flags&units=si')
		print('This is the temp for ', city)
		data = response.json()
		current_temp = data['currently']['temperature']
		daily = data['daily']['data']
		daily_high = daily[0]['temperatureHigh']
		daily_high_round = int(round(daily_high,0))
		print(daily_high_round)
		if daily_high_round < uk_temps[1]:
			colder_citys.append(city)
			colder_temps.append(daily_high_round)
		i = i + 1
	print(colder_citys)
	print(colder_temps)
	if len(colder_citys) != 0: 
		picker = random.randint(0,len(colder_citys)-1)
		print(str(colder_citys[picker]) + " is only " + str(colder_temps[picker]) + " degrees. " + str(uk_temps[0]) +" is way hotter at " + str(uk_temps[1]) + " degrees!")
		return [colder_citys[picker],colder_temps[picker]]
	else:
		return ['Absoloutely no where',0]



word_gen = [["Great Britain ","Britain ","The UK ","The British Isles ","The United Kingdom "] #0
,["SWEATS ", "is MELTING ", "BOILS ", "SWELTERS ", "IS BLAZING ", "SCORCHES ","SIZZLES ","BAKES ","IS TROPICAL ","IS RED HOT ","IS HOTTER THAN HELL ","Gets out the suncream "] #1
,["in the sun as the temperature ", "as the sun shines down and it ", "as the mercury ","as the sun's rays beat down and it ","as clouds clear and it "] #2
,["climbs HIGHER than ","raises ABOVE ", "INCREASES to ", "BREAKS through to "] #3
,["making us HOTTER than ", "BEATING even ", "causing us to SWEAT more than ", "putting us on course to be WARMER than "] #4
,[" which ONLY has a measley ", " which ONLY reaches ", " which BARELY hits ", " which is a MERE ", " which CAN'T even get above "] #5
,["Great Britain ","Britain ","The UK "] #6
,["SWEATS!", "is MELTING!", "BOILS!", "SWELTERS!", "IS BLAZING!", "SCORCHES!","SIZZLES!","BAKES! ","IS TROPICAL! ","IS RED HOT!"]] #7

def word_generator():
	index_list = []
	for words in word_gen:
		index_list.append(random.randint(0,len(words)-1))
	while index_list[2] == index_list[7]:
		index_list[7] = random.randint(0,len(word_gen[7])-1) 
	return index_list


def headline_generator():
	trends = trending.get_trends()
	index = word_generator()
	uk_temp = uk_city_checker()
	world_temps_gen = world_temps(uk_temp)
	return (word_gen[0][index[0]]) + word_gen[1][index[1]] + word_gen[2][index[2]] + word_gen[3][index[3]] + str(uk_temp[1]) + str(" degrees ") + word_gen[4][index[4]] + str(world_temps_gen[0]) + word_gen[5][index[5]] + str(world_temps_gen[1]) + " degrees while " + word_gen[6][index[6]] + word_gen[7][index[7]] + " #dailyweather #UKweather #uk #weather #dailymail " + trends



