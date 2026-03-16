import pandas as pd

data = {
'property_id':[1,2,3],
'location':['Chennai','Delhi','Chennai'],
'bedrooms':[3,5,4],
'area':[1200,2000,1500],
'price':[5000000,8000000,6500000]
}

property_data = pd.DataFrame(data)

print(property_data.groupby('location')['price'].mean())

print("Bedrooms >4")
print(property_data[property_data['bedrooms']>4])

print("Largest Area Property")
print(property_data.loc[property_data['area'].idxmax()])
