from __future__ import annotations

from syntheseus_paroutes.files import TARGET_FILES, ensure_file_downloaded


def get_target_smiles_list(n: int) -> list[str]:
    ensure_file_downloaded(TARGET_FILES[n])
    with open(TARGET_FILES[n]) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]  # NOTE: no header
