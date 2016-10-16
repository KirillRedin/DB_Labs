import string
import requests
import lxml.etree as etree

url1 = 'http://www.doroga.ua/'
root = etree.Element("root")
count = 1

doc = etree.SubElement(root, "data")
tree = etree.HTML(requests.get(url1).text)
url = tree.xpath('/html/body//a//@href')

for a in url:
    if(string.find(a, 'www.doroga.ua')!=-1 and string.find(a, 'javascript') == -1):
        if count <= 20:
            tree = etree.HTML(requests.get(a).text)
            img = tree.xpath('/html/body//img/@src')
            text1 = tree.xpath('/html/body//a[@class="CadetBlueLink"]')
            text2 = tree.xpath('/html/body//p//text()')
            url_el = etree.SubElement(doc,"page", url = a)
            for i in img:
                etree.SubElement(url_el, "photo").text = i
            for i in text1:
                etree.SubElement(url_el, "text").text = i.text
            for i in text2:
                etree.SubElement(url_el, "text").text = i
        count = count + 1

tree = etree.tostring(root, pretty_print = True, encoding = 'utf-8', xml_declaration = True)
f = open("first.xml","w")
f.writelines(tree)
f.close()