import lxml.etree as etree
tree = etree.parse("first.xml")
count = 0
min = -1
root = tree.getroot()
text = tree.xpath("//page")
mpage = text[0].attrib
for a in text:
    s = a.xpath(".//photo/text()")
    for st in s:
        count = count + 1
    if min == -1:
        min = count
    if count < min:
        min = count
        mpage = a.attrib
    count = 0
print mpage, ":", min