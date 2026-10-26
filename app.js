// PSP MasterLab Interactive Application Logic

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initNavigation();
  initCopyButtons();
  initSearch();
  initScrollTop();
  initMobileMenu();
});

// Theme Management - Default is now LIGHT MODE
function initTheme() {
  const themeToggle = document.getElementById('themeToggle');
  const savedTheme = localStorage.getItem('psp_theme') || 'light';
  
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('psp_theme', newTheme);
      updateThemeIcon(newTheme);
      showToast(`Switched to ${newTheme.toUpperCase()} mode`);
    });
  }
}

function updateThemeIcon(theme) {
  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    // If currently light, button shows moon (to switch to dark)
    // If currently dark, button shows sun (to switch to light)
    themeToggle.innerHTML = theme === 'light' ? '🌙' : '☀️';
    themeToggle.title = theme === 'light' ? 'Switch to Dark Mode' : 'Switch to Light Mode';
  }
}

// Navigation & Tab Switching with Stealth Support URL Cloaking
function initNavigation() {
  const navItems = document.querySelectorAll('.nav-item');
  const sections = document.querySelectorAll('.practical-section');

  // Microsoft Support KB disguise mapping
  const disguiseMap = {
    'prac1': 'support-information-repair-kb30214',
    'prac2': 'support-information-repair-kb40125',
    'prac3': 'support-information-repair-kb50198',
    'prac4': 'support-information-repair-kb60231',
    'prac5': 'support-information-repair-kb70142',
    'prac6': 'support-information-repair-kb80319',
    'prac7': 'support-information-repair-kb90214',
    'prac8': 'support-information-repair-kb99482'
  };

  const reverseMap = {
    'support-information-repair-kb30214': 'prac1',
    'support-information-repair-kb40125': 'prac2',
    'support-information-repair-kb50198': 'prac3',
    'support-information-repair-kb60231': 'prac4',
    'support-information-repair-kb70142': 'prac5',
    'support-information-repair-kb80319': 'prac6',
    'support-information-repair-kb90214': 'prac7',
    'support-information-repair-kb99482': 'prac8',
    'support-information-repair': 'prac3',
    'support-repair': 'prac3',
    'support': 'prac1'
  };

  function switchTab(targetId) {
    // Hide all sections
    sections.forEach(sec => sec.classList.remove('active'));
    navItems.forEach(nav => nav.classList.remove('active'));

    // Show target section
    const targetSection = document.getElementById(targetId);
    if (targetSection) {
      targetSection.classList.add('active');
    }

    // Activate corresponding nav item
    const activeNav = document.querySelector(`.nav-item[data-target="${targetId}"]`);
    if (activeNav) {
      activeNav.classList.add('active');
    }

    // Close mobile menu if open
    const sidebar = document.querySelector('.sidebar');
    if (sidebar && sidebar.classList.contains('open')) {
      sidebar.classList.remove('open');
    }

    // Scroll to top of main content
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // STEALTH URL: Replace the URL hash with Microsoft Support Information Repair KB
    const disguiseSlug = disguiseMap[targetId] || 'support-information-repair';
    history.replaceState(null, null, `#${disguiseSlug}`);

    // Update document title with KB tag to maintain authentic Microsoft Support look
    const kbNum = disguiseSlug.split('-kb')[1];
    if (kbNum) {
      document.title = `Microsoft Support: Windows & PC Help (KB${kbNum})`;
    } else {
      document.title = `Microsoft Support: Windows & PC Help`;
    }
  }

  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = item.getAttribute('data-target');
      switchTab(targetId);
    });
  });

  // Check URL hash on initial load
  const rawHash = (window.location.hash || '').replace('#', '').trim();
  let resolvedTab = 'prac1';

  if (rawHash) {
    // 1. Direct match with practical ID (e.g., #prac3)
    if (document.getElementById(rawHash)) {
      resolvedTab = rawHash;
    } 
    // 2. Disguise URL match (e.g., #support-information-repair-kb50198 or #support-information-repair)
    else if (reverseMap[rawHash]) {
      resolvedTab = reverseMap[rawHash];
    }
    // 3. Fallback prefix check (if hash contains 'repair' or 'support')
    else if (rawHash.includes('50198') || rawHash.includes('prac3')) {
      resolvedTab = 'prac3';
    }
  }

  switchTab(resolvedTab);
}

