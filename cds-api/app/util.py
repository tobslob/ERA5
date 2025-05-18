import xarray as xr
import os


def load_variable(file_path: str, variable: str):
    VAR_SHORTNAMES = {
        "2m_temperature": "t2m",
        "total_precipitation": "tp",
        "10m_u_component_of_wind": "u10",
        "10m_v_component_of_wind": "v10"
    }

    mapped_var = VAR_SHORTNAMES.get(variable, variable)
    ext = os.path.splitext(file_path)[1].lower()

    if ext in [".grib", ".grib2"]:
        ds = xr.open_dataset(
            file_path,
            engine="cfgrib",
            backend_kwargs={"filter_by_keys": {"shortName": mapped_var}}
        )
    elif ext in [".nc", ".netcdf"]:
        ds = xr.open_dataset(file_path, engine="netcdf4")
    else:
        raise ValueError("Unsupported file format")

    if mapped_var not in ds.data_vars:
        raise Exception(
            f"Variable '{mapped_var}' not found. Available: {list(ds.data_vars)}")

    return ds, mapped_var
