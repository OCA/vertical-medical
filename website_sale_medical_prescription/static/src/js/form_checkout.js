/* Copyright 2016 LasLabs Inc.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */

odoo.define('website_sale_medical_prescription.form_checkout', function(require){
  "use strict";

  var snippet_animation = require('web_editor.snippets.animation');
  var $ = require('$');
  
  snippet_animation.registry.medical_prescription_checkout = snippet_animation.Class.extend({

    selector: '.js_medical_prescription_checkout',

    start: function() {
      var self = this;
      this.$target.find('.js_medical_prescription_new')
        .addClass('hidden')
        .prop('disabled', true);
      this.$target.find('.js_medical_prescription_pharmacy')
        .addClass('hidden')
        .prop('disabled', true);
      this.$target.find('.js_medical_prescription')
        .change(function(event) {
          self.onchangePrescription(event, self);
        });
      this.$target.find('.js_medical_prescription_acquisition')
        .change(function(event) {
          self.onchangeAcquisition(event, self);
        });
      this.$target.find('.js_medical_prescription_gender')
        .change(self.onchangeGender);
    },
    
    onchangeGender: function(event) {
      var $target = $(event.target);
      var $isPreg = $target.parents('.js_medical_prescription_patient')
        .find('.js_medical_prescription_is_pregnant');
      if ($target.val() == 'f') {
        $isPreg.removeClass('hidden').prop('disabled', false);
      } else {
        $isPreg.addClass('hidden').prop('disabled', true).prop('checked', false);
      }
    },
    
    onchangePrescription: function(event, self) {
      var $rxNew = self.$target.find('.js_medical_prescription_new');
      if ($(event.target).val() == '0') {
        $rxNew.removeClass('hidden').prop('disabled', false);
      } else {
        $rxNew.addClass('hidden').prop('disabled', true);
      }
    },
    
    onchangeAcquisition: function(event, self) {
      var $pharmacySel = self.$target.find('.js_medical_prescription_pharmacy');
      if ($(event.target).val() == 'transfer') {
        $pharmacySel.removeClass('hidden').prop('disabled', false);
      } else {
        $pharmacySel.addClass('hidden').prop('disabled', true);
      }
    },
    
  });
  
  return {medical_prescription_checkout: snippet_animation.registry.medical_prescription_checkout};

});
