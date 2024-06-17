chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({ hello: 'world' }, function() {
      console.log('Value is set to "world".');
    });
  });
  