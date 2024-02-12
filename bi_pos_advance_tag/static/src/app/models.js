/** @odoo-module */

import { Order, Orderline, Payment } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

// New orders are now associated with the current table, if any.
patch(Order.prototype, {
    setup(_defaultObj, options) {
        super.setup(...arguments);
        this.product_data = this.product_data || false;
    },
    //@override
    set_product_data(product_data){
        this.product_data = product_data;
    },
    get_product_data(){
        return this.product_data;
    },
    export_as_JSON() {          
        const json = super.export_as_JSON(...arguments);
        json.product_data = this.product_data;
        return json;
    },
    init_from_JSON(json){
        super.init_from_JSON(...arguments); 
        this.product_data = json.product_data;
    },
});