sudo apt-get install cmake tmux
tar -xvf ns-allinone*
cp ./makeAllCharts.sh ./makeChart.sh ./ns-allinone-3.43/ns-3.43/
cp ./scratch/* ./ns-allinone-3.43/ns-3.43/scratch/
cd ./ns-allinone-3.43/ns-3.43
mkdir data
./ns3 configure
