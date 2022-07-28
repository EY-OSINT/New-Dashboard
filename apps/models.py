from flask_login import UserMixin

from apps import db
from sqlalchemy.ext.declarative import declarative_base

class target(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column (db.String,unique=True)
    scan_key    = db.relationship('scan',backref='target', lazy=True, primaryjoin="target.id==scan.target_id")
    def __init__(self, name):
        self.name        = name
    def __repr__(self):
        return str(self.id) + ' - ' + str(self.name)


class scan(db.Model): 
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column (db.String)
    date            = db.Column (db.Date)
    target_id       = db.Column (db.Integer,db.ForeignKey('target.id'),nullable=False)
    """
    subdomain_key   = db.relationship('subdomain',backref='scan', lazy=True, primaryjoin="scan.id==subdomain.scan_id")
    url_key         = db.relationship('url',backref= 'scan',lazy=True, primaryjoin='scan.id==url.scan_id')
    domain_key      = db.relationship('domain',backref='',lazy=True,primaryjoin='scan.id==domain.scan_id')
    path_key        = db.relationship('path',backref= 'scan',lazy=True, primaryjoin='scan.id==path.scan_id')
    github_key      = db.relationship('github',backref= 'scan',lazy=True, primaryjoin='scan.id==github.scan_id')
"""
    def __init__(self, name, date,target_id):
        self.name           = name
        self.date           = date
        self.target_id     = target_id
    def __repr__(self):
        return str(self.id) + ' - ' + str(self.name)+ ' - ' + str(self.date)

class domain(db.Model): 
    dom_id  =   db.Column(db.Integer, primary_key=True)
    name    =   db.Column (db.String)
    scan_id =   db.Column (db.Integer,db.ForeignKey('scan.id'),nullable=False)
    def __init__(self, name,dom_id,scan_id):
        self.dom_id         = dom_id
        self.name           = name
        self.scan_id        = scan_id
    def __repr__(self):
        return str(self.id) + ' - ' + str(self.domain)        
