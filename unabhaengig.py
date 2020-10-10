from math import ceil
import pandas as pd
import numpy as np
import json       
import pathlib
    
tabelleEigenverbrauch = json.loads(pathlib.Path( "./data/eigenverbrauch.json").read_text())
tabelleAutarkie = json.loads(pathlib.Path( "./data/autarkie.json").read_text())

#Hilfsfunktion zum Berechnen des Verhältnisses PV/Last
def SetRatioPV(last, pv):
    ratio_pv = (pv/last*1000)
    return ratio_pv
           
#Hilfsfunktion zum Berechnen des Verhältnisses Bat/Last
def SetRatioBat(last, bat):
    ratio_bat = (bat/last*1000)
    return ratio_bat
              
#Funktion zum Interpolieren aus Matrix
def SucheWertAusMatrix(table, x, y):
                       
    #x-Index suchen
    xi = ceil(x/0.0625)+1                                            
    #y-Index suchen
    yi = ceil(y/0.0625)+1                      
                       
    obenLinks = table[yi-1][xi-1]
    obenRechts = table[yi-1][xi]
    untenLinks = table[yi][xi-1]
    untenRechts = table[yi][xi]
                       
    xInterpoliertOben = obenLinks + (x-table[0][xi-1])*(obenRechts-obenLinks)/(table[0][xi]-table[0][xi-1])
    xInterpoliertUnten = untenLinks + (x-table[0][xi-1])*(untenRechts-untenLinks)/(table[0][xi]-table[0][xi-1])
    if(yi>1):
        interpoliert = xInterpoliertOben + (y-table[yi-1][0]) * (xInterpoliertUnten-xInterpoliertOben)/(table[yi][0]-table[yi-1][0])
        return interpoliert
                        
    return xInterpoliertUnten
           
#Funktion zum Ermitteln des Eigenverbrauchsanteils
def GetEigenverbrauch(ratio_pv, ratio_bat):
    eigen = SucheWertAusMatrix(tabelleEigenverbrauch, ratio_pv, ratio_bat)
    return eigen
           
#Funktion zum Ermitteln des Autarkiegrades
def GetAutarkie(ratio_pv, ratio_bat):
    autark = SucheWertAusMatrix(tabelleAutarkie, ratio_pv, ratio_bat)
    return autark
           
#Funktion zum Ermitteln des Direktsanteils vom Eigenverbrauch
def GetDirektverbrauchEigen(ratio_pv):
    dir_eigen = SucheWertAusMatrix(tabelleEigenverbrauch, ratio_pv, 0)
    return dir_eigen
           
#Funktion zum Ermitteln des Direktsanteils vom Autarkiegrad
def GetDirektverbrauchAutarkie(ratio_pv):
    dir_autarkie = SucheWertAusMatrix(tabelleAutarkie, ratio_pv, 0)
    return dir_autarkie

if __name__ == "__main__":
    last_list = list(range(2000,10000,500))
    pv_list = np.arange(1.0, 20.0,0.5).tolist()
    bat_list = np.arange(0.0, 20.0, 0.52).tolist()

    length = len(last_list)*len(pv_list)*len(bat_list)

    i = 1

    df = pd.DataFrame(columns = ["Stromverbrauch", "PV-Leistung", "Batterie", "Eigenverbrauch", "Autarkie"])

    for last in last_list:
        for pv in pv_list:
            for bat in bat_list:
                print("Fortschritt: ","{:.2f}".format(i/length*100),"%")
                ratio_pv = SetRatioPV(last, pv)
                ratio_bat = SetRatioBat(last, bat)

                eigenverbrauch = GetEigenverbrauch(ratio_pv, ratio_bat)
                #print("Eigenverbrauch: ", eigenverbrauch)
                autarkie = GetAutarkie(ratio_pv, ratio_bat)
                #print("Autarkie: ", autarkie)
                dir_eigen = GetDirektverbrauchEigen(ratio_pv)
                dir_aut = GetDirektverbrauchAutarkie(ratio_pv)

                new = {
                    "Stromverbrauch": last,
                    "PV-Leistung": pv,
                    "Batterie": bat,
                    "Eigenverbrauch": eigenverbrauch,
                    "Autarkie": autarkie
                }
                df = df.append(new, ignore_index = True)
                i += 1
    df.to_csv("./output/all_data.csv")
    df.to_excel("./output/all_data.xlsx")