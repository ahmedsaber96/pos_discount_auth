odoo.define('pos_discount_auth.DiscountAuthPopup', function (require) {
    "use strict";

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { _t } = require('web.core');
    const ajax  = require("web.ajax");

   const { useRef, useState } = owl;
    class DiscountAuthPopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();

            this.state = useState({
                authCode: '',
                errorMessage: "",
                inputHasError: false,

            });
            this.inputAuthCodeRef = useRef('input-auth-code-ref');
        }


        async confirm() {
            try {
                if(this.state.authCode.length !== 4){
                    throw new Error("Authorized code must be a 4 digits number.");
                }
            }catch (_error){
                this.state.inputHasError = true;
                this.state.errorMessage = this.env._t(_error.message);
                return;
            }

            //Make Http request to user
            const resultPromise = await ajax.rpc("/pos_discount_auth_code", {"cashier_auth_code": this.state.authCode})
            const result = await resultPromise;
            console.log("Auth Result: ", resultPromise, "Result", result)
            if(result.authenticated){
                this.state.inputHasError = false;
            }else{
                this.state.inputHasError = true;
                this.state.errorMessage = this.env._t("Auth Code Not correct!");
                return;
            }

            return super.confirm();
        }

        cancel(){
            console.log("Confirm work fine!")
            return super.cancel();
        }

        getPayload(){
            return {
                discountAuthPopupHasError: this.state.inputHasError,
            }
        }


    }

    DiscountAuthPopup.template =  "pos_discount_auth.DiscountAuthPopup";
    DiscountAuthPopup.defaultProps = {
        cancelText: _t('Cancel'),
        title: _t('Cash In/Out'),
    };
        Registries.Component.add(DiscountAuthPopup);
        return DiscountAuthPopup;
});