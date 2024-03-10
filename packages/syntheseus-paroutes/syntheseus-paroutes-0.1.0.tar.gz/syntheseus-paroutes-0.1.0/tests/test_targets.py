import pytest

from syntheseus_paroutes import get_target_smiles_list


@pytest.mark.parametrize("n", [1, 5])
def test_inventory(n: int):
    smiles = get_target_smiles_list(n)

    # Test length is correct
    assert len(smiles) == 10_000
