# This file is part of the contract_invoice_line_merger module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool

from .contract import *
from .invoice import *


def register():
    Pool.register(
        InvoiceLine,
        ContractConsumption,
        module='contract_invoice_line_merger', type_='model')
