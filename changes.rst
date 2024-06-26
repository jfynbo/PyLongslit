26.06.2024
--------------

Hardcoded nframes in mkspecbias.py and mkspecflat.py made dynamic
by automatic determination based on the number of files in the list.

reducescience.py and reducestd.py made into one script,
here all input/output made dynamic so the scripts no longer
depend on pre-determined number of files. This edit allows
for cosmic ray removal for standard stars also.