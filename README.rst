##########
py ngrams
##########

These n-grams are based on the largest publicly-available, genre-balanced corpus of English - the 520 million word Corpus of Contemporary American English (COCA).

.. image:: https://badge.fury.io/py/ngrams.svg
    :target: https://pypi.python.org/pypi/ngrams

=======
Install
=======

.. code-block:: bash

    pip install ngrams

=======
Example
=======

.. code-block:: python

    from ngrams.generate import Ngrams

    number = 1

    ngrams = Ngrams(params)

    print ngrams.result()

=======
License
=======

MIT
