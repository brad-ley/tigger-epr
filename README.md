[![DOI](https://zenodo.org/badge/511248877.svg)](https://zenodo.org/doi/10.5281/zenodo.10038327)

`pip install -r requirements.txt` to install necessary python packages

For a typical RS TiGGER experiment:
1. Data is acquired with LabVIEW vis on control PC (each experiment should be given its own folder as the data processing produces a lot of additional files that are sorted into the parent folder; it is good in the file names to *at least* include the modulation coil current and frequency. Usual naming: `./<experiment>/<temp>/<current>mA_<freq>kHz.dat` )
2. Run `onefileRapidscanGUI.py` on the computer with the data file (run with Python, open using IP address output by Python)
3. Open file in vi using the full pathname (app will strip ' ' from each side of the string if they are present)
4. Adjust experimental settings to match experiment and coil
5. Auto-phase signal (if this doesn't work, try manual phasing to match what is expected for given EPR spectrum)
6. `Batch deconvolve` to apply same deconvolution process to all time points in the file (this will also generate a times.txt file that uses the number of averages from the TiGGER file name to calculate the amount of time that has passed during the experiment)
7. Run `onefileAnimateSlowscan.py` in your command line using `python onefileAnimateSlowscan.py [filename: string] [B field offset: float (default 0)] [auto-phase: boolean (default False)]`. This will make all the TiGGER output files for the given experimental file name (it actually reads the .feather filename that is generated from `onefileRapidscanGUI.py` but you can pass it the name of the original file). The `B field offset` allows you to shift the center of the output plots so that the resonances are centered even if the RS modulation coil phase or timing is a bit off. `auto-phase` does its best to phase each time point to a pure absorptive signal which is useful if the temperature of the sample drifts during the experiment; if `auto-phase` is off, the phase that as applied using `onefileRapidscanGUI.py` is applied to all time points. 
8. The results are all in the folder of your original data file!
