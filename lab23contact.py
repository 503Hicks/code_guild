
import csv 


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    header = lines.pop(0).split(', ')
    contacts = []
    for line in lines:
        data = line.split(', ')
        item = {}
        for i in range(len(data)):
            item.update({header[i]: data [i]})
        contacts.append(item)
print(contacts)

#     # print(lines)
#     print(header)
#     print(data)








# def read_contacts():
#     with open('contacts.csv', 'r') as file:
#         lines = file.read().split('\n')
#     header = lines.pop(0).split(', ')
#     contacts = []
#     for line in lines:
#         data = line.split(', ')
#         item = {}
#         for i in range(len(data)):
#             item.update({header[i]: data[i]})
#         contacts.append(item)
#     return contacts
# print(read_contacts())