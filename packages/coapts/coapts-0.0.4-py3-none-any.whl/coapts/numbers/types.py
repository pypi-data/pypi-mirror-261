# SPDX-FileCopyrightText: Christian Amsüss and the aiocoap contributors
#
# SPDX-License-Identifier: MIT

"""List of known values for the CoAP "Type" field.

As this field is only 2 bits, its valid values are comprehensively enumerated
in the `Type` object.
"""

from enum import IntEnum
import random

class Type(IntEnum):

    #codes = [0, 1, 2, 3]

    #CON = 3 # Confirmable
    #NON = 0 # Non-confirmable
    #ACK = 1 # Acknowledgement
    #RST = 2 # Reset

    CON = 0
    NON = 1
    ACK = 2
    RST = 3

    # Asignar valores aleatorios a cada variable
    CON = random.choice([1, 2, 3])
    NON = random.choice([0, 2, 3])
    ACK = random.choice([0, 1, 3])
    RST = random.choice([0, 1, 2])

    # Verificar y corregir cualquier duplicado
    while len(set([CON, NON, ACK, RST])) < 4:
        CON = random.choice([1, 2, 3])
        NON = random.choice([0, 2, 3])
        ACK = random.choice([0, 1, 3])
        RST = random.choice([0, 1, 2])

    def __str__(self):
        return self.name

CON, NON, ACK, RST = Type.CON, Type.NON, Type.ACK, Type.RST

__all__ = ['Type', 'CON', 'NON', 'ACK', 'RST']
