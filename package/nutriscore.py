# !/usr/bin/env python
# -*- coding: utf-8 -*-

import package.dataOFF

class Nutriscore:
    def __init__(self):
        self.score = package.dataOFF.get_data("nutriscore_grade")
