#! /bin/bash
# nodes sinks power name_of_experiment time

echo $4

for alg in OLSR AODV DSR DSDV;
do
    date > ./time/"$4$alg".txt
    ./ns3 run "manet-power --CSVfileName=$alg-$4.csv --protocol=$alg --nWifis=$1 --nSinks=$2 --NewCSV=true --TotalTime=$5 --MaxY=500 --MaxX=300 --TPow=$3 --CSVSpecfileName=$alg.Spec.csv"
    date >> ./time/"$4$alg".txt
done
#python ./makePlot.py "$4"
#python ./makeRate.py "$4"
#python ./makeNoSpecialPlot.py "$4"
