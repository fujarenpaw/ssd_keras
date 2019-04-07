#!/usr/bin/env python
# coding: utf-8

from xml.dom.minidom import parseString


def createXml(posAry, fileName, width, height):
    xml_template = '<?xml version="1.0" encoding="UTF-8"?>\
    <annotation>\
      <folder>XXX</folder>\
      <source>\
        <database>XXX</database>\
        <annotation>XXX</annotation>\
        <image>XXX</image>\
        <flickrid>XXX</flickrid>\
      </source>\
      <owner>\
        <flickrid>XXX</flickrid>\
        <name>?</name>\
      </owner>\
      <segmented>0</segmented>\
    </annotation>'

    dom = parseString(xml_template)

    # channelノードを取得
    root = dom.getElementsByTagName("annotation")[0]

    # サブノードの生成
    subnode = dom.createElement('filename')
    subnode.appendChild(dom.createTextNode(str(fileName) + ".jpg"))
    # itemノードにsubnodeノードを追加
    root.appendChild(subnode)

    size = dom.createElement('size')

    subnode = dom.createElement('width')
    subnode.appendChild(dom.createTextNode(str(width)))
    # itemノードにsubnodeノードを追加
    size.appendChild(subnode)

    subnode = dom.createElement('height')
    subnode.appendChild(dom.createTextNode(str(height)))
    # itemノードにsubnodeノードを追加
    size.appendChild(subnode)

    subnode = dom.createElement('depth')
    subnode.appendChild(dom.createTextNode("1"))
    # itemノードにsubnodeノードを追加
    size.appendChild(subnode)

    for pos in posAry:
        # itemノードを生成
        item = dom.createElement('object')
        # channelノードに追加
        root.appendChild(item)

        # サブノードの生成
        subnode = dom.createElement('name')
        subnode.appendChild(dom.createTextNode("character"))
        # itemノードにsubnodeノードを追加
        item.appendChild(subnode)

        subnode = dom.createElement('pose')
        subnode.appendChild(dom.createTextNode("Unspecified"))
        # itemノードにsubnodeノードを追加
        item.appendChild(subnode)

        subnode = dom.createElement('truncated')
        subnode.appendChild(dom.createTextNode("0"))
        # itemノードにsubnodeノードを追加
        item.appendChild(subnode)

        subnode = dom.createElement('difficult')
        subnode.appendChild(dom.createTextNode("1"))
        # itemノードにsubnodeノードを追加
        item.appendChild(subnode)

        bndbox = dom.createElement('bndbox')

        subnode = dom.createElement('xmin')
        subnode.appendChild(dom.createTextNode(str(pos[0])))
        # itemノードにsubnodeノードを追加
        bndbox.appendChild(subnode)

        subnode = dom.createElement('ymin')
        subnode.appendChild(dom.createTextNode(str(pos[1])))
        # itemノードにsubnodeノードを追加
        bndbox.appendChild(subnode)

        subnode = dom.createElement('xmax')
        subnode.appendChild(dom.createTextNode(str(pos[2])))
        # itemノードにsubnodeノードを追加
        bndbox.appendChild(subnode)

        subnode = dom.createElement('xmax')
        subnode.appendChild(dom.createTextNode(str(pos[3])))
        # itemノードにsubnodeノードを追加
        bndbox.appendChild(subnode)

        # itemノードにsubnodeノードを追加
        item.appendChild(bndbox)

    # domをxmlに変換して整形
    print(dom.toprettyxml())

    with open(r"autoOutput\xml\\" + str(fileName) + '.xml', mode='w', encoding='utf-8') as f:
        f.write(dom.toprettyxml())


test = [[1, 2, 3, 4], [5, 6, 7, 8]]
createXml(test, 10, 500, 200)
