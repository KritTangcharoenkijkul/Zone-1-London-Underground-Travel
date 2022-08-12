%===================================================================
% Station
%===================================================================
stationList([paddington_b,
        edgwareroad_b,
        marylebone_b,
        bakerstreet_b,
        regentspark_b,
        oxfordcircus_b,
        piccadillycircus_b,
        charingcross_b,
        embankment_b,
        waterloo_b,
        lambethnorth_b,
        elephantcastle_b,
        paddington_h,
        edgwareroad_h,
        bakerstreet_h,
        greatportlandstr_h,
        eustonsquare_h,
        kingscross_h,
        farringdon_h,
        barbican_h,
        moorgate_h,
        liverpoolstreet_h,
        aldgateeast_h,
        bakerstreet_m,
	greatportlandstr_m,
        eustonsquare_m,
        kingscross_m,
        farringdon_m,
        barbican_m,
        moorgate_m,
        liverpoolstreet_m,
        aldgatetube_m
        nottinghillgate_c,
        lancastergate_c,
        marblearch_c,
        bondstreet_c,
        oxfordcircus_c,
        tottenhamcourtroad_c,
        holborn_c,
        chancerylane_c,
        stpauls_c,
        bankmonument_c,
        liverpoolstreet_c,
        earlscourt_p,
        gloucesterroad_p,
        southkensington_p,
        knightsbridge_p,
        hydeparkcorner_p,
        greenpark_p,
        piccadillycircus_p,
        leicestersquare_p,
        coventgarden_p,
        holborn_p,
        russellsquare_p,
        kingscross_p,
        edgwareroad_d,
        paddington_d,
        bayswater_d,
        nottinghillgate_d,
        highstreetkensington_d,
        earlscourt_d,
        gloucesterroad_d,
        southkensington_d,
        sloanesquare_d,
        victoria_d,
        stjamesspark_d,
        westminster_d,
        embankment_d,
        temple_d,
        blackfriars_d,
        mansionhouse_d,
        cannonstreet_d,
        bankmonument_d,
        towerhill_d,
        aldgateeast_d,
        edgwareroad_o,
        paddington_o,
        bayswater_o,
        nottinghillgate_o,
        highstreetkensington_o,
        earlscourt_o,
        gloucesterroad_o,
        southkensington_o,
        sloanesquare_o,
        victoria_o,
        stjamesspark_o,
        westminster_o,
        embankment_o,
        temple_o,
        blackfriars_o,
        mansionhouse_o,
        cannonstreet_o,
        bankmonument_o,
        towerhill_o,
        bakerstreet_o,
        greatportlandstr_o,
        eustonsquare_o,
        kingscross_o,
        farringdon_o,
        barbican_o,
        moorgate_o,
        liverpoolstreet_o,
        aldgatetube_o,
        bakerstreet_j,
        bondstreet_j,
        greenpark_j,
        westminster_j,
        waterloo_j,
        southwark_j,
        londonbridge_j,
        vauxhall_v,
        pimlico_v,
        victoria_v,
        greenpark_v,
        oxfordcircus_v,
        warrenstreet_v,
        euston_v,
        kingscross_v,
        waterloo_n,
        embankment_n,
        charingcross_n,
        leicestersquare_n,
        tottenhamcourtroad_n,
        goodgestreet_n,
        warrenstreet_n,
        euston_n,
        morningtoncrescent_n,
        kingscross_n,
        angel_n,
        oldstreet_n,
        moorgate_n,
        bankmonument_n,
        londonbridge_n,
        borough_n,
        elephantcastle_n]).				

%===================================================================





%=====================================================================================================================================
%  A STAR
%=====================================================================================================================================
distance(X,Y,Z) :- dist(X,Y,Z).
distance(X,Y,Z) :- dist(Y,X,Z).




astar(Start, Destination, Path, Cost) :- getHn(Start,Destination,Hn),
				   	 search(Destination,[[Start,[Start],Hn]],[_,Path,Cost]).

search(Station, [[Station,Path,TotalCost]|T], [Station,Path,TotalCost]) :- !.
search(Destination, [[Station,Path,TotalCost]|T], Result) :- expand([Station,Path,TotalCost],Destination,ExpandedNode),
							     append(T, ExpandedNode, NewQ),
							     minsort(NewQ, PriorityQ),
							 

							     %write("\n\nQUEUE: "),write(NewQ),
							     %write("\nMIN SORT: "),write(PriorityQ),write("\n")
			
							     search(Destination,PriorityQ, Result).



expand([Station,Path,_], Destination, Return) :- findall(X, distance(Station,X,_),NextStations),
				   		 checkPassedNode(NextStations, Path, [], NewNextStations),
				    		 createNode(NewNextStations, Destination, Path, [], Return).


