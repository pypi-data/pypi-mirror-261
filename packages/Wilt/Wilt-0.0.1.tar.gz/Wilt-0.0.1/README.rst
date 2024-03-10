****
Wilt
****
The simplest possible code metric::

   W Whitespace
   I Integrated over
   L Lines of
   T Text

An implementation of WILT from a great talk by Robert Smallshire called
Confronting Complexity [1]_ [2]_. In the talk there were quite a few other
visualisations that inspire development this package.

Install with::

   pipx install Wilt

The metric can be calculated like::

  $ wilt /usr/lib/python3.12/unittest/case.py
  2677.75

  $ wilt '/usr/lib/python3.12/**/*.py'
  346219.0

  $ echo "    foo" | wilt -i 2 -
  2.0

____

.. [1] https://www.youtube.com/watch?v=W44Ub5ykBY4
.. [2] http://ticosa.org/output/Robert%20Smallshire-Confronting%20Complexity-%20TICOSA%202014.pdf
