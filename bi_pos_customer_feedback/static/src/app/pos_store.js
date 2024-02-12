/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {

    async _processData(loadedData) {
        await super._processData(loadedData);
        let self = this;
    },
    async _save_to_server(orders, options) {
        if (!orders || !orders.length) {
            return Promise.resolve([]);
        }
        this.set_synch('connecting', orders.length);
        options = options || {};

        var self = this;
        var timeout = typeof options.timeout === 'number' ? options.timeout : 30000 * orders.length;

        // Keep the order ids that are about to be sent to the
        // backend. In between create_from_ui and the success callback
        // new orders may have been added to it.
        // var order_ids_to_sync = $.pluck(orders, 'id');

        // we try to send the order. shadow prevents a spinner if it takes too long. (unless we are sending an invoice,
        // then we want to notify the user that we are waiting on something )
        var order_ids_to_sync = orders.map((o) => o.id);
        var args = [orders.map(function (order){
                order.to_invoice = options.to_invoice || false;
                return order;
            })];
        args.push(options.draft || false);
        return this.orm.call(
                'pos.order',
                'create_from_ui',
                args,
            )
            .then(async function (server_ids) {
                order_ids_to_sync.forEach(function (order_id){
                    self.db.remove_order(order_id);
                });
                var current_order = self.env.services.pos.get_order();
                var current_client = current_order.get_partner()
                if (current_client){
                    if (current_client.feedback_email){
                        await self.orm.call(
                            'res.partner',
                            'send_customer_feedback_mail',
                            [[],current_client,current_order.name],
                        ).then(function () {
                            return true
                        });
                    }
                }
                self.failed = false;
                self.set_synch('connected');
                return server_ids;
            }).catch(function (error){
                console.warn('Failed to send orders:', orders);
                if(error.code === 200 ){    // Business Logic Error, not a connection problem
                    // Hide error if already shown before ...
                    if ((!self.failed || options.show_error) && !options.to_invoice) {
                        self.failed = error;
                        self.set_synch('error');
                        throw error;
                    }
                }
                self.set_synch('disconnected');
                throw error;
            });
    },
    
});