// content.js
// Runs on every webpage and sends the current URL for phishing check

(function () {
  try {
    const currentUrl = window.location.href;

    // Avoid infinite loop on warning page
    if (currentUrl.startsWith("chrome-extension://")) {
      return;
    }

    chrome.runtime.sendMessage({
      type: "CHECK_URL",
      url: currentUrl
    });

  } catch (error) {
    console.error("❌ Content script error:", error);
  }
})();
