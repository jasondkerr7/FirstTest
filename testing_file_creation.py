import pandas as pd
import os

t = pd.DataFrame({'Last Names':['Kerr','Kerr','Sichel','Vallido','Kerr','Sichel','Kurz'],
                  'Height':[3,1,4,2,0,10,0.5],
                  'Money':[1,2,3,12,20,101,0.5],
                  'Rankz':[1,1,1,1,2,3,2]
                    })

cred_json = os.environ['SERVICE_ACCOUNT_CREDENTIALS_JSON']
counter = 0
for x in cred_json:
  print(x)
  counter += 1
  if counter >= 10:
    break

print(type(cred_json))
