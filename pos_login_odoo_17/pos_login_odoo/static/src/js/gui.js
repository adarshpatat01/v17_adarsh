/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { session } from "@web/session";
import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";

import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    async closePos() {
        var session_data = session.uid
            this.orm.call(
                    'res.users',
                    'get_config_id',
                    [1,session_data]
                    ).then(function(output) {
                     if(output === true){

                        self.posmodel.env.services.pos.push_orders().then(function(){
                            var url = "/web/session/logout";
                            window.location = session.debug ? $.param.querystring(url, {debug: session.debug}) : url;
                        });
                    }else{

                        self.posmodel.env.services.pos.push_orders().then(function(){
                        var url = "/web#action=point_of_sale.action_client_pos_menu";
                        window.location = session.debug ? $.param.querystring(url, {debug: session.debug}) : url;
                        });
                    }
            });

        }


});
