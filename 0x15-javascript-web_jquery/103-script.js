#!/usr/bin/node
$(document).ready(function() {
    // Function to fetch and display the translation
    function fetchTranslation() {
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
    }
  
    // Handle click event on the Translate button
    $('#btn_translate').click(function() {
      fetchTranslation();
    });
  
    // Handle Enter key press when the input field is focused
    $('#language_code').keypress(function(event) {
      if (event.which === 13) { // 13 is the Enter key
        fetchTranslation();
      }
    });
  });
