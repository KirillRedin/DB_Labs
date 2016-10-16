import lxml.etree as etree
import requests


url = "http://freedelivery.com.ua/dlya-kompyuterov-19/aksessuary-20"
root = etree.Element("root")

tree = etree.HTML(requests.get(url).text)
doc = etree.SubElement(root, "data")
name = tree.xpath('//h4/a/text()')
image = tree.xpath('//*[@class="image"]//img/@src')
price = tree.xpath('//*[@class="price"]/text()' )

for i in range(20):
    node = etree.SubElement(doc, 'product', id = str(i+1))
    etree.SubElement(node, 'name').text = name[i]
    etree.SubElement(node, 'price').text = price[i]
    etree.SubElement(node, 'image').text = image[i]

tree = etree.tostring(root, pretty_print = True, encoding = 'utf-8', xml_declaration = True)
f = open("third.xml","w")
f.writelines(tree)
f.close()

data = open('file.xsl')
xslt_content = data.read()
xslt_root = etree.XML(xslt_content)
dom = etree.parse('third.xml')
transform = etree.XSLT(xslt_root)
result = transform(dom)
f = open('result.html', 'w')
f.write(str(result))
f.close()