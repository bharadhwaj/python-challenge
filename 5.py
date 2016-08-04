import webbrowser
import requests
import re

nothing_val = ['12345']

while True:
	link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing_val[0]
	contents = requests.get(link)
	nothing_val = re.findall('[0-9]+', contents.text)
	if contents.text == "Yes. Divide by two and keep going.":
		nothing_val = ['8022']
	elif contents.text == "There maybe misleading numbers in the \ntext. One example is 82683. Look only for the next nothing and the next nothing is 63579":
		nothing_val = ['63579']
	elif nothing_val:
		print nothing_val[0]
	else:
		break
print contents.text

url = "http://www.pythonchallenge.com/pc/def/" + contents.text
webbrowser.open_new_tab(url)
