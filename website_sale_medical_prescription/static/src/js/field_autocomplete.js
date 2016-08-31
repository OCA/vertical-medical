/* Copyright 2016 LasLabs Inc.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */

odoo.define('website_field_autocomplete_prescription.field_autocomplete', function(require){
  "use strict";

  var snippet_animation = require('web_editor.snippets.animation');
  var $ = require('$');
  require('website_field_autocomplete_related.field_autocomplete');

  snippet_animation.registry.field_autocomplete = snippet_animation.registry.field_autocomplete.extend({

    autocompleteselect: function(event, ui) {
      var self = this;
      event.preventDefault();
      this._super(event, ui);
      _.each($('.o_website_form_date'),
             $.proxy(self.onchangeDate, self));
    },
    
    onchangeDate: function(target) {
        var $target = $(target);
        if ($target.val().indexOf('-') !== -1) {
            var date = new Date($target.val());
            date = [date.getMonth(), date.getDate(), date.getFullYear()];
            $target.val(date.join('/'));
        }
    },
    
  });

});
