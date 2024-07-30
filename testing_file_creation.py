import pandas as pd
import os

t = pd.DataFrame({'Last Names':['Kerr','Kerr','Sichel','Vallido','Kerr','Sichel','Kurz'],
                  'Height':[3,1,4,2,0,10,0.5],
                  'Money':[1,2,3,12,20,101,0.5],
                  'Rankz':[1,1,1,1,2,3,2]
                    })

cred_json = os.environ['SERVICE_ACCOUNT_CREDENTIALS_JSON']
counter = 0

print('Starting')
for i in range(0,7):
  print(i,'-',cred_json[i])

for i in range(0,7):
  x = i * -1
  print(x,'-',cred_json[x])
  
