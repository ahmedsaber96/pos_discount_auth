odoo.define('pos_discount_auth.CustomNumpadWidget', function (require) {
    "use strict";

    //inherit from Numpad class
    const NumpadWidget = require("point_of_sale.NumpadWidget")
    const Registries = require('point_of_sale.Registries');
    const CustomNumpadWidget = (NumpadWidget)=>{
        return class extends NumpadWidget{

            async changeMode(mode) {
                if (!this.hasPriceControlRights && mode === 'price') {
                    return;
                }
                if (!this.hasManualDiscount && mode === 'discount') {
                    return;
                }

                if(mode !== "discount"){
                    this.trigger('set-numpad-mode', {
                        mode
                    });
                }else{
                    const { confirmed, payload } = await this.showPopup('DiscountAuthPopup');
                    if(confirmed){
                        if(!payload.discountAuthPopupHasError){
                            this.trigger('set-numpad-mode', {
                                mode
                            });
                        }
                    }
                }


            }
        }
    }

    Registries.Component.extend(NumpadWidget, CustomNumpadWidget);
});