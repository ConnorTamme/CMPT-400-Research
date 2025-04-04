#! /bin/bash

# nodes sinks power name_of_experiment time


#./makeChart.sh 30 1 1000 "Sanity Check" 400
#./makeChart.sh 80 10 5 "High Nodes, High Sinks, Regular Power" 300
#./makeChart.sh 80 2 5 "High Nodes, Low Sinks, Regular Power" 300
./makeChart.sh 80 10 10 "High Nodes, High Sinks, High Power" 300
./makeChart.sh 80 2 10 "High Nodes, Low Sinks, High Power" 300
./makeChart.sh 30 10 5 "Low Nodes, High Sinks, Regular Power" 300
./makeChart.sh 30 2 5 "Low Nodes, Low Sinks, Regular Power" 300
./makeChart.sh 30 10 10 "Low Nodes, High Sinks, High Power" 300
./makeChart.sh 30 2 10 "Low Nodes, Low Sinks, High Power" 300



