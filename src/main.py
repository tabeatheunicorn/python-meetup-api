from typing import List
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from .models import (
    Device,
    MeasurementMeta,
    MeasurementData,
    get_all_device_from_data_folder,
    get_all_measurements_for_device,
    get_measurement_data_from_id,
    NoMeasurementsFoundException,
)
from .utils import create_graph

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/devices", response_model=List[Device])
def get_all_devices():
    return get_all_device_from_data_folder()


@app.get("/device/{device_id}/measurements", response_model=List[MeasurementMeta])
def get_measurements_for_device(device_id: str):
    try:
        return get_all_measurements_for_device(device_name=device_id)
    except NoMeasurementsFoundException:
        return HTTPException(status_code=404, detail="No measurements for device found")


@app.get("/measurements/{measurement_id}", response_model=MeasurementData)
def get_data_from_measurement(measurement_id):
    try:
        return get_measurement_data_from_id(measure_id=measurement_id)
    except FileNotFoundError:
        return HTTPException(
            status_code=404, detail=f"Measurement {measurement_id} not found."
        )


# https://fastapi.tiangolo.com/advanced/custom-response/
@app.get("/measurements/{measurement_id}/graph", response_class=HTMLResponse)
def get_graph_from_measurement(measurement_id):
    try:
        data: MeasurementData = get_measurement_data_from_id(measure_id=measurement_id)
    except FileNotFoundError:
        return HTTPException(
            status_code=404, detail=f"Measurement {measurement_id} not found."
        )
    return create_graph(data=data)
