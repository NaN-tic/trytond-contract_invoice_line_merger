# This file is part of the contract_invoice_line_merger module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval


__all__ = ['ContractConsumption']
__metaclass__ = PoolMeta


class ContractConsumption:
    __name__ = 'contract.consumption'
    invoice_line = fields.Many2One('account.invoice.line',
        'Merged Invoice Line', readonly=True,
        states={
            'invisible': ~Eval('invoice_line'),
        })

    @classmethod
    def _invoice(cls, consumptions):
        consumptions = [c for c in consumptions if not c.invoice_line]
        return super(ContractConsumption, cls)._invoice(consumptions)
