var ControlView = Backbone.View.extend({
  initialize: function(options) {
    this.applicantForm = options.applicantForm;
  },
  events: {
    'click .show-form': 'showForm'
  },
  showForm: function() {
    this.applicantForm.render();
  },
})

