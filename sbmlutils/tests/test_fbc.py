"""
Unit tests for fbc.
"""
from __future__ import print_function, absolute_import
import cobra
import libsbml
import os

import sbmlutils.fbc as fbc
from sbmlutils.tests import data

FBC_SBML = os.path.join(data.data_dir, 'fbc/diauxic_fba.xml')


def test_load_cobra_model():
    assert os.path.exists(FBC_SBML)
    fbc.load_cobra_model(FBC_SBML)


def test_reaction_info():
    cobra_model = fbc.load_cobra_model(FBC_SBML)
    df = fbc.cobra_reaction_info(cobra_model)
    assert df is not None
    print(df)

    assert df.objective.loc('v4') == 1
    assert df.objective.loc('v1') == 1




def test_mass_balance():

    doc = libsbml.readSBMLFromFile(data.DEMO_SBML)

    # add defaults
    fbc.add_default_flux_bounds(doc)

    import tempfile
    f = tempfile.NamedTemporaryFile('w', suffix='xml')
    libsbml.writeSBMLToFile(doc, f.name)
    f.flush()
    model = cobra.io.read_sbml_model(f.name)

    # mass/charge balance
    for r in model.reactions:
        mb = r.check_mass_balance()
        # all metabolites are balanced
        assert len(mb) == 0
