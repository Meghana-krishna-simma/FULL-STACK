// Bootstrap 5 custom validation with jQuery enhancements
$(document).ready(function () {
  'use strict';
  // Select the form using jQuery
  var forms = $('.needs-validation');
  // Loop over them and prevent submission
  forms.on('submit', function (event) {
    var form = this;
    if (form.checkValidity() === false) {
      event.preventDefault();
      event.stopPropagation();
    }
    form.classList.add('was-validated');
  });
});
