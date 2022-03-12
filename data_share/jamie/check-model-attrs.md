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
import dask

#dask.config.set({"array.slicing.split_large_chunks": True})

#get esm datastore
odie = pooch.create(
    # Use the default cache folder for the operating system
    path="./.cache",
    base_url="https://storage.googleapis.com/cmip6/",
    # The registry specifies the files that can be fetched
    registry={
        "pangeo-cmip6.csv": "574af6b61f90e30ea45605b2b290f80c1a3a7b7dbfb44e7ae68977c1abc76b1c",
    },
)

file_path = odie.fetch("pangeo-cmip6.csv")
df_og = pd.read_csv(file_path)
```

```{code-cell} ipython3
query = "variable_id=='cl' & table_id=='Amon' & source_id=='MRI-ESM2-0'"
#query = "variable_id=='cl' & table_id=='Amon' & experiment_id=='hist-stratO3'"
#query = "variable_id=='sftlf' & table_id=='fx' & source_id=='BCC-ESM1'"
df = df_og.query(query)

print(df.drop_duplicates(['experiment_id'])['experiment_id'])
```

```{code-cell} ipython3
#sea area percentage parameters:
lp_var_id = "sftlf" #Percentage of the grid cell occupied by land (including lakes) [%]
lp_monthly_table = "fx" #fixed variables
lp_exp_id = "1pctCO2"

#model parameters:
var_id = "cl"
monthly_table = "Amon"


def save_model(mod_id, exp_id, lev_conversion, slice_time):
    query = "variable_id=='"+lp_var_id+"' & experiment_id=='"+lp_exp_id+"' & source_id=='"+mod_id+"' & table_id=='"+lp_monthly_table+"'"
    lp_df = df_og.query(query)
    zstore_url = lp_df["zstore"].values[0]
    lp_ds = xr.open_zarr(fsspec.get_mapper(zstore_url), consolidated=True)
    
    #Cloud Data
    query = "variable_id=='"+var_id+"' & experiment_id=='"+exp_id+"' & source_id=='"+mod_id+"' & table_id=='"+monthly_table+"'"
    cloud_df = df_og.query(query)
    zstore_url = cloud_df["zstore"].values[0]
    ds = xr.open_zarr(fsspec.get_mapper(zstore_url), consolidated=True)

    lp_ds = lp_ds.reindex_like(ds, method="nearest")
    ds_water = ds.where(lp_ds.sftlf == 0.0) #only values over water
    ds_subset = ds_water.where(ds_water.lev*lev_conversion > 0.7)
    
    ds_subset = ds_subset.sel(lat=slice(15, 40),  #15-40 degrees North latitude 
                                    lon=slice(225, 235)) #and about 125 to 135 degrees west longitude
    if slice_time:
        ds_subset = ds_subset.isel(time=slice(0, 6000))

    print(ds_subset.lon.attrs)


    
save_model("CESM2", "ssp585", 1, False)
save_model("CESM2", "piControl", 1, False)
    
    

#save_model("CESM2", "abrupt-4xCO2", -(1/1000), False)
#save_model("CESM2", "ssp585", 1, False)
#save_model("UKESM1-0-LL", "abrupt-4xCO2", 1, False)
```

```{code-cell} ipython3

```
