%===================================================================
% Bakerloo Line
%===================================================================
dist(paddington_b,edgwareroad_b,3).
dist(edgwareroad_b,marylebone_b,2).
dist(marylebone_b,bakerstreet_b,1).
dist(bakerstreet_b,regentspark_b,2).
dist(regentspark_b,oxfordcircus_b,2).
dist(oxfordcircus_b,piccadillycircus_b,2).
dist(piccadillycircus_b,charingcross_b,2).
dist(charingcross_b,embankment_b,2).
dist(embankment_b,waterloo_b,2).
dist(waterloo_b,lambethnorth_b,1).
dist(lambethnorth_b,elephantcastle_b,3).
%===================================================================
%
%%===================================================================
% Hammersmith and City Line
%===================================================================
dist(paddington_h,edgwareroad_h,3).
dist(edgwareroad_h,bakerstreet_h,3).
dist(bakerstreet_h,greatportlandstr_h,3).
dist(greatportlandstr_h,eustonsquare_h,2).
dist(eustonsquare_h,kingscross_h,2).
dist(kingscross_h,farringdon_h,4).
dist(farringdon_h,barbican_h,1).
dist(barbican_h,moorgate_h,2).
dist(moorgate_h,liverpoolstreet_h,2).
dist(liverpoolstreet_h,aldgateeast_h,4).
%===================================================================
%
%%%===================================================================
% Metro Line
%===================================================================
dist(bakerstreet_m,greatportlandstr_m,3).
dist(greatportlandstr_m,eustonsquare_m,2).
dist(eustonsquare_m,kingscross_m,2).
dist(kingscross_m,farringdon_m,4).
dist(farringdon_m,barbican_m,1).
dist(barbican_m,moorgate_m,2).
dist(moorgate_m,liverpoolstreet_m,2).
dist(liverpoolstreet_m,aldgatetube_m,2).

%%%%===================================================================
% Central Line
%===================================================================
dist(nottinghillgate_c,queensway_c,2).
dist(queensway_c,lancastergate_c,1).
dist(lancastergate_c,marblearch_c,3).
dist(marblearch_c,bondstreet_c,1).
dist(bondstreet_c,oxfordcircus_c,1).
dist(oxfordcircus_c,tottenhamcourtroad_c,2).
dist(tottenhamcourtroad_c,holborn_c,2).
dist(holborn_c,chancerylane_c,1).
dist(chancerylane_c,stpauls_c,2).
dist(stpauls_c,bankmonument_c,2).
dist(bankmonument_c,liverpoolstreet_c,2).
%===================================================================
%%%%%===================================================================
% Picca Line
%===================================================================
dist(earlscourt_p,gloucesterroad_p,2).
dist(gloucesterroad_p,southkensington_p,1).
dist(southkensington_p,knightsbridge_p,3).
dist(knightsbridge_p,hydeparkcorner_p,2).
dist(hydeparkcorner_p,greenpark_p,2).
dist(greenpark_p,piccadillycircus_p,1).
dist(piccadillycircus_p,leicestersquare_p,2).
dist(leicestersquare_p,coventgarden_p,1).
dist(coventgarden_p,holborn_p,1).
dist(holborn_p,russellsquare_p,2).
dist(russellsquare_p,kingscross_p,2).
%===================================================================

%===================================================================
%%%%%===================================================================
% District Line
%===================================================================
dist(edgwareroad_d,paddington_d,3).
dist(paddington_d,bayswater_d,2).
dist(bayswater_d,nottinghillgate_d,2).
dist(nottinghillgate_d,highstreetkensington_d,3).
dist(highstreetkensington_d,earlscourt_d,3).
dist(earlscourt_d,gloucesterroad_d,2).
dist(gloucesterroad_d,southkensington_d,1).
dist(southkensington_d,sloanesquare_d,2).
dist(sloanesquare_d,victoria_d,2).
dist(victoria_d,stjamesspark_d,2).
dist(stjamesspark_d,westminster_d,2).
dist(westminster_d,embankment_d,2).
dist(embankment_d,temple_d,2).
dist(temple_d,blackfriars_d,2).
dist(blackfriars_d,mansionhouse_d,1).
dist(mansionhouse_d,cannonstreet_d,1).
dist(cannonstreet_d,bankmonument_d,2).
dist(bankmonument_d,towerhill_d,2).
dist(towerhill_d,aldgateeast_d,2).
%===================================================================


