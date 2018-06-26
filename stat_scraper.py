from bs4 import BeautifulSoup
import requests

def html_stripper(html_array):
	stripped_array = []
	for x in html_array:
		stripped_array.append(x.getText().replace(" ","").replace("\n",""))

	return stripped_array 

website = "http://theaudl.com/spiders/players/szaccaro"
#website saved into variable

extract_content = requests.get(website, timeout=10)
#gets the content from url

raw_html = BeautifulSoup(extract_content.content, "html.parser")
#uses beautiful soup to extract the HTML from the website

stat_table_html = raw_html.find_all(class_='views-table')
#finds anything in the html with the class views-table and saves it as the new variable

games_played = raw_html.find_all(class_='views-field-games-played')

points_played = raw_html.find_all(class_='views-field-points-played')

assists = raw_html.find_all(class_='views-field-assists')

goals = raw_html.find_all(class_='views-field-goals')

years = raw_html.find_all(class_='views-field-year')



points_played = html_stripper(points_played)
games_played = html_stripper(games_played)
assists = html_stripper(assists)
goals = html_stripper(goals)
years = html_stripper(years)


stat = {}

for i in range(0,len(years)):
	year = years[i]
	if year == "YR":
		continue
	stat[year]={}
	stat[year]["games_played"] = games_played[i]
	stat[year]["points_played"] = points_played[i]
	stat[year]["assists"] = assists[i]
	stat[year]["goals"] = goals[i]

	#print year
	#print i



#print stat

print stat["2014"]["assists"]
