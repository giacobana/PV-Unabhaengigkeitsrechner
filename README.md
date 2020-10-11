# Calculator for optimal Photovoltaic Systems with Battery Storage

Helps you in finding the best combination of residential solar systeme (PV) and battery storage for any given energy consumption.

Input parameters:
- Yearly energy consumption (in kilowatt hours)
- Installed capacity of photovoltaik systeme (in kilowatt peak)
- Capacyity of energy storage (in kilowatt hours)

Calculation:
- Self-consumption of produced solar power for any possible combination of energy consumption, PV and battery (percentage of the produced solar power)
- Self-sufficiency from the energy grid for any possible combination of energy consumption, PV and battery (percentage of the yearly energy consumption)

Output:
- Excel file where every row is a combination of energy consumption, PV capacity, battery capacity, percentage of self-consumption and percentage of self-sufficiency
- CSV file where every row is a combination of energy consumption, PV capacity, battery capacity, percentage of self-consumption and percentage of self-sufficiency

*Credits*
Calculator has been developed following the approach and calculations of HTW Berlin. However, tool of HTW Berlin is only available on a webpage with graphical user interface without the possibility to obtain combinations in bulk.

For furhter information follow: https://pvspeicher.htw-berlin.de/unabhaengigkeitsrechner/

## How to use

In the main function of the python script ```python unabhaengig.py``` needs to be specified for which amounts of... 
- Energy consumption (list "last_list" / min: 2,000 kWh max: 20,000 kWh)
- PV capacity (list "pv_list" / min: 1,0 kWp max 20,0 kWp)
- battery capacity (list "bat_list" / min: 0,0 kWh max 20,0 kWh)...
self-consumption an self-sufficiency should be calculated.

After specifying, run the script in your IDE or command line.

### Prerequisites

- Pyhton 3.5 or newer
- Install dependencies via ```pip install -r requirements.txt```

### Run in CLI

To use this script, simply use ```python unabhaengig.py``` to run the script.
