from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CustomerProfile(models.Model):
    _name = 'profiles.customer'
    _description = 'Customer Profile'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'display_name'

    is_company = fields.Boolean(
        string='Is Company',
        default=False,
        tracking=True
    )
    
    # Common fields
    name = fields.Char(
        string='Name',
        required=True,
        tracking=True,
        index=True
    )
    display_name = fields.Char(
        string='Display Name',
        compute='_compute_display_name',
        store=True
    )
    active = fields.Boolean(
        default=True,
        tracking=True
    )
    
    # Individual fields
    last_name = fields.Char(
        string='Last Name',
        tracking=True
    )
    id_number = fields.Char(
        string='ID Number',
        tracking=True,
        copy=False
    )
    nationality = fields.Char(
        string='Nationality',
        tracking=True
    )
    
    # Company fields
    address = fields.Text(
        string='Address',
        tracking=True
    )
    landline = fields.Char(
        string='Landline Number',
        tracking=True
    )
    tax_id = fields.Char(
        string='Tax ID',
        tracking=True,
        copy=False
    )
    owner_name = fields.Char(
        string='Owner Name',
        tracking=True
    )

    @api.depends('name', 'last_name', 'is_company')
    def _compute_display_name(self):
        for record in self:
            if record.is_company:
                record.display_name = record.name
            else:
                record.display_name = f"{record.name} {record.last_name or ''}"

    @api.onchange('is_company')
    def _onchange_is_company(self):
        if self.is_company:
            self.last_name = False
            self.id_number = False
            self.nationality = False
        else:
            self.address = False
            self.landline = False
            self.tax_id = False
            self.owner_name = False

    @api.constrains('id_number', 'tax_id')
    def _check_identification(self):
        for record in self:
            if record.is_company and not record.tax_id:
                raise ValidationError('Tax ID is required for companies')
            if not record.is_company and not record.id_number:
                raise ValidationError('ID Number is required for individuals')