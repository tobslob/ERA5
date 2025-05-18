import xarray as xr
import os


def load_variable(file_path: str, variable: str):
    VAR_SHORTNAMES = {
        "2m_temperature": "t2m",
        "total_precipitation": "tp",
    }

    mapped_var = VAR_SHORTNAMES.get(variable, variable)
    ext = os.path.splitext(file_path)[1].lower()

    if ext in [".grib", ".grib2"]:
        try:
            ds = xr.open_dataset(
                file_path,
                engine="cfgrib",
                backend_kwargs={"filter_by_keys": {"shortName": mapped_var}}
            )
            if mapped_var not in ds.data_vars:
                raise ValueError(
                    "Filtered dataset did not contain the variable.")
        except Exception as e:
            print(
                f"[cfgrib fallback] Filter failed: {e}. Retrying without filter...")
            ds = xr.open_dataset(file_path, engine="cfgrib")
            if mapped_var not in ds.data_vars:
                raise Exception(
                    f"Variable '{mapped_var}' not found even after fallback. Available: {list(ds.data_vars)}"
                )

    elif ext in [".nc", ".netcdf"]:
        ds = xr.open_dataset(file_path, engine="netcdf4")
    else:
        raise ValueError("Unsupported file format")

    if mapped_var not in ds.data_vars:
        raise Exception(
            f"Variable '{mapped_var}' not found. Available: {list(ds.data_vars)}")

    return ds, mapped_var
