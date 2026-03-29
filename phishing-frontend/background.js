// background.js
// Handles communication between content script and backend ML API

chrome.runtime.onMessage.addListener((message, sender) => {
  if (message.type !== "CHECK_URL" || !message.url) {
    return;
  }

  console.log("🔍 Checking URL:", message.url);

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      url: message.url
    })
  })
    .then(response => {
      if (!response.ok) {
        throw new Error("Backend response not OK");
      }
      return response.json();
    })
    .then(data => {
      console.log("🧠 Backend response:", data);

      if (data.prediction === "phishing") {
        const explanation = encodeURIComponent(
          data.explanation || "Suspicious website detected"
        );

        const confidence = encodeURIComponent(
          data.confidence !== undefined ? data.confidence : "N/A"
        );

        chrome.tabs.update(sender.tab.id, {
          url: chrome.runtime.getURL(
            `warning.html?explanation=${explanation}&confidence=${confidence}`
          )
        });
      }
    })
    .catch(error => {
      console.error("❌ Error contacting backend:", error);
    });
});
