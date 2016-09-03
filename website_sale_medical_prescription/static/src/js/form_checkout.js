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
      this.$target.find('.js_medical_prescription_new')
        .addClass('hidden')
        .find(':input')
        .prop('disabled', true);
      this.$target.find('.js_medical_prescription_pharmacy')
        .addClass('hidden')
        .find(':input')
        .prop('disabled', true);
      this.$target.find('.js_medical_prescription')
        .change($.proxy(this.onchangePrescription, this));
      this.$target.find('.js_medical_prescription_acquisition')
        .change($.proxy(this.onchangeAcquisition, this));
      this.$target.find('.js_medical_prescription_gender')
        .change($.proxy(this.onchangeGender, this));
    },
    
    onchangeGender: function(event) {
      var $target = $(event.currentTarget);
      var $isPreg = $target.parents('.js_medical_prescription_patient')
        .find('.js_medical_prescription_is_pregnant');
      if ($target.val() == 'f') {
        $isPreg.removeClass('hidden').prop('disabled', false);
      } else {
        $isPreg.addClass('hidden').prop('disabled', true).prop('checked', false);
      }
    },
    
    onchangePrescription: function(event) {
      var $rxNew = this.$target.find('.js_medical_prescription_new');
      if ($(event.currentTarget).val() == '0') {
        $rxNew.removeClass('hidden').find(':input').prop('disabled', false);
      } else {
        $rxNew.addClass('hidden').find(':input').prop('disabled', true);
      }
    },
    
    onchangeAcquisition: function(event) {
      var $pharmacySel = this.$target.find('.js_medical_prescription_pharmacy');
      if ($(event.currentTarget).val() == 'transfer') {
        $pharmacySel.removeClass('hidden').find(':input').prop('disabled', false);
      } else {
        $pharmacySel.addClass('hidden').find(':input').prop('disabled', true);
      }
    },
    
  });
  
  return {medical_prescription_checkout: snippet_animation.registry.medical_prescription_checkout};

});
