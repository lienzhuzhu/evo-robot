import numpy as np
import matplotlib.pyplot as plt

#backLeg_sensor_data = np.load("data/backLeg.npy")
#frontLeg_sensor_data = np.load("data/frontLeg.npy")
#
#plt.plot(backLeg_sensor_data, 'r-', label="Back Leg")
#plt.plot(frontLeg_sensor_data, 'b:', label="Front Leg")

BackLeg_targetAngles = np.load("data/BackLeg_targetAngles.npy")
plt.plot(np.arange(BackLeg_targetAngles.size), BackLeg_targetAngles, label="BackLeg targetAngles")

FrontLeg_targetAngles = np.load("data/FrontLeg_targetAngles.npy")
plt.plot(np.arange(FrontLeg_targetAngles.size), FrontLeg_targetAngles, label="FrontLeg targetAngles")

plt.title("Motor Commands")
plt.xlabel("Steps")
plt.ylabel("Value in Radians")

plt.legend()
plt.show()
