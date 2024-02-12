    /** @odoo-module */

import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { _t } from "@web/core/l10n/translation";
import { onMounted, useRef, useState } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { SuccessfulRemoveTagPopup } from "@bi_pos_advance_tag/app/successfullremovetagpopup";
import { SuccessfulTagPopup } from "@bi_pos_advance_tag/app/successtagpopup";

// IMPROVEMENT: This code is very similar to TextInputPopup.
//      Combining them would reduce the code.
export class AddProductTagsPopup extends AbstractAwaitablePopup {
    static template = "bi_pos_advance_tag.AddProductTagsPopup";
    static defaultProps = {
        confirmText: _t("Confirm"),
        cancelText: _t("Cancel"),
        title: "Add tag",
        body: "",
    };

    /**
     * @param {Object} props
     * @param {string} props.startingValue
     */
    setup() {
        super.setup();
        this.pos=usePos();
        this.inputRef = useRef("input");
        this.popup = useService("popup");
        this.state = useState({tagInput: ''});
        $('#remove').show();
        this.orm = useService("orm");
    }
    imageUrl(id){
        return `/web/image?model=product.product&field=image_512&id=${id}&unique=1`;
    }

    changeInput(event){
        var self = this;
        var tag = this.state.tagInput;
        var tags = self.env.services.pos.all_product_tag;
        var is_exist = $.each(tags, function(v) {
            return v.name == tag;
        });
        if(is_exist.length == 0 && tag != ""){
            $('#remove').hide();
            $('.confirm').text("Create and Add");
        }else{
            $('#remove').show();
            $('.confirm').text("Add");
        }
    }
    async remove(){
        var self = this;
        var tag = this.state.tagInput;
        var product_id = this.pos.get_order().get_product_data();
        var product=this.env.services.pos.db.get_product_by_id(product_id)
        if(!tag){
            alert("Please Select Tag.")
        }else{
            var tags = self.env.services.pos.all_product_tag;
            var is_exist = $.grep(tags, function(v) {
                    return v.name == tag;
                });
            if(is_exist.length != 0){
                let tg_id = is_exist[0].id;
                await this.orm.call(
                    'pos.product.tag',
                    'remove_tag_operation',
                    [ is_exist[0].name,product.id],
                    ).then(async function(result) {
                    if (result) {
                        if(self.env.services.pos.db.product_by_tag_id[tg_id]){
                            self.env.services.pos.db.product_by_tag_id[tg_id] = self.env.services.pos.db.product_by_tag_id[tg_id].filter(function(item) {
                                return item.id != product.id;
                            });
                        }else{
                            self.env.services.pos.db.product_by_tag_id[tg_id] = [product];
                        }
                        self.popup.add(SuccessfulRemoveTagPopup,{
                            result: is_exist[0].name,
                        });
                        self.props.close({ confirmed: true, payload: null });
                    }
                });
            }
        }
    }
    async confirm(){
        var tag = this.state.tagInput;
        var product_id = this.pos.get_order().get_product_data();
        var product=this.env.services.pos.db.get_product_by_id(product_id)
        if(!tag){
            alert("Please Create and Add Product Tag.")
        }else{
            var self = this;

            var tags = self.env.services.pos.all_product_tag;
            var is_exist = $.grep(tags, function(v) {
                    return v.name == tag;
                });
            if(is_exist.length != 0){
                let tg_id = is_exist[0].id;
                await this.orm.call('pos.product.tag',
                    'add_tag_operation',
                    [is_exist[0].name,product.id],
                    ).then(async function(result) {
                    if (result) {
                        if(self.env.services.pos.db.product_by_tag_id[tg_id]){
                            self.env.services.pos.db.product_by_tag_id[tg_id].push(product);
                        }else{
                            self.env.services.pos.db.product_by_tag_id[tg_id] = [product];
                        }
                        self.popup.add(SuccessfulTagPopup, {
                            result: is_exist[0].name,
                        });
                        self.props.close({ confirmed: false, payload: null });
                    }
                });
            }else{
                await this.orm.call( 'pos.product.tag',
                    'add_tag_operation',
                    [tag,product.id],
                    
                    ).then(async function(result) {
                    if (result) {
                        let vals = {
                            'id' : result[0],
                            'name' : result[1],
                        }
                        self.env.services.pos.all_product_tag.push(vals);
                        if(self.env.services.pos.db.product_by_tag_id[result[0]]){
                            self.env.services.pos.db.product_by_tag_id[result[0]].push(product);
                        }else{
                            self.env.services.pos.db.product_by_tag_id[result[0]] = [product];
                        }
                        self.popup.add(SuccessfulTagPopup, {
                            result: result[1],
                        })
                        self.props.close({ confirmed: false, payload: null });
                    }
                });
            }
        }
    }
    
    
}
