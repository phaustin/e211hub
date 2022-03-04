---
jupytext:
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

```{code-cell} ipython3
import xarray as xr
import pooch
import pandas as pd
import fsspec
from pathlib import Path
import json
import plotly.graph_objects as go
from scipy import signal
import matplotlib.pyplot as plt


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
        "pangeo-cmip6.csv": "ab52d9390668761b98351b5e37136d9943b3d6ea9c7f624908ff122b70626d27",
    },
)

file_path = odie.fetch("pangeo-cmip6.csv")
df_og = pd.read_csv(file_path)
```

```{code-cell} ipython3
#sea area percentage parameters:
lp_var_id = "sftlf" #Percentage of the grid cell occupied by land (including lakes) [%]
#lp_exp_id = "piControl"
lp_monthly_table = "fx" #fixed variables

#model parameters:
var_id = "cllcalipso"
monthly_table = "CFmon"


mod_id = "GFDL-CM4"
exp_id_list = ["historical"]
#exp_id_list = ["ssp245", "piControl"]

for exp_id in exp_id_list:
    
    #get the lats and lons for our data:
    query = "variable_id=='"+lp_var_id+"' & experiment_id=='"+exp_id+"' & source_id=='"+mod_id+"' & table_id=='"+lp_monthly_table+"'"
    lp_df = df_og.query(query)
    zstore_url = lp_df["zstore"].values[0]
    lp_ds = xr.open_zarr(fsspec.get_mapper(zstore_url), consolidated=True)
    
    #Cloud Data
    query = "variable_id=='"+var_id+"' & experiment_id=='"+exp_id+"' & source_id=='"+mod_id+"' & table_id=='"+monthly_table+"'"
    cloud_df = df_og.query(query)
    zstore_url = cloud_df["zstore"].values[0]
    ds = xr.open_zarr(fsspec.get_mapper(zstore_url), consolidated=True)
    
    
    #print(lp_ds.lat)
    lp_ds = lp_ds.reindex_like(ds, method="nearest")
    #print(lp_ds.lat)
    
    ds_water = ds.where(lp_ds.sftlf == 0.0) #only values over water
    ds_subset = ds_water.sel(lat=slice(15, 40),  #15-40 degrees North latitude 
                                    lon=slice(225, 235)) #and about 125 to 135 degrees west longitude
    
    spatial_mean = ds_subset.mean(dim=["lat", "lon"])
    
    if (exp_id == "piControl"):
        times = xr.cftime_range(start="1850", periods=6000, freq="M", calendar="noleap")
        times = times.shift(-1, "M").shift(16, "D").shift(12, "H")
    else:
        times = spatial_mean.indexes["time"]

    cloud_cover = spatial_mean[var_id].values
    cloud_cover_filt = filter_cloud_cover(cloud_cover, 10)
    
    
    plt.plot(times, cloud_cover_filt)

plt.show()
```

```{code-cell} ipython3

```
