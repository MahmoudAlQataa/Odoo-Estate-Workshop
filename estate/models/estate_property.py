from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError, UserError
from odoo.tools.float_utils import float_compare, float_is_zero
# from odoo.tools import 

class EstateProperty(models.Model): #Odoo Class (Using ORM) = SQL Tables
    _name = "estate.property" #SQL Table Name, not a field 
    _description = "Estate App Main Model" #SQL Table Description, not a field 
    _author = "M.Alqataa" #SQL Table Author, not a field
    _order = "id desc" #SQL Table Order, not a field
    _inherit = ["mail.thread", "mail.activity.mixin"] #Inheriting the estate.property model from the estate module and adding the mail features to it

    
    name = fields.Char(required=True) # Attributes (required, default, readonly, string, copy)
    description = fields.Text(default="Write your description here")
    date_available = fields.Date(string="Available Form", default=fields.Date.today() + relativedelta(months=6), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    has_garden = fields.Boolean()
    garden_area = fields.Integer()
    total_area = fields.Integer(compute="_compute_total_area")


    @api.depends("living_area", "garden_area") # self = is all the records in the 
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
            
    property_type_id = fields.Many2one("estate.property.type") #definnig a new fields that take info from another table
    property_tag_id = fields.Many2many("estate.property.tag")
    
    sales_person_id = fields.Many2one("res.users")
    user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)  
    partner_id = fields.Many2one("res.partner")
    
    offer_ids = fields.One2many("estate.property.offer", "property_id") #("tabel name" , "the key name")
    
    state = fields.Selection(
        selection=[
            ("new" , "New"),
            ("offer_received" , "Offer Recevied"),
            ("offer_accepted" , "Offer Accepted"),
            ("sold" , "Sold"),
            ("cancelled" , "Cancelled"),
            ],
        default="new", required=True, copy=False
        
    )
    
    def sell_property(self):
        for record in self:
            if record.state == "cancelled":
                raise UserError("This property was Cancelled you can't sell it")
            else:
                record.state = "sold"
                
    def cancel_property(self):
        for record in self:
            if record.state == "sold":
                raise UserError("This property was Sold you can't Cancel it")
            else:
                record.state = "cancelled"
                
    best_price = fields.Float(compute="_compute_best_price", string="Best Offer")

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price = 0.0
                
    
                
    # SQL Contraints
    _check_expected_price = models.Constraint(
        'CHECK(expected_price > 0)',
        'It can\'t be 0 or less',
    )

    _check_selling_price = models.Constraint(
        'CHECK(selling_price >= 0)',
        'It can\'t be 0 or less',
    )
    
    _check_name = models.Constraint(
        'UNIQUE(name)',
        'The Property Name has aleardy taken',
    )

    # selling_price close to 90% of the expected_price
    @api.constrains("expected_price", "selling_price")
    def _check_valid_selling_price(self):
        for record in self:
            if float_compare(record.selling_price, 0.9*record.expected_price, precision_digits=2) < 0 and not float_is_zero(record.selling_price, precision_digits=2):
                raise ValidationError("Selling price con't be lower than 90% of the expected price!")
                