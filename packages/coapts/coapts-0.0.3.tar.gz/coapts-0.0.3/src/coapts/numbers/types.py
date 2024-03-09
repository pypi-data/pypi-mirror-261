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
    valores_disponibles = [0, 1, 2, 3]

    # Variable CON
    nuevo_valor_CON = CON
    while nuevo_valor_CON == CON:
        nuevo_valor_CON = random.choice(valores_disponibles)
    CON = nuevo_valor_CON

    # Variable NON
    nuevo_valor_NON = NON
    while nuevo_valor_NON == NON or nuevo_valor_NON == CON:
        nuevo_valor_NON = random.choice(valores_disponibles)
    NON = nuevo_valor_NON

    # Variable ACK
    nuevo_valor_ACK = ACK
    while nuevo_valor_ACK == ACK or nuevo_valor_ACK == CON or nuevo_valor_ACK == NON:
        nuevo_valor_ACK = random.choice(valores_disponibles)
    ACK = nuevo_valor_ACK

    # Variable RST
    nuevo_valor_RST = RST
    while nuevo_valor_RST == RST or nuevo_valor_RST == CON or nuevo_valor_RST == NON or nuevo_valor_RST == ACK:
        nuevo_valor_RST = random.choice(valores_disponibles)
    RST = nuevo_valor_RST

    def __str__(self):
        return self.name

CON, NON, ACK, RST = Type.CON, Type.NON, Type.ACK, Type.RST

__all__ = ['Type', 'CON', 'NON', 'ACK', 'RST']
