# -*- coding: utf-8 -*-
from odoo import http

class Grafana(http.Controller):
    @http.route('/grafana/grafana/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/grafana/grafana/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('grafana.listing', {
            'root': '/grafana/grafana',
            'objects': http.request.env['grafana.grafana'].search([]),
        })

    @http.route('/grafana/grafana/objects/<model("grafana.grafana"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('grafana.object', {
            'object': obj
        })
