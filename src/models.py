from typing import Tuple, List
from pathlib import Path
from pydantic import BaseModel

class Device(BaseModel):
    name: str
    description: str


class MeasurementMeta(BaseModel):
    id: int
    device_id: int

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
        return ""  # Wenn keine Datei gefunden wird, gebe eine leere Beschreibung zurück
    


def get_all_device_from_data_folder():
    subfolders = [subfolder for subfolder in DATA_FOLDER.iterdir() if subfolder.is_dir()]
    devices = [
        Device(
            name=subfolder.name,
            description=get_device_description(subfolder.name)
        )
        for subfolder in subfolders
    ]
    return devices
    