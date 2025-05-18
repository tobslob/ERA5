from app.climate_service import download_era5_data
from app.util import load_variable
import asyncio
from concurrent.futures import ThreadPoolExecutor


def ensure_list(value):
    return value if isinstance(value, list) else [value]


def fetch_climate_data(params):
    product_type = ensure_list(params["product_type"])
    data_format = params["data_format"]
    variable = ensure_list(params["variable"])
    year = ensure_list(params["year"])
    month = ensure_list(params["month"])
    day = ensure_list(params["day"])
    time = ensure_list(params.get("time", "12:00"))
    area = params["area"]
    # download_format = params["download_format"]

    return download_era5_data(product_type, data_format, variable, year, month, day, area, time)


async def extract_chart_data(file_path: str, lat: float, lon: float, variable: str = "t2m"):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        ds, mapped_var = await loop.run_in_executor(pool, load_variable, file_path, variable)
    data = ds[mapped_var]

    time_coord = None
    for coord in ["time", "valid_time"]:
        if coord in data.coords:
            time_coord = coord
            break

    if not time_coord:
        raise Exception("No time coordinate found in dataset.")

    data = data.sel(latitude=lat, longitude=lon, method="nearest")

    results = []
    for i in range(data.sizes[time_coord]):
        results.append({
            "time": str(data.coords[time_coord].values[i]),
            "lat": float(data.coords["latitude"].values),
            "lon": float(data.coords["longitude"].values),
            "value": round(float(data.values[i]), 2)
        })

    return results


async def extract_map_data(file_path, time: str, variable: str):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        ds, mapped_var = await loop.run_in_executor(pool, load_variable, file_path, variable)

    data = ds[mapped_var]

    import numpy as np
    parsed_time = np.datetime64(time)

    # Use "time", not "valid_time"
    if "time" in data.dims:
        data = data.sel(time=parsed_time, method="nearest")
    else:
        raise ValueError("No 'time' dimension found in dataset")

    values = data.values
    lat = data.latitude.values
    lon = data.longitude.values

    result = []
    for i in range(len(lat)):
        for j in range(len(lon)):
            result.append({
                "lat": float(lat[i]),
                "lon": float(lon[j]),
                "value": round(float(values[i][j]), 2)
            })

    return result