%%%%%===================================================================
% Circle Line
%===================================================================
dist(edgwareroad_o,paddington_o,3).
dist(paddington_o,bayswater_o,2).
dist(bayswater_o,nottinghillgate_o,2).
dist(nottinghillgate_o,highstreetkensington_o,3).
dist(highstreetkensington_o,earlscourt_o,3).
dist(earlscourt_o,gloucesterroad_o,2).
dist(gloucesterroad_o,southkensington_o,1).
dist(southkensington_o,sloanesquare_o,2).
dist(sloanesquare_o,victoria_o,2).
dist(victoria_o,stjamesspark_o,2).
dist(stjamesspark_o,westminster_o,2).
dist(westminster_o,embankment_o,2).
dist(embankment_o,temple_o,2).
dist(temple_o,blackfriars_o,2).
dist(blackfriars_o,mansionhouse_o,1).
dist(mansionhouse_o,cannonstreet_o,1).
dist(cannonstreet_o,bankmonument_o,2).
dist(bankmonument_o,towerhill_o,2).
dist(towerhill_o,aldgatetube_o,4).
dist(aldgatetube_o,liverpoolstreet_o,2).
dist(liverpoolstreet_o,moorgate_o,2).
dist(moorgate_o,barbican_o,2).
dist(barbican_o,farringdon_o,1).
dist(farringdon_o,kingscross_o,4).
dist(kingscross_o,eustonsquare_o,2).
dist(eustonsquare_o,greatportlandstr_o,2).
dist(greatportlandstr_o,bakerstreet_o,3).
%===================================================================

%%%%%===================================================================
% Jubilee Line
%===================================================================
dist(bakerstreet_j,bondstreet_j,2).
dist(bondstreet_j,greenpark_j,2).
dist(greenpark_j,westminster_j,3).
dist(westminster_j,waterloo_j,2).
dist(waterloo_j,southwark_j,1).
dist(southwark_j,londonbridge_j,2).


%%%%%===================================================================
% Victoria Line
%===================================================================
dist(vauxhall_v, pimlico_v,1).
dist(pimlico_v, victoria_v,3).
dist(victoria_v, greenpark_v,2).
dist(greenpark_v,oxfordcircus_v,2).
dist(oxfordcircus_v,warrenstreet_v,2).
dist(warrenstreet_v,euston_v,1).
dist(euston_v,kingscross_v,2).

%%%%%===================================================================
% Northern Line
%===================================================================

dist(waterloo_n, embankment_n,2).
dist(embankment_n, charingcross_n,1).
dist(charingcross_n,leicestersquare_n,2).
dist(leicestersquare_n,tottenhamcourtroad_n,1).
dist(tottenhamcourtroad_n,goodgestreet_n,1).
dist(goodgestreet_n,warrenstreet_n,2).
dist(warrenstreet_n,euston_n,1).
dist(euston_n,morningtoncrescent_n,2).
dist(euston_n,kingscross_n,2).
dist(kingscross_n,angel_n,2).
dist(angel_n,oldstreet_n,3).
dist(oldstreet_n,moorgate_n,1).
dist(moorgate_n,bankmonument_n,3).
dist(bankmonument_n,londonbridge_n,2).
dist(londonbridge_n,borough_n,2).
dist(borough_n,elephantcastle_n,1).

%%%%%===================================================================
% All Junction
% %===================================================================
dist(paddington_b,paddington_h,5).
dist(paddington_o,paddington_h,5).
dist(paddington_b,paddington_o,5).
dist(paddington_b,paddington_d,5).
dist(paddington_o,paddington_d,5).
dist(paddington_h,paddington_d,5).


dist(edgwareroad_b,edgewareroad_h,10).
dist(edgwareroad_b,edgewareroad_d,4).
dist(edgwareroad_b,edgewareroad_o,5).
dist(edgwareroad_h,edgewareroad_d,4).
dist(edgwareroad_h,edgewareroad_o,5).
dist(edgwareroad_d,edgewareroad_o,4).

dist(bakerstreet_b,bakerstreet_h,4).
dist(bakerstreet_b,bakerstreet_m,5).
dist(bakerstreet_b,bakerstreet_o,6).
dist(bakerstreet_b,bakerstreet_j,4).
dist(bakerstreet_h,bakerstreet_m,4).
dist(bakerstreet_h,bakerstreet_o,5).
dist(bakerstreet_h,bakerstreet_j,6).
dist(bakerstreet_m,bakerstreet_o,4).
dist(bakerstreet_m,bakerstreet_j,5).
dist(bakerstreet_o,bakerstreet_j,6).

