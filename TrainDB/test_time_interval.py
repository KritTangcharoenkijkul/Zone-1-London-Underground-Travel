from pyswip import Prolog
import requests
import json



prolog = Prolog()
prolog.consult("astar_nextstation.pl")
prolog.consult("location.pl")



station_list = "phaya_thai_airlink,ratchaprarop,makkasan,ramkhamhaeng,hua_mak,ban_thap_chang,latkrabang,suvarnabhumi,mo_chit,saphan_kwai,ari,sanam_pao,victory_monument,phaya_thai,ratchathewi,siam,chit_lom,ploen_chit,nana,asok,phrom_phong,thong_lo,ekkamai,phra_khanong,on_nut,bang_chak,punnawithi,udom_suk,bang_na,bearing,samrong,national_stadium,siam_silom_line,ratchadamri,sala_daeng,chong_nonsi,surasak,saphan_taksin,krung_thon_buri,wongwian_yai,pho_nimit,talat_phlu,wutthakat,bang_wa,hua_lamphong,sam_yan,si_lom,lumphini,klong_toei,queen_sirkit_national_covention_center,sukhumvit,phetchaburi,phra_ram_9,thailand_cultural_center,huai_kwang,sutthisan,ratchadaphisek,lat_phrao,phahon_yothin,chatuchak_park,kamphaen_phet,bang_sue,tao_poon,khlong_bang_phai,talad_bang_yai,sam_yaek_bang_yai,bang_phlu,bang_rak_yai,bang_rak_noi_tha_it,sai_ma,phra_nang_klao_bridge,yaek_nonthaburi1,bang_krasor,nonthaburi_civic_center,ministry_of_public_health,yaek_tiwanon,wong_sawang,bang_son,tao_poon_purple"
station_list = station_list.split(",")

start = "ekkamai"
destination = "chong_nonsi"

consult_list = ["mon_fri_6_7","mon_fri_7_9","mon_fri_9_9h",
                "mon_fri_9h_16","mon_fri_16_16h","mon_fri_16h_17",
                "mon_fri_17_19h","mon_fri_19h_20","mon_fri_20_21",
                "mon_fri_21_22","mon_fri_22_24",
                "sat_sun_6_8","sat_sun_8_9","sat_sun_9_11",
                "sat_sun_21_22","sat_sun_22_24","sat_11_15h",
                "sat_15h_19","sat_19_21","sun_11_21"]

for i in range(len(consult_list)):
    prolog.consult(consult_list[i] + ".pl")

    print("\n\n" + consult_list[i])
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

