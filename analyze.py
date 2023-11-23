import numpy as np
import matplotlib.pyplot as plt

#backLeg_sensor_data = np.load("data/backLeg.npy")
#frontLeg_sensor_data = np.load("data/frontLeg.npy")
#
#plt.plot(backLeg_sensor_data, 'r-', label="Back Leg")
#plt.plot(frontLeg_sensor_data, 'b:', label="Front Leg")

targetAngles = np.load("data/targetAngles.npy")
#x = np.linspace(0, 2*np.pi, targetAngles.size)
plt.plot(np.arange(targetAngles.size), targetAngles)

plt.show()
