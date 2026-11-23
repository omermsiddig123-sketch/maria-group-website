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
MENU = ("القائمة", "Menu", "菜单")
SKIP = ("انتقل إلى المحتوى", "Skip to content", "跳转至内容")
RELATED = ("استكشف المزيد", "Explore further", "继续浏览")
BUYER = ("طلب عرض سعر", "Request a quotation", "申请报价")
SUPPLIER = ("تقديم عرض توريد", "Submit a supplier proposal", "提交供货方案")
DOCS = ("طلب مستندات الشركة", "Request company documents", "索取企业资料")
EMAIL_HINT = ("تفتح الروابط مسودة في تطبيق البريد.", "These links open a draft in your email app.", "这些链接会在邮件应用中打开邮件草稿。")
QR_HINT = ("امسح الرمز في WeChat، أو افتح الصورة واحفظها للمسح من ألبوم هاتفك.",
           "Scan in WeChat, or open and save the image to scan from your phone’s photo album.",
           "请使用微信扫码，或打开并保存图片后从手机相册识别。")
QR_LINK = ("فتح صورة الرمز", "Open QR image", "打开二维码图片")
OFFICES = (
    ("مكاتب شركة ماريا للأنشطة المتعددة المحدودة", "بورتسودان، حي الأغاريق، جوار بنك أفريقيا والخليج، السودان", "أم درمان، حي العمدة، مقابل بنك البركة، السودان"),
    ("Maria Multi Activities Co. Ltd. offices", "Al Aghareeq District, beside the Bank of Africa and Gulf, Port Sudan, Sudan", "Al Omda District, opposite Al Baraka Bank, Omdurman, Sudan"),
    ("Maria Multi Activities Co. Ltd. 办公地点", "苏丹港阿加里格区，非洲及海湾银行旁，苏丹", "恩图曼阿尔欧姆达区，巴拉卡银行对面，苏丹"),
)
SUBJECT_FIELDS = (
    "Company:\nProduct / specifications:\nQuantity / packaging:\nDestination / delivery terms:\nReply contact:",
    "Company:\nProduct / country of origin:\nSpecifications / packing:\nQuantity / lead time:\nReply contact:",
    "Requesting company:\nDocument required:\nPurpose:\nReply contact:",
)

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
        return f'<a class="card" href="{url(key)}">{emblem}<h3>{escape(entry[i])}</h3>{summary_text}<span>{DETAIL[i]}</span></a>'

    def cards(keys, summary=False):
        return '<div class="cards">' + "".join(card(key, summary) for key in keys) + "</div>"

    def enquiry_links():
        topics = (BUYER, SUPPLIER, DOCS)
        subjects = ("Quotation request", "Supplier proposal", "Company documents enquiry")
        buttons = []
        for j, (labels, subject, body) in enumerate(zip(topics, subjects, SUBJECT_FIELDS)):
            href = f"mailto:info@maria.sd?subject={quote('Maria Group | ' + subject)}&amp;body={quote(body)}"
            buttons.append(f'<a class="button {"primary" if j == 0 else "outline"}" href="{href}">{labels[i]}</a>')
        return '<div class="actions">' + "".join(buttons) + f'</div><p class="note">{EMAIL_HINT[i]}</p>'

    langs = "".join(f'<a href="{url(page, target)}" lang="{target if target != "zh" else "zh-Hans"}"'
                    + (' aria-current="page"' if target == lang else "") + f'>{label}</a>'
                    for target, label in zip(LANGS, LABELS))
    nav = "".join(link(key, PAGES[key][i], "is-active" if page in group else "", page == key)
                  for key, group in NAV.items())
    contact_link = link("contact", PAGES["contact"][i], "button primary", page == "contact")
    header = f'''<a class="skip" href="#content">{SKIP[i]}</a>
<header class="header"><div class="frame header-inner">
<a class="brand" href="{url('')}" aria-label="{HOME[i]}">{logo('maria-group-official-header.png', NAME[i], 'header-logo')}</a>
<nav class="desktop-nav" aria-label="{MENU[i]}">{nav}</nav>
<div class="header-actions"><div class="languages">{langs}</div>{contact_link}</div>
<details class="mobile-nav"><summary>{MENU[i]}</summary><nav aria-label="{MENU[i]}">{nav}{contact_link}</nav></details>
</div></header>'''

    if not page:
        title, description = NAME[i], HERO_TEXT[i]
        body = f'''<section class="hero"><div class="frame hero-inner">
<div><p class="eyebrow">{NAME[i]}</p><h1>{HERO[i]}</h1><p class="lead">{description}</p>
<div class="actions">{link('sectors', PAGES['sectors'][i], 'button light')}{link('partnerships', PAGES['partnerships'][i], 'button ghost')}</div></div>
<div class="hero-art" aria-hidden="true"><div class="logo-panel">{logo('maria-group-mark.png', '', 'hero-logo')}</div></div>
</div></section>
<section class="frame section"><h2>{BUSINESS[i]}</h2>{cards(('industry','trade'), True)}</section>'''
    else:
        entry = PAGES[page]
        title, description = entry[i], entry[3+i]
        emblem = logo(f"maria-image-{entry[7]}.webp", title, "page-image") if len(entry) > 7 else ""
        body = f'''<section class="page-hero"><div class="frame">
<div class="crumb">{link('', HOME[i])}<span aria-hidden="true">/</span><span>{escape(title)}</span></div>
<div class="page-heading"><div><h1>{escape(title)}</h1><p class="lead">{escape(description)}</p></div>{emblem}</div>
</div></section>'''
        keys = entry[6].split()
        if keys:
            body += f'<section class="frame section"><h2>{RELATED[i]}</h2>{cards(keys, page in {"sectors", "industry", "brands", "trade"})}</section>'
        if page in {"partnerships", "contact"}:
            body += f'<section class="frame section enquiry"><h2>{PAGES["contact"][i] if page == "partnerships" else BUYER[i]}</h2>{enquiry_links()}</section>'
        if page == "contact":
            body += f'''<section class="frame section contact-methods">
<div class="contact-card"><h2>Email &amp; WhatsApp</h2><a dir="ltr" href="mailto:info@maria.sd">info@maria.sd</a>
<a dir="ltr" href="https://wa.me/249912336204">WhatsApp +249 912336204</a><a dir="ltr" href="tel:+249912500211">+249 912500211</a></div>
<div class="contact-card"><h2>WeChat</h2><a dir="ltr" href="#wechat-qr">+249 912500211</a><p>{QR_HINT[i]}</p>
<a class="qr-link" id="wechat-qr" href="{asset('wechat-contact-qr.jpg')}">{logo('wechat-contact-qr.jpg', QR_LINK[i], 'qr')}<span>{QR_LINK[i]}</span></a></div>
<div class="contact-card"><h2>{OFFICES[i][0]}</h2><p>{OFFICES[i][1]}</p><p>{OFFICES[i][2]}</p></div></section>'''
    footer = f'''<footer><div class="frame footer-inner"><div><strong>{NAME[i]}</strong>
<span dir="ltr">Maria Group Co. Ltd.</span></div><nav aria-label="{MENU[i]}">
{link('about',PAGES['about'][i])}{link('companies',PAGES['companies'][i])}{link('contact',PAGES['contact'][i])}</nav></div></footer>'''
    html_lang = "zh-Hans" if lang == "zh" else lang
    heading = f"{title} | {NAME[i]}" if page else title
    alternates = "\n".join(f'<link rel="alternate" hreflang="{target if target != "zh" else "zh-Hans"}" href="{url(page,target)}">' for target in LANGS)
    return location, f'''<!doctype html>
<html lang="{html_lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="{escape(description)}">
<title>{escape(heading)}</title>
<link rel="icon" href="{asset('favicon.png')}">
<link rel="stylesheet" href="{asset('corporate.css')}">
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
