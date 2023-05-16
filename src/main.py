from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/devices")
def get_all_devices():
    ...
    
@app.get("/device/{device_id}/measurements")
def get_measurements_for_device(device_id):
    ...
    
@app.get("/measurements/{measurement_id}")
def get_data_from_measurement(measurement_id):
    ...
    

@app.get("/measurements/{measurement_id}/graph")
def get_graph_from_measurement(measurement_id):
    ...