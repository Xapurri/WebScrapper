# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:47:44 2020

@author: Xapurri
"""


from bs4 import BeautifulSoup as bs
import re, pandas as pd, os
try:
    os.remove('csv$.txt')
    os.remove('data.xlsx')
    print('Deleted old files\n')
except:
    print('Previous file not found')
    pass
titulo =[]
precio = []
a=1
error = 0
escerror = 0
psa = '\n\n---------------------\n\n'
# old distritos = ['Eixample','Gràcia','Horta-Guinardó','Les Corts','Nou Barris','Sant Andreu','Sant Martí','Sarria-Sant Gervasi','Sants-Montjuíc','Ciutat Vella']
distritos = ['Tibidabo','Gracia','Sants-Montjuic','La Barceloneta','El Raval','El Gotic', 'Sant Pere,Santa Caterina','Sant Gervasi-Galvany','El Putxet i el Farro','La Bonanova','Sarria','Les Tres Torres','La Dreta de Eixample','La nova esquerra de Eixample','La Nova Esquerra Eixample','Sagrada Familia','Sant antoni','El Fort Pienc','Horta-Guinardo','Les Corts','Nou Barris','Sant Andreu','Sant MArti']


#delimitadores
delimiters = ('<','>','title=')
regexPattern = '|'.join(map(re.escape, delimiters))
pricedelimiter = ('"/','/"')
regexPricePattern = '|'.join(map(re.escape, pricedelimiter))

with open('csv$.txt','a+') as file:
    file.write('link$Piso$Precio$Habitaciones$m2$Escalera$Inmobiliaria\n')

url= 'www.idealista.es/'

def auto(distr):
    titulo = []
    escerror = 0
    a=1
    global error
    with open(distritos[distr]+'.txt','r',encoding='utf-8') as file:
        datos=bs(file, features = 'lxml')
        todo = datos.find_all('div', attrs={"class":"item-info-container"}) 
        for line in todo:
            titulo+=[line]
        for i in range(len(titulo)):
            try:
                name = titulo[a].find_all('a', attrs={'class':'item-link'})
                name2 = re.split(regexPattern, str(name))
                link = re.split(regexPricePattern, str(name))
                precio = titulo[a].find_all('span', attrs={'class':'item-price h2-simulated'})
                precio2 = re.split(regexPattern, str(precio))            
                tmn = titulo[a].find_all('span', attrs={'class':'item-detail'})
                tmn2 = re.split(regexPattern, str(tmn))
                if int(tmn2[2]) > 14:
                    m2 = tmn2[2]
                    habitaciones = ' '
                    escalera = tmn2[10]
                else:
                    habitaciones = tmn2[2]
                    m2 = tmn2[10]
                    if len(tmn2)<18:
                        escalera = []
                        
                    elif tmn2[18] == ' ':
                        escalera = tmn2[20]
                    else:
                    
                        escalera = tmn2[18]
                    
    
                try:
                    inmo = titulo[a].find_all('a', attrs={'data-markup':'listado::logo-agencia'})
                    inmo = re.split('"',str(inmo))
                except:
                    continue
                a+=1
                '''with open('datos.txt', 'a+', encoding='utf-8') as docu:
                    docu.write(str(url+link[1])+'\n')
                    docu.write(str(name2[3])+'\n')
                    docu.write((precio2[2])+'\n')
                    docu.write(str(tmn3)+'\n')
                    try:
                        docu.write(str(inmo[5])+'\n\n')
                        docu.write('----\n\n')
                    except:
                        docu.write('\n----\n\n')
                        continue'''
                with open('csv$.txt','a+') as csv:
                    csv.write(str(url+link[1])+'$')
                    csv.write(str(name2[3])+'$')
                    csv.write((precio2[2])+'$')
                    #csv.write(str(tmn2)+'$')
                    csv.write(str(habitaciones)+'$')
                    csv.write((m2)+'$')
                    if escalera != []:
                        if escalera == ' con ascensor' or escalera == ' sin ascensor' or escalera =='04 abr ':
                            escalera=''
                        else:
                            z = 1
                        csv.write(str(escalera)+'$')
                    else:
                        escalera = ''
                        csv.write(str(escalera)+'$')
                        escerror+=1
    
                    try:
                        csv.write(str(inmo[5]+'\n'))
                        #docu.write('----\n\n')
                    except:
                        csv.write('\n')
                        continue
                    
            except:
                 a+=1
                 error+=1
                 print('Error in block ',a,', error num:' ,error,'\n')
                 pass
        print(distritos[distr]+' finished!\n')

def excel_maker():

    pd.read_csv('csv$.txt', sep='$', encoding='latin1',dtype='unicode',error_bad_lines=False).to_excel('data.xlsx', sheet_name='sheet1', index=False)
    file = pd.read_csv('csv$.txt', sep='$', encoding='latin1',dtype='unicode',error_bad_lines=False)
    print(psa+'Done!\n')
    print('Rows: '+str(len(file))+'\nTotal Errors: '+str(error)+psa)
    
    
for distr in range(len(distritos)):
    auto(distr)
excel_maker()
