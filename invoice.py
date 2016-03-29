# This file is part of the contract_invoice_line_merger module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['InvoiceLine']


class InvoiceLine:
    __metaclass__ = PoolMeta
    __name__ = 'account.invoice.line'

    @classmethod
    def _merge_lines(cls, grouped_lines):
        Consumption = Pool().get('contract.consumption')
        consumptions = [l.origin for l in grouped_lines
            if isinstance(l.origin, Consumption)]
        super(InvoiceLine, cls)._merge_lines(grouped_lines)
        Consumption.write(consumptions, {'invoice_line': grouped_lines[0]})
