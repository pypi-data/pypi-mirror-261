from __future__ import annotations

import warnings
from typing import Sequence

import numpy as np
import pandas as pd
from rdkit import RDLogger
from rdkit.Chem import AllChem
from syntheseus.interface.bag import Bag
from syntheseus.interface.models import BackwardReactionModel
from syntheseus.interface.molecule import Molecule
from syntheseus.interface.reaction import SingleProductReaction

try:
    import keras
except ImportError:
    warnings.warn("Keras not installed, PaRoutes model will not be available.")

try:
    from rdchiral.main import rdchiralRunText
except ImportError:
    warnings.warn("rdchiral not installed, PaRoutes model will not be available.")


from syntheseus_paroutes.files import MODEL_DUMP_FILE, UNIQUE_TEMPLATE_FILE, ensure_file_downloaded

# Turn off rdkit logger
lg = RDLogger.logger()
lg.setLevel(RDLogger.CRITICAL)


def get_fingerprint(smiles: str) -> np.ndarray:
    mol = AllChem.MolFromSmiles(smiles)
    assert mol is not None
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
    return np.array(fp, dtype=np.float32)


class PaRoutesModel(BackwardReactionModel):
    def __init__(self, max_num_templates: int = 50, **kwargs):
        super().__init__(**kwargs)
        self.max_num_templates = max_num_templates
        self._build_model()

    def _build_model(
        self,
    ):
        """Builds template classification model."""

        # Template library
        ensure_file_downloaded(UNIQUE_TEMPLATE_FILE)
        self._template_df = pd.read_csv(UNIQUE_TEMPLATE_FILE, sep="\t", compression="gzip")

        # Keras model
        ensure_file_downloaded(MODEL_DUMP_FILE)
        self._model = keras.models.load_model(
            MODEL_DUMP_FILE,
            custom_objects={
                "top10_acc": keras.metrics.TopKCategoricalAccuracy(k=10, name="top10_acc"),
                "top50_acc": keras.metrics.TopKCategoricalAccuracy(k=50, name="top50_acc"),
            },
        )

    def _get_reactions(
        self,
        inputs: list[Molecule],
        num_results: int,
    ) -> list[Sequence[SingleProductReaction]]:
        # Make fingerprint array
        fingperprints = np.array([get_fingerprint(mol.smiles) for mol in inputs])

        # Call model
        template_softmax = self._model(fingperprints, training=False).numpy()
        assert template_softmax.shape == (len(inputs), len(self._template_df))
        template_argsort = np.argsort(-template_softmax, axis=1)

        # Run reactions for most likely templates
        output: list[list[SingleProductReaction]] = []
        for mol_i, mol in enumerate(inputs):
            curr_rxn_list: list[SingleProductReaction] = []
            for template_rank in range(self.max_num_templates):
                # Get template at this rank
                template_idx = template_argsort[mol_i, template_rank]
                curr_template_row = self._template_df.iloc[template_idx]
                curr_softmax_value = float(template_softmax[mol_i, template_idx])

                # Run reaction
                reactants_list: list[str] = rdchiralRunText(curr_template_row.retro_template, mol.smiles)

                # Filter out possible duplicates (the same template can be used multiple times but give the same reactants)
                reactant_sets = set(frozenset(s.split(".")) for s in reactants_list)

                # Create reaction outputs
                for reactant_strs in reactant_sets:
                    reactant_mols = [Molecule(smiles=s, make_rdkit_mol=False) for s in reactant_strs]
                    curr_rxn_list.append(
                        SingleProductReaction(
                            reactants=Bag(reactant_mols),
                            product=mol,
                            metadata={
                                "template": curr_template_row.retro_template,
                                "probability": curr_softmax_value,
                                "template_idx": template_idx,  # type: ignore[typeddict-item]
                                "template_rank": template_rank,  # type: ignore[typeddict-item]
                                "template_library_occurence": curr_template_row.library_occurence,  # type: ignore[typeddict-item]
                            },
                        )
                    )
            output.append(curr_rxn_list[:num_results])

        return output
