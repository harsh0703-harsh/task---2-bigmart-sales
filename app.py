from flask import Flask, render_template, request

import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open("random_forest.pkl", 'rb'))
x_values = pickle.load(open("re_x_valuues.pkl", 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

##### Item_Weight
        Item_Weight = request.form['Item_Weight']

##### Item_Fat_Content
        Item_Fat_Content=request.form['Item_Fat_Content']
        if(Item_Fat_Content=='Low Fat'):
            Low_Fat=1
            Regular=0
        else:
            Low_Fat=0
            Regular=1

###### Item_Visibility
        Item_Visibility=float(request.form['Item_Visibility'])
        Item_Visibility=np.sqrt(Item_Visibility)

        Item_Type=request.form['Item_Type']
        if(Item_Type=="Dairy"):
            Item_Type_Dairy=1
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
  #kardiyo          Baking_Goods=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Soft Drinks"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=1
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=='Meat'):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=1
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Fruits and Vegetables"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=1
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Household"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=1
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Baking Goods"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Snack Foods"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=1
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Frozen Foods"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=1
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Breakfast"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=1
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Health and Hygiene"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=1
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Hard Drinks"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=1
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Canned"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=1
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Breads"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=1
            Starchy_Foods=0
            Others=0
            Seafood=0
        elif(Item_Type=="Starchy Foods"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=1
            Others=0
            Seafood=0
        elif(Item_Type=="Others"):
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=1
            Seafood=0
        else:
            Item_Type_Dairy=0
            Item_Type_Soft_Drinks=0
            Item_Type_Meat=0
            Fruits_and_Vegetables=0
            Household=0
            Snack_Foods=0
            Frozen_Foods=0
            Breakfast=0
            Health_and_Hygiene=0
            Hard_Drinks=0
            Canned=0
            Breads=0
            Starchy_Foods=0
            Others=0
            Seafood=1

### Item_MRP
        Item_MRP=float(request.form['Item_MRP'])

### Outlet_Establishment_Year
        Outlet_Establishment_Year=int(request.form['Outlet_Establishment_Year'])

## Outlet Location Type
        Outlet_Location_Type= request.form['Outlet_Location_Type']
        if(Outlet_Location_Type=="Tier 1"):
            Tier2=0
            Tier3=0
        elif(Outlet_Location_Type=="Tier 2"):
            Tier2=1
            Tier3=0
        else:
            Tier2=0
            Tier3=1


## Outlet Size
        Outlet_Size=request.form['Outlet_Size']
        if(Outlet_Size=="Medium"):
            Value=1
        elif(Outlet_Size=="Small"):
            Value=2
        else:
            Value=0

        Outlet_Type = request.form['Outlet_Type']

        if(Outlet_Type=="Supermarket Type1"):
            SupermarketType1 =1 
            SupermarketType2 =0
            SupermarketType3 =0
        elif(Outlet_Type=="Supermarket Type2"):
            SupermarketType1 =0 
            SupermarketType2 =1
            SupermarketType3 =0
        elif(Outlet_Type=="Supermarket Type3"):
            SupermarketType1 =0 
            SupermarketType2 =0
            SupermarketType3 =1       
        else:
            SupermarketType1 =0 
            SupermarketType2 =0
            SupermarketType3 =0

        standard_to.fit_transform(x_values)
        prediction=model.predict(standard_to.transform([[Item_Weight,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Value,Regular,Breads,Breakfast,Canned,Item_Type_Dairy,Frozen_Foods,Fruits_and_Vegetables,Hard_Drinks,Health_and_Hygiene,Household,Item_Type_Meat,Others,Seafood,Snack_Foods,Item_Type_Soft_Drinks,Starchy_Foods,Tier2,Tier3,SupermarketType1,SupermarketType2,SupermarketType3]]))
        print(prediction)
        return render_template('index.html',Price=prediction)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)