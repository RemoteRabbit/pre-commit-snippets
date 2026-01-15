// Custom JavaScript for pre-commit-snippet documentation

// Add copy feedback for inline code
document.addEventListener("DOMContentLoaded", function() {
  // Track external link clicks (for analytics if configured)
  document.querySelectorAll('a[href^="http"]').forEach(function(link) {
    link.addEventListener("click", function() {
      if (typeof gtag !== "undefined") {
        gtag("event", "click", {
          event_category: "outbound",
          event_label: link.href
        });
      }
    });
  });
});

// Keyboard shortcuts
document.addEventListener("keydown", function(event) {
  // Press '/' to focus search (if not already in an input)
  if (event.key === "/" && document.activeElement.tagName !== "INPUT") {
    event.preventDefault();
    var searchInput = document.querySelector(".md-search__input");
    if (searchInput) {
      searchInput.focus();
    }
  }
});
