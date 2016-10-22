These n-grams are based on the largest publicly-available, genre-balanced corpus of English - the 520 million word Corpus of Contemporary American English (COCA).

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
