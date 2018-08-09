import pandas as pd
import xlrd as xl


df1 = pd.read_csv('csvlinuxdata.csv')
df2 = pd.read_csv('onesourcecsv.csv')
# print df1['Hostname']
# if df2['OS']=='Red Hat(Linux)':
#     print 'linux'

df2.loc[df2['OS'] == 'Red Hat(Linux)', 'OS'] = 'Linux'
print df2
# df2.columns = map(str.lower, df2.columns)
df2.Hostname = df2.Hostname.astype(str).str.lower()
df2.to_csv('updatedonesource.csv',  encoding='utf-8')

# df1.join(df2, lsuffix='_df1', rsuffix='_df2')
# df1.to_csv('newjoin.csv', encoding='utf-8')
# df_final = df_all.swaplevel(axis='columns')[df.columns[1:]]
# df_final

# df_all = pd.concat([df1, df2],
#                    axis='columns', keys=['Linux', 'Onesource'])
# print df_all
# df_final = df_all.swaplevel(axis='columns')[df1.columns[1:]]
# df_final.to_csv('new.csv', encoding='utf-8')

