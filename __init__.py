# This file is part of the contract_invoice_line_merger module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import contract
from . import invoice


def register():
    Pool.register(
        contract.ContractConsumption,
        invoice.InvoiceLine,
        module='contract_invoice_line_merger', type_='model')
