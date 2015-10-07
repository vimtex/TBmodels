#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    05.10.2015 16:54:52 CEST
# File:    change_uc.py

from common import *

import numpy as np

class HrPrintTestCase(CommonTestCase):
    def createH(self, t1, t2, uc=None):

        builder = tbmodels.Builder()

        # create the two atoms
        builder.add_atom([1], [0, 0, 0.], 1)
        builder.add_atom([-1], [0.5, 0.5, 0.2], 0)
        builder.add_atom([0.], [0.75, 0.15, 0.6], 0)

        # add hopping between different atoms
        builder.add_hopping(((0, 0), (1, 0)),
                           tbmodels.helpers.combine([0, -1], [0, -1], 0),
                           t1,
                           phase=[1, -1j, 1j, -1])

        # add hopping between neighbouring orbitals of the same type
        builder.add_hopping(((0, 0), (0, 0)),
                           tbmodels.helpers.neighbours([0, 1],
                                                        forward_only=True),
                           t2,
                           phase=[1])
        builder.add_hopping(((1, 0), (1, 0)),
                           tbmodels.helpers.neighbours([0, 1],
                                                        forward_only=True),
                           -t2,
                           phase=[1])
        self.model = builder.create(uc=uc)

    def test0(self):
        self.createH(0.1, 0.211)
        res = ' created by the TBModels package    Wed, 07 Oct 2015 13:09:32 CEST\n           3\n           7\n    1    1    1    1    1    1    1\n   -1   -1    0    0    0    0.000000    0.000000\n   -1   -1    0    1    0    0.000000    0.000000\n   -1   -1    0    2    0    0.000000    0.000000\n   -1   -1    0    0    1   -0.100000    0.000000\n   -1   -1    0    1    1    0.000000    0.000000\n   -1   -1    0    2    1    0.000000    0.000000\n   -1   -1    0    0    2    0.000000    0.000000\n   -1   -1    0    1    2    0.000000    0.000000\n   -1   -1    0    2    2    0.000000    0.000000\n   -1    0    0    0    0    0.211000    0.000000\n   -1    0    0    1    0    0.000000    0.000000\n   -1    0    0    2    0    0.000000    0.000000\n   -1    0    0    0    1    0.000000    0.100000\n   -1    0    0    1    1   -0.211000    0.000000\n   -1    0    0    2    1    0.000000    0.000000\n   -1    0    0    0    2    0.000000    0.000000\n   -1    0    0    1    2    0.000000    0.000000\n   -1    0    0    2    2    0.000000    0.000000\n    0   -1    0    0    0    0.211000    0.000000\n    0   -1    0    1    0    0.000000    0.000000\n    0   -1    0    2    0    0.000000    0.000000\n    0   -1    0    0    1    0.000000   -0.100000\n    0   -1    0    1    1   -0.211000    0.000000\n    0   -1    0    2    1    0.000000    0.000000\n    0   -1    0    0    2    0.000000    0.000000\n    0   -1    0    1    2    0.000000    0.000000\n    0   -1    0    2    2    0.000000    0.000000\n    0    0    0    0    0    1.000000    0.000000\n    0    0    0    1    0    0.100000    0.000000\n    0    0    0    2    0    0.000000    0.000000\n    0    0    0    0    1    0.100000    0.000000\n    0    0    0    1    1   -1.000000    0.000000\n    0    0    0    2    1    0.000000    0.000000\n    0    0    0    0    2    0.000000    0.000000\n    0    0    0    1    2    0.000000    0.000000\n    0    0    0    2    2    0.000000    0.000000\n    0    1    0    0    0    0.211000    0.000000\n    0    1    0    1    0    0.000000    0.100000\n    0    1    0    2    0    0.000000    0.000000\n    0    1    0    0    1    0.000000    0.000000\n    0    1    0    1    1   -0.211000    0.000000\n    0    1    0    2    1    0.000000    0.000000\n    0    1    0    0    2    0.000000    0.000000\n    0    1    0    1    2    0.000000    0.000000\n    0    1    0    2    2    0.000000    0.000000\n    1    0    0    0    0    0.211000    0.000000\n    1    0    0    1    0    0.000000   -0.100000\n    1    0    0    2    0    0.000000    0.000000\n    1    0    0    0    1    0.000000    0.000000\n    1    0    0    1    1   -0.211000    0.000000\n    1    0    0    2    1    0.000000    0.000000\n    1    0    0    0    2    0.000000    0.000000\n    1    0    0    1    2    0.000000    0.000000\n    1    0    0    2    2    0.000000    0.000000\n    1    1    0    0    0    0.000000    0.000000\n    1    1    0    1    0   -0.100000    0.000000\n    1    1    0    2    0    0.000000    0.000000\n    1    1    0    0    1    0.000000    0.000000\n    1    1    0    1    1    0.000000    0.000000\n    1    1    0    2    1    0.000000    0.000000\n    1    1    0    0    2    0.000000    0.000000\n    1    1    0    1    2    0.000000    0.000000\n    1    1    0    2    2    0.000000    0.000000'
        self.assertEqual(res, self.model.to_hr())
    

if __name__ == "__main__":
    unittest.main()