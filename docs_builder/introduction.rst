Overview
============
Introduction
------------
**sbmlutils** are python utilities for working with `SBML <http://www.sbml.org>`_.
This python package provides handy features like HTML reports of SBML models, helper functions for model creation and manipulation, interpolation functions to add experimental data to models, or annotation of models.

Main features of **sbmlutils** are

- :ref:`SBML creator` : The modelcreator provides utilities for the creation of SBML models. Supports `comp` and `fbc` models. Model information is managed in python data structures which are used to create the models.
- :ref:`SBML distrib` : Support for encoding distributions and uncertainties in SBML.
- :ref:`SBML report` : HTML report of SBML models. This provides overview of the model contents.
- :ref:`SBML annotation` : Helper functions for the annotation of SBML models. Annotations are hereby defined in separate annotation files with annotations being matched to ids based on regular expression matching.
- :ref:`SBML converters` : Converters from and to SBML, e.g. xpp.
- :ref:`SBML interpolation` : Helper functions for working with data interpolation in SBML models.

Source code is available from
`https://github.com/matthiaskoenig/sbmlutils
<https://github.com/matthiaskoenig/sbmlutils>`_.

To report bugs, request features or asking questions please file an
`issue
<https://github.com/matthiaskoenig/sbmlutils/issues>`_.

If you use sbmlutils please cite
`https://doi.org/10.5281/zenodo.597149
<https://doi.org/10.5281/zenodo.597149>`_.

Installation
------------
The sbmlutils package is available from `pypi
<https://pypi.python.org/pypi/sbmlutils>`_ and can be installed via::

    pip install sbmlutils


For detailed installation instructions see
`https://github.com/matthiaskoenig/sbmlutils
<https://github.com/matthiaskoenig/sbmlutils>`_.

