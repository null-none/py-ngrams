These n-grams are based on the largest publicly-available, genre-balanced corpus of English -- the 520 million word Corpus of Contemporary American English (COCA). With this n-grams data (2, 3, 4, 5-word sequences, with their frequency), you can carry out powerful queries offline -- without needing to access the corpus via the web interface.

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
