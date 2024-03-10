# Syntheseus PaRoutes

This is a small python package which provides access to the
[PaRoutes benchmark](https://github.com/MolecularAI/PaRoutes)
with the classes defined in [syntheseus](https://github.com/microsoft/syntheseus/).

The package provides the following:

```python
from syntheseus_paroutes.model import PaRoutesModel
model = PaRoutesModel()  # a syntheseus BackwardReactionModel object using pre-trained PaRoutes template classifier

from syntheseus_paroutes.inventory import PaRoutesInventory
inventory = PaRoutesInventory(n=5)  # inventory from their "n=5" benchmark

from syntheseus_paroutes.targets import get_target_smiles_list
targets = get_target_smiles_list(n=5)  # test SMILES for "n=5" benchmark
```

## Development

Ensure to install all pre-commit hooks and run unit tests (provided by pytest).
