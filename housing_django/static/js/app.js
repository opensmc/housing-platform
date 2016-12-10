$(document).ready(function() {
  // Setting CSRF token from cookie.
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
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
  var controlView = new ControlView({
    el: $('.control-view'),
    collection: applicantsCollection,
    applicantForm: applicantForm
  });
  var applicantssList = new ApplicantListView({
    el: $('#applicant-list'),
    collection: applicantsCollection,
    applicantForm: applicantForm
  });
});