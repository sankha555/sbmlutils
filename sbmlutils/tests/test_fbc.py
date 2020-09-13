"""
Unit tests for fbc.
"""

import os
import cobra
import libsbml
import sbmlutils.fbc as fbc
from sbmlutils.sbmlio import read_sbml, write_sbml
from sbmlutils.tests import FBC_SBML, DEMO_SBML


def test_load_cobra_model():
    assert os.path.exists(FBC_SBML)
    fbc.load_cobra_model(FBC_SBML)


def test_reaction_info():
    cobra_model = fbc.load_cobra_model(FBC_SBML)
    df = fbc.cobra_reaction_info(cobra_model)
    assert df is not None
    print(df)

    assert df.at['v1', 'objective_coefficient'] == 1
    assert df.at['v2', 'objective_coefficient'] == 1
    assert df.at['v3', 'objective_coefficient'] == 1
    assert df.at['v4', 'objective_coefficient'] == 1
    assert df.at['EX_Ac', 'objective_coefficient'] == 0
    assert df.at['EX_Glcxt', 'objective_coefficient'] == 0
    assert df.at['EX_O2', 'objective_coefficient'] == 0
    assert df.at['EX_X', 'objective_coefficient'] == 0


def test_mass_balance(tmp_path):
    doc = read_sbml(DEMO_SBML)

    # add defaults
    fbc.add_default_flux_bounds(doc)

    import tempfile
    f = tempfile.NamedTemporaryFile('w', suffix='xml')
    libsbml.writeSBMLToFile(doc, f.name)
    f.flush()
    filepath = tmp_path / "test.xml"
    write_sbml(doc, filepath=filepath)

    model = cobra.io.read_sbml_model(str(filepath))

    # mass/charge balance
    for r in model.reactions:
        mb = r.check_mass_balance()
        # all metabolites are balanced
        assert len(mb) == 0
