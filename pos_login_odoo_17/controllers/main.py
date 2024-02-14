# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import http, fields, _
import logging
from odoo.http import request
# from openerp.addons.web.controllers.main import Home
from odoo.http import Response
from odoo.exceptions import AccessError
import ctypes
import easygui
from odoo.addons.website.controllers.main import Website

_logger = logging.getLogger(__name__)


class PosWebsiteLogin(Website):

    @http.route(website=True, auth="public")
    def web_login(self, redirect=None, *args, **kw):
        response = super(PosWebsiteLogin, self).web_login(redirect=redirect, *args, **kw)
        values = request.params.copy()
        session_id = request.env['pos.session'].sudo().search([('state', '=', 'opened'), ('user_id', '=', request.uid)])
        if not redirect and request.params['login_success']:
            if request.env['res.users'].browse(request.uid).has_group('base.group_user'):
                if request.env['res.users'].browse(request.uid).pos_config:
                    if session_id:
                        config_id = request.env['res.users'].browse(request.uid).pos_config
                        config_id.open_existing_session_cb()
                        redirect = '/pos/web'
                    else:
                        config_id = request.env['res.users'].browse(request.uid).pos_config
                        current_session_id = request.env['pos.session'].sudo().search(
                            [('state', '=', 'opened'), ('config_id', '=', config_id.id)])
                        if current_session_id:
                            easygui.msgbox("Another session is already opened for this point of sale!",
                                           title="AccessError")
                            redirect = '/web/session/logout'
                        else:
                            config_id.open_ui()
                            redirect = '/pos/web'
                else:
                    redirect = '/web?'
            else:
                redirect = '/'
            return request.redirect(redirect)
        return response

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
