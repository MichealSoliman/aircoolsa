# -*- coding: utf-8 -*-
import json

faq_items = [
    {
        "q": "ما هي الخدمات التي تقدمها شركة إير كول للمكيفات بجدة؟",
        "a": "نقدم ست خدمات متكاملة للمكيفات في جدة: فك وتركيب المكيفات، صيانة الأعطال الميكانيكية والكهربائية، غسيل وتنظيف الوحدات بمضخات الضغط مع أغطية عزل لحماية الأثاث، تعقيم مجاري الهواء بمواد مخصصة للمكيفات، فحص كشف التسريب وشحن الفريون، وتمديد مواسير النحاس المعزولة."
    },
    {
        "q": "كيف أطلب صيانة مكيف في جدة؟",
        "a": "يمكنك طلب الخدمة مباشرة بالاتصال على رقم 0533553620 أو مراسلتنا عبر واتساب، أو تسجيل بياناتك في نموذج طلب الخدمة بالصفحة لتحديد الموعد المناسب لزيارة الفني."
    },
    {
        "q": "متى يحتاج المكيف إلى الغسيل والتنظيف في جدة؟",
        "a": "يحتاج المكيف للغسيل المتخصص عند ضعف تدفق الهواء، أو انبعاث روائح رطوبة، أو تساقط مياه داخل الغرفة، أو بمرور 4 إلى 6 أشهر على آخر تنظيف نظراً لطبيعة مناخ جدة الساحلي وارتفاع الرطوبة والأتربة."
    },
    {
        "q": "ما هي علامات نقص الفريون ولماذا ينقص؟",
        "a": "أهم العلامات: خروج هواء فاتر لا يبرد، وتكون ثلج على ماسورة النحاس الخارجية، وعمل الضاغط دون توقف. الفريون لا ينقص ذاتياً في الدورة المغلقة إلا في حال وجود تسريب؛ لذلك يقوم فني إير كول بفحص التسريب أولاً قبل تعبئة الغاز المناسب لجهازك."
    },
    {
        "q": "هل يمكن فك المكيف ونقله دون فقدان غاز الفريون؟",
        "a": "نعم، يقوم فني إير كول بإجراء عملية حبس الفريون (Pump Down) داخل وحدة الكمبروسر الخارجية قبل فك المواسير، مما يحافظ على كامل وسيط التبريد ويوفر تكلفة إعادة التعبئة."
    },
    {
        "q": "كم تكلفة صيانة وتنظيف المكيفات في أحياء جدة؟",
        "a": "تبدأ أسعار الغسيل من 100 ريال لمكيف السبليت، وتبدأ رسوم كشف وتشخيص العطل من 100 ريال، وشحن الفريون يبدأ من 150 ريال، وفك وتركيب السبليت يبدأ من 180 ريال. نعرض عليك التكلفة قبل بدء العمل دون مفاجآت."
    },
    {
        "q": "ما هي ماركات وأنواع المكيفات التي تخدمونها في جدة؟",
        "a": "نصون ماركات المكيفات الشائعة في السعودية مثل: جري (Gree)، دايكن (Daikin)، إل جي (LG)، كارير (Carrier)، ميديا (Midea)، ميتسوبيشي (Mitsubishi)، أو جنرال (O General)، يورك (York)، الزامل (Zamil)، وسامسونج (Samsung)، لمكيفات السبليت والمخفي الكونسيلد والكاسيت والمركزي."
    },
    {
        "q": "هل تقدم شركة إير كول ضماناً على قطع الغيار وأعمال الصيانة؟",
        "a": "نعم، نركب قطع غيار مطابقة للمواصفات ونقدم ضماناً مكتوباً على العمل والقطع المستبدلة، مع التزام تام بإعادة المعاينة في حال تكرر نفس العطل خلال فترة الضمان."
    },
    {
        "q": "هل تعملون في حيي السكني بجدة؟",
        "a": "نعم، تغطي إير كول كافة مناطق وأحياء جدة في الشمال والوسط والجنوب والشرق، بما فيها الحمدانية، أبحر، الروضة، الصفا، السلامة، الشاطئ، البلد، الفيحاء، وباقي الأحياء. يمكنك التواصل معنا لتحديد موعد زيارة الفني."
    }
]

hvac_business_schema = {
    "@context": "https://schema.org",
    "@type": "HVACBusiness",
    "@id": "https://aircoolsa.com/#business",
    "name": "إير كول",
    "alternateName": "Air Cool",
    "url": "https://aircoolsa.com/",
    "logo": "https://aircoolsa.com/assets/images/logo.webp",
    "image": "https://aircoolsa.com/assets/images/hero-ac-jeddah.jpg",
    "telephone": "+966533553620",
    "priceRange": "$$",
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "جدة",
        "addressRegion": "منطقة مكة المكرمة",
        "addressCountry": "SA"
    },
    "areaServed": {
        "@type": "City",
        "name": "جدة"
    },
    "openingHoursSpecification": [
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
            "opens": "08:00",
            "closes": "22:00"
        },
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": "Friday",
            "opens": "13:00",
            "closes": "22:00"
        }
    ],
    "sameAs": [],
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "خدمات المكيفات بجدة",
        "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "فك وتركيب مكيفات بجدة"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "صيانة مكيفات بجدة"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "تنظيف وغسيل مكيفات بجدة"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "تعقيم مكيفات بجدة"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "شحن فريون وفحص تسريب بجدة"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "تمديد نحاس المكيفات بجدة"}}
        ]
    }
}

website_schema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": "https://aircoolsa.com/#website",
    "url": "https://aircoolsa.com/",
    "name": "إير كول",
    "inLanguage": "ar",
    "publisher": {
        "@id": "https://aircoolsa.com/#business"
    }
}

faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["a"]
            }
        } for item in faq_items
    ]
}

print("Schema prepared successfully.")

