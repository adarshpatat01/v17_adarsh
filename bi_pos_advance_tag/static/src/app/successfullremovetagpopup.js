    /** @odoo-module */

import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { _t } from "@web/core/l10n/translation";
import { onMounted, useRef, useState } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";


// IMPROVEMENT: This code is very similar to TextInputPopup.
//      Combining them would reduce the code.
export class SuccessfulRemoveTagPopup extends AbstractAwaitablePopup {
    static template = "bi_pos_advance_tag.SuccessfulRemoveTagPopup";
    static defaultProps = {
        confirmText: _t("Confirm"),
        cancelText: _t("Ok"),
        title: "Pos Multi UOM",
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
    clickCancel() {
        console.log("SuccessfulRemoveTagPopup----------")
        this.pos.showScreen('ProductScreen');
    
    }
    
    
}