dist(oxfordcircus_b,oxfordcircus_c,6).
dist(oxfordcircus_v,oxfordcircus_c,5).
dist(oxfordcircus_b,oxfordcircus_v,6).

dist(piccadillycircus_b,piccadillycircus_p,3).

dist(charingcross_b,charingcross_n,3).

dist(embankment_b,embankment_d,5).
dist(embankment_b,embankment_n,5).
dist(embankment_b,embankment_o,5).
dist(embankment_o,embankment_d,5).
dist(embankment_o,embankment_n,5).
dist(embankment_n,embankment_d,5).

dist(greatportlandstr_h,greatportlandstr_o,5).
dist(greatportlandstr_m,greatportlandstr_o,5).
dist(greatportlandstr_h,greatportlandstr_m,5).

dist(eustonsquare_h,eustonsquare_m,6).
dist(eustonsquare_o,eustonsquare_m,6).
dist(eustonsquare_h,eustonsquare_o,6).

dist(kingscross_h,kingscross_m,6).
dist(kingscross_h,kingscross_p,6).
dist(kingscross_h,kingscross_o,6).
dist(kingscross_h,kingscross_v,6).
dist(kingscross_h,kingscross_n,6).
dist(kingscross_p,kingscross_m,6).
dist(kingscross_p,kingscross_o,6).
dist(kingscross_p,kingscross_v,6).
dist(kingscross_p,kingscross_n,6).
dist(kingscross_m,kingscross_o,6).
dist(kingscross_m,kingscross_v,6).
dist(kingscross_m,kingscross_n,6).
dist(kingscross_o,kingscross_v,6).
dist(kingscross_o,kingscross_n,6).
dist(kingscross_v,kingscross_n,6).

dist(farringdon_h,farringdon_m,6).
dist(farringdon_o,farringdon_m,6).
dist(farringdon_h,farringdon_o,6).


dist(barbican_h,barbican_m,6).
dist(barbican_o,barbican_m,6).
dist(barbican_h,barbican_o,6).

dist(moorgate_h,moorgate_m,6).
dist(moorgate_o,moorgate_m,6).
dist(moorgate_h,moorgate_o,6).
dist(moorgate_n,moorgate_m,6).
dist(moorgate_o,moorgate_n,6).
dist(moorgate_h,moorgate_n,6).

dist(liverpoolstreet_h,liverpoolstreet_m,6).
dist(liverpoolstreet_h,liverpoolstreet_c,6).
dist(liverpoolstreet_h,liverpoolstreet_o,6).
dist(liverpoolstreet_m,liverpoolstreet_c,6).
dist(liverpoolstreet_m,liverpoolstreet_o,6).
dist(liverpoolstreet_c,liverpoolstreet_o,6).

dist(aldgateeast_h,aldgateeast_d,6).

dist(aldgatetube_m,aldgatetube_o,6).

dist(nottinghillgate_d,nottinghillgate_o,3).
dist(nottinghillgate_d,nottinghillgate_c,3).
dist(nottinghillgate_c,nottinghillgate_o,3).

dist(bondstreet_c,bondstreet_j,3).


dist(tottenhamcourtroad_c,tottenhamcourtroad_n,3).

dist(holborn_c,holborn_p,3).

dist(bankmonument_c,bankmonument_d,5).
dist(bankmonument_c,bankmonument_o,5).
dist(bankmonument_c,bankmonument_n,5).
dist(bankmonument_d,bankmonument_o,5).
dist(bankmonument_d,bankmonument_n,5).
dist(bankmonument_o,bankmonument_n,5).

dist(earlscourt_p,earlscourt_d,5).
dist(earlscourt_p,earlscourt_o,5).
dist(earlscourt_d,earlscourt_o,5).

dist(gloucesterroad_p,gloucesterroad_d,5).
dist(gloucesterroad_p,gloucesterroad_o,5).
dist(gloucesterroad_d,gloucesterroad_o,5).

dist(southkensington_p,southkensington_d,5).
dist(southkensington_p,southkensington_o,5).
dist(southkensington_d,southkensington_o,5).

dist(greenpark_p,greenpark_j,5).
dist(greenpark_p,greenpark_v,5).
dist(greenpark_v,greenpark_j,5).


dist(leicestersquare_p,leicestersquare_n,5).

dist(towerhill_d,towerhill_o,5).

dist(waterloo_n,waterloo_j,5).
dist(waterloo_b,waterloo_j,5).
dist(waterloo_n,waterloo_b,5).

dist(londonbridge_n,londonbridge_j,5).

dist(elephantcastle_b,elephantcastle_n,5).
