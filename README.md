This project focus on analyzing retail product returns using Python.
The main goal  of this project is to identify category-wise return trends and understand which product categories have higher return rates.

The analysis is performed using Pandas for data manipulation and Matplotlib for visualization.

🎯 Objectives

Create a sample retail dataset

Perform basic Exploratory Data Analysis (EDA)

Analyze category-wise product returns

Calculate return percentage per category

Visualize results using bar charts

🛠️ Tools & Technologies Used

Python

Pandas – Data analysis and manipulation

Matplotlib – Data visualization

 Google Colab

CSV file format

📂 Dataset Description

The dataset contains the following columns:

Column Name	Description
Order_ID	Unique order identifier
Product_Name	Name of the product
Category	Product category
Sales	Product price
Quantity	Quantity ordered
Returned	Indicates whether product was returned (Yes/No)

A derived column:

Returned_Flag → Yes = 1, No = 0 (used for calculations)

🔍 Project Workflow
1️⃣ Data Creation

A dummy retail dataset is created using a Python dictionary.

The dataset is converted into a Pandas DataFrame.

2️⃣ Saving & Loading Data

The DataFrame is saved as a CSV file.

The CSV file is reloaded to simulate a real-world workflow.

3️⃣ Exploratory Data Analysis (EDA)

Checked data structure using info()

Verified missing values using isnull()

Generated statistical summaries using describe()

4️⃣ Data Transformation

Converted categorical return values (Yes/No) into numerical format (1/0) for analysis.

5️⃣ Category-wise Return Analysis

Calculated total returns per category.

Calculated total orders per category.

Computed return percentage for each category.

6️⃣ Data Visualization

Created a bar chart to visualize category-wise product returns.

📊 Key Insights

Electronics category shows a higher number of returns.

Clothing also has a noticeable return rate.

Furniture products have comparatively fewer returns.

Visualization helps in quickly identifying problematic categories.

📈 Output Visualization

Bar Chart: Category-wise Product Returns
This chart clearly compares the number of returned products across different categories.

🚀 How to Run the Project

Open Google Colab 

Upload the notebook file

Run all cells sequentially

Ensure pandas and matplotlib libraries are installed

pip install pandas matplotlib

📌 Future Improvements

Use a real-world retail dataset

Add monthly or yearly trend analysis

Perform customer-based return analysis

Add more visualizations (pie charts, line charts)

Apply machine learning for return prediction


⭐ Conclusion

This project demonstrates how Python can be used for data analysis and visualization to extract meaningful business insights from retail data.
It is suitable for beginner to intermediate level data analysis projects.
