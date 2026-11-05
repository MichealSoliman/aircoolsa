# -*- coding: utf-8 -*-
with open('index.html', encoding='utf-8') as f:
    html = f.read()

# 1. FIX NAVBAR
old_nav_header = '''    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">

        <!-- Logo -->
        <a href="/"
          class="flex items-center gap-3 group focus:outline-none focus:ring-2 focus:ring-brand-blue rounded-lg p-1"
          aria-label="إير كول - الصفحة الرئيسية">
          <img src="/assets/images/logo.webp" alt="إير كول" width="147" height="99" class="h-12 md:h-14 w-auto object-contain">
        </a>

        <!-- Desktop Navigation Links -->
        <nav class="hidden lg:flex items-center gap-7 text-sm font-bold text-slate-700"
          aria-label="روابط الموقع الرئيسية">
          <a href="/" class="text-brand-blue border-b-2 border-brand-blue py-1 transition-colors">الرئيسية</a>
          <a href="/services/" class="hover:text-brand-blue py-1 transition-colors">خدماتنا</a>
          <a href="#pricing-guide" class="hover:text-brand-blue py-1 transition-colors">الأسعار</a>
          <a href="#districts-coverage" class="hover:text-brand-blue py-1 transition-colors">أحياء جدة</a>
          <a href="/about/" class="hover:text-brand-blue py-1 transition-colors">من نحن</a>
          <a href="/blog/" class="hover:text-brand-blue py-1 transition-colors">المدونة والنصائح</a>
          <a href="/contact/" class="hover:text-brand-blue py-1 transition-colors">تواصل معنا</a>
        </nav>

        <!-- Header Actions -->
        <div class="hidden sm:flex items-center gap-3">
          <a href="https://wa.me/966533553620" target="_blank" rel="noopener noreferrer"
            class="btn-whatsapp text-sm py-2.5 px-4 shadow-sm" aria-label="تواصل مع فني تكييف عبر واتساب" data-loc="header">
            <svg class="w-4 h-4 fill-current">
              <use href="#icon-whatsapp" />
            </svg>
            <span>واتساب</span>
          </a>
          <a href="tel:+966533553620" class="btn-primary text-sm py-2.5 px-4 shadow-sm"
            aria-label="اتصال هاتفي مباشر بفني المكيفات" data-loc="header">
            <svg class="w-4 h-4">
              <use href="#icon-phone" />
            </svg>
            <span>اتصل الآن</span>
          </a>
        </div>

        <!-- Mobile Menu Hamburger Button -->
        <div class="lg:hidden flex items-center">'''

new_nav_header = '''    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20 gap-4">

        <!-- Logo -->
        <a href="/"
          class="flex items-center gap-3 group focus:outline-none focus:ring-2 focus:ring-brand-blue rounded-lg p-1 flex-shrink-0"
          aria-label="إير كول - الصفحة الرئيسية">
          <img src="/assets/images/logo.webp" alt="إير كول" width="147" height="99" class="h-11 md:h-13 w-auto object-contain">
        </a>

        <!-- Desktop Navigation Links -->
        <nav class="hidden lg:flex items-center gap-5 xl:gap-8 text-sm font-bold text-slate-700"
          aria-label="روابط الموقع الرئيسية">
          <a href="/" class="text-brand-blue border-b-2 border-brand-blue py-1 transition-colors whitespace-nowrap">الرئيسية</a>
          <a href="/services/" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">خدماتنا</a>
          <a href="#pricing-guide" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">الأسعار</a>
          <a href="#districts-coverage" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">أحياء جدة</a>
          <a href="/about/" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">من نحن</a>
          <a href="/blog/" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">المدونة والنصائح</a>
          <a href="/contact/" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">تواصل معنا</a>
        </nav>

        <!-- Header Actions -->
        <div class="hidden sm:flex items-center gap-2.5 flex-shrink-0">
          <a href="https://wa.me/966533553620" target="_blank" rel="noopener noreferrer"
            class="btn-whatsapp text-xs sm:text-sm py-2 px-3 sm:px-4 shadow-sm" aria-label="تواصل مع فني تكييف عبر واتساب" data-loc="header">
            <svg class="w-4 h-4 fill-current">
              <use href="#icon-whatsapp" />
            </svg>
            <span>واتساب</span>
          </a>
          <a href="tel:+966533553620" class="btn-primary text-xs sm:text-sm py-2 px-3 sm:px-4 shadow-sm"
            aria-label="اتصال هاتفي مباشر بفني المكيفات" data-loc="header">
            <svg class="w-4 h-4">
              <use href="#icon-phone" />
            </svg>
            <span>اتصل الآن</span>
          </a>
        </div>

        <!-- Mobile Menu Hamburger Button -->
        <div class="lg:hidden flex items-center">'''

if old_nav_header in html:
    html = html.replace(old_nav_header, new_nav_header)
    print("Nav header replaced successfully.")
else:
    print("WARNING: old_nav_header not matched exactly, trying regex.")

