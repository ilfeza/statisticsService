from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas
from app.database import get_db
from app.utils import calculate_statistics

router = APIRouter()



@router.post("/{device_id}/measures/", response_model=schemas.MeasureCreate)
def create_measure_for_device(device_id, measure: schemas.MeasureCreate, db=Depends(get_db)):
    device = crud.get_device(db, device_id=device_id)
    if not device:
        device_create = schemas.DeviceCreate(id=device_id, name="Device_name")
        crud.create_device(db, device=device_create)

    return crud.create_measure(db=db, measure=measure, device_id=device_id)
@router.get("/{device_id}/status/", response_model=schemas.StatisticsResponse)
def get_device_stats(device_id, start_time=None, end_time=None, db=Depends(get_db)):
    measures = crud.get_measures(db, device_id=device_id, start_time=start_time, end_time=end_time)

    return {
        "x": calculate_statistics([m.x for m in measures]),
        "y": calculate_statistics([m.y for m in measures]),
        "z": calculate_statistics([m.z for m in measures])
    }
