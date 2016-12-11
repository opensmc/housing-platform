var ControlView = Backbone.View.extend({
  initialize: function(options) {
    this.applicantForm = options.applicantForm;
  },
  events: {
    'click .new-applicant': 'newApplicant'
  },
  newApplicant: function() {
    this.applicantForm.render();
  },
})

