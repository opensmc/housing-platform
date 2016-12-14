var ApplicantModel = Backbone.Model.extend({
  urlRoot: '/ajax/applicant/',
  defalut: {
    id: null,
    name: '',
    county: '',
    address: '',
  }
})