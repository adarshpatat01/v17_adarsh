/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ProductsWidget } from "@point_of_sale/app/screens/product_screen/product_list/product_list";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";
import { Component, onMounted, useState, useEffect, useRef } from "@odoo/owl";

patch(ProductsWidget.prototype, {
    setup() {
        super.setup();
        this.pos=usePos();
        this.popup = useService("popup");
        this.orm = useService("orm");
        this.newState = useState({ searchTag: [] });
        onMounted(() => this._mounted());
        this.state1 = this.tag_data()
        this.dataState = useState({selectedHighlightTag:'' });
    },
    
     _mounted(){
        $(".tag-clear-home-button").hide();
        $(".tag-home-button").show();
    },
    get selectedTagId() {
        return this.env.services.pos.selectedTagId;
    },
    get searchTag() {
        return this.newState.searchTag;
    },
    _switchCategory(event) {
        this.newState.searchTag = [];
        this.env.services.pos.selectedTagId=[];
        $(".tag-clear-home-button").hide();
        $(".tag-home-button").show();
        $('.breadcrumb').removeClass('tag-highlight');
        super._switchCategory(event);
    },
    getImageUrl(product) {
        return (
            (product.image_128 &&
                `/web/image?model=product.product&field=image_128&id=${product.id}&unique=${product.write_date}`) ||
            ""
        );
    },
    getFormattedUnitPrice(product) {
        const formattedUnitPrice = this.env.utils.formatCurrency(product.lst_price);
        if (product.to_weight) {
            return `${formattedUnitPrice}`;
        } else {
            return formattedUnitPrice;
        }
    },
    
    get productsToDisplay() {
        var self = this;
        let products = [];
        if (this.newState.searchTag.length > 0) {
            $(".tag-clear-home-button").show();
            $(".tag-home-button").hide();
            this.newState.searchTag.forEach(function(search){
                let prod = self.env.services.pos.db.product_by_tag_id[search['id']]
                if(prod != undefined && prod.length>0 ){
                    for(var pro in prod){
                        if(products.length == 0){
                            products.push(prod[pro])
                        }
                        else{
                            if(!products.includes(prod[pro]))
                            {
                                products.push(prod[pro]);
                            }
                        }
                    }
                }
            })
            return products;
        } else {
            let list = [];
            if (this.searchWord !== '') {
                list = this.env.services.pos.db.search_product_in_category(
                    this.selectedCategoryId,
                    this.searchWord
                );
            } else {
                list = this.env.services.pos.db.get_product_by_category(this.selectedCategoryId);
            }
            return list.sort(function (a, b) { return a.display_name.localeCompare(b.display_name) });
        }
    },
    _tryAddProductTag(event) {
        this.env.services.pos.selectedTagId=event;
        this.newState.searchTag.push(event);
    },
    _clearSearchTag(event) {
        this.env.services.pos.selectedTagId=event;
        this.newState.searchTag.pop(event);
    },
    _clearTags(){
        this.newState.searchTag = [];
        this.env.services.pos.selectedTagId=[];
        $('.breadcrumb').removeClass('tag-highlight');
        $(".tag-clear-home-button").hide();
        $(".tag-home-button").show();
    },
    tag_data(){
        let tags=this.env.services.pos.all_product_tag;
        let tag_data=[];
        $.each(tags, function( i, tag ){
            if(tag){
                tag_data.push(tag)
            }
        });
        return tag_data;
    },
    _onSelectedTag(event){
        var self = this;
        this.dataState.selectedHighlightTag = event['id'];
        var id= this.dataState.selectedHighlightTag;
        const $xyz = $('.xyz');
        $.each($xyz,function(issue1,issue){
            if(id == issue.dataset.id){
                if(!issue.classList.contains('tag-highlight')){
                    self._tryAddProductTag(event);
                    issue.classList.add('tag-highlight');
                }
                else{
                    issue.classList.remove('tag-highlight');
                    self._clearSearchTag(event);
                }
            }
        });
    },
});