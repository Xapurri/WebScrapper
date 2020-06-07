# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:09:48 2020

@author: Xapurri
"""

'Gràcia','Eixample','Gràcia','Horta-Guinardó','Les Corts','Nou Barris','Sant Andreu','Sant Martí','Sarria-Sant Gervasi','Sants-Montjuíc','Ciutat Vella'


import pyautogui as gui, pyperclip, time, keyboard

'''

DretaEixample = 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/la-dreta-de-l-eixample/pagina-'
AntEsqEixample = 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/l-antiga-esquerra-de-l-eixample/pagina-'
NovEsqEixample = 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/la-nova-esquerra-de-l-eixample/pagina-'
SagradaFamilia = 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/la-sagrada-familia/pagina-'
SantAntoni = 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/sant-antoni/pagina-'
FortPienc = 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/el-fort-pienc/pagina-'
Gracia = 'https://www.idealista.com/alquiler-viviendas/barcelona/gracia/pagina-'
HortaGuinardo = 'https://www.idealista.com/alquiler-viviendas/barcelona/horta-guinardo/pagina-'
LesCorts = 'https://www.idealista.com/alquiler-viviendas/barcelona/les-corts/pagina-'
NouBarris = 'https://www.idealista.com/alquiler-viviendas/barcelona/nou-barris/pagina-'
SantAndreu = 'https://www.idealista.com/alquiler-viviendas/barcelona/sant-andreu/pagina-'
SantMarti = 'https://www.idealista.com/alquiler-viviendas/barcelona/sant-marti/pagina-'
SGGalvany = 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/sant-gervasi-galvany/pagina-'
PutxetFarro = 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/el-putxet-i-el-farro/pagina-'
SGBonanova = 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/sant-gervasi-la-bonanova/pagina-'
Sarria = 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/sarria/pagina-'
TresTorres = 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/les-tres-torres/pagina-'
Tibidabo = 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/vallvidrera-el-tibidabo-i-les-planes/pagina-'
SantsMontjuic = 'https://www.idealista.com/alquiler-viviendas/barcelona/sants-montjuic/pagina-'
CiutatVella = 'https://www.idealista.com/alquiler-viviendas/barcelona/ciutat-vella/'
Raval = 'https://www.idealista.com/alquiler-viviendas/barcelona/ciutat-vella/el-raval/pagina-'
Gotic = 'https://www.idealista.com/alquiler-viviendas/barcelona/ciutat-vella/el-gotic/pagina-'
SantaCaterinaIRibera = 'https://www.idealista.com/alquiler-viviendas/barcelona/ciutat-vella/sant-pere-santa-caterina-i-la-ribera/pagina-'
ciutat-vella/la-barceloneta = https://www.idealista.com/alquiler-viviendas/barcelona/ciutat-vella/la-barceloneta/pagina-
'''


nameDistrito = ['Tibidabo','Gracia','Sants-Montjuic','La Barceloneta','El Raval','El Gotic', 'Sant Pere,Santa Caterina','Sant Gervasi-Galvany','El Putxet i el Farro','La Bonanova','Sarria','Les Tres Torres','La Dreta de Eixample','La nova esquerra de Eixample','La Nova Esquerra Eixample','Sagrada Familia','Sant antoni','El Fort Pienc','Horta-Guinardo','Les Corts','Nou Barris','Sant Andreu','Sant MArti']
Distritos = ['sarria-sant-gervasi/vallvidrera-el-tibidabo-i-les-planes','Gracia','Sants-Montjuic', 'ciutat-vella/la-barceloneta','ciutat-vella/el-raval', 'ciutat-vella/el-gotic', 'ciutat-vella/sant-pere-santa-caterina-i-la-ribera', 'sarria-sant-gervasi/sant-gervasi-galvany', 'sarria-sant-gervasi/el-putxet-i-el-farro', 'sarria-sant-gervasi/sant-gervasi-la-bonanova', 'sarria-sant-gervasi/Sarria', 'sarria-sant-gervasi/les-tres-torres', 'eixample/la-dreta-de-l-eixample', 'eixample/l-antiga-esquerra-de-l-eixample', 'eixample/la-nova-esquerra-de-l-eixample', 'eixample/la-sagrada-familia', 'eixample/sant-antoni', 'eixample/el-fort-pienc', 'horta-guinardo', 'les-corts', 'nou-barris', 'sant-andreu', 'sant-marti']
Distritos_links = ['https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/vallvidrera-el-tibidabo-i-les-planes/pagina-','https://www.idealista.com/alquiler-viviendas/barcelona/gracia/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/sants-montjuic/pagina-','https://www.idealista.com/alquiler-viviendas/barcelona/ciutat-vella/la-barceloneta/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/ciutat-vella/el-raval/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/ciutat-vella/el-gotic/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/ciutat-vella/sant-pere-santa-caterina-i-la-ribera/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/sant-gervasi-galvany/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/el-putxet-i-el-farro/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/sant-gervasi-la-bonanova/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/sarria/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/sarria-sant-gervasi/les-tres-torres/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/la-dreta-de-l-eixample/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/l-antiga-esquerra-de-l-eixample/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/la-nova-esquerra-de-l-eixample/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/la-sagrada-familia/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/sant-antoni/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/eixample/el-fort-pienc/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/horta-guinardo/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/les-corts/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/nou-barris/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/sant-andreu/pagina-', 'https://www.idealista.com/alquiler-viviendas/barcelona/sant-marti/pagina-']
finurl = '.htm?ordenado-por=precios-asc'

Distrito_id = 0
raw_data = ''
status = 1
Excepcion_Distritos = ['sarria-sant-gervasi/','eixample/','ciutat-vella/']
#--------------------#

def auto_txt_save():
    with open(nameDistrito[dis]+'.txt','a+',encoding="utf-8") as f:   
      f.write(str(raw_data) + '\n')

def tor_scrapper():
    global raw_data
    keyboard.press_and_release('ctrl+shift+i')
    gui.sleep(0.5)
    gui.click(1340,341)
    time.sleep(0.5)
    gui.click(button='right')
    time.sleep(0.5)
    gui.click(1399,577)
    time.sleep(0.5)
    gui.click(1679,586)
    time.sleep(0.5)
    raw_data = pyperclip.paste()
    auto_txt_save()
    keyboard.press_and_release('ctrl+shift+i')



for dis in range(len(Distritos)):
    indent=1
    status = 1
    row = 0
    while status == 1:
        
        url=Distritos_links[dis]+str(indent)+finurl
        pyperclip.copy(url)
        time.sleep(3)
        #gui.click(1018,1056)
        time.sleep(3)
        gui.click(95,195)
        gui.click(492,65)
        keyboard.press_and_release('ctrl+v, enter')
        time.sleep(10)
        
        
        #checks if new url is the same as the one pasted

        gui.click(95,195)   #clica en un sitio irrelevante
        time.sleep(0.5)
        gui.click(818,67, button='right')
        time.sleep(0.5)
        gui.click(845,126)
        time.sleep(0.5)
       
        check_url = pyperclip.paste()

        if url == check_url:
            print('Coinciden')
            
            status = 1
        else:
            lowDistrito = Distritos[dis]
            new_url =  'https://www.idealista.com/alquiler-viviendas/barcelona/'+ lowDistrito.lower() + '/?ordenado-por=precios-asc'
            if check_url == new_url and row ==0:
                print('Primera Página')
                status = 1
                row = 1

            else:
                status = 0
                print(Distritos[dis]+' finished')
                break
        indent+=1    
        tor_scrapper()
            

    
    
       
    
    


      
        
    
