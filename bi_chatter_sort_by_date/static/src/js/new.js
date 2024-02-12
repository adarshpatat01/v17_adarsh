/** @odoo-module **/

import { Chatter } from "@mail/core/web/chatter";
import { patch } from "@web/core/utils/patch";

patch(Chatter.prototype, {
     setup() {
        super.setup();
    },
    async onClickChatterSortByAscending(event) {
            if(this.props.Ascending) {
                this.props.Ascending = false
                this.state.thread.Ascending = false
                this.render(true);

            } else {
                this.props.Ascending = true
                this.state.thread.Ascending = true
                this.render(true);
            }
   },
});