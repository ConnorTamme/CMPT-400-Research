#! /bin/bash
# nodes sinks power name_of_experiment time

echo $4

for alg in OLSR AODV DSR DSDV;
do
    ./ns3 run "fanet-power --CSVfileName=./data/$alg-$4 --protocol=$alg --nWifis=$1 --nSinks=$2 --NewCSV=true --TotalTime=$5 --MaxY=500 --MaxX=300 --TPow=$3 --CSVSpecfileName=$alg.Spec.csv"
    for i in {1..9};
    do
        ./ns3 run "fanet-power --CSVfileName=./data/$alg-$4 --protocol=$alg --nWifis=$1 --nSinks=$2 --NewCSV=false --TotalTime=$5 --MaxY=500 --MaxX=300 --TPow=$3 --CSVSpecfileName=$alg.Spec.csv"
    done
done
#python ./makePlot.py "$4"
#python ./makeRate.py "$4"
#python ./makeNoSpecialPlot.py "$4"
