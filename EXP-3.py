import pandas as pd

data = {
'Product':['Pen','Book','Bag'],
'Price':[10,50,200],
'Quantity':[5,3,2]
}

sales_data = pd.DataFrame(data)

sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

print(sales_data)
