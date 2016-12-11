var ControlView = Backbone.View.extend({
  initialize: function(options) {
    this.applicantForm = options.applicantForm;
  },
  events: {
    'click .new-applicant': 'showNewApplicant'
  },
  showNewApplicant: function() {
    this.applicantForm.render();
  },
})

