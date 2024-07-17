import pandas as pd

t = pd.DataFrame({'Names1':['Jason','Jason','Jacob','Brad','Jason','Jacob','Sean'],
                  'Names2':[np.nan,'MF','Sichel',np.nan,np.nan,np.nan,'MF'],
                  'Names3':[np.nan,'Kurz',np.nan,np.nan,np.nan,np.nan,'Kurz'],
                  'Height':[3,1,4,2,0,10,0.5],
                  'Money':[1,2,3,np.nan,20,101,0.5],
                  'Rankz':[1,1,1,1,2,3,2]
                    })

t.to_csv('file_creation_test_jjbs.csv')