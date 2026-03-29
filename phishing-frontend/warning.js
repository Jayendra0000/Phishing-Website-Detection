document.addEventListener("DOMContentLoaded", () => {
  const params = new URLSearchParams(window.location.search);
  const explanation = params.get("explanation");
  const confidence = params.get("confidence");
  
  // Update explanation
  const explanationElement = document.getElementById("ai-explanation");
  if (explanation && explanationElement) {
    explanationElement.textContent = decodeURIComponent(explanation);
  } else {
    explanationElement.textContent = "The AI detected suspicious patterns in the URL structure and website characteristics that match known phishing techniques.";
  }
  
  // Update confidence
  const confidenceText = document.getElementById("confidence-text");
  const confidenceFill = document.getElementById("confidence-fill");
  
  let confidenceLevel = "Medium";
  let confidenceWidth = "75%";
  let confidenceColor = "#ff9800";
  
  if (confidence) {
    const confidenceValue = decodeURIComponent(confidence).toLowerCase();
    
    if (confidenceValue.includes("high") || confidenceValue.includes("90") || confidenceValue.includes("95")) {
      confidenceLevel = "High";
      confidenceWidth = "95%";
      confidenceColor = "#e53935";
    } else if (confidenceValue.includes("low") || confidenceValue.includes("50") || confidenceValue.includes("60")) {
      confidenceLevel = "Low";
      confidenceWidth = "55%";
      confidenceColor = "#ffb74d";
    } else {
      confidenceLevel = "Medium";
      confidenceWidth = "75%";
      confidenceColor = "#ff9800";
    }
    
    confidenceText.textContent = confidenceLevel;
  }
  
  confidenceFill.style.width = confidenceWidth;
  confidenceFill.style.background = `linear-gradient(to right, ${confidenceColor}, ${confidenceColor})`;
  
  // Update detection time
  const detectionTimeElement = document.getElementById("detection-time");
  const now = new Date();
  const timeString = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  const dateString = now.toLocaleDateString([], { month: 'short', day: 'numeric' });
  detectionTimeElement.textContent = `${dateString} at ${timeString}`;
  
  // Add button event listeners
  document.getElementById("go-back-btn").addEventListener("click", () => {
    // Add visual feedback
    const button = document.getElementById("go-back-btn");
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Redirecting...';
    button.disabled = true;
    
    // Go back after a short delay for visual feedback
    setTimeout(() => {
      window.history.back();
    }, 500);
  });
  
  document.getElementById("proceed-btn").addEventListener("click", () => {
    // Show final warning
    if (confirm("⚠️ SECURITY WARNING ⚠️\n\nYou are about to proceed to a website identified as a phishing threat.\n\nThis is strongly discouraged and may result in theft of personal information, passwords, or financial details.\n\nAre you absolutely sure you want to continue?")) {
      // If user insists, close this warning page
      window.close();
    }
  });
  
  // Add some visual effects
  setTimeout(() => {
    document.querySelectorAll('.detail-box').forEach((box, index) => {
      setTimeout(() => {
        box.style.opacity = '1';
        box.style.transform = 'translateY(0)';
      }, index * 150);
    });
  }, 300);
});