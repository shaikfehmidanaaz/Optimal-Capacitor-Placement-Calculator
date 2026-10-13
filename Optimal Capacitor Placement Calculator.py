
OPTIMAL CAPACITOR PLACEMENT CALCULATOR
--------------------------------------
Enter line voltage (kV): 11
Enter target power factor (e.g., 0.95): 0.95
Enter number of buses: 2

Enter details for Bus 1
Active power (kW): 100
Initial power factor: 0.80
Feeder resistance per phase (ohms): 0.5

Enter details for Bus 2
Active power (kW): 150
Initial power factor: 0.85
Feeder resistance per phase (ohms): 0.8

========== RESULTS ==========
Bus | Load(kW) | Capacitor(kVAR) | Loss Before(kW) | Loss After(kW)
------------------------------------------------------------------------
  1 |   100.00 |           42.13 |          0.0175 |         0.0125
  2 |   150.00 |           29.75 |          0.0632 |         0.0447

========== PLACEMENT SUGGESTION ==========
Suggested bus: Bus 2
Estimated loss reduction: 0.0185 kW
Required capacitor at this bus: 29.75 kVAR
Total calculated capacitor requirement: 71.88 kVAR
