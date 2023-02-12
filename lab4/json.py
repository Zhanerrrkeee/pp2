import json 
f1 = open('sample.json', 'r') 
f2 = open('output_json.txt', 'w') 
 
Dict = json.loads(f1.read()) 
 
f2.write('Interface Status\n') 
f2.write('================================================================================\n') 
f2.write('DN                                                 Description           Speed    MTU\n') 
f2.write('-------------------------------------------------- --------------------  ------  ------\n') 
 
cnt = 1 
 
for i in Dict['imdata']: 
    if cnt == 4: 
        break 
    f2.write(json.dumps(i["l1PhysIf"]["attributes"]["dn"])) 
    f2.write('                            ') 
    f2.write(json.dumps(i["l1PhysIf"]["attributes"]["speed"])) 
    f2.write(' ') 
    f2.write(json.dumps(i["l1PhysIf"]["attributes"]["mtu"])) 
    f2.write('\n') 
    cnt+=1
