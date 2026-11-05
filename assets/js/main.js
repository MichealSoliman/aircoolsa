/**
 * Air Cool Jeddah - Main JavaScript
 * Handles navigation, accessible mobile drawer, keyboard tabs, FAQ accordion, and GA4 event delegation.
 */

document.addEventListener('DOMContentLoaded', () => {
  // =========================================================================
  // 1. Mobile Menu Drawer (Accessible with Esc, inert, aria-hidden, focus trap)
  // =========================================================================
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileMenuOverlay = document.getElementById('mobileMenuOverlay');
  const mobileMenuCloseBtn = document.getElementById('mobileMenuCloseBtn');

  function openMobileMenu() {
    if (!mobileMenu) return;
    mobileMenu.classList.remove('translate-x-full');
    mobileMenu.classList.add('translate-x-0');
    mobileMenu.removeAttribute('inert');
    mobileMenu.setAttribute('aria-hidden', 'false');

    if (mobileMenuOverlay) {
      mobileMenuOverlay.classList.remove('hidden');
      setTimeout(() => mobileMenuOverlay.classList.remove('opacity-0'), 10);
    }
    if (mobileMenuBtn) {
      mobileMenuBtn.setAttribute('aria-expanded', 'true');
    }
    document.body.style.overflow = 'hidden';

    // Focus first link or close button inside menu
    if (mobileMenuCloseBtn) {
      mobileMenuCloseBtn.focus();
    }
  }

  function closeMobileMenu() {
    if (!mobileMenu) return;
    mobileMenu.classList.add('translate-x-full');
    mobileMenu.classList.remove('translate-x-0');
    mobileMenu.setAttribute('inert', '');
    mobileMenu.setAttribute('aria-hidden', 'true');

    if (mobileMenuOverlay) {
      mobileMenuOverlay.classList.add('opacity-0');
      setTimeout(() => mobileMenuOverlay.classList.add('hidden'), 300);
    }
    if (mobileMenuBtn) {
      mobileMenuBtn.setAttribute('aria-expanded', 'false');
      mobileMenuBtn.focus();
    }
    document.body.style.overflow = '';
  }

  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', () => {
      const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    });
  }

  if (mobileMenuCloseBtn) {
    mobileMenuCloseBtn.addEventListener('click', closeMobileMenu);
  }

  if (mobileMenuOverlay) {
    mobileMenuOverlay.addEventListener('click', closeMobileMenu);
  }

  // Close mobile menu on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileMenu && !mobileMenu.classList.contains('translate-x-full')) {
      closeMobileMenu();
    }
  });

  // Close menu when a link inside mobile drawer is clicked
  if (mobileMenu) {
    mobileMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        closeMobileMenu();
      });
    });
  }

  // =========================================================================
  // 2. Sticky Header Elevation on Scroll
  // =========================================================================
  const siteHeader = document.getElementById('siteHeader');
  if (siteHeader) {
    const handleScroll = () => {
      if (window.scrollY > 20) {
        siteHeader.classList.add('shadow-md', 'bg-white/95', 'backdrop-blur-md');
        siteHeader.classList.remove('bg-white');
      } else {
        siteHeader.classList.remove('shadow-md', 'bg-white/95', 'backdrop-blur-md');
        siteHeader.classList.add('bg-white');
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
  }

  // =========================================================================
  // 3. Accessible FAQ Accordion (Kept strictly in DOM, toggles hidden)
  // =========================================================================
  const accordionButtons = document.querySelectorAll('.faq-toggle-btn');
  accordionButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';
      const targetId = btn.getAttribute('aria-controls');
      const content = document.getElementById(targetId);
      const icon = btn.querySelector('.faq-icon');

      // Close other open accordions in the same container for clean UX
      const parent = btn.closest('.faq-container');
      if (parent) {
        const otherBtns = parent.querySelectorAll('.faq-toggle-btn');
        otherBtns.forEach((otherBtn) => {
          if (otherBtn !== btn && otherBtn.getAttribute('aria-expanded') === 'true') {
            otherBtn.setAttribute('aria-expanded', 'false');
            const otherContent = document.getElementById(otherBtn.getAttribute('aria-controls'));
            const otherIcon = otherBtn.querySelector('.faq-icon');
            if (otherContent) otherContent.classList.add('hidden');
            if (otherIcon) otherIcon.classList.remove('rotate-180');
          }
        });
      }

      // Toggle current
      if (isExpanded) {
        btn.setAttribute('aria-expanded', 'false');
        if (content) content.classList.add('hidden');
        if (icon) icon.classList.remove('rotate-180');
      } else {
        btn.setAttribute('aria-expanded', 'true');
        if (content) content.classList.remove('hidden');
        if (icon) icon.classList.add('rotate-180');
      }
    });
  });

  // =========================================================================
  // 4. Interactive AC Diagnostic Tabs (Static HTML panels, Arrow Navigation)
  // =========================================================================
  const tabList = document.querySelector('[role="tablist"]');
  const tabs = document.querySelectorAll('[role="tab"]');
  const panels = document.querySelectorAll('[role="tabpanel"]');

  if (tabList && tabs.length > 0 && panels.length > 0) {
    function activateTab(newTab) {
      const targetPanelId = newTab.getAttribute('aria-controls');

      // Update tabs state & styles
      tabs.forEach((tab) => {
        tab.setAttribute('aria-selected', 'false');
        tab.setAttribute('tabindex', '-1');
        tab.classList.remove('bg-brand-blue', 'text-white', 'border-brand-blue', 'shadow-md');
        tab.classList.add('bg-white', 'text-slate-700', 'border-slate-200');
      });

      newTab.setAttribute('aria-selected', 'true');
      newTab.setAttribute('tabindex', '0');
      newTab.classList.remove('bg-white', 'text-slate-700', 'border-slate-200');
      newTab.classList.add('bg-brand-blue', 'text-white', 'border-brand-blue', 'shadow-md');
      newTab.focus();

      // Show matching panel, hide others via hidden attribute
      panels.forEach((panel) => {
        if (panel.id === targetPanelId) {
          panel.removeAttribute('hidden');
        } else {
          panel.setAttribute('hidden', '');
        }
      });
    }

    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        activateTab(tab);
      });
    });

    // Keyboard navigation (ArrowLeft & ArrowRight for RTL / LTR tabs)
    tabList.addEventListener('keydown', (e) => {
      const currentTab = document.activeElement;
      if (!currentTab || currentTab.getAttribute('role') !== 'tab') return;

      const tabsArray = Array.from(tabs);
      const currentIndex = tabsArray.indexOf(currentTab);
      let targetIndex = null;

      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault();
        targetIndex = (currentIndex + 1) % tabsArray.length;
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        targetIndex = (currentIndex - 1 + tabsArray.length) % tabsArray.length;
      } else if (e.key === 'Home') {
        e.preventDefault();
        targetIndex = 0;
      } else if (e.key === 'End') {
        e.preventDefault();
        targetIndex = tabsArray.length - 1;
      }

      if (targetIndex !== null) {
        activateTab(tabsArray[targetIndex]);
      }
    });
  }

  // =========================================================================
  // 5. Cleaning Price Calculator (ac-cleaning-jeddah)
  // =========================================================================
  const calcContainer = document.getElementById('cleaningCalculator');
  const calcUnits = document.getElementById('calcUnits');
  const calcType = document.getElementById('calcType');
  const calcResultDisplay = document.getElementById('calcResultDisplay');
  const calcWaBtn = document.getElementById('calcWaBtn');

  if (calcContainer && calcUnits && calcType && calcResultDisplay && calcWaBtn) {
    function updateCalculator() {
      const units = parseInt(calcUnits.value, 10) || 1;
      const type = calcType.value;
      const typeText = calcType.options[calcType.selectedIndex]?.text || 'مكيف';
      let total = 0;
      let displayHtml = '';
      let waText = '';

      if (type === 'split') {
        let unitPrice = 150;
        if (units === 1) {
          unitPrice = 150;
        } else if (units <= 3) {
          unitPrice = 120;
        } else if (units <= 7) {
          unitPrice = 100;
        } else {
          unitPrice = 80;
        }
        total = units * unitPrice;
        displayHtml = `${total} <span class="text-sm font-bold text-slate-600">ريال</span> <span class="text-xs text-slate-400 font-normal">(${unitPrice} ر.س / مكيف)</span>`;
        waText = `السلام عليكم، أرغب في حجز غسيل ${units} مكيف ${typeText} في جدة، التقدير الاسترشادي ${total} ريال.`;
      } else {
        // Special types: window, floor, concealed, cassette
        const basePrices = {
          window: 80,
          floor: 200,
          concealed: 250,
          cassette: 180
        };
        const base = basePrices[type] || 150;
        total = units * base;
        displayHtml = `تبدأ من ${total} <span class="text-sm font-bold text-slate-600">ريال</span> <span class="text-xs text-slate-400 font-normal">(${base} ر.س / مكيف)</span>`;
        waText = `السلام عليكم، أرغب في الاستفسار وحجز تنظيف ${units} مكيف ${typeText} في جدة، التقدير الاسترشادي يبدأ من ${total} ريال.`;
      }

      calcResultDisplay.innerHTML = displayHtml;
      calcWaBtn.href = `https://wa.me/966533553620?text=${encodeURIComponent(waText)}`;

      // Fire GA4 Event for calculator interaction
      if (typeof gtag === 'function') {
        gtag('event', 'calc_use', {
          page_path: window.location.pathname,
          units: units,
          ac_type: type,
          estimated_total: total,
          link_location: 'calculator'
        });
      }
    }

    calcUnits.addEventListener('change', updateCalculator);
    calcType.addEventListener('change', updateCalculator);
  }

  // =========================================================================
  // 6. GA4 Event Delegation (click_call, click_whatsapp)
  // =========================================================================
  function resolveLinkLocation(el) {
    if (el.hasAttribute('data-loc')) {
      return el.getAttribute('data-loc');
    }
    const locElement = el.closest('[data-loc]');
    if (locElement) {
      return locElement.getAttribute('data-loc');
    }
    if (el.closest('#siteHeader') || el.closest('#topBar')) return 'header';
    if (el.closest('#hero')) return 'hero';
    if (el.closest('#cleaningCalculator')) return 'calculator';
    if (el.closest('#services')) return 'services';
    if (el.closest('#pricing-guide') || el.closest('#pricing')) return 'pricing';
    if (el.closest('#districts-coverage') || el.closest('#districts')) return 'districts';
    if (el.closest('#faq') || el.closest('.faq-container')) return 'faq';
    if (el.closest('aside') || el.closest('#sidebar')) return 'sidebar';
    if (el.closest('#siteFooter')) return 'footer';
    if (el.closest('#mobileStickyBar')) return 'sticky_bar';
    if (el.closest('#airCoolContactForm')) return 'form';
    return 'page';
  }

  document.addEventListener('click', (e) => {
    const link = e.target.closest('a');
    if (!link) return;

    const href = link.getAttribute('href') || '';
    const location = resolveLinkLocation(link);

    // Call Click
    if (href.startsWith('tel:')) {
      if (typeof gtag === 'function') {
        gtag('event', 'click_call', {
          page_path: window.location.pathname,
          link_location: location
        });
      }
    }

    // WhatsApp Click
    if (href.includes('wa.me') || href.includes('whatsapp.com')) {
      if (typeof gtag === 'function') {
        gtag('event', 'click_whatsapp', {
          page_path: window.location.pathname,
          link_location: location
        });
      }
    }
  });
});
