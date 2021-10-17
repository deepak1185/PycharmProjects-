import pandas

#df1 = pandas.DataFrame([[2,3,6],[10,20,30]])
#df1


df1=pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","value"],index=["first","second"])
print(df1)

df1

# df2=pandas.DataFrame([[{}]])
# type(df1)
# print(dir(df1))
print(df1.mean())

