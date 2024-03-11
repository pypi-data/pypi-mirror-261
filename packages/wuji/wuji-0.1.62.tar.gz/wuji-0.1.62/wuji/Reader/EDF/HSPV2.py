#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   HSPV2
@Time        :   2023/9/14 15:41
@Author      :   Xuesong Chen
@Description :
"""
import re

import numpy as np

from wuji.Reader.EDF.Base import Base


class HSPV2EDFReader(Base):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _assign_signal_types(self):
        self.signal_type = []
        for idx, sig in enumerate(self.signal_labels):
            if re.search('E[CK]G', sig, re.IGNORECASE):
                self.signal_type.append('ecg')
            elif re.search('S[pa]O2', sig, re.IGNORECASE):
                self.signal_type.append('spo2')
            elif re.search('ABD', sig, re.IGNORECASE):
                self.signal_type.append('abd')
            elif re.search('CHEST|THO', sig, re.IGNORECASE):
                self.signal_type.append('chest')
            elif re.search('C3-M2|C4-M1|F3-M2|F4-M1|O1-M2|O2-M1', sig, re.IGNORECASE):
                self.signal_type.append('eeg')
            elif re.search('EMG', sig, re.IGNORECASE):
                self.signal_type.append('emg')
            elif re.search('EOG', sig, re.IGNORECASE):
                self.signal_type.append('eog')
            elif re.search('Snore', sig, re.IGNORECASE):
                self.signal_type.append('snore')
            elif re.search('position', sig, re.IGNORECASE):
                self.signal_type.append('position')
            elif re.search('Flow|NEW AIR|AirFlow', sig, re.IGNORECASE):
                self.signal_type.append('flow')
            elif re.search('Numeric Aux', sig, re.IGNORECASE):
                self.signal_type.append('trigger')
            elif re.search('Pressure', sig, re.IGNORECASE):
                self.signal_type.append('nasal_pressure')
            else:
                self.signal_type.append('unk')
        self.signal_type = np.array(self.signal_type)
