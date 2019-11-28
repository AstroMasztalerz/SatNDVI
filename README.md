# SatNDVI
Python code snippet to produce NDVI images from Red and NIR spectral channel images from satellites.
This small snippet will produce NDVI images with false-color palletes using NIR and R band images from satellite (Band 3 for R, Band 4 for NIR)
Prefferably use with cloudless, calibrated images that have had waterbody masks applied, or you can apply waterbody masks after NDVI processing.
NDVI is scaled on -1 to 1 scale, representing quality of vegetation. Tested with Himawari8 data.
Uses AstroPy and MatPlotLib
