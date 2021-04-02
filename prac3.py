import pandas as pd
d ={'col1':[1,2,3],'col2':[4,5,6]}
df =  pd.DataFrame(data =d)
print(df)
print(df.dtypes)
df = pd.DataFrame(data = d,dtype = float)
print(df.dtypes)
print(df)

#Accessing single value from a data frame

data = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(data = data,columns = ['col1','col2','col3'],dtype = float,index=[1,2,3])
print(df)
#returns value at a specific location
print(df.at[1,'col2'])
#returns size
print(df.size)
#returns all values
print(df.values)
#Return a tuple representing the dimensionality of the DataFrame.
print(df.shape)
#Access a group of rows and columns by label(s) or a boolean array.
print(df.loc[2])