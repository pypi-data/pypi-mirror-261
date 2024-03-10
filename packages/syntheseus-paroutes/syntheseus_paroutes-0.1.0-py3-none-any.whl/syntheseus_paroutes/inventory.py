from __future__ import annotations

from syntheseus.search.mol_inventory import SmilesListInventory

from syntheseus_paroutes.files import STOCK_FILES, ensure_file_downloaded


class PaRoutesInventory(SmilesListInventory):
    def __init__(self, n: int = 5, **kwargs):
        # Load stock molecules

        ensure_file_downloaded(STOCK_FILES[n])
        with open(STOCK_FILES[n]) as f:
            stock_smiles = f.readlines()
        super().__init__(smiles_list=stock_smiles, canonicalize=True, **kwargs)
