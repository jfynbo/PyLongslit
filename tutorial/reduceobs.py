import numpy as np
import glob as glob
from astropy.io import fits

"""
This is a python program to reduce the observation frames 
(both Science and Standard Star).

This script is not meant to be called directly, but rather to be imported
and called from reducscience.py or reducestd.py.
"""


def reduce_obs(ysize, xsize, centers, standard_star_reduction = False):
    print('Script running')
    print('\n ---Using the following parameters:---\n')
    print(f'ysize = {ysize}')
    print(f'xsize = {xsize}')
    print(f'Is this a standard star reduction? = {standard_star_reduction}\n')
    print(f'Object centers: {centers}\n')
    print('\n -------------------------------------\n')


    BIASframe = fits.open('../rawbias/BIAS.fits')
    BIAS = np.array(BIASframe[0].data)
    FLATframe = fits.open('../rawflats/Flat.fits')
    FLAT = np.array(FLATframe[0].data)

    rawimages = sorted(glob.glob("crr*.fits"))

    n_rawimages = len(rawimages)

    print('Number of raw images:', n_rawimages)

    outnames = [f'sub{n}.fits' for n in range(1, n_rawimages+1)]

    if len(centers) != n_rawimages:
        raise ValueError(
            'The number of centers must be equal to the number of raw images'
            )

    #Read the raw file, subtract overscan, bias and divide by the flat
    for n in range(0, n_rawimages):
        spec = fits.open(rawimages[n])
        print('Info on file:')
        print(spec.info())
        specdata = np.array(spec[1].data)
        mean = np.mean(specdata[2067:ysize-5,10:xsize-1])
        specdata = specdata - mean
        print('Subtracted the median value of the overscan :',mean)
        specdata = (specdata-BIAS)/FLAT
        hdr = spec[0].header
        specdata1 = specdata[50:1750,centers[n]-100:centers[n]+100] 
        print(outnames[n])
        fits.writeto(outnames[n],specdata1,hdr,overwrite=True)

    #Add and rotate

    sum = np.zeros_like(fits.open(outnames[0])[0].data)

    for n in range(0, n_rawimages):
            sub = fits.open(outnames[n])
            sum = sub[0].data


    rot = np.rot90(sum, k=3)
    hduout = fits.PrimaryHDU(rot)
    hduout.header.extend(hdr, strip=True, update=True,
            update_first=False, useblanks=True, bottom=False)
    hduout.header['DISPAXIS'] = 1
    hduout.header['NEXP'] = len(rawimages)
    hduout.header['CRVAL1'] = 1
    hduout.header['CRVAL2'] = 1
    hduout.header['CRPIX1'] = 1
    hduout.header['CRPIX2'] = 1
    hduout.header['CRVAL1'] = 1
    hduout.header['CRVAL1'] = 1
    hduout.header['CDELT1'] = 1
    hduout.header['CDELT2'] = 1
    hduout.writeto(
        "../obj.fits" if not standard_star_reduction else "../std.fits",
        overwrite=True
    )


    #Arcframe
    arclist = open('raw_arcs.list')
    nframes = len(arclist.readlines())
    arclist.seek(0)

    specdata = np.zeros((ysize,xsize),float)
    for i in range(0,nframes):
        spec = fits.open(str.rstrip(arclist.readline()))
        data = spec[1].data
        if ((len(data[0,:]) != xsize) or (len(data[:,0]) != ysize)): sys.exit(spec.name + ' has wrong image size')
        specdata += data
    mean = np.mean(specdata[2067:ysize-5,10:xsize-1])
    specdata = specdata - mean
    print('Subtracted the median value of the overscan :',mean)
    specdata = (specdata-BIAS)/FLAT
    hdr = spec[0].header
    center = int((centers[0])/1.)
    specdata1 = specdata[50:1750,center-100:center+100]
    rot = np.rot90(specdata1, k=3)
    hduout = fits.PrimaryHDU(rot)
    hduout.header.extend(hdr, strip=True, update=True,
            update_first=False, useblanks=True, bottom=False)
    hduout.header['DISPAXIS'] = 1
    hduout.header['CRVAL1'] = 1
    hduout.header['CRVAL2'] = 1
    hduout.header['CRPIX1'] = 1
    hduout.header['CRPIX2'] = 1
    hduout.header['CRVAL1'] = 1
    hduout.header['CRVAL1'] = 1
    hduout.header['CDELT1'] = 1
    hduout.header['CDELT2'] = 1
    hduout.writeto(
        "../arcsub.fits" if not standard_star_reduction else "../arcsub_std.fits",
        overwrite=True
    )

    if standard_star_reduction:
            print("\n\n\033[91m\n\nATTENTION:\033[0m THIS REDUCTION HAS BEEN RUN AS A STANDARD STAR REDUCTION")
            print("If this is an object reduction, please use \"reducescience.py\" script, "  +
            "and re-run both the standard star and science object reductions. \n\n")

    else:
            print("\n\n\033[91m\n\nATTENTION:\033[0m THIS REDUCTION HAS BEEN RUN AS A SCIENCE OBJECT REDUCTION")
            print("If this is a standard star reduction, please use \"reducestd.py\" script," +
            "and re-run both the standard star and science object reductions. \n\n")