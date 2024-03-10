"""Code to fetch PaRoutes files."""

import os
from pathlib import Path

import requests
import tqdm
from syntheseus.reaction_prediction.utils.downloading import get_cache_dir

# Constants where the files will be accessed from
BASE_PATH = get_cache_dir("syntheseus_paroutes")

N_LIST = [1, 5]

TARGET_FILES = {n: str(BASE_PATH / f"n{n}-targets.txt") for n in N_LIST}
STOCK_FILES = {n: str(BASE_PATH / f"n{n}-stock.txt") for n in N_LIST}
UNIQUE_TEMPLATE_FILE = str(BASE_PATH / "uspto_unique_templates.csv.gz")
MODEL_DUMP_FILE = str(BASE_PATH / "uspto_keras_model.hdf5")
ROUTE_JSON_FILES = {n: str(BASE_PATH / f"n{n}-routes.json") for n in N_LIST}

# Copied from PaRoutes github:
# https://github.com/MolecularAI/PaRoutes/blob/634d8545c4163feeb260ea631223c249bf80adc0/data/download_data.py#L75C1-L124C2
FILES_TO_DOWNLOAD = [
    {
        "filename": "chembl_10k_route_distance_model.ckpt",
        "url": "https://zenodo.org/record/4925903/files/chembl_10k_route_distance_model.ckpt?download=1",
    },
    {
        "filename": "n1-routes.json",
        "url": "https://zenodo.org/record/7341155/files/ref_routes_n1.json?download=1",
    },
    {
        "filename": "n1-targets.txt",
        "url": "https://zenodo.org/record/7341155/files/targets_n1.txt?download=1",
    },
    {
        "filename": "n1-stock.txt",
        "url": "https://zenodo.org/record/7341155/files/stock_n1.txt?download=1",
    },
    {
        "filename": "n5-routes.json",
        "url": "https://zenodo.org/record/7341155/files/ref_routes_n5.json?download=1",
    },
    {
        "filename": "n5-targets.txt",
        "url": "https://zenodo.org/record/7341155/files/targets_n5.txt?download=1",
    },
    {
        "filename": "n5-stock.txt",
        "url": "https://zenodo.org/record/7341155/files/stock_n5.txt?download=1",
    },
    {
        "filename": "uspto_template_library.csv",
        "url": "https://zenodo.org/record/7341155/files/uspto_template_library.csv?download=1",
    },
    {
        "filename": "selected_reactions_all.csv",
        "url": "https://zenodo.org/record/7341155/files/selected_reactions_all.csv?download=1",
    },
    {
        "filename": "uspto_keras_model.hdf5",
        "url": "https://zenodo.org/record/7341155/files/uspto_keras_model.hdf5?download=1",
    },
    {
        "filename": "uspto_unique_templates.csv.gz",
        "url": "https://zenodo.org/record/7341155/files/uspto_unique_templates.csv.gz?download=1",
    },
    {
        "filename": "all_routes.json.gz",
        "url": "https://zenodo.org/record/7341155/files/all_loaded_routes.json.gz?download=1",
    },
]


def _download_file(url: str, filename: str) -> None:
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get("content-length", 0))
        pbar = tqdm.tqdm(total=total_size, desc=os.path.basename(filename), unit="B", unit_scale=True)
        with open(filename, "wb") as fileobj:
            for chunk in response.iter_content(chunk_size=1024):
                fileobj.write(chunk)
                pbar.update(len(chunk))
        pbar.close()


def ensure_file_downloaded(file: str) -> None:
    """Checks if one of the files given is present, and if not, downloads it."""
    file = Path(file)
    if file.exists():
        return

    # Create parent directories if they don't exist, otherwise download will fail
    file.parent.mkdir(parents=True, exist_ok=True)

    for filespec in FILES_TO_DOWNLOAD:
        if file.name == filespec["filename"]:
            _download_file(filespec["url"], str(file))
            return
    raise ValueError(f"File {file} not found in FILES_TO_DOWNLOAD.")