checkPassedNode([],Path,NewStations, NewStations).
checkPassedNode([Station|T], Path, NewStations, Return) :- in(Station, Path) -> checkPassedNode(T, Path, NewStations, Return);
									     	 append(NewStations,[Station],NNewStation),
				   					      	 checkPassedNode(T, Path, NNewStation, Return).

in(Station, [PassedStation|Path]) :- Station == PassedStation -> !;in(Station,Path).

createNode([], Destination, Path, Nodes, Nodes).
createNode([Station|T], Destination,Path,Nodes, ExpandedNodes) :- append(Path, [Station], NewPath), 
					                          append(Nodes, [[Station, NewPath, 0]], NewNodes),
					      	 		  createNode(T, Destination, Path, NewNodes, Result),
					    			  %write("RESULT: "),write(Result),write("\n"),
					     			  getFn(Result, Destination, [], ExpandedNodes).

getFn([], Destination, Nodes, Nodes).
getFn([[Station, [FromPath|ToPath], TotalCost]|T], Destination, Nodes, Return) :- getGn(ToPath,FromPath, 0, Gn),
								    	 	  getHn(Station,Destination,Hn), Fn is Gn + Hn,
										  %write("FN: "),write(Fn),
                                                        	    		  append(Nodes, [[Station, [FromPath|ToPath], Fn]], NewNodes),
								     		  getFn(T, Destination, NewNodes, Return).

getGn([], From, Acc, Acc).
getGn([To|T], From, Acc, Gn) :-	distance(From,To,StepCost),!, NewAcc is Acc + StepCost, 
				getGn(T, To, NewAcc, Gn).


power(X,Result) :- Result is X * X.
getHn(Start, Destination, HeuristicValue) :- location(_,Start,X1,Y1), location(_,Destination,X2,Y2),
					     generateDistance(X1,Y1,X2,Y2,Distance),
					     HeuristicValue is Distance/106.666667. %max deltaV train 

generateDistance(X1, Y1, X2, Y2, ReturnV2) :- R is 6371e3, % metres
					      LatRadian1 is X1*pi/180,
    					      LatRadian2 is X2*pi/180,
    					      DifLat is (X2 - X1)*pi/180,
  					      DifLon is (Y2 - Y1)*pi/180,
    					      A1 is sin(DifLat/2) * sin(DifLat/2),
    					      A2 is cos(LatRadian1) * cos(LatRadian2),
    					      A3 is sin(DifLon/2) * sin(DifLon/2),
    				    	      A is A1 + A2 * A3,
    					      C is 2 * atan2(sqrt(A), sqrt(1-A)),
    					      D is R*C,
      					      ReturnV2 is D / 1000.


minsort(List, Return) :- setof([TotalCost,Station,Cost], member([Station,Cost,TotalCost], List), Result),
			 findall([Cost,TotalCost,Station], member([Station,Cost,TotalCost],Result),Return).

%=====================================================================================================================================


%=====================================================================================================================================
% Which Train
%=====================================================================================================================================
trainPath([Station|Path], Col, Row, Result) :- location(Train, Station, _, _),
				     whichTrain(Path, [Train], TrainList),
				     includeWalk(TrainList, Row, Col, Result). % confusion between width and row = ="
				     

whichTrain([], TrainList, TrainList).
whichTrain([Station|Path], TrainList, Result) :- location(Train, Station, _, _),
						 append(TrainList, [Train], NewTrainList),
				 		 whichTrain(Path, NewTrainList, Result).

includeWalk(Lst, Row, Col, Return) :- checkWalk(Lst,[],0, 1, Row, Col, Return).

checkWalk([], Return, AccR, AccC, AccR, AccC, Return).
checkWalk([H|T], Result, AccR, AccC, Row, Col, Return) :- isDifferent(H,T) -> append(Result, [walk], X), NewAccC is AccC + 1,checkWalk(T, X, AccR, NewAccC, Row, Col, Return)
                                                       		  ;append(Result, [H],X), NewAccR is AccR + 1, checkWalk(T, X, NewAccR, AccC, Row, Col, Return).

isDifferent(X,[Y|T]) :- X \= Y,!.



%=====================================================================================================================================


%=====================================================================================================================================
% Get Closest Train Station
%=====================================================================================================================================
findClosestStation(X1, Y1, Result) :- stationList(Stations),findMinDistance(Stations, X1, Y1, [9999,a], Result).

findMinDistance([], X1, Y1, [Distance|Station], [Station,Distance]).
findMinDistance([HStation|TStation], X1, Y1, [Distance|Station], Result) :- location(_,HStation,X2,Y2),
									    generateDistance(X1,Y1,X2,Y2, NewDistance),
									    NewDistance =< Distance -> 
									    findMinDistance(TStation, X1, Y1, [NewDistance| HStation], Result);
									    findMinDistance(TStation, X1, Y1, [Distance|Station],Result).
%=====================================================================================================================================
