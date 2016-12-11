var ApplicantListView = Backbone.View.extend({
  initialize: function(options) {
    this.listenTo(this.collection, 'sync', this.render);
    this.listenTo(this.collection, 'add', this.render);
    this.listenTo(this.collection, 'change', this.render);
    this.template = Handlebars.compile($('#applicant-template').html());
    this.applicantForm = options.applicantForm;
  },
  events: {
    'click .delete-applicant' : 'deleteApplicant',
    'click .update-applicant' : 'updateApplicant',
  },
  updateApplicant: function(e) {
    this.applicantForm.render($(e.target).attr('data-id'));
  },
  deleteApplicant: function(e) {

  },
  render: function() {
    var templateResults = this.template({
      applicants: this.collection.toJSON().reverse()
    })
    this.$el.html(templateResults);
  },
  template: null
});