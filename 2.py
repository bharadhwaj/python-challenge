from string import maketrans
import webbrowser

sample_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
url_text = "map"

input_format = "abcdefghijklmnopqrstuvwxyz"
output_format = "cdefghijklmnopqrstuvwxyzab"
final_format = maketrans(input_format, output_format)

print sample_text.translate(final_format)

url = "http://www.pythonchallenge.com/pc/def/" + url_text.translate(final_format) + ".html"
webbrowser.open_new_tab(url)