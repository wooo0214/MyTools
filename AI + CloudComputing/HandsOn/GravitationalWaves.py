'''
Detecting Gravitational Waves events and sources

big data | python | linux

## Data sources

- https://www.ligo.caltech.edu/page/ligo-data
- https://gwosc.org/
- https://www.virgo-gw.eu/science/gw-universe/catalog-of-gravitational-wave-events/

## Software setup

https://github.com/gw-odw/odw-2021/blob/master/setup.md
You can install a Linux and follow the opt3.

## Study hubs

https://ask.igwn.org/t/open-data-workshop-study-hubs-2024/881

## Workshop 2024

https://gwosc.org/odw/odw2024/


What are gravitational waves events?
> Ripples in space-time caused by passing gravitational waves from cataclysmic cosmic events such as colliding neutron stars or black holes, or by supernovae.

Introduction to LIGO/Virgo data

'''

# using the mybinder setup to execute online jyputer notebook > not stable

# Gravitational Wave Open Data Workshop #4 (2021)
# https://gw-odw.thinkific.com/courses/take/gw-open-data-workshop-4/texts/24465187-welcome

'''
set up Google Colab to run the tutorials
https://colab.research.google.com/

'''
## Tutorial 1.1 Discovering open data from GW observatories. Introducing gwosc package, find_datasets module and bacis arguments to query datasets.

# ! pip install -q 'gwosc==0.5.4'
import gwosc
print(gwosc.__version__)

from gwosc.datasets import find_datasets
from gwosc import datasets

### Excercise 1: How many months did O2 last? (Hint: check the output of find_datasets(type='run') to find the correct label to use)
# 9. To query for the GPS time interval for an observing run. To convert the gps time to UTC: https://gwosc.org/gps/
print(run_segment('O2_16KHZ_R1')) # UTC 2016-11-30T16:00:00, 2017-08-25T22:00:00, so O2 lasts for 9 months.
print(run_segment('O2_4KHZ_R1'))

### Excercise 2: How many GWTC-1-confident events were detected during O1?
# 3
O1_events = datasets.find_datasets(type='events', catalog='GWTC-1-confident', segment=run_segment('O1'))
print(O1_events)

### Excercise 3: What file URL contains data for V1 4096 seconds around GW170817?
# http://gwosc.org/eventapi/json/GWTC-1-confident/GW170817/v3/V-V1_GWOSC_4KHZ_R1-1187006835-4096.hdf5
urls = get_event_urls('GW170817', duration=4096, detector='V1')
print(urls)

'''
detectors:
'G1' - GEO600
'H1' - LIGO-Hanford
'L1' - LIGO-Livingston
'V1' - (Advanced) Virgo
'K1' -  KAGRA

'''

## Tutorial 1.2: Introduction to GWpy: a python package for gravitational astrophysics, and walk-through how you can use this to speed up access to, and processing of, GWOSC data.

'''
Environment issues:

need to install gwpy 2.1.2 to support astropy 5 as mentioned in https://github.com/gwpy/gwpy/pull/1435, but then getting error: 
---> 2 ldata = TimeSeries.fetch_open_data('L1', *segment, verbose=True)
--> 153     cache = get_urls(detector, int(start), int(ceil(end)), **url_kw)
TypeError: get_urls() got an unexpected keyword argument 'tag'

Sovled: install the latest ! pip install -q 'gwpy==3.0.8'

'''

# Fast Fourier Transform. Calculating the power spectral density

# https://gwosc.org/o2speclines/

### Quiz 1
'''
Q: Plot the data for the LIGO-Hanford detector around GW190412. Looking at your new LIGO-Handford plot, can your eye identify a signal peak?

# get Hanford data
hdata3 = TimeSeries.fetch_open_data('H1', int(gps)-512, int(gps)+512, cache=True)
hasd3 = hdata3.asd(fftlength=4, method="median")

plot3 = hasd3.plot()
ax3 = plot.gca()

plot.show(warn=False)
'''
