"""NaN-aware reductions for sensor readings with missing values."""
import numpy as np

nan = np.nan
readings = np.array([
    [21.5, 22.0, nan, 23.1, 22.8],
    [19.0, nan, nan, 18.5, 19.4],
    [25.2, 24.8, 25.5, 26.0, nan],
])
print(readings)
print(repr(readings[1]))

print("plain sum (propagates nan):", readings.sum())
print("nansum:", np.nansum(readings))
print("nansum per sensor:", np.nansum(readings, axis=1))
print("nanmean per sensor:", np.round(np.nanmean(readings, axis=1), 4))
print("nanmean per time step:", np.round(np.nanmean(readings, axis=0), 4))
print("nanmax per sensor:", np.nanmax(readings, axis=1))
print("nanmin per sensor:", np.nanmin(readings, axis=1))
print("nanargmax per sensor:", np.nanargmax(readings, axis=1))
print("nanstd per sensor:", np.round(np.nanstd(readings, axis=1), 4))
print("nanmedian overall:", np.nanmedian(readings))
print("nanpercentile 75 per sensor:", np.nanpercentile(readings, 75, axis=1))

missing = np.isnan(readings)
print("missing mask:")
print(missing)
print("missing per sensor:", missing.sum(axis=1))
print("valid per time step:", (~missing).sum(axis=0))

# fill missing values with the sensor mean
fill = np.nanmean(readings, axis=1, keepdims=True)
filled = np.where(missing, fill, readings)
print("filled:")
print(np.round(filled, 3))
print("no nan left:", not np.isnan(filled).any())
print("mean preserved:", np.allclose(filled.mean(axis=1), fill.ravel()))

print("nancumsum row 1:", np.nancumsum(readings[1]))
print("nanprod of [2, nan, 3]:", np.nanprod(np.array([2.0, nan, 3.0])))

clean = readings[~np.isnan(readings)]
print("clean values:", clean)
print("np.mean of clean == nanmean:", np.isclose(clean.mean(), np.nanmean(readings)))
