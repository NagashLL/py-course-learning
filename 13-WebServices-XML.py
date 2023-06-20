import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Chuck</name>
        <phone type="inti">
        +1 734 303 4456
        </phone>
    <email hide="yes"/>
</person>
'''
#we can use triple quotes to basically create a new file inside of a block of code, kind of how like
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))



input = '''
<people>
    <users>
    <user id="6">
    <name>Chuck</name>
        <phone type="inti">
        +1 734 303 4456
        </phone>
    <email hide="yes"/>
    </user>
    <user id="12">
    <name>Brian</name>
        <phone type="inti">
        +1 999 888 777
        </phone>
    <email hide="yes"/>
    </user>
    </users>
</people>
'''

tree2 = ET.fromstring(input)

lst = tree2.findall('users/user')
print ('User count:', len(lst))

for item in lst:
    print ('Name:', item.find('name').text)
    print ('Phone:', str(item.find('phone').text))
    print ('Attribute:', item.get("id"))
