#business intelligence course => absenteeism at a company during work time
import pandas as pd
raw_csv_data = pd.read_csv("/Users/chrysspoetry/Downloads/Absenteeism_data.csv")
#copyint the data so as not to distort the original data

df =raw_csv_data.copy()

#setting maximum columns and rows
# pd.options.display.max_columns = None
# pd.options.display.max_rows = None
# print(df)
# print(df.info())
#dropping the tables we dont need
df =df.drop(["ID"], axis=1)
# print(sorted(df["Reason for Absence"].unique()))
# print(df["Reason for Absence"].unique())
# print(len(df["Reason for Absence"].unique()))

reason =pd.get_dummies(df["Reason for Absence"], drop_first=True) #droping the reason number one
#
# reason["check"] = reason.sum(axis =1)
# print(reason)
# print(reason["check"].sum(axis = 0))
# print(reason["check"].unique())
# reason.drop(["check"], axis =1)
#to avoid multicollinearity, the reason for absence should be dropped
df =df.drop(["Reason for Absence"], axis=1)
#grouping the observation

reason_type_1 = reason.loc[:, 1:14].max(axis=1)
reason_type_2 = reason.loc[:, 15:17].max(axis=1)
reason_type_3 = reason.loc[:, 18:21 ].max(axis=1)
reason_type_4 = reason.loc[:, 22:28].max(axis =1)

# print(reason_type_1)
# print(reason_type_2)
# print(reason_type_3)
# print(reason_type_4)

#concatenation in python => step three
df = pd.concat([df,reason_type_1,reason_type_2,reason_type_3,reason_type_4], axis =1)
#
#assigning meaningful names to the groups
column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
 'Daily Work Load Average', 'Body Mass Index' ,'Education', 'Children', 'Pets',
 'Absenteeism Time in Hours', 'Reason 1', 'Reason 2', 'Reason 3', 'Reason 4']

#used the output to define a new variable column names
df.columns = column_names
# print(df.columns.values)

#creating a checkpoint in pandas
df_reason_mod = df.copy()
df_reason_mod # to be reffered to, instead of re-running the code from the beginning
# it refers to storing the current value of the code than the content of a variable

#analysis of the date column

#there is need to convert the date value to timestamp
df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], format="%d/%m/%Y")
# print(df_reason_mod)
# print(type(df_reason_mod['Date']))
# print(df_reason_mod.info())

#extracting the month value
# print(df_reason_mod['Date'][0].month)
lists_month =[]
for i in range(df_reason_mod.shape[0]): #in order not to hard code the values
    lists_month.append(df_reason_mod["Date"][i].month)


df_reason_mod["Month value"] = lists_month
# print(df_reason_mod.head(20))
list_week = []
for i in range(df_reason_mod.shape[0]):
    list_week.append(df_reason_mod['Date'][i].weekday())

# print(list_week)
df_reason_mod["week value"] = list_week
# print(df_reason_mod)

def week_to_days(date_value):
    return date_value.weekday()

# week = week_to_days(df_reason_mod['Date'])
# print(week)

df_reason_mod =df_reason_mod.drop(['Date'], axis=1)
#creating another checkpoint
df_reason_date_mod =df_reason_mod.copy()
# print(df_reason_date_mod)
df_reason_date_mod['Education'] = df_reason_date_mod['Education'].map({1:0, 2:1, 3:1, 4:1})

# print(df_reason_date_mod)

#final checkpoint
df_preprocessed = df_reason_date_mod.copy()

#analytical tool used to solve the business tasks => A model
#software component containing the code that would execute the model => module
# importing the module

from absenteeism_module import * 
#applying the module developed by data scientist, mathematicians, programmers and ml engineers
