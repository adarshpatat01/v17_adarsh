/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {

    async _processData(loadedData) {
        await super._processData(loadedData);
        this.db.product_by_tag_id = {};
        this.db.product_list = [];
        this._loadPOSProductTag(loadedData['pos.product.tag']);
        this.selectedTagId=null;
        this.add_product(loadedData["product.product"]);
    },
    add_product(products) {
        var self = this;
        for(var i = 0, len = products.length; i < len; i++){
            var product = products[i];
            product.tag_ids.forEach(function(tgs) {
                if(self.db.product_by_tag_id[tgs]){
                    self.db.product_by_tag_id[tgs].push(product);
                }else{
                    self.db.product_by_tag_id[tgs] = [product];
                }
            });
           
        }
           
    },

    _loadPOSProductTag(product_tags){
        var self=this;
        self.all_product_tag = product_tags;
        self.product_tag_by_id = {};
        product_tags.forEach(function(tgs) {
            self.product_tag_by_id[tgs.id] = tgs;
        });
    },
    async addProductToCurrentOrder(product, options = {}) {

        if (Number.isInteger(product)) {
            product = this.db.get_product_by_id(product);
        }
        this.get_order() || this.add_new_order();
        product = this.db.get_product_by_id(product.id)
        this.env.services.pos.get_order().set_product_data(product.id);
        options = { ...options, ...(await product.getAddProductOptions()) };


        if (!Object.keys(options).length) {
            return;
        }

        // Add the product after having the extra information.
        await this.addProductFromUi(product, options);
        this.numberBuffer.reset();
    }
    
});