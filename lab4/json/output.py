import json

f=open("sampledata.json")
memory=json.load(f)


print('Interface Status')
print('='*50)
print('DN',' '*15,'Description','Speed', 'MTU', sep=5*' ')
print('-'*50)
y=0
for i in memory['imdata']:
    y+=1
    out1=i["l1PhysIf"]["attributes"]["dn"]
    out11=i["l1PhysIf"]["attributes"]["fecMode"]
    out111=i["l1PhysIf"]["attributes"]["mtu"]

    print(out1,' '*5,out11,' '*2,out111)
    if y==3:
        break