// Copy Code Button Handling
function initCopyButtons() {
  // Individual snippet copy
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-code-target');
      let codeText = '';

      if (targetId) {
        const codeElement = document.getElementById(targetId);
        if (codeElement) {
          codeText = codeElement.innerText;
        }
      } else {
        // Fallback: look for pre code inside the same wrapper
        const wrapper = btn.closest('.code-wrapper');
        if (wrapper) {
          const codeEl = wrapper.querySelector('pre code') || wrapper.querySelector('pre');
          if (codeEl) codeText = codeEl.innerText;
        }
      }

      if (codeText) {
        copyToClipboard(codeText, btn);
      }
    });
  });

  // "Copy Entire Practical" buttons
  document.querySelectorAll('.copy-all-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const section = btn.closest('.practical-section');
      if (!section) return;

      const codeSnippets = section.querySelectorAll('pre code, pre');
      let fullCode = `# ${section.querySelector('.section-title')?.innerText || 'PSP Lab Practical'}\n\n`;

      codeSnippets.forEach((codeEl, idx) => {
        const qCard = codeEl.closest('.question-card');
        const qTitle = qCard?.querySelector('.q-title')?.innerText || `Question ${idx + 1}`;
        fullCode += `\n# ==================================================\n`;
        fullCode += `# ${qTitle}\n`;
        fullCode += `# ==================================================\n\n`;
        fullCode += codeEl.innerText.trim() + '\n\n';
      });

      copyToClipboard(fullCode, btn, 'Entire Practical Copied!');
    });
  });
}

function copyToClipboard(text, buttonEl, customToastMsg = 'Code copied to clipboard!') {
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).then(() => {
      triggerCopySuccess(buttonEl, customToastMsg);
    }).catch(err => {
      fallbackCopyText(text, buttonEl, customToastMsg);
    });
  } else {
    fallbackCopyText(text, buttonEl, customToastMsg);
  }
}

function fallbackCopyText(text, buttonEl, customToastMsg) {
  const textArea = document.createElement('textarea');
  textArea.value = text;
  textArea.style.position = 'fixed';
  textArea.style.left = '-9999px';
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();
  try {
    document.execCommand('copy');
    triggerCopySuccess(buttonEl, customToastMsg);
  } catch (err) {
    showToast('Failed to copy code', true);
  }
  document.body.removeChild(textArea);
}

function triggerCopySuccess(buttonEl, toastMsg) {
  if (buttonEl) {
    const originalHtml = buttonEl.innerHTML;
    buttonEl.classList.add('copied');
    buttonEl.innerHTML = `✓ Copied!`;
    setTimeout(() => {
      buttonEl.classList.remove('copied');
      buttonEl.innerHTML = originalHtml;
    }, 2000);
  }
  showToast(toastMsg);
}

// Toast Alert
function showToast(message, isError = false) {
  let toast = document.getElementById('pspToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'pspToast';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }

  toast.innerHTML = isError ? `⚠️ ${message}` : `📋 ${message}`;
  toast.style.borderColor = isError ? 'var(--accent-rose)' : 'var(--accent-cyan)';
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, 2500);
}

// Helper to escape regex special characters
function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// Remove all search highlights safely from container
function removeHighlights(container) {
  if (!container) return;
  const marks = container.querySelectorAll('mark.search-highlight');
  marks.forEach(mark => {
    const parent = mark.parentNode;
    if (parent) {
      parent.replaceChild(document.createTextNode(mark.textContent), mark);
      parent.normalize();
    }
  });
}

// Recursively highlight text nodes matching regex
function highlightTextNodes(element, regex) {
  if (element.nodeType === Node.TEXT_NODE) {
    const text = element.nodeValue;
    if (regex.test(text)) {
      const fragment = document.createDocumentFragment();
      let lastIdx = 0;
      regex.lastIndex = 0;
      let match;
      while ((match = regex.exec(text)) !== null) {
        if (match.index > lastIdx) {
          fragment.appendChild(document.createTextNode(text.substring(lastIdx, match.index)));
        }
        const mark = document.createElement('mark');
        mark.className = 'search-highlight';
        mark.textContent = match[0];
        fragment.appendChild(mark);
        lastIdx = regex.lastIndex;
      }
      if (lastIdx < text.length) {
        fragment.appendChild(document.createTextNode(text.substring(lastIdx)));
      }
      element.parentNode.replaceChild(fragment, element);
    }
  } else if (
    element.nodeType === Node.ELEMENT_NODE &&
    element.nodeName !== 'SCRIPT' &&
    element.nodeName !== 'STYLE' &&
    !element.classList.contains('search-highlight') &&
    !element.classList.contains('copy-btn') &&
    !element.classList.contains('btn-primary')
  ) {
    Array.from(element.childNodes).forEach(child => highlightTextNodes(child, regex));
  }
}

// Search Filter & Interactive Keyword Highlighter
function initSearch() {
  const searchInput = document.getElementById('searchInput');
  const countBadge = document.getElementById('searchCount');
  const mainContent = document.querySelector('.main-content');
  if (!searchInput) return;

  // Keyboard shortcut Ctrl+K
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      searchInput.focus();
    }
  });

  searchInput.addEventListener('input', () => {
    const query = searchInput.value.trim();

    // 1. Clear previous highlights
    if (mainContent) {
      removeHighlights(mainContent);
    }

    if (!query || query.length < 2) {
      if (countBadge) {
        countBadge.classList.remove('visible');
        countBadge.textContent = '0';
      }
      // Reset visibility to currently active tab
      document.querySelectorAll('.question-card').forEach(card => card.style.display = '');
      document.querySelectorAll('.practical-section').forEach(sec => {
        const isCurrentActive = document.querySelector(`.nav-item.active`)?.getAttribute('data-target') === sec.id;
        sec.style.display = isCurrentActive ? 'block' : 'none';
        const header = sec.querySelector('.section-header');
        const theory = sec.querySelector('.theory-card');
        if (header) header.style.display = '';
        if (theory) theory.style.display = '';
      });
      return;
    }

    const regex = new RegExp(escapeRegExp(query), 'gi');
    let totalCardsMatched = 0;

    // Filter cards and highlight keywords across ALL practicals
    document.querySelectorAll('.practical-section').forEach(sec => {
      let sectionHasMatch = false;

      // Check theory card
      const theory = sec.querySelector('.theory-card');
      if (theory) {
        if (regex.test(theory.innerText)) {
          highlightTextNodes(theory, regex);
          sectionHasMatch = true;
        }
      }

      // Check question cards
      sec.querySelectorAll('.question-card').forEach(card => {
        if (regex.test(card.innerText)) {
          card.style.display = '';
          highlightTextNodes(card, regex);
          sectionHasMatch = true;
          totalCardsMatched++;
        } else {
          card.style.display = 'none';
        }
      });

      // Show/hide section based on matches
      sec.style.display = sectionHasMatch ? 'block' : 'none';
      const header = sec.querySelector('.section-header');
      if (header) header.style.display = sectionHasMatch ? '' : 'none';
      if (theory) theory.style.display = sectionHasMatch ? '' : 'none';
    });

    // Update match badge
    const markCount = document.querySelectorAll('mark.search-highlight').length;
    if (countBadge) {
      countBadge.textContent = `${markCount} ${markCount === 1 ? 'match' : 'matches'}`;
      countBadge.classList.add('visible');
    }
  });

  // Enter key scrolls smoothly to the first highlighted word
  searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const firstMark = document.querySelector('mark.search-highlight');
      if (firstMark) {
        firstMark.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  });
}

// Scroll To Top Button
function initScrollTop() {
  const scrollBtn = document.getElementById('scrollTopBtn');
  if (!scrollBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      scrollBtn.classList.add('visible');
    } else {
      scrollBtn.classList.remove('visible');
    }
  });

  scrollBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// Mobile Menu Drawer
function initMobileMenu() {
  const toggleBtn = document.getElementById('menuToggle');
  const sidebar = document.querySelector('.sidebar');

  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!sidebar.contains(e.target) && !toggleBtn.contains(e.target) && sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
      }
    });
  }
}
