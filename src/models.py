from typing import Tuple, List, Optional
from pathlib import Path
from pydantic import BaseModel

class Device(BaseModel):
    name: str
    description: str


class MeasurementMeta(BaseModel):
    measure_id: str
    file_size: Optional[float]

class MeasurementData(BaseModel):
    meta: MeasurementMeta
    data: List[Tuple[float, float]]


DATA_FOLDER = Path(__file__).parents[1].joinpath("example-data")

def get_device_description(device_name: str):
    device_info_file = DATA_FOLDER / device_name / "info.txt"

    if device_info_file.exists():
        with open(device_info_file, "r") as file:
            return file.read().strip()
    else:
        return ""


def get_all_device_from_data_folder() -> List[Device]:
    subfolders = [subfolder for subfolder in DATA_FOLDER.iterdir() if subfolder.is_dir()]
    devices = [
        Device(
            name=subfolder.name,
            description=get_device_description(subfolder.name)
        )
        for subfolder in subfolders
    ]
    return devices

class NoMeasurementsFoundException(Exception):
    pass

def get_all_measurements_for_device(device_name) -> List[MeasurementMeta]:
    measurement_folder: Path = DATA_FOLDER / device_name
    measurement_files: List[Path] = measurement_folder.glob("*.csv")

    measurements = [
        MeasurementMeta(
            measure_id=f"{device_name}-{file.stem}",
            file_size=file
        )
        for file in measurement_files
    ]
    if len(measurements) == 0:
        raise NoMeasurementsFoundException
    return measurements


def get_measurement_data_from_id(measure_id: str):
    device_name, filename = measure_id.split("-")

    measurement_folder = DATA_FOLDER / device_name
    measurement_file = measurement_folder / (filename + ".csv")
    
    if not measurement_file.exists():
        raise FileNotFoundError

    # Read the content of the file and create a MeasurementData object
    # Assuming the file contains the data in the same format as before
    with open(measurement_file, "r") as file:
        lines = file.readlines()
        data = [
            tuple(map(float, line.strip().split(",")))
            for line in lines[1:]  # Skip the header line
        ]
        print(data)
        measurement_data = MeasurementData(meta=MeasurementMeta(measure_id=measure_id), data=data)
        return measurement_data
