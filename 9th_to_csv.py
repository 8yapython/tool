import datetime
import pandas as pd

dt_now = datetime.datetime.now()
df = pd.DataFrame()

#CSVを作る ...空です。
df.to_csv('/Users/knospear/Downloads/MyPython/9th/'+str(dt_now)+'.csv')
print(str(dt_now),'fin')