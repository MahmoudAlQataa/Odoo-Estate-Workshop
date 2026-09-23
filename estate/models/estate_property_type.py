from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type" # sql table name
    _description = "Estate Property Type Model" # sql table description
    
    name = fields.Char(required=True)
    
    # SQL Contraints
    _check_name = models.Constraint(
        'UNIQUE(name)',
        'The Tyoe Name has aleardy taken',
    )
    
    property_ids = fields.One2many("estate.property", "property_type_id")
    