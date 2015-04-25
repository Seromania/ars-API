# -*- coding: cp1252 -*-
import urllib2
import StringIO
import lxml.html as lh
import codecs

class SeroARSAPI(object):
    """Seros Ars-Regendi API"""
    
    def __init__(self, id):
        self.ID = id
        self.StateDict = {}

        self._get_allData()

    def _get_allData(self):

#-----------ERSTE SEITE-----------------
        lastkey = str("")
        response = urllib2.urlopen("http://www.ars-regendi.com/state/%s/haushalt.html" % self.ID)
        content = response.read()
        tree = lh.fromstring(content)
        for key in zip(*[iter(tree.xpath('//td/text()'))]*1):          
            if lastkey == "":
                self.StateDict["Statesname"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Taxes on capital" in lastkey:
                self.StateDict["Taxes on capital"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Taxes on capital revenue" in str(lastkey):
                self.StateDict["Taxes on capital revenue"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Acquisition taxes" in lastkey:
                self.StateDict["Acquisition taxes"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Acquisition taxes revenue" in str(lastkey):
                self.StateDict["Acquisition taxes revenue"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Excise taxes" in lastkey:
                self.StateDict["Excise taxes"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Excise taxes revenue" in str(lastkey):
                self.StateDict["Excise taxes revenue"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Tariff" in lastkey:
                self.StateDict["Tariff"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Tariff revenue" in str(lastkey):
                self.StateDict["Tariff revenue"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Public assets" in str(lastkey):
                self.StateDict["Public assets"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "State income" in str(lastkey):
                self.StateDict["State income"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Other state income" in str(lastkey):
                self.StateDict["Other state income"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Total state income" in str(lastkey):
                self.StateDict["Total state income"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE administration" in str(lastkey):
                self.StateDict["PE administration"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE justice" in str(lastkey):
                self.StateDict["PE justice"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE education" in str(lastkey):
                self.StateDict["PE education"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE family" in str(lastkey):
                self.StateDict["PE family"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE environment" in str(lastkey):
                self.StateDict["PE environment"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE health" in str(lastkey):
                self.StateDict["PE health"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE defence" in str(lastkey):
                self.StateDict["PE defence"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE subsidies" in str(lastkey):
                self.StateDict["PE subsidies"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE others" in str(lastkey):
                self.StateDict["PE others"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE projects" in str(lastkey):
                self.StateDict["PE projects"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE payments" in str(lastkey):
                self.StateDict["PE payments"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Living costs" in str(lastkey):
                self.StateDict["Living costs"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Basic income" in str(lastkey):
                self.StateDict["Basic income"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE basic income" in str(lastkey):
                self.StateDict["PE basic income"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Welfare" in str(lastkey):
                self.StateDict["Welfare"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE welfare" in str(lastkey):
                self.StateDict["PE welfare"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Pensions" in str(lastkey):
                self.StateDict["Pensions"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "PE pensions" in str(lastkey):
                self.StateDict["PE pensions"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Public expenditure" in str(lastkey):
                self.StateDict["Public expenditure"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Money supply" in str(lastkey):
                self.StateDict["Money supply"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "National debt" in str(lastkey):
                self.StateDict["National debt"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Nominal interest" in str(lastkey):
                self.StateDict["Nominal interest"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "Payment of interest" in str(lastkey):
                self.StateDict["Payment of interest"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            if "New indebtedness" in str(lastkey):
                self.StateDict["New indebtedness"] = str(key[0].encode('utf-8')).split()[0].replace(',','')
                
            lastkey = key
        #endfor
        
#------------ZWEITE Seite-------------------
        lastkey = str("")
        response = urllib2.urlopen("http://www.ars-regendi.com/state/%s/detail1.html" % self.ID)
        content = response.read()
        tree = lh.fromstring(content)
        for key in zip(*[iter(tree.xpath('//td/text()'))]*1):
            if "Area" in str(lastkey):
                self.StateDict["Area"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Population density" in str(lastkey):
                self.StateDict["Population density"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Starved to death" in str(lastkey):
                self.StateDict["Starved to death"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Population" in str(lastkey):
                self.StateDict["Population"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Children" in str(lastkey):
                self.StateDict["Children"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Apprentices" in str(lastkey):
                self.StateDict["Apprentices"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Employable persons" in str(lastkey):
                self.StateDict["Employable persons"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Pensioners" in str(lastkey):
                self.StateDict["Pensioners"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Contingent of immigrants" in str(lastkey):
                self.StateDict["Contingent of immigrants"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Unemployed" in str(lastkey):
                self.StateDict["Unemployed"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Birthrate" in str(lastkey):
                self.StateDict["Birthrate"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Mortality rate" in str(lastkey):
                self.StateDict["Mortality rate"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Immigration" in str(lastkey):
                self.StateDict["Immigration"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Migration" in str(lastkey):
                self.StateDict["Migration"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            lastkey = key
            #endfor

#-------------DRITTE SEITE-------------
        count = 1
        response = urllib2.urlopen("http://www.ars-regendi.com/state/%s/detail2.html" % self.ID)
        content = response.read()
        tree = lh.fromstring(content)
        for key in tree.xpath("//img[contains(@src,'http://www.ars-regendi.com/images/content/balken')]/@alt"):
            if count == 1:
                self.StateDict["Standard of knownledge"] = key
                count = 2
                continue
            if count == 3:
                self.StateDict["Level of progress"] = key
                count = 4
                continue
            if count == 5:
                self.StateDict["Automation"] = key
                count = 6
                continue        
            if count == 7:
                self.StateDict["Sports"] = key
                count = 8
                continue        
            if count == 9:
                self.StateDict["Arts"] = key
                count = 10
                continue        
            if count == 11:
                self.StateDict["Entertainment"] = key
                count = 12
                continue
            if count == 13:
                self.StateDict["Tourism"] = key
                count = 14
                continue
            if count == 15:
                self.StateDict["Religion"] = key
                break
            count = count + 1

#--------------VIERTE SEITE--------------
        count = 1
        response = urllib2.urlopen("http://www.ars-regendi.com/state/%s/detail3.html" % self.ID)
        content = response.read()
        tree = lh.fromstring(content)
        for key in tree.xpath("//img[contains(@src,'http://www.ars-regendi.com/images/content/balken')]/@alt"):
            if count == 1:
                self.StateDict["Civil rights"] = key
                count = 2
                continue
            if count == 3:
                self.StateDict["Animal rights"] = key
                count = 4
                continue
            if count == 5:
                self.StateDict["Equality of opportunity"] = key
                count = 6
                continue
            if count == 7:
                self.StateDict["Discrimination"] = key
                count = 8
                continue
            if count == 9:
                self.StateDict["Statism"] = key
                break
            count = count + 1

#--------------FUENFTE SEITE-------------
        lastkey = str("")
        count = 0
        response = urllib2.urlopen("http://www.ars-regendi.com/state/%s/detail4.html" % self.ID)
        content = response.read()
        tree = lh.fromstring(content)
        for key in tree.xpath("//img[contains(@src,'http://www.ars-regendi.com/images/content/balken')]/@alt"):
            if count == 0:
                self.StateDict["Health"] = key
                count = 1
                continue
            if count == 1:
                count = 2
                continue
            if count == 2:
                self.StateDict["Environment"] = key
                count = 3
                continue
            if count == 3:
                count = 4
                continue
            if count == 4:
                self.StateDict["Infrastructure"] = key
                count = 5
                continue
            if count == 5:
                count = 6
                continue
            if count == 6:
                self.StateDict["Tax burden"] = key 
                break

        for key in zip(*[iter(tree.xpath('//td/text()'))]*1):
            if "Lifespan" in str(lastkey):
                self.StateDict["Lifespan"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
            if "Free time" in str(lastkey):
                self.StateDict["Free time"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
            if "Happiness" in str(lastkey):
                self.StateDict["Happiness"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
            

            lastkey = key

#------------SECHSTE SEITE------------
        lastkey = str("")
        count = 1
        response = urllib2.urlopen("http://www.ars-regendi.com/state/%s/detail5.html" % self.ID)
        content = response.read()
        tree = lh.fromstring(content)
        for key in tree.xpath("//img[contains(@src,'http://www.ars-regendi.com/images/content/balken')]/@alt"):
            if count == 1:
                self.StateDict["Petty offenses"] = key
                count = 2
                continue
            if count == 3:
                self.StateDict["Capital crimes"] = key
                count = 4
                continue
            if count == 5:
                self.StateDict["Shadow economy"] = key
                count = 6
                continue
            if count == 7:
                self.StateDict["Corruption"] = key
                count = 8
                continue
            if count == 9:
                self.StateDict["Military"] = key
                break
            count = count + 1
            
        for key in zip(*[iter(tree.xpath('//td/text()'))]*1):
            if "Nuclear power" in str(lastkey):
                self.StateDict["Nuclear power"] = str(key[0].encode('utf-8')).split()[0]
            if "Conscription" in str(lastkey):
                self.StateDict["Conscription"] = str(key[0].encode('utf-8')).split()[0]
            lastkey = key
    

#.-----------SIEBTE SEITE-------------
        lastkey = str("")
        response = urllib2.urlopen("http://www.ars-regendi.com/state/%s/detail6.html" % self.ID)
        content = response.read()
        tree = lh.fromstring(content)
        for key in zip(*[iter(tree.xpath('//td/text()'))]*1):
            #print(key)
            if "Gross domestic product" in str(lastkey):
                self.StateDict["Gross domestic product"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Imports" in str(lastkey):
                self.StateDict["Imports"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Exports" in str(lastkey):
                self.StateDict["Exports"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Private consumption" in str(lastkey):
                self.StateDict["Private consumption"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Government purchases" in str(lastkey):
                self.StateDict["Government purchases"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Gross investment" in str(lastkey):
                self.StateDict["Gross investment"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Net income" in str(lastkey):
                self.StateDict["Net income"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Living costs" in str(lastkey):
                self.StateDict["Living costs"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Labour Time" in str(lastkey):
                self.StateDict["Labour Time"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Exchange rate" in str(lastkey):
                self.StateDict["Exchange rate"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Nominal interest" in str(lastkey):
                self.StateDict["Nominal interest"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Saving ratio" in str(lastkey):
                self.StateDict["Saving ratio"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Inflation" in str(lastkey):
                self.StateDict["Inflation"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Economy growth" in str(lastkey):
                self.StateDict["Economy growth"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Stock index" in str(lastkey):
                self.StateDict["Stock index"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Money supply" in str(lastkey):
                self.StateDict["Money supply"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Capital" in str(lastkey):
                self.StateDict["Capital"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Ground price" in str(lastkey):
                self.StateDict["Ground price"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Commodity index" in str(lastkey):
                self.StateDict["Commodity index"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "GDP in $" in str(lastkey):
                self.StateDict["GDP in $"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Real GDP" in str(lastkey):
                self.StateDict["Real GDP"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
            
            lastkey = key

#------------ACHTE SEITE-----------
        lastkey = str("")
        count = 1
        response = urllib2.urlopen("http://www.ars-regendi.com/state/%s/detail7.html" % self.ID)
        content = response.read()
        tree = lh.fromstring(content)
        for key in tree.xpath("//img[contains(@src,'http://www.ars-regendi.com/images/content/balken')]/@alt"):
            if count == 1:
                self.StateDict["Bureaucracy"] = key
                count = 2
                continue
            if count == 3:
                self.StateDict["Int. reputation"] = key
                count = 4
                break
            count = count + 1

        for key in zip(*[iter(tree.xpath('//td/text()'))]*1):
            if "Unionist" in str(lastkey):
                self.StateDict["Unionist"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
            if "GINI-Coefficient" in str(lastkey):
                self.StateDict["GINI-Coefficient"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
            lastkey = key

#------------REGENT SEITE---------
        lastkey = str("")
        response = urllib2.urlopen("http://www.ars-regendi.com/state/%s/regent.html" % self.ID)
        content = response.read()
        tree = lh.fromstring(content)
        for key in zip(*[iter(tree.xpath('//td/text()'))]*1):
            if "Age" in str(lastkey):
                self.StateDict["Age-Regent"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Popularity" in str(lastkey):
                self.StateDict["Popularity-Regent"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Power" in str(lastkey):
                self.StateDict["Power-Regent"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Int. reputation" in str(lastkey):
                self.StateDict["Int. reputation-Regent"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Health" in str(lastkey):
                self.StateDict["Health-Regent"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Influence" in str(lastkey):
                self.StateDict["Influence-Regent"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                
            if "Elections" in str(lastkey):
                self.StateDict["Elections-Left-Regent"] = str(key[0].encode('utf-8')).split()[0].split()[0].replace(',','')
                self.StateDict["Elections-Regent"] = str(key[0].encode('utf-8')).split()[8].split()[0].replace('%','')
                
            lastkey = key
        self.StateDict["Regent"] = tree.xpath("//a[contains(@href,'http://forum.ars-regendi.com/member.php?action=profile')]/text()")[0]

        #self._print_all_data()

    def _print_all_data(self):
        for k,v in self.StateDict.items():
            print k, ': ', v

    def getData(self, string):
        if self.StateDict.has_key(string) == True:
            return self.StateDict[string]
        else:
            return False

    def getAllData(self):
        return self.StateDict
