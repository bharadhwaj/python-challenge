import webbrowser

with open("text4.txt", "r") as text4:
    content = ""
    for line in text4:
        content += line
length = len(content)
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"
small_letter = []
i = 4
while i < length-4:
	if content[i] in small:
		if content[i-4] in small and content[i-3] in caps and content[i-2] in caps and content[i-1] in caps:
			if content[i+4] in small and content[i+3] in caps and content[i+2] in caps and content[i+1] in caps:
				small_letter.append(content[i])
		i += 4
	else:
		i += 1
required_text = ''.join(small_letter)
print required_text
url = "http://www.pythonchallenge.com/pc/def/" + required_text + ".php"
webbrowser.open_new_tab(url)