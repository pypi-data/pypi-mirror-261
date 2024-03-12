# -*- coding: utf-8 -*-
# This file is part of the cashbook-planner from m-ds for Tryton.
# The COPYRIGHT file at the top level of this repository contains the
# full copyright notices and license terms.

from trytond.pool import Pool
from .ir import Rule
from .planner import ScheduledBooking, ScheduledBookingCashbookRel
from .cashbook import Cashbook, CashbookLine
from .cron import Cron
from .nextrun import NextRun


def register():
    Pool.register(
        Rule,
        ScheduledBooking,
        NextRun,
        Cashbook,
        CashbookLine,
        Cron,
        ScheduledBookingCashbookRel,
        module='cashbook_planner', type_='model')
