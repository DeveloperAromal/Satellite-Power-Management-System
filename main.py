# main.py
import time
import csv
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from system import Satellite
from controllers import PidController

def execute(duration = 3600, dt = 1.0):
    satelliteModel = Satellite()
    pid_controller = PidController()

    with open('./data/thermaldat.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time (s)', 'Temperature (C)', 'Cooling Power (W)'])

        for t in np.arange(0, duration, dt):
            current_temp = satelliteModel.temp
            cooling_power = pid_controller.compute(current_temp, dt)
            new_temp = satelliteModel.update(cooling_power, dt)

            writer.writerow([t, new_temp, cooling_power])
            print(f"Time: {t:.1f}s, Temp: {new_temp:.2f}°C, Cooling Power: {cooling_power:.2f}W")
            time.sleep(0.001)

if __name__ == '__main__':
    execute()
