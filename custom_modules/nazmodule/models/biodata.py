from odoo import models, fields

class Biodata(models.Model):
    _name = 'nazmodule.biodata'
    _description = 'Biodata'

    name = fields.Char(string='Nama')
    fullname = fields.Char(string='Nama Lengkap')
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    umur = fields.Integer(string='Umur')
    anak_keberapa = fields.Integer(string='Anak ke Berapa')
    jenis_kelamin = fields.Selection([
        ('laki-laki', 'Laki-Laki'),
        ('perempuan', 'Perempuan'),
    ], string='Jenis Kelamin')
    foto = fields.Binary(string='Foto')

    pendidikan_sd = fields.Boolean(string='SD')
    pendidikan_smp = fields.Boolean(string='SMP')
    pendidikan_sltp = fields.Boolean(string='SLTP')
    pendidikan_sma = fields.Boolean(string='SMA')
    pendidikan_smk = fields.Boolean(string='SMK')
    pendidikan_smu = fields.Boolean(string='SMU')
    pendidikan_slta = fields.Boolean(string='SLTA')
    pendidikan_kuliah = fields.Boolean(string='KULIAH')
