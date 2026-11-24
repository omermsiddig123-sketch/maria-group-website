"""Generate the three language editions with Python 3, without dependencies."""
import json
from html import escape
from pathlib import Path
from posixpath import relpath
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
PAGES = json.loads((ROOT / "site/content.json").read_text(encoding="utf-8"))
LANGS = ("ar", "en", "zh")
LABELS = ("العربية", "English", "简体中文")
NAME = ("ماريا قروب المحدودة", "Maria Group Co. Ltd.", "玛丽亚集团")
NAV = {"about": {"about", "companies"}, "sectors": {"sectors", "industry", "trade"},
       "brands": {"brands", "rhino", "sila", "al-afaf"}, "products": {"products", "food", "metal"},
       "partnerships": {"partnerships", "contact"}}
HOME = ("الرئيسية", "Home", "首页")
DETAIL = ("استكشف", "Explore", "查看详情")
HERO = ("الصناعة والتجارة الدولية", "Industry and international trade", "工业与国际贸易")
HERO_TEXT = (
    "مجموعة أعمال سودانية تجمع بين الأنشطة الصناعية والاستيراد والتصدير والتوريد للأسواق المحلية والدولية.",
    "A Sudanese business group spanning industrial activities, imports, exports and sourcing for local and international markets.",
    "一家业务涵盖工业、进口、出口及采购的苏丹企业集团，面向本地及国际市场。",
)
BUSINESS = ("مجالات أعمالنا", "Our businesses", "集团业务")
HOME_ABOUT = (
    "مجموعة أعمال سودانية تعمل في الصناعة والتجارة الدولية، وتشمل أعمالها في السودان شركة ماريا للأنشطة المتعددة المحدودة.",
    "A Sudanese business group spanning industry and international trade, with Maria Multi Activities Co. Ltd. among its businesses in Sudan.",
    "玛丽亚集团是一家业务涵盖工业与国际贸易的苏丹企业集团，在苏丹的业务包括 Maria Multi Activities Co. Ltd.。",
)
ART_LABELS = (
    ("الصناعة", "التجارة الدولية"),
    ("Industry", "International trade"),
    ("工业", "国际贸易"),
)
MENU = ("القائمة", "Menu", "菜单")
SKIP = ("انتقل إلى المحتوى", "Skip to content", "跳转至内容")
RELATED = ("استكشف المزيد", "Explore further", "继续浏览")
DOCS = ("طلب مستندات الشركة", "Request company documents", "索取企业资料")
EMAIL_HINT = ("يفتح الزر مسودة في تطبيق البريد.", "This button opens a draft in your email app.", "此按钮会在邮件应用中打开邮件草稿。")
ENQUIRIES = ("الاستفسارات", "Enquiries", "业务咨询")
RODEENA = ("رودينا (RODEENA)", "RODEENA", "RODEENA")
RODEENA_PROFILE = (
    "شركة تجارة دولية تأسست عام 2019 ومقرها مدينة الشارقة للإعلام، الإمارات العربية المتحدة. تعمل في استيراد المواد الخام والمعدات الصناعية وتصدير المحاصيل الزراعية، وتتعاون تجارياً مع ماريا قروب مع احتفاظ كل شركة بكيانها القانوني المستقل.",
    "An international trading company established in 2019 and based in Sharjah Media City, United Arab Emirates. It imports raw materials and industrial equipment and exports agricultural crops. RODEENA and Maria Group collaborate commercially and remain legally independent.",
    "RODEENA 成立于 2019 年，总部位于阿联酋沙迦媒体城，从事原材料和工业设备进口以及农产品出口。RODEENA 与玛丽亚集团开展商业合作，双方各自保有独立的法律主体地位。",
)
MARIA_MULTI = ("شركة ماريا للأنشطة المتعددة المحدودة", "Maria Multi Activities Co. Ltd.", "Maria Multi Activities Co. Ltd.")
RODEENA_COMPANIES = (
    (("رودينا الإمارات", "RODEENA UAE", "RODEENA 阿联酋"), ("المركز الرئيسي لتنسيق العمليات التجارية الدولية.", "Head office for coordinating international trade operations.", "负责协调国际贸易业务的总部。")),
    (("رودينا تنزانيا", "RODEENA Tanzania", "RODEENA 坦桑尼亚"), ("شركة مستقلة تعمل في الاستيراد والتصدير.", "An independent import and export company.", "从事进出口业务的独立公司。")),
)
INDUSTRIES = ("مصانع راينو وأنشطتها", "RHINO manufacturing", "RHINO 制造业务")
EXPORT_PRODUCTS = ("منتجات التصدير", "Export products", "出口产品")
COMPANY_LINK = ("عرض شركات المجموعة", "View group companies", "查看集团企业")
STATUS_ACTIVE = ("قيد التشغيل", "Operational", "已投产")
STATUS_SOON = ("قريباً", "Coming soon", "即将推出")
FACTORY_IMAGES = {
    "oil": ("rhino-oil-illustration.jpg", ("رسم توضيحي لإنتاج زيوت الطعام", "Edible oil production illustration", "食用油生产示意图")),
    "iron": ("rhino-iron-illustration.jpg", ("رسم توضيحي لتشكيل الحديد", "Steel forming illustration", "钢材成型示意图")),
    "biscuits": ("spider-biscuits-illustration.webp", ("تصميم توضيحي لبسكويت SPIDER", "SPIDER biscuit concept illustration", "SPIDER 饼干概念示意图")),
}
ILLUSTRATION = ("صورة توضيحية", "Illustrative image", "示意图")
FACTORY_STATUS = dict.fromkeys(("oil", "iron", "biscuits"), STATUS_ACTIVE)
FACTORY_STATUS.update(dict.fromkeys(("beverages", "tomato"), STATUS_SOON))

