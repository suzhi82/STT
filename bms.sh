#!/usr/bin/env bash

# List the mission(s) below
date

# The 1st mission
rm /home/spike777/STT/results/*.csv
sleep 2

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/A01-ICT.conf -o /home/spike777/STT/results/A01-ICT.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B01-GOOGL.conf -o /home/spike777/STT/results/B01-GOOGL.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B02-FB.conf -o /home/spike777/STT/results/B02-FB.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B03-TSLA.conf -o /home/spike777/STT/results/B03-TSLA.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B04-TWTR.conf -o /home/spike777/STT/results/B04-TWTR.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B05-CSCO.conf -o /home/spike777/STT/results/B05-CSCO.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B06-AAPL.conf -o /home/spike777/STT/results/B06-AAPL.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B07-AMZN.conf -o /home/spike777/STT/results/B07-AMZN.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B08-NVDA.conf -o /home/spike777/STT/results/B08-NVDA.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B09-AMD.conf -o /home/spike777/STT/results/B09-AMD.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B10-MSFT.conf -o /home/spike777/STT/results/B10-MSFT.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B11-T.conf -o /home/spike777/STT/results/B11-T.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B12-NTES.conf -o /home/spike777/STT/results/B12-NTES.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B13-BABA.conf -o /home/spike777/STT/results/B13-BABA.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B14-BIDU.conf -o /home/spike777/STT/results/B14-BIDU.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B15-ANET.conf -o /home/spike777/STT/results/B15-ANET.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B16-LMT.conf -o /home/spike777/STT/results/B16-LMT.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/B17-0700HK.conf -o /home/spike777/STT/results/B17-0700HK.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/C01-JOBS.conf -o /home/spike777/STT/results/C01-JOBS.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/C02-AUJOBS.conf -o /home/spike777/STT/results/C02-AUJOBS.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/D01-COMM.conf -o /home/spike777/STT/results/D01-COMM.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/D02-AUPROP.conf -o /home/spike777/STT/results/D02-AUPROP.csv

sleep 10

/usr/bin/python3.6 /home/spike777/STT/ttt.py -c /home/spike777/STT/D03-CHINAPROP.conf -o /home/spike777/STT/results/D03-CHINAPROP.csv

sleep 10

sh /home/spike777/STT/mgf.sh /home/spike777/STT/results/


