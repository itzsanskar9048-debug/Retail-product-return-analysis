

import pandas as pd

# Create dataset
data = {
    "Order_ID": [1,2,3,4,5,6,7,8,9,10],
    "Product_Name": ["Mobile","Shirt","Laptop","Jeans","Sofa",
                     "TV","Shoes","Table","Headphones","Kurti"],
    "Category": ["Electronics","Clothing","Electronics","Clothing","Furniture",
                 "Electronics","Clothing","Furniture","Electronics","Clothing"],
    "Sales": [15000,1200,55000,2000,32000,40000,2500,15000,3000,1800],
    "Quantity": [1,2,1,1,1,1,1,1,1,2],
    "Returned": ["Yes","No","Yes","Yes","No","No","Yes","No","Yes","Yes"]
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv("retail_data.csv", index=False)

df

     
Order_ID	Product_Name	Category	Sales	Quantity	Returned
0	1	Mobile	Electronics	15000	1	Yes
1	2	Shirt	Clothing	1200	2	No
2	3	Laptop	Electronics	55000	1	Yes
3	4	Jeans	Clothing	2000	1	Yes
4	5	Sofa	Furniture	32000	1	No
5	6	TV	Electronics	40000	1	No
6	7	Shoes	Clothing	2500	1	Yes
7	8	Table	Furniture	15000	1	No
8	9	Headphones	Electronics	3000	1	Yes
9	10	Kurti	Clothing	1800	2	Yes

df = pd.read_csv("retail_data.csv")
df.head()

     
Order_ID	Product_Name	Category	Sales	Quantity	Returned
0	1	Mobile	Electronics	15000	1	Yes
1	2	Shirt	Clothing	1200	2	No
2	3	Laptop	Electronics	55000	1	Yes
3	4	Jeans	Clothing	2000	1	Yes
4	5	Sofa	Furniture	32000	1	No

df.info()

     
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 6 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   Order_ID      10 non-null     int64 
 1   Product_Name  10 non-null     object
 2   Category      10 non-null     object
 3   Sales         10 non-null     int64 
 4   Quantity      10 non-null     int64 
 5   Returned      10 non-null     object
dtypes: int64(3), object(3)
memory usage: 612.0+ bytes

# Check missing values
df.isnull().sum()

# Convert Returned column to numeric
df["Returned_Flag"] = df["Returned"].map({"Yes": 1, "No": 0})

df

     
Order_ID	Product_Name	Category	Sales	Quantity	Returned	Returned_Flag
0	1	Mobile	Electronics	15000	1	Yes	1
1	2	Shirt	Clothing	1200	2	No	0
2	3	Laptop	Electronics	55000	1	Yes	1
3	4	Jeans	Clothing	2000	1	Yes	1
4	5	Sofa	Furniture	32000	1	No	0
5	6	TV	Electronics	40000	1	No	0
6	7	Shoes	Clothing	2500	1	Yes	1
7	8	Table	Furniture	15000	1	No	0
8	9	Headphones	Electronics	3000	1	Yes	1
9	10	Kurti	Clothing	1800	2	Yes	1

df.describe()

     
Order_ID	Sales	Quantity	Returned_Flag
count	10.00000	10.000000	10.000000	10.000000
mean	5.50000	16750.000000	1.200000	0.600000
std	3.02765	19198.683404	0.421637	0.516398
min	1.00000	1200.000000	1.000000	0.000000
25%	3.25000	2125.000000	1.000000	0.000000
50%	5.50000	9000.000000	1.000000	1.000000
75%	7.75000	27750.000000	1.000000	1.000000
max	10.00000	55000.000000	2.000000	1.000000

# Total returns per category
category_returns = df.groupby("Category")["Returned_Flag"].sum()
category_returns

     
Returned_Flag
Category	
Clothing	3
Electronics	3
Furniture	0

dtype: int64

# Total orders per category
category_total = df.groupby("Category")["Order_ID"].count()

# Return percentage
return_percentage = (category_returns / category_total) * 100
return_percentage

     
0
Category	
Clothing	75.0
Electronics	75.0
Furniture	0.0

dtype: float64

import matplotlib.pyplot as plt

category_returns.plot(kind="bar")
plt.title("Category-wise Product Returns")
plt.xlabel("Category")
plt.ylabel("Number of Returns")
plt.show()

     

Most of the returned products are from clothing cateogry
Electronics cateogry has moderate returned products
Furniture cateory has least returned products
