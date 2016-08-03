import webbrowser

def make_set(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

with open("text3.txt", "r") as text3:
    content = ""
    for line in text3:
        content += line

characters = make_set(content)

rare_set = [x for x in characters if content.count(x) == 1]
rare =  ''.join(rare_set)
print rare

url = "http://www.pythonchallenge.com/pc/def/" + rare + ".html"
webbrowser.open_new_tab(url)