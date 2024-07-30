import pandas as pd
import os

t = pd.DataFrame({'Last Names':['Kerr','Kerr','Sichel','Vallido','Kerr','Sichel','Kurz'],
                  'Height':[3,1,4,2,0,10,0.5],
                  'Money':[1,2,3,12,20,101,0.5],
                  'Rankz':[1,1,1,1,2,3,2]
                    })

cred_json = os.environ['SERVICE_ACCOUNT_CREDENTIALS_JSON']
s_char = cred_json.index('~~~')
e_char = cred_json.index('%%%')
  
test = eval(cred_json[s_char+3:e_char])
print('Type of test::', type(test))
print('Type of test key::', type(test['test1']))
print('string of test2::', test['test2'])
