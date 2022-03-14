---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# plot cl from archive

+++

read cl cloud fraction for 11 lowest model levels from zarr files in `models/`

```{code-cell} ipython3
import xarray as xr
import pooch
import pandas as pd
import fsspec
from pathlib import Path
import json
from matplotlib import pyplot as plt
from scipy import signal


def filter_cloud_cover(cloud_cover, n_years):
    #using average month length for now
    fs = 1/(30.437*24*60*60) #1 month in Hz (sampling frequency)
    nyquist = fs / 2 # 0.5 times the sampling frequency
    cutoff =  1/(n_years*365*24*60*60)# cutoff in Hz, n_years in Hz
    normal_cutoff = cutoff / nyquist
    
    b, a = signal.butter(5, normal_cutoff, btype='lowpass') #low pass filter
    cloud_cover_filt = signal.filtfilt(b, a, cloud_cover)
    return cloud_cover_filt


#get esm datastore
odie = pooch.create(
    # Use the default cache folder for the operating system
    path="./.cache",
    base_url="https://storage.googleapis.com/cmip6/",
    # The registry specifies the files that can be fetched
    registry={
        "pangeo-cmip6.csv": None,
    },
)

file_path = odie.fetch("pangeo-cmip6.csv")
df_og = pd.read_csv(file_path)
```

```{code-cell} ipython3
hit = df_og['table_id'] == 'Amon'
amon_table=  df_og[hit]
hit = amon_table['source_id']=='CMCC-CM2-HR4'
cmcc = amon_table[hit]
amon_table.head()
cmcc
```

```{code-cell} ipython3
with  open('models.json') as models_json:
      models_dict = json.load(models_json)                                                                                                                                      
# if we want to use all the models:                                                                                                  
model_options = []                                                                                                                   
for model in models_dict["models"]:                                                                                                  
    mod_id = model["mod_id"]                                                                                                         
    model_options.append({"label": mod_id, "value": mod_id})      
```

```{code-cell} ipython3
model_options
```

```{code-cell} ipython3
var_id = "cl"
exp_id_list=['piControl'] 
mod_id="CanESM5"
#mod_id = "BCC-ESM1"
for exp_id in exp_id_list:
    ds = xr.open_zarr(Path('models/'+mod_id+'_'+exp_id+'.zarr'))
    spatial_mean = ds.mean(dim=["lat", "lon", "lev"])

    if (exp_id == "piControl") | (exp_id == "historical") | (exp_id == "abrupt-4xCO2"):
        times = xr.cftime_range(start="1850", periods=len(spatial_mean[var_id]), freq="M", calendar="noleap")
        times = times.shift(-1, "M").shift(16, "D").shift(12, "H")
    else:
        times = spatial_mean.indexes["time"]

    if (mod_id == "CESM2") & (exp_id == "ssp585"):
        cloud_cover = spatial_mean[var_id].values*100
    else:
        cloud_cover = spatial_mean[var_id].values

    cloud_cover_filt = filter_cloud_cover(cloud_cover, 10)
```

```{code-cell} ipython3
ds['cl']
```

```{code-cell} ipython3
spatial_mean
```

```{code-cell} ipython3
times
```

```{code-cell} ipython3
help(times)
```

```{code-cell} ipython3
fig, ax = plt.subplots(1,1, figsize=(10,8))
ax.plot(times.to_datetimeindex(),spatial_mean['cl'].values);
```

```{code-cell} ipython3
fig, ax = plt.subplots(1,1, figsize=(10,8))
ax.plot(times.to_datetimeindex(),cloud_cover_filt);
```
