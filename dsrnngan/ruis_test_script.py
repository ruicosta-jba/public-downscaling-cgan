
import numpy as np
import xarray as xr

import read_config

FCST_PATH = "/app/data/ERA5_raw/ruis_ERA5_nc_files/"

#load_fcst

ds_path = os.path.join(FCST_PATH, "/era5_total_precipitation_1980-01_hourly_80E-180E_60S-35N.nc")
# ds = xr.open_dataset(ds_path)
