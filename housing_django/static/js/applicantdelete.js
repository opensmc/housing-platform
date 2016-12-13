var ApplicantDeleteForm = Backbone.View.extend({ 
  initialize: function() {
    this.template = Handlebars.compile($('#applicant-delete-tmp').html());
  },
  events: {
    'click .delete-btn': 'submitForm'
  },
  submitForm: function(e) {
    e.preventDefault();
    if(this.applicantId) {
      var model = this.collection.get(this.applicantId);
      model.destroy({
        success: function() {
          this.$el.find('.delete-modal').modal('hide');
        }.bind(this)
      });
    }
  },
  render: function(applicantId) {
    this.applicantId = applicantId;
    var applicant;
    if (applicantId) { 
      applicant = this.collection.get(applicantId).toJSON();
    }
    var templateResults = this.template({
      applicant: applicant
    })    
    
    this.$el.html(templateResults);
  },
})