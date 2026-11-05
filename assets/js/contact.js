/**
 * Air Cool Jeddah - Contact & Booking Form Handler
 * Validates inputs, handles district selection, submits to API, dispatches GA4 generate_lead,
 * and falls back to prefilled WhatsApp if offline or endpoint unavailable.
 * STRICT: No localStorage usage.
 */

document.addEventListener('DOMContentLoaded', () => {
  const contactForm = document.getElementById('airCoolContactForm');
  if (!contactForm) return;

  const nameInput = document.getElementById('clientName');
  const phoneInput = document.getElementById('clientPhone');
  const districtSelect = document.getElementById('clientDistrict');
  const customDistrictContainer = document.getElementById('customDistrictContainer');
  const customDistrictInput = document.getElementById('customDistrict');
  const serviceSelect = document.getElementById('serviceType');
  const notesInput = document.getElementById('clientNotes');
  const honeypotInput = document.getElementById('website_honey');
  const submitBtn = document.getElementById('formSubmitBtn');
  const formStatus = document.getElementById('formStatus');

  // Dynamic toggle for "حي آخر"
  if (districtSelect && customDistrictContainer && customDistrictInput) {
    districtSelect.addEventListener('change', () => {
      if (districtSelect.value === 'other') {
        customDistrictContainer.classList.remove('hidden');
        customDistrictInput.setAttribute('required', 'required');
        customDistrictInput.focus();
      } else {
        customDistrictContainer.classList.add('hidden');
        customDistrictInput.removeAttribute('required');
        customDistrictInput.value = '';
      }
    });
  }

  // Validate Saudi phone number: matches 05XXXXXXXX, 5XXXXXXXX, +9665XXXXXXXX, 009665XXXXXXXX
  function isValidSaudiPhone(phone) {
    const cleaned = phone.replace(/[\s\-\(\)]/g, '');
    const regex = /^(05|5|\+9665|009665)[0-9]{8}$/;
    return regex.test(cleaned);
  }

  function showError(inputEl, message) {
    const parent = inputEl.closest('.form-group');
    if (!parent) return;
    let errorEl = parent.querySelector('.field-error');
    if (!errorEl) {
      errorEl = document.createElement('p');
      errorEl.className = 'field-error text-red-600 text-xs mt-1.5 font-medium';
      parent.appendChild(errorEl);
    }
    errorEl.textContent = message;
    inputEl.classList.add('border-red-500', 'focus:ring-red-400');
    inputEl.classList.remove('border-brand-border');
  }

  function clearError(inputEl) {
    const parent = inputEl.closest('.form-group');
    if (!parent) return;
    const errorEl = parent.querySelector('.field-error');
    if (errorEl) {
      errorEl.remove();
    }
    inputEl.classList.remove('border-red-500', 'focus:ring-red-400');
    inputEl.classList.add('border-brand-border');
  }

  [nameInput, phoneInput, districtSelect, customDistrictInput, serviceSelect].forEach((input) => {
    if (input) {
      input.addEventListener('input', () => clearError(input));
      input.addEventListener('change', () => clearError(input));
    }
  });

  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Honeypot anti-spam check
    if (honeypotInput && honeypotInput.value) {
      // Silently ignore bot submission
      return;
    }

    let isValid = true;

    // Validate Name
    if (!nameInput || !nameInput.value.trim() || nameInput.value.trim().length < 3) {
      showError(nameInput, 'يرجى كتابة الاسم الكريم (3 أحرف على الأقل)');
      isValid = false;
    } else {
      clearError(nameInput);
    }

    // Validate Phone
    if (!phoneInput || !phoneInput.value.trim() || !isValidSaudiPhone(phoneInput.value.trim())) {
      showError(phoneInput, 'يرجى إدخال رقم جوال سعودي صحيح يبدأ بـ 05 (مثال: 0533553620)');
      isValid = false;
    } else {
      clearError(phoneInput);
    }

    // Validate District
    let finalDistrict = '';
    if (!districtSelect || !districtSelect.value) {
      showError(districtSelect, 'يرجى اختيار الحي داخل جدة');
      isValid = false;
    } else if (districtSelect.value === 'other') {
      if (!customDistrictInput || !customDistrictInput.value.trim()) {
        showError(customDistrictInput, 'يرجى كتابة اسم الحي داخل جدة');
        isValid = false;
      } else {
        clearError(customDistrictInput);
        finalDistrict = customDistrictInput.value.trim();
      }
    } else {
      clearError(districtSelect);
      finalDistrict = districtSelect.options[districtSelect.selectedIndex].text;
    }

    // Validate Service
    if (!serviceSelect || !serviceSelect.value) {
      showError(serviceSelect, 'يرجى اختيار نوع الخدمة المطلوبة');
      isValid = false;
    } else {
      clearError(serviceSelect);
    }

    if (!isValid) return;

    const formData = {
      name: nameInput.value.trim(),
      phone: phoneInput.value.trim(),
      district: finalDistrict,
      service: serviceSelect.options[serviceSelect.selectedIndex].text,
      serviceValue: serviceSelect.value,
      notes: notesInput ? notesInput.value.trim() : '',
      city: 'جدة'
    };

    // UI Loading state
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = `
        <svg class="animate-spin -ml-1 mr-2 h-5 w-5 text-white inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
        </svg>
        جاري معالجة الطلب...
      `;
    }

    if (formStatus) {
      formStatus.classList.add('hidden');
      formStatus.textContent = '';
    }

    const actionUrl = contactForm.getAttribute('action') || '';
    const hasLiveEndpoint = actionUrl && actionUrl !== '#' && !actionUrl.startsWith('javascript:');

    const waFallbackMessage = `السلام عليكم شركة إير كول،\nأرغب في حجز موعد خدمة مكيفات:\n• الاسم: ${formData.name}\n• رقم الجوال: ${formData.phone}\n• الحي في جدة: ${formData.district}\n• الخدمة المطلوبة: ${formData.service}\n• وصف المشكلة: ${formData.notes || 'لا يوجد'}`;
    const waFallbackUrl = `https://wa.me/966533553620?text=${encodeURIComponent(waFallbackMessage)}`;

    if (hasLiveEndpoint) {
      try {
        const response = await fetch(actionUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(formData)
        });

        if (response.ok) {
          formStatus.className = 'p-4 rounded-xl text-sm font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200 mt-4';
          formStatus.textContent = 'تم استلام طلبك بنجاح! سيتواصل معك فني إير كول في أقرب وقت لتأكيد الموعد والتفاصيل.';
          formStatus.classList.remove('hidden');
          contactForm.reset();
          if (customDistrictContainer) customDistrictContainer.classList.add('hidden');

          // GA4 generate_lead event
          if (typeof gtag === 'function') {
            gtag('event', 'generate_lead', {
              page_path: window.location.pathname,
              link_location: 'form'
            });
          }
        } else {
          throw new Error('Server returned ' + response.status);
        }
      } catch (err) {
        // Fallback gracefully to WhatsApp
        formStatus.className = 'p-4 rounded-xl text-sm font-medium bg-amber-50 text-amber-900 border border-amber-200 mt-4 flex flex-col gap-2';
        formStatus.innerHTML = `
          <span>تعذر الإرسال التلقائي عبر الخادم حالياً. تفضل بمتابعة طلبك فوراً عبر واتساب إير كول المباشر:</span>
          <a href="${waFallbackUrl}" target="_blank" rel="noopener noreferrer" class="btn-whatsapp text-center text-sm py-2" data-loc="form">
            متابعة إرسال الطلب عبر واتساب
          </a>
        `;
        formStatus.classList.remove('hidden');
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = `إرسال طلب الخدمة`;
        }
      }
    } else {
      // Default behavior when endpoint is pending confirmation:
      // Show confirmation message and direct to WhatsApp
      formStatus.className = 'p-4 rounded-xl text-sm font-medium bg-emerald-50 text-emerald-900 border border-emerald-200 mt-4 flex flex-col gap-2';
      formStatus.innerHTML = `
        <p class="font-bold text-emerald-800">جاري توجيهك لتأكيد موعد الخدمة مباشرة عبر واتساب إير كول...</p>
        <a href="${waFallbackUrl}" target="_blank" rel="noopener noreferrer" class="btn-whatsapp text-center py-2.5 text-sm mt-1" data-loc="form">
          اضغط هنا إذا لم يفتح واتساب تلقائياً
        </a>
      `;
      formStatus.classList.remove('hidden');

      // GA4 generate_lead event
      if (typeof gtag === 'function') {
        gtag('event', 'generate_lead', {
          page_path: window.location.pathname,
          link_location: 'form'
        });
      }

      setTimeout(() => {
        window.open(waFallbackUrl, '_blank');
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = `إرسال طلب الخدمة`;
        }
      }, 700);
    }
  });
});
