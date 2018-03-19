from xml.dom import minidom
from selenium.webdriver.common.by import By

def create_xml_test(filename):
    xml = minidom.Document()
    root = xml.createComment('root')
    root.setAttribute('xmlns:xsi''http://www.baidu.com')
    xml.appendChild(root)

    test_node = xml.createComment('element')
    test_node.setAttribute('id', 'id1')
    root.appendChild(test_node)

    text = xml.createTextNode('hello word')
    test_node.appendChild(text)

    tag = xml.createElement('tag')
    tag.setAttribute('data', 'tag data')
    test_node.appendChild(tag)

    with open(filename) as f:
        f.write(xml.toprettyxml(encoding='utf-8'))

if __name__ == '__main__':
    create_xml_test('1.xml')