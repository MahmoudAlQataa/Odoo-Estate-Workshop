from odoo import models,fields
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"
    
    price = fields.Float()
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True, ondelete="cascade")
    
    status = fields.Selection(selection=[ ('accepted', 'Accepted'),('refused', 'Refused') ])
    
    def accept_offer(self):
        for record in self:
            if record.property_id.state == 'offer_accepted':
                raise UserError("This Property already had an offer accepted")
            record.status = 'accepted'
            record.property_id.write({
                "partner_id" : record.partner_id,
                "selling_price" : record.price,
                "state" : "offer_accepted"
            })
            
    def refuse_offer(self):
        for record in self:
            if record.status == "accepted":
                raise UserError("Accepted offer can't be refused")
            else:
                record.status = 'refused'
                
                
