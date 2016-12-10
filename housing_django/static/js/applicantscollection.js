var ApplicantsCollection = Backbone.Collection.extend({
  model: ApplicantModel,
  url: 'ajax/applicants',
  initialize: function() {
    this.fetch();
  }
});
