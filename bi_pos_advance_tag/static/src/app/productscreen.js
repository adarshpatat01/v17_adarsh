/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { Order, Orderline, Payment } from "@point_of_sale/app/store/models";
import { _t } from "@web/core/l10n/translation";
import { Component, onMounted, useExternalListener, useState } from "@odoo/owl";
import { AddProductTagsPopup } from "@bi_pos_advance_tag/app/addproducttagpopup";



patch(ProductScreen.prototype, {
    /**
     * For accessibility, pressing <space> should be like clicking the product.
     * <enter> is not considered because it conflicts with the barcode.
     *
     * @param {KeyPressEvent} event
     */
   
   setup() {
        super.setup();
        var self = this;
        $(".product-list").dblclick(function(event){
            let selectedOrder = self.pos.get_order();
            let selectedLine = selectedOrder.get_selected_orderline();
            selectedOrder.removeOrderline(selectedLine);
            var product_id = self.pos.get_order().get_product_data();
            var product=self.env.services.pos.db.get_product_by_id(product_id)
            if(product){
                self.popup.add(AddProductTagsPopup, {product:product});
            }else{
                return;
            }
        });
        onMounted(() => this._mounted());
    },
    _mounted() {
        var self = this;
       
        // self.env.posbus.trigger('start-cash-control');
        $(".product-list").dblclick(function(event){
            let selectedOrder = self.pos.get_order();
            let selectedLine = selectedOrder.get_selected_orderline();
            selectedOrder.removeOrderline(selectedLine);
            var product_id = self.pos.get_order().get_product_data();
            var product=self.env.services.pos.db.get_product_by_id(product_id)
            if(product){
                self.popup.add(AddProductTagsPopup, {product:product});
            }else{
                return;
            }
        });
    },
});