QR_HINT = ("امسح الرمز في WeChat، أو افتح الصورة واحفظها للمسح من ألبوم هاتفك.",
           "Scan in WeChat, or open and save the image to scan from your phone’s photo album.",
           "请使用微信扫码，或打开并保存图片后从手机相册识别。")
QR_LINK = ("فتح صورة الرمز", "Open QR image", "打开二维码图片")
OFFICES = (
    ("مكاتب شركة ماريا للأنشطة المتعددة المحدودة", "بورتسودان، حي الأغاريق، جوار بنك أفريقيا والخليج، السودان", "أم درمان، حي العمدة، مقابل بنك البركة، السودان"),
    ("Maria Multi Activities Co. Ltd. offices", "Al Aghareeq District, beside the Bank of Africa and Gulf, Port Sudan, Sudan", "Al Omda District, opposite Al Baraka Bank, Omdurman, Sudan"),
    ("Maria Multi Activities Co. Ltd. 办公地点", "苏丹港阿加里格区，非洲及海湾银行旁，苏丹", "恩图曼阿尔欧姆达区，巴拉卡银行对面，苏丹"),
)
EMAIL_WHATSAPP = ("البريد الإلكتروني وواتساب", "Email & WhatsApp", "电子邮件与 WhatsApp")
DOCUMENT_FIELDS = (
    "الشركة الطالبة:\nالمستند المطلوب:\nالغرض:\nبيانات التواصل:",
    "Requesting company:\nDocument required:\nPurpose:\nReply contact:",
    "申请公司：\n所需资料：\n用途：\n联系方式：",
)

SITE_ORIGIN = "https://maria-group-official-2026.onrender.com"
SPECIFICATIONS = (
    ("المواصفات والمقاسات", "العنصر", "المتوفر"),
    ("Specifications and sizes", "Item", "Available"),
    ("规格与尺寸", "项目", "供应规格"),
)
OIL_SPECS = (
    (("العلامات التجارية", "Brands", "品牌"), ("حور، جودي، أبو حمزة، راينو", "Hoor, Joudi, Abu Hamza, RHINO", "Hoor、Joudi、Abu Hamza、RHINO")),
    (("سعات العبوات لكل علامة", "Pack sizes for each brand", "各品牌包装容量"), ("4.5 و9 و18 لتر", "4.5, 9 and 18 litres", "4.5 升、9 升和 18 升")),
)
SHEET_SPECS = (
    (("زنك أمريكي", "American-style roofing sheets", "美式镀锌屋面板"), ("طول 4 أو 6 متر، عرض 1.20 متر", "4 or 6 m long, 1.20 m wide", "长 4 或 6 米，宽 1.20 米")),
    (("زنك بلدي", "Local-style roofing sheets", "本地式镀锌屋面板"), ("طول 16 أو 20 قدم، عرض 80 سم", "16 or 20 ft long, 80 cm wide", "长 16 或 20 英尺，宽 80 厘米")),
)
TUBE_SPECS = (
    (("مواسير مربعة ودائرية", "Square and round tubes", "方管和圆管"), ("جميع المقاسات. حدّد المقاس والسماكة المطلوبة عند التواصل.", "All sizes. Specify the dimensions and wall thickness when contacting us.", "供应各类尺寸。联系时请注明所需尺寸及壁厚。")),
)
PRODUCT_SPECS = {
    "oil": OIL_SPECS, "iron": SHEET_SPECS + TUBE_SPECS,
    "zinc": SHEET_SPECS, "pipes": TUBE_SPECS,
}

