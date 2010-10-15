import numpy as np
import matplotlib.pyplot as plt

filename = 'friday_evening'
#filename = 'friday_afternoon'
#filename = 'friday_morning'
filename = 'sunday_afternoon'
filename = 'monday_alkaline'
filename = 'alkaline_opamp'
filename = 'wednesday_dcell'
filename = 'wednesday_dcell_2'


f = np.loadtxt(filename + '.CSV', delimiter=',')

# careful, vbatt and ibatt get switched in the data files
time_sec = f[:,0] / 1000
Vbatt = f[:,1] * 5 / 1024
Ibatt = f[:,2] * 5 / 1024 / 1

Vbatt = Vbatt[:-1]
Ibatt = Ibatt[:-1]

time_intervals = np.diff(time_sec)
charge_mAh = Ibatt * time_intervals / 3600
cumulative_mAh = charge_mAh.cumsum()

cumulative_mAh = time_sec[:-1]
# convert to charge delivered instead of time

plt.plot(cumulative_mAh, Vbatt, label='batt voltage (volts)')
plt.plot(cumulative_mAh, Ibatt, label='battery current (amps)')
plt.xlabel('current delivered (amp-hour)')
plt.ylabel('')
plt.grid()
#plt.title('170mA, 2.5ohm load, 5V supply')
#plt.title('alkaline 200mA, 1 ohm load, 10V supply')
#plt.title('alkaline with opamp feedback, 1ohm load 10V supply')
#plt.legend()
plt.savefig(filename + '.pdf')
plt.show()
