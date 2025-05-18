import os
import cdsapi
from dotenv import load_dotenv

load_dotenv()


def download_era5_data(product_type, data_format, variable, year, month, day, area, time):

    url = os.environ["ERA5_API_URL"]
    key = os.environ["ERA5_API_KEY"]

    if not url or not key:
        raise Exception("CDS API credentials are missing")

    c = cdsapi.Client(f"{url}/api", key)

    output_dir = os.path.abspath("./output")
    os.makedirs(output_dir, exist_ok=True)

    filename = f"era5_{variable[0]}_{year[0]}.{data_format}"
    target_path = os.path.join(output_dir, filename)

    request_payload = {
        'product_type': product_type,
        'format': data_format,
        'variable': variable,
        'year': year,
        'month': month,
        'day': day,
        'area': area,
        'time': time,
        # 'download_format': download_format
    }

    print("CDS Request Payload:", request_payload)

    try:
        c.retrieve(
            'reanalysis-era5-single-levels',
            request_payload,
            target_path
        )
    except Exception as e:
        print("CDS API Error:", str(e))
        raise e

    return target_path
