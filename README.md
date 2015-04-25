# ars-API

# Requirements
Python2.7

# Installation

Linux
------
1. Install lxml<br>
  $ apt-get install libxml2-dev libxslt1-dev python-dev<br>
  $ apt-get install python-lxml

2. Put the arsapi.py into the folder of your .py

Windows
--------
http://lxml.de/installation.html

#Notes
This API is not the fastest, since I could not find out a better way than parsing the webpages to get the Data I wanted.

#Functions to use
getData("data") //returns the value of "data"<br>
getAllData() //returns the dictionary with all data<br>

#How to Use
```
from arsapi import SeroARSAPI

api = SeroARSAPI(<StateID>) #This can take a while, since it has to load about 8 webpages and parses them to get all the data

data = api.getData(<Parsed Data>) #getData return False if given Parameter is not known

if data is not False:
    print data
else:
    print("Key was unknown")
```
    
#Parsed Data
*  PE payments
*  Level of progress
*  Other state income
*  Religion
*  PE education
*  Conscription
*  Saving ratio
*  Exports
*  Infrastructure
*  Government purchases
*  Net income
*  Tourism
*  Gross investment
*  New indebtedness
*  Public assets
*  Nominal interest
*  Military
*  PE justice
*  Stock index
*  Health-Regent
*  Migration
*  Mortality rate
*  Elections-Regent
*  Employable persons
*  Taxes on capital revenue
*  Influence-Regent
*  Entertainment
*  Discrimination
*  Pensions
*  Sports
*  Pensioners
*  Public expenditure
*  National debt
*  Int. reputation
*  Gross domestic product
*  Unemployed
*  GDP in $
*  Unionist
*  Tariff
*  Population
*  Acquisition taxes
*  Lifespan
*  Capital crimes
*  Labour Time
*  PE health
*  PE administration
*  Power-Regent
*  Welfare
*  Happiness
*  Total state income
*  PE others
*  Arts
*  Environment
*  PE basic income
*  Health
*  Acquisition taxes revenue
*  Corruption
*  Free time
*  Bureaucracy
*  PE defence
*  Apprentices
*  Area
*  Immigration
*  Automation
*  Economy growth
*  Money supply
*  Payment of interest
*  Exchange rate
*  Excise taxes
*  Petty offenses
*  PE projects
*  Birthrate
*  Population density
*  PE pensions
*  Animal rights
*  Statism
*  Imports
*  PE subsidies
*  Private consumption
*  Excise taxes revenue
*  Nuclear power
*  Children
*  Ground price
*  PE welfare
*  Popularity-Regent
*  PE environment
*  Living costs
*  Regent
*  PE family
*  Capital
*  Civil rights
*  GINI-Coefficient
*  Standard of knownledge
*  Shadow economy
*  Statesname
*  Elections-Left-Regent
*  Int. reputation-Regent
*  Starved to death
*  Tariff revenue
*  Tax burden
*  Taxes on capital
*  Real GDP
*  Commodity index
*  Age-Regent
*  Equality of opportunity
*  Contingent of immigrants
*  Basic income
*  Inflation
*  Staatenklasse