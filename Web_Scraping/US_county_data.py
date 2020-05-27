import json
import requests 
import json
from lxml import html
import pandas as pd
import csv

for i in county['Georgia']:
    url = "http://www.statsamerica.org/USCP/geo_response_HC.aspx?term={place}".format(place = i)
    response = requests.post(url, data=payload)
    county_ids.append(json.loads(response.text)[0]['id'])
county_string = '%5E'.join(county_ids)

 

url = "http://www.statsamerica.org/USCP/sbs_output.aspx?dash_set=full&dash_type=a&geography={places}&sort=topic&output_type=ci&dash_content=10&level1=dash&comp_type=&output_style=JSON".format(places = county_string )
# url1 = "http://www.statsamerica.org/USCP/report_output.aspx"
# payload = {"output_set":"pt1","output_style":"JSON","geo1":"106000","report_context":"states"}
response = requests.post(url, data=payload)
html_data = response.text.replace('{"main_report": ','').replace('", "js_commands": "set_label(\'Overview\')"}','')

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')
table_header = [cell.text for cell in BeautifulSoup(html_data)("th")]
                         
table_data = [[cell.text for cell in row("td")]
                         for row in BeautifulSoup(html_data)("tr")]
df = pd.DataFrame(table_data[1:], columns = table_header) 

df.to_excel('Counties.xlsx')