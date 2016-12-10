var ApplicantCreationForm = Backbone.View.extend({ 
  initialize: function() {
    this.template = Handlebars.compile($("#applicant-form-tmp").html());
  },
  events: {
    'click .btn-primary': 'submitForm'
  },
  submitForm: function(e) {
    e.preventDefault();
    if(this.applicantId) {
      console.log("updatd")
      var model = this.collection.get(this.applicantId);
      model.set({
        name: this.$el.find('.name').val(),
        county: this.$el.find('.county').val(),
        address: this.$el.find('.address').val(),
      });
      model.save();
    } else {
      this.collection.create({
        name: this.$el.find('.name').val(),
        county: this.$el.find('.county').val(),
        address: this.$el.find('.address').val(),
      });
    }
    $('#data-modal').modal('hide');
  },
  render: function(applicantId) {
    this.applicantId = applicantId;
    var applicant;
    if (applicantId) { 
      applicant = this.collection.get(applicantId).toJSON()
    }
    var templateResults = this.template({
      applicant: applicant
    })    
    
    this.$el.html(templateResults);
  },
})