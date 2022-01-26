# Marketing_Campaign_Predictor

An ML based tool to check whether marketing team's campaign resulted in customer's purchase conversion or not


![Tool](results/app.JPG?raw=true "Gradio App")

## Parameters ##

recency - months since last purchase

history - value of the historical purchases in Euros

used_discount - indicates if the customer used a discount before

used_bogo - indicates if the customer used a buy one get one before

zip_code - class of the zip code as Suburban/Urban/Rural

is_referral - indicates if the customer was acquired from referral channel

channel - channels that the customer using, Phone/Web/Multichannel

offer - the offers sent to the customers, Discount/But One Get One/No Offer

conversion - customer conversion(buy or not)

## Machine Learning Implementation ##

https://user-images.githubusercontent.com/47096512/149586974-507cdb29-e197-4f11-870b-0b261a938d54.mp4


F1 score metric obtained is 30% for this imbalanced dataset. (This could be improved by finetuning)

## Logs

![MLFlow](results/mlflow.JPG?raw=true "MLFLow")

## Deployment

![FASTAPI](results/fastapi.JPG?raw=true "FASTAPI")

![Docker](results/Docker.JPG?raw=true "Docker")

## Explainable AI

[please click here](results/dashboard.html)

## Exploratory Data Analysis ##

![EDA1](results/EDA1.png?raw=true "EDA1")

![EDA2](results/EDA2.png?raw=true "EDA2")

![EDA3](results/EDA3.png?raw=true "EDA3")

![EDA4](results/EDA4.png?raw=true "EDA4")

![EDA5](results/EDA5.png?raw=true "EDA5")

![EDA6](results/EDA6.png?raw=true "EDA6")










