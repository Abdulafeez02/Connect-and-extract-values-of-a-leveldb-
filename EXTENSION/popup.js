document.addEventListener('DOMContentLoaded', function() {
    chrome.storage.sync.get('hello', function(data) {
      document.getElementById('value').innerText = data.hello;
    });
  });

