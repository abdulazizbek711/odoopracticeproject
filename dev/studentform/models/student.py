from odoo import api, fields, models

class StudentForm(models.Model):
    _name = 'university.student'
    _description = 'Admission for 2024/2025'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    passportnumber = fields.Char(string='Passport Number', required = True)
    nation = fields.Char(string='Nation', required=True)
    facultyname = fields.Char(string='Faculty Name', required=True)
