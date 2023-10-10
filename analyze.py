import numpy
import matplotlib.pyplot

backLeg_sensor_data = numpy.load("data/sensor.npy")
matplotlib.pyplot.plot(backLeg_sensor_data)
matplotlib.pyplot.show()
