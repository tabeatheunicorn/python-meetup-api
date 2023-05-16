from fastapi.responses import HTMLResponse
from typing import List
from fastapi import FastAPI

from .models import Device, MeasurementMeta, MeasurementData

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/devices", response_model=List[Device])
def get_all_devices():
    return []
    
@app.get("/device/{device_id}/measurements", response_model=List[MeasurementMeta])
def get_measurements_for_device(device_id):
    return []
    
@app.get("/measurements/{measurement_id}", response_model=MeasurementData)
def get_data_from_measurement(measurement_id):
   ...
    

#https://fastapi.tiangolo.com/advanced/custom-response/
@app.get("/measurements/{measurement_id}/graph", response_class=HTMLResponse)
def get_graph_from_measurement(measurement_id):
    ...