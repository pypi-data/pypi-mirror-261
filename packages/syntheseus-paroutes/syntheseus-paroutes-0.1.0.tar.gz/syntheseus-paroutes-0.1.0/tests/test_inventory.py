import pytest

from syntheseus_paroutes import PaRoutesInventory


@pytest.mark.parametrize("n", [1, 5])
def test_inventory(n: int):
    inv = PaRoutesInventory(n=n)

    # Test length is correct
    assert (
        len(inv.purchasable_mols())
        == {
            1: 13432,
            5: 13326,  # NOTE: looks like this file might contain some duplicates
        }[n]
    )
