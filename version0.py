import config
import requests
import random

##city_list = ['Vienna','New York','BARCELONA','Rio De Janeiro','Bangkok','Sydney','Dubrovnik','Cape Town','Los Angeles','Orlando','Mexico City','Athens','Istanbul','Tel Aviv','Moscow','ABU DHABI','Amsterdam','Ankara','BAGHDAD',
##'BAKU','Beijing','Belgrade','Berlin','Budapest','Buenos Aires','Cairo','CARACAS','Copenhagen','DAMASCUS','Dhaka','Gibralta','GUATAMALA','Havana','Hong Kong','JAKARATA','KABUL','Kathmandu','Kiev','Kuala Lumper','KUWAIT','Lisbon',
##'MADRID','Manila','Monaco','NAIROBI','New Delhi','Singapore','TOKYO','Zagreb']
##uk_city_list = ['Brighton','London','Liverpool','Edinburgh','Leicester','Plymouth']



def uk_high_temp():
	i = 0
	max_temp = -9999
	for city in config.uk_citys:
		response = requests.get(config.uk_citys[i])
		print('This is the temp for', config.uk_city_list[i])
		data = response.json()
		current_temp = data['currently']['temperature']
		daily = data['daily']['data']
		daily_high = daily[0]['temperatureHigh']
		daily_high_round = int(round(daily_high,0))
		print(daily_high_round)
		if daily_high_round > max_temp:
			max_temp = daily_high_round
			hottest_city = config.uk_city_list[i]
		i = i + 1
	print("The hottest city in the uk is "+str(hottest_city)+" with a temperature of "+ str(max_temp))
	return [hottest_city,max_temp]

def world_temps():
	i = 0
	uk_temp_run = uk_high_temp()
	colder_citys = []
	colder_temps = []
	for city in config.world_citys:
		response = requests.get(config.world_citys[i])
		print('This is the temp for ', config.city_list[i])
		data = response.json()
		current_temp = data['currently']['temperature']
		daily = data['daily']['data']
		daily_high = daily[0]['temperatureHigh']
		daily_high_round = int(round(daily_high,0))
		print(daily_high_round)
		if daily_high_round < uk_temp_run[1]:
			colder_citys.append(config.city_list[i])
			colder_temps.append(daily_high_round)
		i = i + 1
	print(colder_citys)
	print(colder_temps)
	picker = random.randint(0,len(colder_citys)-1)
	print(str(colder_citys[picker]) + " is only " + str(colder_temps[picker]) + " degrees. " + str(uk_temp_run[0]) +" is way hotter at " + str(uk_temp_run[1]) + " degrees!")
	return [colder_citys[picker],colder_temps[picker]]


word_gen = [["Great Britain ","Britain ","The UK ","The British Isles ","The United Kingdom "] #0
,["SWEATS ", "is MELTING ", "BOILS ", "SWELTERS ", "IS BLAZING ", "SCORCHES ","SIZZLES ","BAKES ","IS TROPICAL ","IS RED HOT ","IS HOT AS HELL "] #1
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
	index = word_generator()
	uk_temp = uk_high_temp()
	world_temps_gen = world_temps()
	return (word_gen[0][index[0]]) + word_gen[1][index[1]] + word_gen[2][index[2]] + word_gen[3][index[3]] + str(uk_temp[1]) + str(" degrees ") + word_gen[4][index[4]] + str(world_temps_gen[0]) + word_gen[5][index[5]] + str(world_temps_gen[1]) + " degrees while " + word_gen[6][index[6]] + word_gen[7][index[7]] + " #dailyweather #UKweather #hot #uk #dailyexpress #dailymail"




