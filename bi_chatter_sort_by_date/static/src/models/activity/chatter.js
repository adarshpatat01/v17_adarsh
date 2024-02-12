/** @odoo-module **/


import core from 'web.core';

registerPatch({
    name: 'Chatter',
    recordMethods: {
        onClickChatterSortByAscending(event) {
//            this.updateDateState(true)
            if(this.thread.Ascending) {
                this.thread.Ascending = false
            } else {
                this.thread.Ascending = true
            }
            this.refresh();
        },
//        onClickChatterSortByDescending(event) {
//            this.updateDateState(false)
//        },
//        updateDateState (order) {
//            this.thread.Ascending = order
//            this.refresh();
//        }
    },
});





