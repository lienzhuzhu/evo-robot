import numpy as np
import matplotlib.pyplot as plt

#backLeg_sensor_data = np.load("data/backLeg.npy")
#frontLeg_sensor_data = np.load("data/frontLeg.npy")
#
#plt.plot(backLeg_sensor_data, 'r-', label="Back Leg")
#plt.plot(frontLeg_sensor_data, 'b:', label="Front Leg")

targetAngles = np.load("data/targetAngles.npy")
plt.plot(np.arange(targetAngles.size), targetAngles, label="targetAngles")

plt.xlabel("Steps")
plt.ylabel("Value in Radians")

plt.legend()
plt.show()
