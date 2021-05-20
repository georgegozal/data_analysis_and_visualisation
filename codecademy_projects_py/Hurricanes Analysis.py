#!/usr/bin/env python
# coding: utf-8

# In[55]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# write your update damages function here:
conversion = {"M": 1000000,
              "B": 1000000000}

def damage_con(dmg,con):
    new_d =[]
    for d in dmg:
        if d =='Damages not recorded':
            new_d.append(d)
        if d[-1] =='M':
            new_d.append(float(d[:-1])*con['M'])
        if d[-1] == 'B':
            new_d.append(float(d[:-1])*con['B'])
    return new_d      
# test function by updating damages

updated_damages = damage_con(damages,conversion)

# 2 
# Create a Table

# Create and view the hurricanes dictionary
def mydict(n,m,y,mx,aa,dm,dth):
    a = list(zip(n,m,y,mx,aa,dm,dth))
    mylist = []
    for item in a:
        mydic={}
        mydic['Name']=item[0]
        mydic['Month']=item[1]
        mydic['Year']=item[2]
        mydic['Max Sustained Wind']=item[3]
        mydic['Areas Affected']=item[4]
        mydic['Damage']=item[5]
        mydic['Death']=item[6]    
        mylist.append(mydic)
    return dict(zip(n,mylist))
    
dict_by_name = mydict(names,months,years,max_sustained_winds, areas_affected, updated_damages, deaths)


# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key

def mydict_year(n,m,y,mx,aa,dm,dth):
    a = list(zip(n,m,y,mx,aa,dm,dth))
    mylist = []
    for item in a:
        mydic={}
        mydic['Name']=item[0]
        mydic['Month']=item[1]
        mydic['Year']=item[2]
        mydic['Max Sustained Wind']=item[3]
        mydic['Areas Affected']=item[4]
        mydic['Damage']=item[5]
        mydic['Death']=item[6]    
        mylist.append(mydic)
        yy=[str(i) for i in y]
    return dict(zip(yy,mylist))
    
dict_by_year= mydict_year(names,months,years,max_sustained_winds, areas_affected, updated_damages, deaths)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in

def count_hur(aaf):
    mydict={}
    mybiglist=[]
    
    for lst in aaf:
        for i in lst:
            mybiglist.append(i)
            
    names=set(mybiglist)
    
    for n in names:
        if n in mybiglist:
            counts=mybiglist.count(n)
            mydict[n]=counts

    return mydict
    
       
arreas_affected_count=count_hur(areas_affected)



# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
max_area = 'Central America'
max_area_count = 0

def max_counts(ma,mac,aafc):
    for k in aafc.keys():
        if aafc[k] >mac:
            ma = k
            mac = aafc[k]
    return ma,mac
area_max_hur = max_counts(max_area,max_area_count,arreas_affected_count)



# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths


def max_deaths(n,d):
    d_max = 0
    
    for num in d:
        if num > d_max:
            d_max=num
    n_max = n[d.index(d_max)]        
    return n_max,d_max
    
deadliest_hur = max_deaths(names,deaths)




# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def categorize_by_deaths(nm,dths,ms):
    hurricanes_by_mortality = {0: 0}
    
    for i in range(1,5):
        a = [num for num in dths if num < ms[i]]
        a.sort()
        mylist={}
        
        for item in a:
            indx=dths.index(item)
            mylist[nm[indx]]=item
        hurricanes_by_mortality[i]=mylist
        for i in a:
            dths.remove(i)

    return hurricanes_by_mortality

hurricanes_by_mortality=categorize_by_deaths(names,deaths,mortality_scale)





# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


def highest_damage(nm,upd):
    damage=0.0
    for num in upd:
        if num =='Damages not recorded':
            continue
        if num > damage:    
            damage=num
    name = nm[upd.index(damage)]
    
    return name,damage

highest_damage_hur,highest_damage_cost=highest_damage(names,updated_damages)
    

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def categorize_by_damage(nm,upd,dmgsc):
    hurricanes_by_damage = {0: 0}
    
    for i in range(1,5):
        a = [num for num in upd if num !='Damages not recorded' and  num < dmgsc[i]]      
        mylist={}
        a.sort()
        for item in a:
            indx=upd.index(item)
            mylist[nm[indx]]=item
        hurricanes_by_damage[i]=mylist
        for i in a:
            upd.remove(i)

    return hurricanes_by_damage
    
    
hurricanes_by_damage=categorize_by_damage(names,updated_damages,damage_scale) 


# In[ ]:




