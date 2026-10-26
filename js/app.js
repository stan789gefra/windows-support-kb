/**
 * PSP Lab Solutions - Client-Side Interactivity
 * Universal Copy-to-Clipboard, Live Search, Theme Switcher, Image Lightbox
 */

// Universal Copy to Clipboard Helper
function copyTextToClipboard(text, onSuccess, onError) {
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).then(onSuccess).catch(err => {
      fallbackCopy(text, onSuccess, onError);
    });
  } else {
    fallbackCopy(text, onSuccess, onError);
  }
}

function fallbackCopy(text, onSuccess, onError) {
  try {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";
    textArea.style.top = "-9999px";
    textArea.style.left = "-9999px";
    textArea.setAttribute("readonly", "");
    document.body.appendChild(textArea);
    textArea.select();
    const successful = document.execCommand("copy");
    document.body.removeChild(textArea);
    if (successful && onSuccess) {
      onSuccess();
    } else if (!successful && onError) {
      onError();
    }
  } catch (err) {
    if (onError) onError(err);
  }
}

// Toast Notification
function showToast(message, type = "success") {
  const container = document.getElementById("toastContainer");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `
    <span class="toast-icon">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
    </span>
    <span>${message}</span>
  `;

  container.appendChild(toast);
  requestAnimationFrame(() => {
    toast.classList.add("show");
  });

  setTimeout(() => {
    toast.classList.remove("show");
    setTimeout(() => {
      toast.remove();
    }, 250);
  }, 2200);
}

// Setup Copy Buttons
function setupCopyButtons() {
  // 1. Snippet Copy Buttons
  document.querySelectorAll(".btn-copy-code").forEach(btn => {
    btn.addEventListener("click", e => {
      e.preventDefault();
      const codeToCopy = btn.getAttribute("data-copy") || "";
      if (!codeToCopy) return;

      copyTextToClipboard(codeToCopy, () => {
        const originalText = btn.innerHTML;
        btn.classList.add("copied");
        btn.innerHTML = `
          <span class="copy-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
          <span class="copy-text">Copied!</span>
        `;
        showToast("Code snippet copied to clipboard! ✓");

        setTimeout(() => {
          btn.classList.remove("copied");
          btn.innerHTML = originalText;
        }, 2000);
      }, () => {
        showToast("Failed to copy. Please manually select code.", "error");
      });
    });
  });

  // 2. Output Copy Buttons
  document.querySelectorAll(".btn-copy-output").forEach(btn => {
    btn.addEventListener("click", e => {
      e.preventDefault();
      const textToCopy = btn.getAttribute("data-copy") || "";
      if (!textToCopy) return;

      copyTextToClipboard(textToCopy, () => {
        btn.classList.add("copied");
        const orig = btn.innerHTML;
        btn.innerHTML = "Copied! ✓";
        showToast("Console output copied to clipboard! ✓");
        setTimeout(() => {
          btn.classList.remove("copied");
          btn.innerHTML = orig;
        }, 1800);
      });
    });
  });

  // 3. Copy All Code per Practical
  document.querySelectorAll(".btn-copy-all").forEach(btn => {
    btn.addEventListener("click", e => {
      e.preventDefault();
      const code = btn.getAttribute("data-copy") || "";
      if (!code) return;

      copyTextToClipboard(code, () => {
        btn.classList.add("copied");
        const orig = btn.innerHTML;
        btn.innerHTML = `
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>All Code Copied!</span>
        `;
        showToast("Full practical code copied to clipboard! ✓");
        setTimeout(() => {
          btn.classList.remove("copied");
          btn.innerHTML = orig;
        }, 2200);
      });
    });
  });

  // 4. Global Copy All Practicals
  const globalCopyBtn = document.getElementById("btnCopyAllGlobal");
  if (globalCopyBtn) {
    globalCopyBtn.addEventListener("click", () => {
      const allCodes = [];
      document.querySelectorAll(".practical-card").forEach(card => {
        const copyAllBtn = card.querySelector(".btn-copy-all");
        if (copyAllBtn) {
          const title = card.querySelector(".practical-title")?.innerText || "";
          allCodes.push(`\n# ${"=".repeat(60)}\n# ${title}\n# ${"=".repeat(60)}\n`);
          allCodes.push(copyAllBtn.getAttribute("data-copy") || "");
        }
      });

      const fullRepoCode = allCodes.join("\n\n");
      copyTextToClipboard(fullRepoCode, () => {
        showToast("Complete PSP repository (all 8 labs) copied to clipboard! ✓");
      });
    });
  }
}

// Lightbox Modal for Plots
function openLightbox(src, caption) {
  const modal = document.getElementById("lightboxModal");
  const img = document.getElementById("lightboxImg");
  const cap = document.getElementById("lightboxCaption");
  const dl = document.getElementById("lightboxDownloadBtn");

  if (!modal || !img) return;

  img.src = src;
  img.alt = caption || "Plot visualization";
  if (cap) cap.textContent = caption || "";
  if (dl) dl.href = src;

  modal.classList.add("active");
  modal.setAttribute("aria-hidden", "false");
}

function closeLightbox() {
  const modal = document.getElementById("lightboxModal");
  if (modal) {
    modal.classList.remove("active");
    modal.setAttribute("aria-hidden", "true");
  }
}

// GitHub Pages Guide Modal
function openGuide() {
  const modal = document.getElementById("guideModal");
  if (modal) {
    modal.classList.add("active");
    modal.setAttribute("aria-hidden", "false");
  }
}

function closeGuide() {
  const modal = document.getElementById("guideModal");
  if (modal) {
    modal.classList.remove("active");
    modal.setAttribute("aria-hidden", "true");
  }
}

// Search and Filter Functionality
function setupSearchAndFilter() {
  const searchInput = document.getElementById("globalSearchInput");
  const searchFeedback = document.getElementById("searchFeedback");
  const searchResultText = document.getElementById("searchResultText");
  const clearSearchBtn = document.getElementById("clearSearchBtn");
  const cards = document.querySelectorAll(".practical-card");
  const navLinks = document.querySelectorAll(".nav-link");

  function performSearch(query) {
    const q = query.trim().toLowerCase();

    if (!q) {
      cards.forEach(c => c.style.display = "");
      navLinks.forEach(l => l.style.display = "");
      if (searchFeedback) searchFeedback.style.display = "none";
      return;
    }

    let matchCount = 0;

    cards.forEach(card => {
      const cardText = card.innerText.toLowerCase();
      if (cardText.includes(q)) {
        card.style.display = "";
        matchCount++;
      } else {
        card.style.display = "none";
      }
    });

    navLinks.forEach(link => {
      const targetId = link.getAttribute("data-target");
      const targetCard = document.getElementById(targetId);
      if (targetCard && targetCard.style.display !== "none") {
        link.style.display = "";
      } else {
        link.style.display = "none";
      }
    });

    if (searchFeedback) {
      searchFeedback.style.display = "flex";
      searchResultText.textContent = `Found ${matchCount} practical lab${matchCount === 1 ? "" : "s"} matching "${query}"`;
    }
  }

  if (searchInput) {
    searchInput.addEventListener("input", e => {
      performSearch(e.target.value);
    });
  }

  if (clearSearchBtn) {
    clearSearchBtn.addEventListener("click", () => {
      if (searchInput) {
        searchInput.value = "";
        performSearch("");
        searchInput.focus();
      }
    });
  }

  // Filter Pills (All, Simulation, Probability, Stochastic)
  const pillBtns = document.querySelectorAll(".pill-btn");
  pillBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      pillBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const filter = btn.getAttribute("data-filter");
      cards.forEach(card => {
        const num = parseInt(card.getAttribute("data-practical"), 10);
        let show = true;

        if (filter === "sim") {
          // Practicals 1, 6, 8 are simulation heavy
          show = [1, 6, 8].includes(num);
        } else if (filter === "prob") {
          // Practicals 2, 3, 7 are probability & statistics
          show = [2, 3, 7].includes(num);
        } else if (filter === "stoch") {
          // Practicals 4, 5, 8 are Markov & stochastic
          show = [4, 5, 8].includes(num);
        }

        card.style.display = show ? "" : "none";
      });
    });
  });
}

// Active Nav Link on Scroll (ScrollSpy)
function setupScrollSpy() {
  const cards = document.querySelectorAll(".practical-card");
  const navLinks = document.querySelectorAll(".nav-link");

  window.addEventListener("scroll", () => {
    let currentId = "";
    const scrollPos = window.scrollY + 100;

    cards.forEach(card => {
      const top = card.offsetTop;
      const height = card.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        currentId = card.id;
      }
    });

    if (currentId) {
      navLinks.forEach(link => {
        if (link.getAttribute("data-target") === currentId) {
          link.classList.add("active");
        } else {
          link.classList.remove("active");
        }
      });
    }
  }, { passive: true });
}

// Theme Toggle
function setupThemeToggle() {
  const btn = document.getElementById("themeToggleBtn");
  const currentTheme = localStorage.getItem("psp-theme") || 
                       (window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");

  document.documentElement.setAttribute("data-theme", currentTheme);

  if (btn) {
    btn.addEventListener("click", () => {
      const theme = document.documentElement.getAttribute("data-theme") === "light" ? "dark" : "light";
      document.documentElement.setAttribute("data-theme", theme);
      localStorage.setItem("psp-theme", theme);
      showToast(`Switched to ${theme} theme`);
    });
  }
}

// Mobile Menu Toggle
function setupMobileMenu() {
  const btn = document.getElementById("mobileMenuBtn");
  const sidebar = document.getElementById("sidebar");

  if (btn && sidebar) {
    btn.addEventListener("click", () => {
      sidebar.classList.toggle("mobile-open");
    });

    // Close on link click
    document.querySelectorAll(".nav-link").forEach(link => {
      link.addEventListener("click", () => {
        sidebar.classList.remove("mobile-open");
      });
    });
  }
}

// Keyboard Shortcuts
function setupKeyboardShortcuts() {
  window.addEventListener("keydown", e => {
    // If typing in input, ignore
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") {
      if (e.key === "Escape") {
        e.target.blur();
      }
      return;
    }

    if (e.key === "/") {
      e.preventDefault();
      const searchInput = document.getElementById("globalSearchInput");
      if (searchInput) searchInput.focus();
    } else if (e.key === "t" || e.key === "T") {
      const themeBtn = document.getElementById("themeToggleBtn");
      if (themeBtn) themeBtn.click();
    } else if (e.key === "Escape") {
      closeLightbox();
      closeGuide();
    }
  });
}

// Initialize Everything
document.addEventListener("DOMContentLoaded", () => {
  setupCopyButtons();
  setupSearchAndFilter();
  setupScrollSpy();
  setupThemeToggle();
  setupMobileMenu();
  setupKeyboardShortcuts();

  // Guide button listener
  const btnGuide = document.getElementById("btnGhGuide");
  if (btnGuide) {
    btnGuide.addEventListener("click", openGuide);
  }
});
