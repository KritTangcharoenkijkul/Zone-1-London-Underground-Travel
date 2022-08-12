from pyswip import Prolog
import requests
import json



prolog = Prolog()
prolog.consult("astar_nextstation.pl")
prolog.consult("location.pl")
prolog.consult("mon_fri_75PM_8PM.pl")


station_list = "paddington_b,edgwareroad_b,marylebone_b,bakerstreet_b,regentspark_b,oxfordcircus_b,piccadillycircus_b,charingcross_b,embankment_b,waterloo_b,lambethnorth_b,elephantcastle_b,paddington_h,edgwareroad_h,bakerstreet_h,greatportlandstr_h,eustonsquare_h,kingscross_h,farringdon_h,barbican_h,moorgate_h,liverpoolstreet_h,aldgateeast_h,bakerstreet_m,eustonsquare_m,kingscross_m,farringdon_m,barbican_m,moorgate_m,liverpoolstreet_m,aldgatetube_m,nottinghillgate_c,lancastergate_c,marblearch_c,bondstreet_c,oxfordcircus_c,tottenhamcourtroad_c,holborn_c,chancerylane_c,stpauls_c,bankmonument_c,liverpoolstreet_cearlscourt_p,gloucesterroad_p,southkensington_p,knightsbridge_p,hydeparkcorner_p,greenpark_p,piccadillycircus_p,leicestersquare_p,coventgarden_p,holborn_p,russellsquare_p,kingscross_pedgwareroad_d,paddington_d,bayswater_d,nottinghillgate_d,highstreetkensington_d,earlscourt_d,gloucesterroad_d,southkensington_d,sloanesquare_d,victoria_d,stjamesspark_d,westminster_d,embankment_d,temple_d,blackfriars_d,mansionhouse_d,cannonstreet_d,bankmonument_d,towerhill_d,aldgateeast_d,edgwareroad_o,paddington_o,bayswater_o,nottinghillgate_o,highstreetkensington_o,earlscourt_o,gloucesterroad_o,southkensington_o,sloanesquare_o,victoria_o,stjamesspark_o,westminster_o,embankment_o,temple_o,blackfriars_o,mansionhouse_o,cannonstreet_o,bankmonument_o,towerhill_o,bakerstreet_o,greatportlandstr_o,eustonsquare_o,kingscross_o,farringdon_o,barbican_o,moorgate_o,liverpoolstreet_o,aldgatetube_o,bakerstreet_j,bondstreet_j,greenpark_j,westminster_j,waterloo_j,southwark_j,londonbridge_j,vauxhall_v,pimlico_v,victoria_v,greenpark_v,oxfordcircus_v,warrenstreet_v,euston_v,kingscross_v,waterloo_n,embankment_n,charingcross_n,leicestersquare_n,tottenhamcourtroad_n,goodgestreet_n,warrenstreet_n,euston_n,morningtoncrescent_n,kingscross_n,angel_n,oldstreet_n,moorgate_n,bankmonument_n,londonbridge_n,borough_n,elephantcastle_n"
station_list = station_list.split(",")

start = "paddington_b"
destination = "elephantcastle_b"
astar_query = "astar("+start+","+destination+ ",PATH,COST)." ## ASTAR
shortest_path_result = list(prolog.query(astar_query))

path_list = []
print(start,destination)
for i in range(len(shortest_path_result[0]['PATH'])):
    path_list.append(str(shortest_path_result[0]['PATH'][i]))

print(str(path_list))
print(str(shortest_path_result[0]['COST']))
'''
for i in range(len(station_list)):
    for j in range(len(station_list)):
        if(station_list[i] != station_list[j]):
            start = station_list[i]
            destination = station_list[j]
        
            astar_query = "astar("+start+","+destination+ ",PATH,COST)." ## ASTAR
            shortest_path_result = list(prolog.query(astar_query))

            path_list = []
            print(start,destination)
            for i in range(len(shortest_path_result[0]['PATH'])):
                path_list.append(str(shortest_path_result[0]['PATH'][i]))

            print(str(path_list))
            print(str(shortest_path_result[0]['COST']))

'''

'''
def getShortestPath(start,destination):
        
    prolog = Prolog()
    prolog.consult("astar_nextstation.pl")
    prolog.consult("TrainDB/location.pl")

    astar_query = "astar("+start+","+destination+ ",PATH,COST)." ## ASTAR
    shortest_path_result = list(prolog.query(astar_query))

    path_list = []
    for i in range(len(shortest_path_result[0]['PATH'])):
        path_list.append(str(shortest_path_result[0]['PATH'][i]))


    train_path_query = "trainPath("+str(path_list)+", ROW, COL, TRAIN)." ## TRAIN PATH
    train_path_result = list(prolog.query(train_path_query))

    train_path_list = []
    for i in range(len(train_path_result[0]['TRAIN'])):
        train_path_list.append(str(train_path_result[0]['TRAIN'][i]))

  
    ans_list = []
    ans_list.append(path_list)
    ans_list.append(str(shortest_path_result[0]['COST']))
    ans_list.append(train_path_list)
    ans_list.append(str(train_path_result[0]['ROW']))
    ans_list.append(str(train_path_result[0]['COL']))
    return ans_list


getShortestPath("ekkamai","chong_nonsi")
'''
'''
def geocode():
    
    api_key = "AIzaSyDrKpCoO724g4gFzfFrmIw-NqgXeQlKSXk"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key="


def findClosestStation():

    prolog = Prolog()
    prolog.consult("astar_nextstation.pl")

    
    geocode()
    closest_station_query = "findClosestStation("+str(lat)+","+str(lng)+",Station)."
    closest_station_result = list(prolog.query(closest_station_query))
    print(closest_station_query)

    print(str(closest_station_result[0]['Station'][0]))
    print(str(closest_station_result[0]['Station'][1]))
    
'''

