#! /bin/bash

# nodes sinks power name_of_experiment time


#./makeChart.sh 30 1 1000 "Sanity_Check" 200
./makeChart.sh 80 10 5 "High_Nodes,_High_Sinks,_Regular_Power" 300
./makeChart.sh 80 2 5 "High_Nodes,_Low_Sinks,_Regular_Power" 300
./makeChart.sh 80 10 10 "High_Nodes,_High_Sinks,_High_Power" 300
./makeChart.sh 80 2 10 "High_Nodes,_Low_Sinks,_High_Power" 300
./makeChart.sh 30 10 5 "Low_Nodes,_High_Sinks,_Regular_Power" 300
./makeChart.sh 30 2 5 "Low_Nodes,_Low_Sinks,_Regular_Power" 300
./makeChart.sh 30 10 10 "Low_Nodes,_High_Sinks,_High_Power" 300
./makeChart.sh 30 2 10 "Low_Nodes,_Low_Sinks,_High_Power" 300



