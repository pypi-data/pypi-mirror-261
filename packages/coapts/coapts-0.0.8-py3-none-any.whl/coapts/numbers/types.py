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

    CON = 0 # Confirmable
    NON = 1 # Non-confirmable
    ACK = 2 # Acknowledgement
    RST = 3 # Reset

    def __str__(self):
        return self.name

# Definimos los posibles valores para cada variable
possible_values = {
    'CON': [1, 2, 3],
    'NON': [0, 2, 3],
    'ACK': [0, 1, 3],
    'RST': [1, 2, 3]
}

# Asignamos valores aleatorios respetando las restricciones
CON = random.choice(possible_values['CON'])
NON = random.choice(possible_values['NON'])
ACK = random.choice(possible_values['ACK'])
RST = random.choice(possible_values['RST'])

__all__ = ['Type', 'CON', 'NON', 'ACK', 'RST']
