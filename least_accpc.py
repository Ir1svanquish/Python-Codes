# leastaccpc.py
# This program uses the scipy.constants.physical constants dictionary
# to determine which are the least accurately known physical constants.

import numpy as np
from scipy.constants import physical_constants
pc = physical_constants

def make_record(k, v):
    """ Return the record for this constant from the key and value of
        its entry in the physical constants dictionary """
    name = k
    val, units, abs_unc = v
    # Calculate the relative uncertainty in ppm (parts per million)
    rel_unc = abs_unc/abs(val)*1.e6
    return name, val, units, rel_unc

dt = [("name","S73"), ("val","f8"), ("units","S20"), ("rel unc","f8")]
constants = np.array([make_record(k, v) for k,v in pc.items()],
dtype=dt)
constants.sort(order="rel unc")

# List the 10 constants with the largest relative uncertainties
for rec in constants[-10:]:
    print("{:.0f} ppm: {:s} = {:g} {:s}".format(rec["rel unc"],
                                                rec["name"].decode(),
                                                rec["val"],
                                                rec["units"].decode()))
