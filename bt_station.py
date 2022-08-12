#Bakerloo Line (Brown)
def baker_station_list():
    baker_station = [
        "paddington_b",
        "edgwareroad_b",
        "marylebone_b",
        "bakerstreet_b",
        "regentspark_b",
        "oxfordcircus_b",
        "piccadillycircus_b",
        "charingcross_b",
        "embankment_b",
        "waterloo_b",
        "lambethnorth_b",
        "elephantcastle_b"]

    return baker_station

#hammers line (Pink)
def hammers_station_list():
    hammers_station = [
        "paddington_h",
        "edgwareroad_h",
        "bakerstreet_h",
        "greatportlandstr_h",
        "eustonsquare_h",
        "kingscross_h",
        "farringdon_h",
        "barbican_h",
        "moorgate_h",
        "liverpoolstreet_h",
        "aldgateeast_h"]
    return hammers_station

#Metro Line (Purple)
def metro_station_list():
    metro_station = [
        "bakerstreet_m",
        "greatportlandstr_m",
        "eustonsquare_m",
        "kingscross_m",
        "farringdon_m",
        "barbican_m",
        "moorgate_m",
        "liverpoolstreet_m",
        "aldgatetube_m"]
    return metro_station

#Central Line (Red)
def central_station_list():
    central_station = [
        "nottinghillgate_c",
        "queensway_c",
        "lancastergate_c",
        "marblearch_c",
        "bondstreet_c",
        "oxfordcircus_c",
        "tottenhamcourtroad_c",
        "holborn_c",
        "chancerylane_c",
        "stpauls_c",
        "bankmonument_c",
        "liverpoolstreet_c"]
    return central_station

#Piccadilly Line (Dark Blue)
def picca_station_list():
    picca_station = [
        "earlscourt_p",
        "gloucesterroad_p",
        "southkensington_p",
        "knightsbridge_p",
        "hydeparkcorner_p",
        "greenpark_p",
        "piccadillycircus_p",
        "leicestersquare_p",
        "coventgarden_p",
        "holborn_p",
        "russellsquare_p",
        "kingscross_p"
        ]
    return picca_station

#District Line (Green)
def district_station_list():
    district_station = [
        "edgwareroad_d",
        "paddington_d",
        "bayswater_d",
        "nottinghillgate_d",
        "highstreetkensington_d",
        "earlscourt_d",
        "gloucesterroad_d",
        "southkensington_d",
        "sloanesquare_d",
        "victoria_d",
        "stjamesspark_d",
        "westminster_d",
        "embankment_d",
        "temple_d",
        "blackfriars_d",
        "mansionhouse_d",
        "cannonstreet_d",
        "bankmonument_d",
        "towerhill_d",
        "aldgateeast_d"
        ]
    return district_station

#Circle Line (Yellow)

def circle_station_list():
    circle_station = [
        "edgwareroad_o",
        "paddington_o",
        "bayswater_o",
        "nottinghillgate_o",
        "highstreetkensington_o",
        "gloucesterroad_o",
        "southkensington_o",
        "sloanesquare_o",
        "victoria_o",
        "stjamesspark_o",
        "westminster_o",
        "embankment_o",
        "temple_o",
        "blackfriars_o",
        "mansionhouse_o",
        "cannonstreet_o",
        "bankmonument_o",
        "towerhill_o",
        "bakerstreet_o",
        "greatportlandstr_o",
        "eustonsquare_o",
        "kingscross_o",
        "farringdon_o",
        "barbican_o",
        "moorgate_o",
        "liverpoolstreet_o",
        "aldgatetube_o"
        ]
    return circle_station

#Jubilee Line (Gray)
def jubilee_station_list():
    jubilee_station = [
        "bakerstreet_j",
        "bondstreet_j",
        "greenpark_j",
        "westminster_j",
        "waterloo_j",
        "southwark_j",
        "londonbridge_j"
        ]
    return jubilee_station

#Victoria Line
def victoria_station_list():
    victoria_station = [
        "vauxhall_v",
        "pimlico_v",
        "victoria_v",
        "greenpark_v",
        "oxfordcircus_v",
        "warrenstreet_v",
        "euston_v",
        "kingscross_v"
        ]
    return victoria_station

#Northern Line
def northern_station_list():
    northern_station = [
        "waterloo_n",
        "embankment_n",
        "charingcross_n",
        "leicestersquare_n",
        "tottenhamcourtroad_n",
        "goodgestreet_n",
        "warrenstreet_n",
        "euston_n",
        "morningtoncrescent_n",
        "kingscross_n",
        "angel_n",
        "oldstreet_n",
        "moorgate_n",
        "bankmonument_n",
        "londonbridge_n",
        "borough_n",
        "elephantcastle_n"
        ]
    return northern_station

def zone_1():
    all_station = baker_station_list() + hammers_station_list() + metro_station_list() + central_station_list() + picca_station_list() + district_station_list() + circle_station_list() + jubilee_station_list() + victoria_station_list() + northern_station_list()
    return all_station
    
