from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"

    name = fields.Char(required=True)
    color = fields.Integer("Color")
    
    
    # SQL Contraints
    _check_name = models.Constraint(
        'UNIQUE(name)',
        'The Tag Name has aleardy taken',
    )