import numpy
import matplotlib.pyplot

backLeg_sensor_data = numpy.load("data/sensor.npy")
frontLeg_sensor_data = numpy.load("data/frontLeg.npy")
matplotlib.pyplot.plot(backLeg_sensor_data, label="Back Leg", linewidth=5)
matplotlib.pyplot.plot(frontLeg_sensor_data, label="Front Leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
