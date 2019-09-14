import requests
import json
import csv
payload = {"returnCount":{},"repository":"partnerfinder","type":"content","filters":[{"field":"region","values":["scm_v_region4"],"type":"like"},{"field":"country","values":["scm_v_country237"],"type":"like"},{"field":"author","values":["PWP"],"type":"exact"}],"returnResults":{"sort":[{"field":"shortname","order":"asc"}],"page":{"size":"600"},"outputFields":["TITLE","EMAIL","PARTNERID","DESCRIPTION","PHONE","AWARDID","FOCUSAREA","LEVEL","URL"]}}
r = requests.post("https://partneredge.sap.com/bin/fiji/es/search-results", data=json.dumps(payload))
json_data = json.loads(r.text)
parsedvalue = json_data['result']['results']
parsedr = parsedvalue['results']
j_data = open('USPartnerList.csv', 'w', newline='')
csvwriter = csv.writer(j_data)
csvwriter.writerow(["PARNTER","WEBSITE","REGION","PARTNER LEVEL","COMPANY EMAIL","CONTACT","CONTACT MAIL","MOBILE","SOLUTION FOCUS"])
for item in parsedr:
    relative_url = item['PARTNERID']
    abs_url = 'https://partneredge.sap.com/bin/partnerfinder/partnerdetails?partnerId='+relative_url
    r1 = requests.get(abs_url)
    json_data1 = json.loads(r1.text)
    Partner = json_data1['companyName']

    addr = json_data1['addresses']
    try:
        region = addr[0]['regionDescr']
    except:
        region = ''
    companymail = json_data1['companyEmail']
    Website = json_data1['companySiteUrl']
    p_level = json_data1['level'].split("-")
    try:
        Level = p_level[1]
    except:
        Level = ''
    try:
        Contact = json_data1['contactName']
    except:
        Contact = ''
    try:
        ContactEmail = json_data1['contactEmail']
    except:
        ContactEmail = ''
    try:
        Mobile = json_data1['contactMobile']
    except:
        Mobile = ''
    SolutionFocus = json_data1['solutionFocuses']
    try:
        SF = SolutionFocus[0]['externalDesc']
    except:
        SF = ''
    scraped_info = {
    'PARTNER' : Partner,
    'WEBSITE' : Website,
    'REGION' : region,
    'PARTNER LEVEL' : Level,
    'COMPANY EMAIL' : companymail,
    'CONTACT' : Contact,
    'CONTACT MAIL' : ContactEmail,
    'MOBILE' : Mobile,
    'SOLUTIONFOCUS' : SF
    }
    csvwriter.writerow(scraped_info.values())
j_data.close()
