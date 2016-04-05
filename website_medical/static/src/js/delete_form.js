/* © 2016-TODAY LasLabs Inc.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */

odoo.define('website_medical.delete_form', function(require){
  "use strict";
  
  var base = require('web_editor.base');
  var core = require('web.core');
  
  base.ready().then(function(){
	$(document.body).find('.medical-form-deactivate').on('submit', function(e){
		var $target = $(e.target);
		$.ajax({
			url: $target.attr('action') + $target.attr('data-model_name'),
			method: 'DELETE',
			data: $target.serializeArray(),
			success: function(data, status, res){
			  data = JSON.parse(data);
			  if (data['error_fields']) {
				// core.bus.trigger('web_client.warning', data['error_fields']);
			  }else{
				var formId = data.model_name + '.deactivate.' + data.rec_id;
				var $formEl = $('form[id="' + formId + '"]');
				var $tableEl = $formEl.closest('table');
				var name = $formEl.attr('data-human_name');
				$formEl.closest('tr').remove();
				if ($tableEl.find('tr').length == 1) {
                  $tableEl.replaceWith(
					'<p>There are currently no ' + name + 's associated with your account.</p>'
				  );
                }
				// core.bus.trigger('web_client.notification', 'Successfully Deleted');
			  }
			},
			error: function(res, status, error){
			  console.log(res);
			},
			complete: function(res, status){
				
			},
		});
		e.preventDefault();
	});
  });
  
});