# 2. FIX EMERGENCY SECTION
old_emergency = '''    <!-- 11. EMERGENCY SECTION -->
    <section class="py-14 bg-gradient-to-r from-brand-navy via-brand-dark to-brand-navy text-white border-b border-slate-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row items-center justify-between gap-8 text-right">

          <div class="max-w-2xl">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-white/10 text-brand-cyan mb-3 border border-white/10">
              بلاغات الأعطال العاجلة
            </span>
            <h2 class="text-2xl sm:text-3xl font-black text-white mb-3">
              توقف المكيف فجأة في جدة؟
            </h2>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-2">
              إذا توقف المكيف عن التبريد أو بدأ بتسريب مياه داخل الغرفة، تواصل معنا مباشرة لتسجيل بلاغ عاجل وتوجيه فني لمعاينة العطل في حيك السكني.
            </p>
            <p class="text-xs text-slate-400">
              ساعات استقبال الطلبات: السبت - الخميس: 08:00 ص - 10:00 م | الجمعة: 01:00 م - 10:00 م
            </p>
          </div>

          <div class="flex flex-wrap items-center gap-3 w-full sm:w-auto">
            <a href="tel:+966533553620" class="btn-primary w-full sm:w-auto text-sm" data-loc="emergency">
              <svg class="w-4 h-4"><use href="#icon-phone" /></svg>
              <span>اتصال مباشر: 0533553620</span>
            </a>
            <a href="https://wa.me/966533553620?text=السلام عليكم، لدي عطل عاجل في المكيف في جدة وأحتاج فنياً بأقرب وقت."
              target="_blank" rel="noopener noreferrer"
              class="btn-whatsapp w-full sm:w-auto text-sm" data-loc="emergency">
              <svg class="w-4 h-4 fill-current"><use href="#icon-whatsapp" /></svg>
              <span>واتساب بلاغات الطوارئ</span>
            </a>
          </div>

        </div>
      </div>
    </section>'''

new_emergency = '''    <!-- 11. EMERGENCY SECTION -->
    <section class="py-12 sm:py-16 bg-brand-navy text-white border-b border-slate-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row items-center justify-between gap-8 text-right">

          <div class="max-w-2xl space-y-3">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-brand-cyan/15 text-brand-cyan border border-brand-cyan/30">
              بلاغات الأعطال العاجلة
            </span>
            <h2 class="text-2xl sm:text-3xl font-black text-white">
              توقف المكيف فجأة في جدة؟
            </h2>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
              إذا توقف المكيف عن التبريد أو بدأ بتسريب مياه داخل الغرفة، تواصل معنا مباشرة لتسجيل بلاغ عاجل وتوجيه فني لمعاينة العطل في حيك السكني.
            </p>
            <div class="flex items-center gap-2 pt-1 text-xs text-brand-cyan font-medium">
              <svg class="w-4 h-4 flex-shrink-0"><use href="#icon-clock" /></svg>
              <span>ساعات استقبال الطلبات: السبت - الخميس (8 ص - 10 م) | الجمعة (1 ظ - 10 م)</span>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full sm:w-auto flex-shrink-0">
            <a href="tel:+966533553620" class="btn-primary text-sm py-3 px-5 text-center flex items-center justify-center gap-2 shadow-sm" data-loc="emergency">
              <svg class="w-4 h-4"><use href="#icon-phone" /></svg>
              <span>اتصال مباشر: 0533553620</span>
            </a>
            <a href="https://wa.me/966533553620?text=السلام عليكم، لدي عطل عاجل في المكيف في جدة وأحتاج فنياً بأقرب وقت."
              target="_blank" rel="noopener noreferrer"
              class="btn-whatsapp text-sm py-3 px-5 text-center flex items-center justify-center gap-2 shadow-sm" data-loc="emergency">
              <svg class="w-4 h-4 fill-current"><use href="#icon-whatsapp" /></svg>
              <span>واتساب بلاغات الطوارئ</span>
            </a>
          </div>

        </div>
      </div>
    </section>'''

if old_emergency in html:
    html = html.replace(old_emergency, new_emergency)
    print("Emergency section replaced successfully.")
else:
    print("WARNING: old_emergency not matched exactly.")

# 3. FIX FOOTER & REMOVE REDUNDANT BARE GREY STRIP
import re
footer_section_regex = r'<!-- 17\. COMPANY DATA.*?<!-- 18\. FOOTER -->\s*<footer id="siteFooter".*?</footer>'

