$(document).ready(function() {
  // Setting CSRF token from cookie.
  var csrftoken = Util.getCookie('csrftoken');
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        // Send the token to same-origin, relative URLs only.
        // Send the token only if the method warrants CSRF protection
        // Using the CSRFToken value acquired earlier
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
  });

  var applicantsCollection = new ApplicantsCollection();
  var applicantForm = new ApplicantCreationForm({
    el: $('.form-view'),
    collection: applicantsCollection,
  });
  var applicantDeleteForm = new ApplicantDeleteForm({
    el: $('.delete-view'),
    collection: applicantsCollection,
  })
  var controlView = new ControlView({
    el: $('.control-view'),
    collection: applicantsCollection,
    applicantForm: applicantForm
  });
  var applicantsList = new ApplicantListView({
    el: $('#applicant-list'),
    collection: applicantsCollection,
    applicantForm: applicantForm,
    applicantDeleteForm: applicantDeleteForm
  });
});