def public_url(lang, page):
    return SITE_ORIGIN + "/" + path_to(lang, page).removesuffix("index.html")

def path_to(lang, page):
    return "/".join([part for part in ("" if lang == "ar" else lang, page, "index.html") if part])

def render(i, page):
    lang = LANGS[i]
    location = Path(path_to(lang, page))
    folder = location.parent.as_posix()

    def url(target, language=lang):
        return relpath(path_to(language, target), folder)

    def asset(name):
        return relpath(f"assets/{name}", folder)

    def link(target, label, style="", current=False):
        active = ' aria-current="page"' if current else ""
        return f'<a class="{style}" href="{url(target)}"{active}>{escape(label)}</a>'

    def logo(filename, label, style):
        return f'<img class="{style}" src="{asset(filename)}" alt="{escape(label)}">'

    def card(key, summary=False):
        entry = PAGES[key]
        emblem = logo(f"maria-image-{entry[7]}.webp", "", "card-image") if len(entry) > 7 else ""
        summary_text = f'<p>{escape(entry[3+i])}</p>' if summary else ""
        photo = ""
        if key in FACTORY_IMAGES:
            filename, labels = FACTORY_IMAGES[key]
            photo = f'<img class="factory-photo factory-photo-{key}" src="{asset(filename)}" alt="{escape(labels[i])}" loading="lazy" decoding="async">'
            emblem = ""
            photo += f'<small class="photo-caption">{ILLUSTRATION[i]}</small>'
        status = FACTORY_STATUS.get(key)
        status_text = f'<small class="factory-status">{status[i]}</small>' if status else ""
        return f'<a class="card" href="{url(key)}">{photo}{emblem}{status_text}<h3>{escape(entry[i])}</h3>{summary_text}<span>{DETAIL[i]}</span></a>'

    def sector_panel(key, label):
        entry = PAGES[key]
        return f"""<a class="sector-panel sector-{key}" href="{url(key)}">
<div class="sector-art" aria-hidden="true"></div><div class="sector-copy">
<h3>{label}</h3><p>{escape(entry[3+i])}</p><span>{DETAIL[i]}</span></div></a>"""

    def cards(keys, summary=False):
        return '<div class="cards">' + "".join(card(key, summary) for key in keys) + "</div>"

    def company_groups():
        rodeena_companies = "".join(
            f'<article class="company-card"><h4>{name[i]}</h4><p>{description[i]}</p></article>'
            for name, description in RODEENA_COMPANIES
        )
        factory_cards = cards(PAGES["industry"][6].split())
        return f"""<div class="company-groups">
<section class="company-group" aria-labelledby="maria-company">
<h3 id="maria-company">{MARIA_MULTI[i]}</h3><p>{escape(PAGES['companies'][3+i])}</p>
<h4 class="company-subheading">{INDUSTRIES[i]}</h4>{factory_cards}
</section>
<section class="company-group" aria-labelledby="rodeena-company">
<h3 id="rodeena-company">{RODEENA[i]}</h3><p>{RODEENA_PROFILE[i]}</p>
<div class="company-cards">{rodeena_companies}</div>
</section>
</div>"""

    def document_request():
        subject = quote(NAME[i] + " | " + DOCS[i])
        body = quote(DOCUMENT_FIELDS[i].replace("\n", "\r\n"))
        href = f"mailto:info@maria.sd?subject={subject}&amp;body={body}"
        return (f'<div class="actions"><a class="button primary" href="{href}">{DOCS[i]}</a></div>'
                f'<p class="note">{EMAIL_HINT[i]}</p>')

    footer_name = '<span dir="ltr" lang="en">Maria Group Co. Ltd.</span>' if lang != "en" else ""
    langs = "".join(f'<a href="{url(page, target)}" lang="{target if target != "zh" else "zh-Hans"}"'
                    + (' aria-current="page"' if target == lang else "") + f'>{label}</a>'
                    for target, label in zip(LANGS, LABELS))
    nav = "".join(link(key, PAGES[key][i], "is-active" if page in group else "", page == key)
                  for key, group in NAV.items())
    contact_link = link("contact", PAGES["contact"][i], "button primary", page == "contact")
    header = f'''<a class="skip" href="#content">{SKIP[i]}</a>
<header class="header"><div class="frame header-inner">
<a class="brand" href="{url('')}" aria-label="{HOME[i]}">{logo('maria-header-web.webp', NAME[i], 'header-logo')}</a>
<nav class="desktop-nav" aria-label="{MENU[i]}">{nav}</nav>
<details class="mobile-nav"><summary>{MENU[i]}</summary><nav aria-label="{MENU[i]}">{nav}{contact_link}</nav></details>
<div class="header-actions"><div class="languages">{langs}</div>{contact_link}</div>
</div></header>'''

    if not page:
        title, description = NAME[i], HERO_TEXT[i]
        body = f'''<section class="hero"><div class="frame hero-inner">
<div class="hero-copy"><p class="eyebrow">{NAME[i]}</p><h1>{HERO[i]}</h1><p class="lead">{description}</p>
<div class="actions">{link('sectors', PAGES['sectors'][i], 'button light')}{link('partnerships', PAGES['partnerships'][i], 'button ghost')}</div></div>
<div class="hero-art" aria-hidden="true"><div class="art-grid"></div><div class="art-beams"><i></i><i></i><i></i><i></i></div>
<div class="art-orbit"><i></i><i></i><i></i></div><div class="art-route"><i></i><i></i><i></i></div></div>
</div></section>
<section class="frame home-intro" aria-labelledby="intro-title">
<div><h2 id="intro-title">{PAGES['about'][i]}</h2><p>{HOME_ABOUT[i]}</p></div>
<div class="intro-links">{link('about', PAGES['about'][i], 'text-link')}{link('companies', PAGES['companies'][i], 'text-link')}</div>
</section>
<section class="home-sectors" aria-labelledby="sectors-title"><div class="frame">
<h2 id="sectors-title">{BUSINESS[i]}</h2>
<div class="sector-panels">{sector_panel('industry', ART_LABELS[i][0])}{sector_panel('trade', ART_LABELS[i][1])}</div>
</div></section>
<section class="frame section" aria-labelledby="companies-title"><h2 id="companies-title">{PAGES['companies'][i]}</h2>
{company_groups()}
<p class="section-link">{link('companies', COMPANY_LINK[i], 'text-link')}</p></section>
<section class="home-sectors" aria-labelledby="export-title"><div class="frame">
<h2 id="export-title">{EXPORT_PRODUCTS[i]}</h2>{cards(('sesame', 'groundnuts'))}
<p class="section-link">{link('exports', PAGES['exports'][i], 'text-link')}</p></div></section>
<section class="frame section home-brands" aria-labelledby="brands-title"><h2 id="brands-title">{PAGES['brands'][i]}</h2>
<div class="brand-grid">{''.join(link(key, label, 'brand-tile') for key, label in (('rhino', 'RHINO'), ('sila', 'SILA'), ('al-afaf', 'AL AFAF')))}</div></section>
<section class="home-partnership"><div class="frame partnership-inner"><div>
<h2>{PAGES['partnerships'][i]}</h2><p>{PAGES['partnerships'][3+i]}</p></div>
<div class="actions">{link('partnerships', PAGES['partnerships'][i], 'button ghost')}{link('contact', PAGES['contact'][i], 'button light')}</div>
</div></section>'''
    else:
        entry = PAGES[page]
        title, description = entry[i], entry[3+i]
        emblem = logo(f"maria-image-{entry[7]}.webp", title, "page-image") if len(entry) > 7 else ""
        body = f'''<section class="page-hero"><div class="frame">
<div class="crumb">{link('', HOME[i])}<span aria-hidden="true">/</span><span>{escape(title)}</span></div>
<div class="page-heading"><div><h1>{escape(title)}</h1><p class="lead">{escape(description)}</p></div>{emblem}</div>
</div></section>'''
        if page in PRODUCT_SPECS:
            spec_title, item_label, sizes_label = SPECIFICATIONS[i]
            rows = "".join(f'<tr><th scope="row">{item[i]}</th><td>{sizes[i]}</td></tr>'
                           for item, sizes in PRODUCT_SPECS[page])
            body += f"""<section class="frame section" aria-labelledby="product-specs">
<h2 id="product-specs">{spec_title}</h2>
<table class="product-specs"><thead><tr><th scope="col">{item_label}</th><th scope="col">{sizes_label}</th></tr></thead>
<tbody>{rows}</tbody></table></section>"""
            if page == "iron":
                body += f'<section class="frame section"><h2>{RELATED[i]}</h2>{cards(("zinc", "pipes", "metal"))}</section>'
        if page == "companies":
            body += f'<div class="frame section">{company_groups()}</div>'
        if page == "exports":
            body += f'<section class="frame section"><h2>{EXPORT_PRODUCTS[i]}</h2>{cards(("sesame", "groundnuts"), True)}<p class="section-link">{link("contact", PAGES["contact"][i], "button primary")}</p></section>'
        keys = entry[6].split()
        if keys and page not in {"companies", "exports", "iron"}:
            body += f'<section class="frame section"><h2>{RELATED[i]}</h2>{cards(keys, page in {"sectors", "industry", "brands", "trade"})}</section>'
        if page in {"partnerships", "contact"}:
            body += f'<section class="frame section enquiry"><h2>{ENQUIRIES[i]}</h2>{document_request()}</section>'
        if page == "contact":
            body += f'''<section class="frame section contact-methods">
<div class="contact-card"><h2>{escape(EMAIL_WHATSAPP[i])}</h2><a dir="ltr" href="mailto:info@maria.sd">info@maria.sd</a>
<a dir="ltr" href="https://wa.me/249912336204">WhatsApp +249 912336204</a><a dir="ltr" href="tel:+249912500211">+249 912500211</a></div>
<div class="contact-card"><h2>WeChat</h2><a dir="ltr" href="#wechat-qr">+249 912500211</a><p>{QR_HINT[i]}</p>
<a class="qr-link" id="wechat-qr" href="{asset('wechat-contact-qr.jpg')}">{logo('wechat-contact-qr.jpg', QR_LINK[i], 'qr')}<span>{QR_LINK[i]}</span></a></div>
<div class="contact-card"><h2>{OFFICES[i][0]}</h2><p>{OFFICES[i][1]}</p><p>{OFFICES[i][2]}</p></div></section>'''
    footer = f'''<footer><div class="frame footer-inner"><div><strong>{NAME[i]}</strong>
{footer_name}</div><nav aria-label="{MENU[i]}">
{link('about',PAGES['about'][i])}{link('companies',PAGES['companies'][i])}{link('contact',PAGES['contact'][i])}</nav></div></footer>'''
    html_lang = "zh-Hans" if lang == "zh" else lang
    heading = f"{title} | {NAME[i]}" if page else title
    alternates = "\n".join(f'<link rel="alternate" hreflang="{target if target != "zh" else "zh-Hans"}" href="{public_url(target, page)}">' for target in LANGS)
    return location, f'''<!doctype html>
<html lang="{html_lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(description)}">
<title>{escape(heading)}</title>
<link rel="icon" href="{asset('favicon.png')}">
<link rel="stylesheet" href="{asset('corporate.css')}">
<link rel="canonical" href="{public_url(lang, page)}">
{alternates}
</head>
<body>{header}
<main id="content" tabindex="-1">{body}</main>
{footer}
</body>
</html>
'''

if __name__ == "__main__":
    for language_index in range(len(LANGS)):
        for slug in ("", *PAGES):
            path, document = render(language_index, slug)
            destination = ROOT / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(document, encoding="utf-8")

    from xml.etree import ElementTree as ET

    sitemap = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for language in LANGS:
        for slug in ("", *PAGES):
            entry = ET.SubElement(sitemap, "url")
            ET.SubElement(entry, "loc").text = public_url(language, slug)
    ET.indent(sitemap)
    ET.ElementTree(sitemap).write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
