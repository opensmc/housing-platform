var ApplicantModel = Backbone.Model.extend({
  url: '/ajax/applicant/',
  defalut: {
    id: null,
    name: '',
    county: '',
    address: '',
  }
})