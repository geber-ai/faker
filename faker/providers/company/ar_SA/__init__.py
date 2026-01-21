from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        "{{company_prefix}} {{company_domain}} {{company_suffix}}",
        "{{company_prefix}} {{last_name}} {{company_suffix}}",
    )

    company_prefixes = (
        "أكاديمية",
        "شركة",
        "عيادات",
        "مؤسسة",
        "متجر",
        "مجموعة",
        "مخابز",
        "مدارس",
        "مركز",
        "مستشفى",
        "مصنع",
        "مقاهي",
        "مكتب",
        "منصة",
    )

    company_domains = (
    "الأغذية",
    "الاتصالات",
    "الاستثمار",
    "الاستشارات",
    "البتروكيماويات",
    "التجارة الإلكترونية",
    "التسويق",
    "التطوير العقاري",
    "التعليم",
    "التقنية",
    "التمويل",
    "الحلول الرقمية",
    "الخدمات اللوجستية",
    "الرعاية الصحية",
    "السياحة",
    "النقل",
    "الأمن السيبراني",
    "التجزئة",
    "الطاقة",
  )
    company_suffixes = (
        "السعودية",
        "القابضة",
        "العالمية",
        "الحديثة",
        "المتكاملة",
        "العربية",
        "المتميزة",
        "الذكية",
        "المتقدمة",
        "الخليجية",
    )
    def company_prefix(self) -> str:
        return self.random_element(self.company_prefixes)
    
    def company_domain(self) -> str:
        return self.random_element(self.company_domains)
