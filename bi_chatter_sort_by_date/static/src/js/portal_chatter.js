/** @odoo-module **/

import PortalChatter from "@portal/js/portal_chatter";

PortalChatter.include({
    events: Object.assign({}, PortalChatter.prototype.events, {
         'click button.o_Chatter_sort_button': '_onSortMessage',

    }),
    _onSortMessage(messages) {
            this.Ascending = this.Ascending ? false : true
            this._reloadChatterContent();
        },

        preprocessMessages(messages) {
            var res = this._super.apply(this, arguments);
            return this.Ascending ? res.reverse() : res
        },

    });
