from fastapi import APIRouter, HTTPException
from app.controller import extract_chart_data, extract_grid_data, fetch_climate_data
from pydantic import BaseModel
from typing import List, Union

router = APIRouter()


class ClimateRequest(BaseModel):
    product_type: Union[str, List[str]]
    data_format: str
    variable: Union[str, List[str]]
    year: Union[str, List[str]]
    month: Union[str, List[str]]
    day: Union[str, List[str]]
    area: List[float]
    time: Union[str, List[str]] = "12:00"
    # download_format: str


@router.post("/")
def get_climate_data(request: ClimateRequest):
    try:
        file_path = fetch_climate_data(request.dict())
        return {"success": True, "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/chart-data")
async def get_chart_data(file_path: str, lat: float, lon: float, variable: str = "t2m"):
    try:
        result = await extract_chart_data(file_path, lat, lon, variable)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/grid")
async def get_grid_data(file_path: str, time: str, variable: str = "t2m"):
    try:
        result = await extract_grid_data(file_path, time, variable)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
