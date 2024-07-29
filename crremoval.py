import astroscrappy
import glob

import os as os

from astropy.io import fits

"""
This is a python program to run cosmic ray removal on observations
(both science and standard frames)
"""

# THESE HAVE TO BE SET MANUALLY
gain = 0.16 # LOOK UP fitsfile[1].header['GAIN']
ron = 4.3 # LOOK UP fitsfile[1].header['RDNOISE']

# THSE CAN BE SET DIFFERENTLY AS NEEDED
frac = 0.01
objlim = 15
sigclip = 5
niter = 5


print('Script running')
print('\n ---Using the following parameters:---\n')
print(f'gain = {gain}')
print(f'ron = {ron}')
print(f'frac = {frac}')
print(f'objlim = {objlim}')
print(f'sigclip = {sigclip}')
print(f'niter = {niter}')
print('----------------------------------------\n')


# Path to folder with science frames
for nn in glob.glob("*crr*.fits"):
    os.remove(nn)
    print(nn)

# Try to open raw_science.list, if it doesn't exist, open raw_std.list
try:
    files = open('raw_science.list')
    print("\nScience observation list found: Using raw_science.list\n")
except FileNotFoundError:
    try:
        files = open('raw_std.list')
        print("\nStandard star observation list found: Using raw_std.list\n")
    except FileNotFoundError:
        raise FileNotFoundError(
            "Either raw_science.list or raw_std.list needs to be provided."
        )


for n in files:
    n = n.strip() # Remove leading/trailing whitespaces
    fitsfile = fits.open(str(n))
    filename = os.path.basename(n)
    print('Removing cosmics from file: ' + filename + '...')
        
    crmask, clean_arr = astroscrappy.detect_cosmics(fitsfile[1].data, sigclip=sigclip, sigfrac=frac, objlim=objlim, cleantype='medmask', niter=niter, sepmed=True, verbose=True)

# Replace data array with cleaned image
    fitsfile[1].data = clean_arr

# Try to retain info of corrected pixel if extension is present.
    try:
        fitsfile[2].data[crmask] = 16 #Flag value for removed cosmic ray
    except:
        print("No bad-pixel extension present. No flag set for corrected pixels")

# Update file
    fitsfile.writeto("crr"+filename, output_verify='fix')

files.close()
