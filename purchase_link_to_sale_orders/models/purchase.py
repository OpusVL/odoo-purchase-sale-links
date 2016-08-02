# -*- coding: utf-8 -*-

##############################################################################
#
# Link from Purchase Order to the Sale Orders that procured it
# Copyright (C) 2016 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    procuring_sale_order_ids = fields.One2many(
       string="Procuring Sale Orders",
       comodel_name='sale.order',
       compute="_compute_procuring_sale_order_ids",
    )
    
    @api.depends('order_line.procurement_ids.sale_line_id.order_id')
    @api.one
    def _compute_procuring_sale_order_ids(self):
        self.procuring_sale_order_ids = self.order_line.mapped('procurement_ids.sale_line_id.order_id')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
