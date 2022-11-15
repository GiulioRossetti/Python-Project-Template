===
API
===

Example of automatically generated documentation from docstrings:

^^^^^^^
Classes
^^^^^^^

------------
``Porofile``
------------

.. currentmodule:: package_name
.. autoclass:: Profile
    :members:
    :inherited-members:

-------------
``Porofiles``
-------------

.. currentmodule:: package_name
.. autoclass:: Profiles
    :members:
    :inherited-members:

Data transformation

.. autosummary::

    Profiles.add_profile


^^^^^^^^^^
Algorithms
^^^^^^^^^^

.. automodule:: package_name.algorithms

``Porofiles`` container sorting methods


.. autosummary::
    :toctree: algs/

    sort_profiles_by_age
    sort_profiles_by_name

^^^
I/O
^^^

.. automodule:: package_name.readwrite

JSON I/O

.. autosummary::
    :toctree: io/

    to_json
    from_json

