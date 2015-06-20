import mechanize
import csv
from bs4 import BeautifulSoup
import math

qty = 'ctl00$ctl00$mainContentPlaceHolder$mainContentPlaceHolder$txtQty'
part = 'ctl00$ctl00$mainContentPlaceHolder$mainContentPlaceHolder$txtPart'
cref = 'ctl00$ctl00$mainContentPlaceHolder$mainContentPlaceHolder$txtCref'

filename = 'digikey.csv'
mylist=[]
with open(filename, 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		mylist.append(row)
		
length = len(mylist)
iter = int(math.ceil(length/20.0))
target = iter*20;
for i in range(0,target-length):
	mylist.append(['',''])
	
br = mechanize.Browser()
br.set_handle_robots(False)



for i in range(0,iter):
	br.open('http://www.digikey.ca/classic/ordering/FastAdd.aspx')
	if(i == 0):
		mySearch = BeautifulSoup(br.response().read())
		print mySearch.find('span', id="ctl00_ctl00_topContentPlaceHolder_lblWebID").text
		print mySearch.find('span', id="ctl00_ctl00_topContentPlaceHolder_lblAccessID").text
	
	br.select_form(nr=0)
	for j in range(0,20):
		tempqty = qty + str(j+1)
		temppart = part + str(j+1)
		#tempcref = cref + str(j+1)
		br[tempqty] = mylist[i*20+j][0]
		br[temppart] = mylist[i*20+j][1]
		#br[tempcref] = mylist[i*20+j][3]
		
	response = br.submit()


#response2 = urlopen(form.click())
#forms2 = ParseResponse(response2, backwards_compat=False)
#form2 = forms2[0]
#print response2.links()

#stuff = urlopen(form2.click(response2.at("#ctl00_ctl00_rightContentPlaceHolder_rightContentPlaceHolder_ctlCartTools_btnCartShare"))).read()

#text_file = open("Log1.html", "w")
#text_file.seek(0)
#text_file.write(response.read())
#text_file.close()
#text_file = open("Log2.html", "w")
#text_file.seek(0)
#text_file.write(br.response().read())
#text_file.close()
