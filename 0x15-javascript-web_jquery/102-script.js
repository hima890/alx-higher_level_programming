#!/usr/bin/node
$(document).ready(function() {
    $('#btn_translate').click(function() {
      // Get the language code from the input field
      const langCode = $('#language_code').val();
      
      // API URL with the language code
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
      
      // Fetch data from the API
      $.get(apiUrl, function(data) {
        // Update the DIV#hello with the translated "Hello"
        $('#hello').text(data.hello);
      }).fail(function() {
        // Handle errors (if any)
        $('#hello').text('Error fetching translation');
      });
    });
  });
