from odoo import models, fields, api

class EstateProperty(models.Model):
    res = super().action_sold()
    
    def action_sold(self):
        
        for record in self:
            self.env["account.move"].create({
                "partner_id": record.partner_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [
                    fields.Command.create({
                        "name": "Property Price",
                        "quantity": 1,
                        "price_unit": record.selling_price,
                    }),
                    fields.Command.create({
                        "name": "6% Commission",
                        "quantity": 1,
                        "price_unit": record.selling_price * 0.06,
                    }),
                    fields.Command.create({
                        "name": "Admin Fees",
                        "quantity": 1,
                        "price_unit": 100,
                    }),
                ],
            })
            
        return res