new_footer = '''    <!-- 17. FOOTER -->
  <footer id="siteFooter" class="bg-brand-navy text-slate-300 pt-16 pb-12 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-10 pb-12 border-b border-slate-800 text-right">

        <!-- Col 1: About Air Cool -->
        <div>
          <div class="inline-block bg-white p-2 rounded-xl shadow-sm mb-4">
            <img src="/assets/images/logo.webp" alt="إير كول" width="147" height="99" class="h-9 w-auto object-contain">
          </div>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed mb-6">
            إير كول شركة متخصصة في صيانة، غسيل، فك وتركيب، شحن فريون، وتمديد نحاس المكيفات في جدة. فنيون مؤهلون وتشخيص دقيق مع توضيح التكلفة قبل بدء العمل.
          </p>
          <div class="flex items-center gap-3">
            <a href="https://wa.me/966533553620" target="_blank" rel="noopener noreferrer"
              class="w-10 h-10 rounded-xl bg-slate-800 hover:bg-brand-whatsapp text-white flex items-center justify-center transition-colors"
              aria-label="واتساب إير كول" data-loc="footer">
              <svg class="w-5 h-5 fill-current"><use href="#icon-whatsapp" /></svg>
            </a>
            <a href="tel:+966533553620"
              class="w-10 h-10 rounded-xl bg-slate-800 hover:bg-brand-blue text-white flex items-center justify-center transition-colors"
              aria-label="اتصال هاتفي" data-loc="footer">
              <svg class="w-5 h-5"><use href="#icon-phone" /></svg>
            </a>
          </div>
        </div>

        <!-- Col 2: Site Quick Links -->
        <div>
          <p class="text-white font-bold text-base mb-4 border-r-2 border-brand-cyan pr-3">روابط الموقع</p>
          <ul class="space-y-2.5 text-xs sm:text-sm text-slate-400">
            <li><a href="/" class="hover:text-brand-cyan transition-colors">الرئيسية</a></li>
            <li><a href="/services/" class="hover:text-brand-cyan transition-colors">خدماتنا</a></li>
            <li><a href="#pricing-guide" class="hover:text-brand-cyan transition-colors">الأسعار</a></li>
            <li><a href="#districts-coverage" class="hover:text-brand-cyan transition-colors">أحياء جدة</a></li>
            <li><a href="/about/" class="hover:text-brand-cyan transition-colors">من نحن</a></li>
            <li><a href="/blog/" class="hover:text-brand-cyan transition-colors">المدونة والنصائح</a></li>
            <li><a href="/privacy/" class="hover:text-brand-cyan transition-colors">سياسة الخصوصية</a></li>
            <li><a href="/contact/" class="hover:text-brand-cyan transition-colors">تواصل معنا</a></li>
          </ul>
        </div>

        <!-- Col 3: The 6 Services -->
        <div>
          <p class="text-white font-bold text-base mb-4 border-r-2 border-brand-cyan pr-3">خدمات المكيفات بجدة</p>
          <ul class="space-y-2.5 text-xs sm:text-sm text-slate-400">
            <li><a href="/ac-installation-jeddah/" class="hover:text-brand-cyan transition-colors">فك وتركيب مكيفات بجدة</a></li>
            <li><a href="/ac-maintenance-jeddah/" class="hover:text-brand-cyan transition-colors">صيانة مكيفات بجدة</a></li>
            <li><a href="/ac-cleaning-jeddah/" class="hover:text-brand-cyan transition-colors">تنظيف وغسيل مكيفات بجدة</a></li>
            <li><a href="/ac-sanitization-jeddah/" class="hover:text-brand-cyan transition-colors">تعقيم مكيفات بجدة</a></li>
            <li><a href="/ac-gas-refilling-jeddah/" class="hover:text-brand-cyan transition-colors">شحن فريون وفحص تسريب بجدة</a></li>
            <li><a href="/ac-copper-piping-jeddah/" class="hover:text-brand-cyan transition-colors">تمديد نحاس المكيفات بجدة</a></li>
            <li><a href="/blog/choosing-ac-company-jeddah/" class="hover:text-brand-cyan transition-colors">دليل اختيار شركة مكيفات</a></li>
          </ul>
        </div>

        <!-- Col 4: Contact & Districts -->
        <div>
          <p class="text-white font-bold text-base mb-4 border-r-2 border-brand-cyan pr-3">معلومات التواصل</p>
          <ul class="space-y-3.5 text-xs sm:text-sm text-slate-400">
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-brand-cyan flex-shrink-0 mt-0.5"><use href="#icon-phone" /></svg>
              <div>
                <a href="tel:+966533553620" class="hover:text-white font-bold text-slate-200" dir="ltr" data-loc="footer">+966 53 355 3620</a>
                <p class="text-xs text-slate-500 mt-0.5">اتصال مباشر أو واتساب</p>
              </div>
            </li>
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-brand-cyan flex-shrink-0 mt-0.5"><use href="#icon-pin" /></svg>
              <div>
                <p class="font-bold text-slate-200">نخدم جميع أحياء جدة</p>
                <p class="text-xs text-slate-500 mt-0.5">شمال، وسط، جنوب وشرق جدة</p>
              </div>
            </li>
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-brand-cyan flex-shrink-0 mt-0.5"><use href="#icon-clock" /></svg>
              <div>
                <p class="text-slate-200 font-bold">السبت - الخميس: 8 ص - 10 م</p>
                <p class="text-xs text-slate-500 mt-0.5">الجمعة: 1 ظهراً - 10 مساءً</p>
              </div>
            </li>
          </ul>
        </div>

      </div>

      <!-- Copyright -->
      <div class="pt-8 text-center text-xs text-slate-500">
        <p>© 2026 إير كول - خدمات التكييف والتبريد بجدة. جميع الحقوق محفوظة.</p>
      </div>

    </div>
  </footer>'''

html = re.sub(footer_section_regex, new_footer, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully.")

