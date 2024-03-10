from syntheseus.interface.bag import Bag
from syntheseus.interface.molecule import Molecule
from syntheseus.interface.reaction import SingleProductReaction

from syntheseus_paroutes import PaRoutesModel


def test_model():

    # Create the model
    model = PaRoutesModel()

    # Call the model
    inputs = [Molecule("NC(=O)Cc1c[nH]c2cc(Br)ccc12"), Molecule("CCc1ccccc1CC(=O)O")]
    output = model(inputs)

    # Check the output (at least the first few)
    assert len(output) == 2
    assert len(output[0]) == 28
    assert output[0][0] == SingleProductReaction(
        product=inputs[0], reactants=Bag((Molecule(smiles="N"), Molecule(smiles="O=C(O)Cc1c[nH]c2cc(Br)ccc12")))
    )
    assert len(output[1]) == 56
    assert output[1][0] == SingleProductReaction(
        product=inputs[1], reactants=Bag([Molecule(smiles="CCc1ccccc1CC(=O)OC")])
    )
