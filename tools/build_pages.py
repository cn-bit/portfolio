"""One-off builder for the case study pages.

The generated HTML files in work/ are the source of truth and can be edited
directly. This script is kept only as a record of how they were assembled.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ("https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500"
         "&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap")


def head(title, desc):
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} | Carl Navè</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title} | Carl Navè">
<meta property="og:description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="../assets/css/main.css?v=202610221816">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<div class="wrap">
  <header class="site-head">
    <a class="wordmark" href="../">Carl Navè</a>
    <nav class="site-nav" aria-label="Main">
      <a href="../#work" aria-current="page">Work</a>
      <a href="../about.html">About</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>
</div>

<main id="main">
  <div class="wrap">
'''


FOOT = '''  </div>
</main>

<footer class="site-foot" id="contact">
  <div class="wrap">
    <div class="contact">
      <h2>For senior client, commercial and customer experience roles, or a conversation about your brand.</h2>
      <ul>
        <li><span class="meta-label">Email</span><a href="mailto:cn@carlnave.com.au">cn@carlnave.com.au</a></li>
        <li><span class="meta-label">LinkedIn</span><a href="https://www.linkedin.com/in/carl-nave/" target="_blank" rel="noopener">linkedin.com/in/carl-nave</a></li>
      </ul>
    </div>
    <div class="colophon meta-label">
      <span>Carl Navè, Melbourne</span>
      <span>Agency work shown was delivered with Antimony Studio.</span>
    </div>
  </div>
</footer>
</body>
</html>
'''


def intro(name, positioning, meta):
    rows = "".join(f"      <div><dt>{k}</dt><dd>{v}</dd></div>\n" for k, v in meta)
    return f'''    <header class="cs-head">
      <a class="cs-back" href="../#work">Selected work</a>
      <h1>{name}</h1>
      <p class="thesis">{positioning}</p>
    </header>

    <dl class="cs-meta">
{rows}    </dl>

'''


def img(project, name, w, h, alt, sizes="(max-width: 600px) 50vw, 680px", lazy=True):
    b = f"../assets/img/{project}/{name}"
    lz = ' loading="lazy"' if lazy else ""
    return (f'      <img src="{b}-800.jpg" srcset="{b}-800.jpg 800w, {b}.jpg {w}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}"{lz}>\n')


def figure(cls, imgs, caption=None):
    cap = f'      <figcaption class="meta-label">{caption}</figcaption>\n' if caption else ""
    return f'    <figure class="cs-figure {cls}">\n' + "".join(imgs) + cap + "    </figure>\n\n"


def section(sid, title, paras, extra=""):
    body = "".join(f"        <p>{p}</p>\n" for p in paras)
    return f'''    <section class="cs-section" aria-labelledby="{sid}">
      <h2 id="{sid}">{title}</h2>
      <div class="body">
{body}{extra}      </div>
    </section>

'''


def credit(text):
    return f'        <p class="credit meta-label">{text}</p>\n'


def result(lines, paras, note=None, link=None):
    li = "".join(f"          <li>{l}</li>\n" for l in lines)
    out = f'        <ul class="markets" aria-label="Result">\n{li}        </ul>\n'
    out += "".join(f"        <p>{p}</p>\n" for p in paras)
    if note:
        out += f'        <p class="meta-label">{note}</p>\n'
    if link:
        out += f'        <p class="meta-label"><a href="{link[0]}" target="_blank" rel="noopener">{link[1]}</a></p>\n'
    return out


def chapter(label, title):
    return f'''    <div class="cs-chapter">
      <p class="meta-label">{label}</p>
      <h2>{title}</h2>
    </div>

'''


def nxt(href, name):
    return f'''    <nav class="cs-next" aria-label="Next project">
      <a href="{href}">
        <span class="meta-label">Next project</span>
        <span class="next-name">{name}</span>
      </a>
    </nav>
'''


WIDE = "(max-width: 1440px) 100vw, 1360px"
TILE4 = "(max-width: 600px) 50vw, 340px"


def intro2(name, disciplines, positioning, meta):
    rows = "".join(f"      <div><dt>{k}</dt><dd>{v}</dd></div>\n" for k, v in meta)
    return f'''    <header class="cs-head">
      <a class="cs-back" href="../#work">Selected work</a>
      <h1>{name}</h1>
      <p class="cs-disciplines">{disciplines}</p>
      <p class="thesis">{positioning}</p>
    </header>

    <dl class="cs-meta">
{rows}    </dl>

'''


def ps(paras, indent=8):
    pad = " " * indent
    return "".join(f"{pad}<p>{p}</p>\n" for p in paras)


def subsections(items):
    """items: list of (subheading or None, [paragraphs])"""
    out = ""
    for head_, paras in items:
        if head_:
            out += f'        <h3 class="cs-sub">{head_}</h3>\n'
        out += ps(paras)
    return out


def block(sid, title, inner, hidden=False):
    cls = ' class="visually-hidden"' if hidden else ""
    return f'''    <section class="cs-section" aria-labelledby="{sid}">
      <h2 id="{sid}"{cls}>{title}</h2>
      <div class="body">
{inner}      </div>
    </section>

'''


def services(items):
    li = "".join(f"          <li>{i}</li>\n" for i in items)
    return f'        <ul class="role-list services">\n{li}        </ul>\n'


def big(lines):
    li = "".join(f"          <li>{l}</li>\n" for l in lines)
    return f'        <ul class="markets" aria-label="Result">\n{li}        </ul>\n'


def visit(url, label):
    return f'        <p class="meta-label visit"><a href="{url}" target="_blank" rel="noopener">{label}</a></p>\n'


def rt_edgar():
    p = "rt-edgar"
    b = intro2("RT Edgar", "Brand Transformation | Customer Experience | Digital Strategy &amp; Delivery",
               "An established real estate group, reimagined for a changing market", [
                   ("Client", "RT Edgar, real estate, Melbourne"),
                   ("Engagement", "From September 2024"),
                   ("My role", "Account Director, Antimony Studio"),
               ])
    b += figure("fig-single shape-wide", [
        img(p, "sign-hanging", 2400, 1600, "A hanging RT Edgar sign in navy with the white wordmark, on a concrete building", WIDE, lazy=False)])
    b += block("context", "Business context", ps([
        "With a history dating back to 1894, RT Edgar is one of Melbourne's established real estate groups, recognised across premium residential markets.",
        "Its longstanding reputation and established client relationships were considerable assets. At the same time, a business operating across multiple offices, agents and marketing channels needed a consistent identity and digital experience that could serve both existing and future customers.",
        "Our engagement brought together brand development, customer experience, website redevelopment and integrated communications as part of a broader programme of modernisation."]))
    b += block("challenge", "The challenge", ps([
        "RT Edgar needed to evolve its brand and digital presence without losing the recognition and trust it had built over generations.",
        "The challenge extended beyond the visual identity. Customers encountered the business through a combination of property listings, search platforms, office communications, agent relationships, printed marketing and the website.",
        "These touchpoints needed to form a coherent customer experience.",
        "The work also involved multiple internal and external stakeholders, with creative, technical and operational decisions that needed to be aligned across the broader programme."]))
    b += block("approach", "Our approach", subsections([
        (None, ["Antimony Studio approached the engagement as an interconnected programme of research, brand development, digital experience and communications."]),
        ("Research &amp; customer experience", [
            "The initial work included competitor research, audience segmentation and customer journey mapping to understand the market, customer needs and opportunities to improve the experience.",
            "These insights informed strategic recommendations and helped establish priorities across the brand and digital workstreams."]),
        ("Brand identity &amp; application", [
            "The creative team refreshed RT Edgar's identity, including the RTE monogram and supporting brand elements.",
            "The refreshed identity was developed for application across customer-facing touchpoints, including property marketing, brochures, sales boards and signage."]),
        ("Website &amp; digital experience", [
            "The website programme brought together the refreshed visual identity, content, customer experience considerations and property search functionality.",
            "Delivery required coordination with the client's communications team, studio specialists and technical stakeholders, including discussions around CMS data, property search requirements and API integrations."]),
        ("Content &amp; integrated communications", [
            "The wider programme included content planning, video production oversight and the development of communications and marketing applications that supported a more consistent brand presence."]),
    ]))
    b += ('    <figure class="cs-figure fig-single">\n'
          '      <div class="panel panel-rte"><img src="../assets/img/rt-edgar/monogram-fireplace.jpg" width="578" height="722" '
          'alt="The refreshed RTE monogram, with Est 1894, over an interior with a marble fireplace" loading="lazy"></div>\n'
          '      <figcaption class="meta-label">The refreshed RTE monogram and lock-up.</figcaption>\n'
          '    </figure>\n\n')
    b += figure("fig-single shape-screen", [
        img(p, "guide-overview", 1920, 1080, "RT Edgar brand guidelines overview: wordmark, RTE monogram, colour palette, typefaces and brand tone", WIDE)],
        "Brand guidelines: the system at a glance.")
    b += figure("fig-pair shape-guide", [
        img(p, "guide-wordmark", 2244, 1406, "Construction grid for the RT Edgar wordmark on navy"),
        img(p, "guide-monogram", 2244, 1406, "Construction grid for the RTE monogram on blue")],
        "Wordmark and monogram construction.")
    b += figure("fig-pair shape-pano", [
        img(p, "desktop-staircase", 1760, 880, "The RT Edgar website home page on desktop: Buy, Sell, Lease and Agents over a sunlit staircase"),
        img(p, "desktop-facade", 1760, 880, "The RT Edgar website home page on desktop over a heritage facade")],
        "The website on desktop.")
    b += block("contribution", "My contribution", ps([
        "As Account Director, I led the client relationship and coordinated delivery across the broader engagement.",
        "My responsibility was to connect the client's objectives with the studio's strategic, creative and technical work, ensuring priorities remained aligned and that the different workstreams progressed together.",
        "I worked directly with RT Edgar stakeholders and external technical partners, managing project communication, briefing, reviews, delivery priorities and the dependencies between brand, content, customer experience and website development.",
        "I also contributed to customer journey mapping and the development of client-facing CX recommendations, helping translate research into practical priorities."])
        + credit("Brand design, specialist strategy, development and creative production were delivered collaboratively by the wider Antimony Studio team."))
    b += figure("fig-pair shape-wide", [
        img(p, "brochure-blue", 2400, 1600, "RT Edgar property brochure with a pale blue cover"),
        img(p, "brochure-navy", 2400, 1600, "RT Edgar property brochure with a navy cover")],
        "Property brochures.")
    b += figure("fig-pair shape-wide", [
        img(p, "spread-feature", 1083, 722, "Brochure spread with a feature statement and interior photography"),
        img(p, "spread-details", 1083, 722, "Brochure spread with property details and a living room")],
        "Brochure spreads.")
    b += ('    <figure class="cs-figure">\n      <div class="fade-seq">\n'
          + "".join(f'        <img src="../assets/img/rt-edgar/boards-{i}-800.jpg" srcset="../assets/img/rt-edgar/boards-{i}-800.jpg 800w, ../assets/img/rt-edgar/boards-{i}.jpg 1920w" sizes="{WIDE}" width="1920" height="1280" alt="{a}" loading="lazy">\n'
                    for i, a in [(1, "RT Edgar sales board in a garden setting"), (2, "Double-sided RT Edgar street billboard"), (3, "RT Edgar campaign board in the street")])
          + '      </div>\n      <figcaption class="meta-label">Sales boards and outdoor campaign.</figcaption>\n    </figure>\n\n')
    b += figure("fig-pair shape-wide", [
        img(p, "board-street", 2025, 1350, "An RT Edgar campaign board on a red brick wall in a Melbourne street"),
        img(p, "stand-navy", 2400, 1600, "A navy RT Edgar open home A-frame on a footpath")],
        "Signage across the city.")
    b += block("services", "Services &amp; deliverables", services([
        "Brand and competitive research", "Audience segmentation and customer journey mapping",
        "CX strategy and recommendations", "Brand identity refresh and design system",
        "Website strategy, design and development", "Property search and technical integration coordination",
        "Content strategy and production", "Printed marketing, sales boards and signage",
        "Client stakeholder and project delivery management"]))
    b += figure("fig-pair shape-wide", [
        img(p, "website-home", 2400, 1600, "The new RT Edgar website on a phone"),
        img(p, "website-agent", 2400, 1600, "An agent profile page on the RT Edgar website")],
        "The website on mobile.")
    b += block("outcome", "Outcome", ps([
        "The engagement brought together previously distinct brand, customer experience and digital workstreams into a coordinated programme.",
        "The resulting work included a refreshed identity, website redevelopment, customer experience recommendations and a consistent suite of marketing applications for use across the business.",
        "My contribution centred on leading the client relationship and helping the different teams deliver an integrated outcome."])
        + visit("https://www.rtedgar.com/", "Visit rtedgar.com"))
    b += nxt("casper-magazine.html", "Casper Magazine")
    return head("RT Edgar", "Client leadership across an integrated brand, customer experience and digital programme for Melbourne real estate group RT Edgar, delivered with Antimony Studio.") + b + FOOT


def bbbb():
    p = "byron-bay-bone-broth"
    b = intro2("Byron Bay Bone Broth", "B2B Channel Development | Product Campaigns | Customer Research &amp; Digital Experience",
               "Connecting commercial growth with a better understanding of the customer", [
                   ("Client", "Byron Bay Bone Broth, wholefood nutrition, Australia"),
                   ("Engagement", "From October 2024, two years"),
                   ("My role", "Account Director, then Client Services Director, Antimony Studio"),
               ])
    b += figure("fig-single shape-pano", [
        img(p, "jar-hinterland", 1728, 864, "A jar of Byron Bay Bone Broth on a mossy rock in the hinterland", WIDE, lazy=False)],
        "Campaign photography courtesy of Byron Bay Bone Broth.")
    b += block("context", "Business context", ps([
        "Byron Bay Bone Broth is an Australian food and wellness business built around traditional nutrition, quality ingredients and wholefood products.",
        "Our engagement coincided with the business expanding its product offering, including the introduction of chicken liver capsules and dehydrated bone broth.",
        "These products presented opportunities to reach new customers while building stronger retail and practitioner distribution channels.",
        "Alongside the commercial rollout, the business was looking to better understand customer behaviour and improve the experience across its digital channels."]))
    b += block("challenge", "The challenge", ps([
        "The business was working across different audiences with distinct motivations and information needs.",
        "Direct consumers wanted to understand the products, their benefits and how they could fit into their daily routines.",
        "Specialty retailers needed a commercially relevant product proposition, suitable sales materials and confidence in the range.",
        "Health practitioners required credible product information and a clear understanding of how the products could be introduced to appropriate clients.",
        "At the same time, the e-commerce experience needed to communicate these propositions effectively and support customers from initial discovery through to purchase and repeat engagement.",
        "The challenge was therefore both commercial and experiential: developing new routes to market while improving how the brand communicated with different customer groups."]))
    b += block("approach", "Our approach", ps(["Antimony's engagement combined two connected programmes."]))
    b += chapter("Chapter one", "Product launch &amp; channel development")
    b += block("chapter-one", "Chapter one approach", hidden=True, inner=subsections([
        ("Audience &amp; market research", [
            "The programme began with identifying suitable retail and practitioner audiences, reviewing the relevance of prospective partners and understanding where the new products could find an appropriate market."]),
        ("B2B &amp; B2C campaign development", [
            "The studio contributed to the development of campaigns supporting the rollout of chicken liver capsules and dehydrated bone broth.",
            "Communications and creative assets needed to address consumer audiences alongside the different requirements of retailers and practitioners."]),
        ("Partner development", [
            "The work included identifying suitable early partners, researching prospective stockists and practitioners, supporting introductions and helping establish opportunities for product adoption and future case studies.",
            "The wider programme also included ambassador and partnership activity to support market awareness."]),
        ("Creative production &amp; rollout", [
            "Antimony coordinated the development and delivery of campaign and product communications, working across the client's commercial priorities and the studio's creative resources."]),
    ]))
    b += figure("fig-pair shape-tall", [
        img(p, "practitioner", 1440, 1800, "A practitioner in a meadow holding a bowl of broth"),
        img(p, "capsules", 695, 869, "Organic chicken liver capsules in an open hand")])
    b += figure("fig-pair shape-wide", [
        img(p, "retail-jars", 1550, 1033, "Three jars of Byron Bay Bone Broth"),
        img(p, "production", 1080, 720, "Broth being filled into jars in the Byron Bay kitchen")])
    b += chapter("Chapter two", "Customer experience &amp; digital optimisation")
    b += block("chapter-two", "Chapter two approach", hidden=True, inner=subsections([
        ("Customer research &amp; segmentation", [
            "The customer experience programme included audience research, stakeholder inputs and the review of customer responses, motivations, objections and information needs.",
            "This work supported segmentation and a more detailed understanding of the different audiences interacting with the brand."]),
        ("Customer journey &amp; lifecycle mapping", [
            "The team developed customer journey and lifecycle work covering key stages and touchpoints across awareness, consideration, purchase and repeat engagement.",
            "This included reviewing digital touchpoints, information requirements, trust signals and opportunities for more relevant customer communications."]),
        ("UX &amp; conversion review", [
            "A structured CRO audit examined the website's homepage, navigation, product pages and conversion pathways.",
            "The findings were developed into prioritised recommendations addressing usability, information hierarchy, education and customer confidence."]),
        ("Digital experience recommendations", [
            "The programme connected customer research and journey mapping with practical opportunities to improve the e-commerce experience, including product communication, site navigation and customer engagement."]),
    ]))
    b += figure("fig-single shape-pano", [
        img(p, "capsules-hero", 1728, 864, "Hands holding a jar of Byron Bay Bone Broth organic chicken liver capsules", WIDE)])
    b += block("contribution", "My contribution", ps([
        "I managed the senior client relationship and delivery across the commercial and digital experience workstreams.",
        "For the product rollout, I contributed to campaign strategy and was directly involved in prospective partner research, retailer and practitioner identification, initial business development and introductions.",
        "I also coordinated the creation and rollout of campaign assets, working with Antimony's creative team and the client's commercial stakeholders.",
        "Once introductions were established, the client's sales team managed final negotiations and account conversion.",
        "Across the CX programme, I contributed to customer research, segmentation, lifecycle and journey mapping, and worked with the studio's specialists to turn findings into prioritised digital recommendations.",
        "A central part of my role was connecting the commercial opportunities with the broader customer experience and ensuring both programmes progressed through delivery."]))
    b += figure("fig-pair shape-wide", [
        img(p, "farm", 1440, 960, "A farmer among pasture-raised chickens at sunrise"),
        img(p, "pouch", 1296, 864, "A pouch of organic beef bone broth beside a creek")])
    b += block("services", "Services &amp; deliverables", services([
        "B2B and B2C product launch campaigns", "Retail and practitioner market research",
        "Prospect identification and partner introductions", "Product and channel communications",
        "Ambassador and partnership programme support", "Campaign creative production and rollout",
        "Customer research and segmentation", "Customer journey and lifecycle mapping",
        "Content and digital touchpoint strategy", "E-commerce UX and CRO audit",
        "Conversion and experience recommendations", "Senior client leadership and multidisciplinary delivery"]))
    b += block("outcome", "Outcome", big(["From around 20 to 48 stockists"]) + ps([
        "The business expanded its active stockist network substantially during the engagement, growing from approximately 20 locations to 48, including 10 health practitioners.",
        "The commercial work supported broader market access through retail and practitioner channels, with account conversion undertaken by the client's sales team.",
        "Alongside this, the CX programme delivered customer research, journey mapping, digital experience analysis and prioritised recommendations for improving customer understanding and online conversion pathways. The conversion recommendations were implemented following user acceptance testing.",
        "Together, the programmes connected commercial channel development with a more informed approach to the customer experience."])
        + visit("https://byronbaybonebroth.com/", "Visit byronbaybonebroth.com"))
    b += nxt("elly-sofocli.html", "Elly Sofoclí")
    return head("Byron Bay Bone Broth", "Connecting B2B retail and practitioner channel growth with research-led customer experience for Byron Bay Bone Broth, delivered with Antimony Studio.") + b + FOOT


def elly():
    p = "elly-sofocli"
    b = intro2("Elly Sofoclí", "International Wholesale Development | Commercial Strategy | Brand &amp; Digital Communications",
               "Building an international wholesale proposition for a Melbourne bridal designer", [
                   ("Client", "Elly Sofoclí, bridal design, Melbourne"),
                   ("Engagement", "From December 2023"),
                   ("My role", "Account Director, Antimony Studio"),
               ])
    b += figure("fig-pair shape-tall", [
        img(p, "portrait-back", 1440, 1800, "Model in a strapless Elly Sofoclí gown with sculpted sleeves, seen from behind", lazy=False),
        img(p, "off-shoulder", 1440, 1800, "Model in an off-the-shoulder Elly Sofoclí ball gown with a long train", lazy=False)],
        "Campaign photography courtesy of Elly Sofoclí.")
    b += block("context", "Business context", ps([
        "Elly Sofoclí is a Melbourne-based bridal designer with an established retail presence and a distinctive approach to contemporary bridalwear.",
        "While the business had developed its reputation through direct relationships with brides, international wholesale presented an opportunity to expand its reach through carefully selected bridal boutiques.",
        "Entering these markets required more than exposure to prospective retailers.",
        "The label needed a clear commercial proposition, an appropriate product offering and a consistent brand presentation that could support relationships with buyers in different countries."]))
    b += block("challenge", "The challenge", ps([
        "The commercial requirements of wholesale differ significantly from selling directly to consumers.",
        "Prospective stockists needed to understand the collection, assess its relevance to their customers and evaluate the commercial terms of a potential partnership.",
        "This required consideration of wholesale pricing, product selection, market suitability and the communication materials used to introduce the brand.",
        "At the same time, the visual identity, website and content needed to present a consistent and credible expression of the label to both retail customers and international wholesale buyers.",
        "The challenge was to establish the foundations for international growth while preserving the brand's premium positioning."]))
    b += block("approach", "Our approach", subsections([
        (None, ["Antimony worked across commercial development, brand identity, website delivery and communications."]),
        ("Wholesale proposition &amp; pricing", [
            "The programme included work on the wholesale pricing strategy and the selection of products suitable for the international stockist offering.",
            "The intention was to present prospective partners with a proposition that made sense commercially and reflected the positioning of the brand."]),
        ("Market research &amp; partner identification", [
            "Potential international markets and bridal retailers were researched to identify suitable prospects.",
            "The focus was on boutiques whose clientele, product positioning and retail environment represented a credible fit for the collection."]),
        ("Business development &amp; introductions", [
            "The programme supported the identification and initial approach to prospective stockists, helping establish introductions for the client's sales team to progress."]),
        ("Brand identity &amp; digital presentation", [
            "The studio developed work across brand identity, website design and development, and supporting content.",
            "These assets helped establish a more consistent presentation of the label across digital channels and supported its introduction to new audiences."]),
        ("Wholesale communications &amp; creative delivery", [
            "Supporting communications and creative materials were coordinated to help present the collection, brand and commercial proposition to potential partners."]),
    ]))
    tiles = [("stationery", 1220, 1525, "The Elly Sofoclí wordmark embossed on textured stationery"),
             ("garment-bag", 1080, 1350, "Black garment bag ribbon printed with the Elly Sofoclí name"),
             ("hanger", 1440, 1800, "A black velvet hanger carrying the Elly Sofoclí wordmark"),
             ("studio", 1440, 1800, "The Elly Sofoclí studio, with a framed artwork and a white sofa")]
    b += ('    <figure class="cs-figure">\n      <div class="fig-tiles four shape-tall">\n'
          + "".join(img(p, n, w, h, a, TILE4).replace("      <img", "        <img") for n, w, h, a in tiles)
          + '      </div>\n      <figcaption class="meta-label">The identity carried through to the moments buyers and brides experience.</figcaption>\n    </figure>\n\n')
    b += block("contribution", "My contribution", ps([
        "I contributed to the development of the international wholesale programme, with particular involvement in commercial research, partner identification and early business development.",
        "I worked on the wholesale pricing strategy and product offering, researched suitable international retailers and facilitated introductions to prospective stockists.",
        "I was also responsible for managing the creation and rollout of supporting communications and design work, coordinating the studio's creative and digital specialists.",
        "Once an introduction had been established, Elly's sales team took responsibility for the final commercial discussions and closing of wholesale accounts.",
        "My role combined commercial thinking, relationship development and creative project management, helping connect the new wholesale proposition with the materials and relationships needed to take it to market."]))
    b += block("services", "Services &amp; deliverables", services([
        "Wholesale market and competitor research", "Wholesale pricing strategy support",
        "Product and collection offering development", "International stockist research and identification",
        "Prospective partner introductions", "Business development support",
        "Brand identity development", "Website design and development",
        "Content and communications planning", "Wholesale communications and creative assets",
        "Creative project and stakeholder management"]))
    b += block("outcome", "Outcome", big(["Queensland", "New York", "China", "South Korea"]) + ps([
        "The programme established the commercial and communication foundations for international wholesale development.",
        "It supported the introduction of the label to prospective stockists across multiple overseas markets and contributed to the development of international retail partnerships, with stockist relationships opened through the programme in Queensland, New York, mainland China and South Korea.",
        "The brand's subsequent stockist network demonstrates an international presence across markets including the United States and Asia.",
        "The commercial development programme was collaborative, with initial research and introductions supported through Antimony and final negotiations managed by the client's sales team."])
        + visit("https://www.ellysofocli.com/", "Visit ellysofocli.com"))
    b += figure("fig-pair shape-tall", [
        img(p, "corset", 1440, 1800, "Back view of a strapless Elly Sofoclí corset gown with a full skirt"),
        img(p, "veil", 1440, 1800, "Model in a fitted lace Elly Sofoclí column gown and veil")])
    b += nxt("femme-connection.html", "Femme Connection")
    return head("Elly Sofoclí", "Building an international wholesale proposition for Melbourne bridal designer Elly Sofoclí, delivered with Antimony Studio.") + b + FOOT


FEMME_TIERS = [
    ("Curator", "0 to 500 points", "Warm, empowering, introductory", "4 emails over 10 to 30 days",
     ["Welcome to Femme Rewards", "Earn Points Fast", "Share the Style. Score Big", "Unlock What's Next"]),
    ("Trendsetter", "501 to 800 points", "Confident, motivational, community-driven", "4 emails over 10 to 30 days",
     ["You're a Trendsetter Now", "Earn More With a Review", "Invite Friends, Climb Faster", "Don't Miss These Rewards"]),
    ("Style Icon", "801 to 1,000 points", "Elevated, stylish, aspirational", "4 emails over 30 days",
     ["Your Icon Status Is Official", "You're $200 Away From VIP", "Get Rewarded for Your Influence", "Your VIP Status Awaits"]),
    ("Visionary", "1,001 to 1,500 points", "Premium, editorial, exclusive", "4 emails over 30 days",
     ["Welcome, Visionary", "Your Style Deserves the Spotlight", "Refer a Fellow Style Leader", "Your Legacy, Your Style"]),
    ("Couture Queen", "1,501 points and above", "Luxe, personalised, relationship-driven", "5 emails over 30 days",
     ["You've Reached the Crown Tier", "Your Exclusive Thank You", "Style That Leads the Way", "Refer Royalty, Be Rewarded", "Let Us Style You Personally"]),
]


def femme_rewards():
    cards = ""
    for i, (name, pts, tone, flow, emails) in enumerate(FEMME_TIERS, 1):
        li = "".join(f"            <li>{e}</li>\n" for e in emails)
        cards += f"""      <li class="tier tier-{i}">
          <p class="tier-step">Tier {i}</p>
          <h3>{name}</h3>
          <p class="tier-points">{pts}</p>
          <p class="tier-tone">{tone}</p>
          <p class="tier-flow">{flow}</p>
          <ol class="tier-emails" aria-label="{name} emails">
{li}          </ol>
        </li>
"""
    return f"""    <figure class="cs-figure rewards" aria-labelledby="rewards-title">
      <div class="rewards-head">
        <h2 id="rewards-title">Femme Rewards: five tiers, 21 lifecycle emails</h2>
        <p>Built on Yotpo and automated in Klaviyo. Each tier has its own tone, offers and calls to action, moving members from first purchase towards the top tier, with a monthly loyalty statement to every member.</p>
      </div>
      <ol class="tiers">
{cards}      </ol>
      <ul class="earn" aria-label="Ways to earn points">
        <li><strong>1 point</strong> per $1 spent</li>
        <li><strong>75 points</strong> for a photo review</li>
        <li><strong>200 points</strong> for a tagged Instagram look</li>
        <li><strong>400 points</strong> for a successful referral</li>
      </ul>
      <figcaption class="meta-label">Loyalty programme structure, from the Femme Rewards email flow overview.</figcaption>
    </figure>

"""


def femme():
    p = "femme-connection"
    b = intro2("Femme Connection", "E-commerce | CRM &amp; Lifecycle Marketing | Loyalty | Integrated Campaigns",
               "Building an integrated customer retention and digital growth programme", [
                   ("Client", "Femme Connection, online womenswear, Australia"),
                   ("Engagement", "2024 to 2026"),
                   ("My role", "Account Director, then Client Services Director, Antimony Studio"),
               ])
    b += FEMME_HERO
    b += block("context", "Business context", ps([
        "Femme Connection is an Australian online fashion retailer operating in a competitive, fast-moving e-commerce market.",
        "The business needed to maintain customer acquisition while developing stronger relationships with existing customers and encouraging repeat purchases.",
        "Our engagement evolved into an ongoing programme spanning brand development, digital experience, CRM, customer lifecycle marketing, loyalty and campaign delivery.",
        "The work required both strategic planning and consistent execution across multiple marketing and e-commerce platforms."]))
    b += block("challenge", "The challenge", ps([
        "Paid acquisition was an important part of the business, but continued growth also depended on converting and retaining more of the customers already entering the brand's ecosystem.",
        "The opportunity was to improve the relationship between acquisition, website experience, customer communications and repeat purchasing.",
        "This required a more coordinated approach to customer lifecycle activity, automated communications, loyalty, campaign planning and performance reporting.",
        "It also needed an ongoing operating rhythm that allowed the client and studio teams to review results, test improvements and prioritise the next stage of work."]))
    b += block("approach", "Our approach", subsections([
        (None, ["Antimony developed and delivered an integrated programme across several connected disciplines."]),
        ("Brand &amp; digital experience", [
            "The engagement included brand identity development and website work, establishing the foundations for a more consistent customer experience.",
            "Ongoing digital optimisation involved reviewing conversion pathways, website usability and opportunities to improve the shopping journey."]),
        ("CRM &amp; lifecycle marketing", [
            "Klaviyo was used to manage customer communications across email and SMS.",
            "The programme included lifecycle flows covering welcome, abandoned cart, checkout, post-purchase and cross-sell opportunities.",
            "The team undertook flow reviews, QA, A/B testing and ongoing refinement to improve the effectiveness of automated and campaign communications."]),
        ("Loyalty &amp; customer retention", [
            "The engagement incorporated Yotpo loyalty strategy, including customer rewards and referral activity.",
            "This work was designed to support repeat purchasing and develop stronger relationships with the existing customer base."]),
        ("Campaigns &amp; partnerships", [
            "The studio supported integrated campaign activity across the retail calendar, alongside influencer, ambassador and affiliate initiatives.",
            "Partnership and campaign work complemented the CRM programme and helped maintain consistency across customer communications."]),
        ("E-commerce &amp; platform development", [
            "The work also involved e-commerce optimisation, integration considerations and scoping for further Shopify development.",
            "This included coordination across marketing, creative, platform and technical workstreams."]),
        ("Performance reporting &amp; optimisation", [
            "Regular reporting, client meetings and reviews connected performance data with practical recommendations.",
            "The programme involved evaluating campaign and flow performance, reviewing channel priorities and identifying opportunities for improvement."]),
    ]))
    b += FEMME_MID
    b += block("contribution", "My contribution", ps([
        "I led the senior client relationship and was responsible for coordinating the ongoing programme across the client and studio teams.",
        "I also had direct responsibility for the email and CRM workstream, including campaign planning, lifecycle strategy, creative reviews, flow QA, testing priorities and performance analysis.",
        "I managed the client reporting and review cadence, bringing together results, recommendations and the next priorities for delivery.",
        "Beyond CRM, I coordinated multidisciplinary work across website development, loyalty, content, digital optimisation and partnerships, helping maintain alignment between commercial objectives and day-to-day execution.",
        "My responsibilities also included participating in Shopify migration scoping and loyalty strategy development, working with the relevant client stakeholders and technical specialists."])
        + credit("Design, development and specialist creative production were delivered collaboratively by Antimony Studio."))
    b += FEMME_BRAND
    b += block("services", "Services &amp; deliverables", services([
        "Brand identity development", "Website and e-commerce experience", "Digital optimisation and CRO",
        "Customer lifecycle strategy", "Klaviyo email and SMS marketing", "Automated flow development and refinement",
        "A/B testing and quality assurance", "Yotpo loyalty and referral strategy",
        "Influencer, ambassador and affiliate programmes", "Integrated retail campaign planning",
        "Shopify migration scoping", "Marketing performance reporting", "Ongoing senior client and project leadership"]))
    b += femme_rewards()
    b += block("outcome", "Outcome", big(["$30,000 to $120,000 a month"]) + ps([
        "The engagement developed from individual brand and marketing workstreams into an ongoing programme connecting customer acquisition, retention, loyalty and e-commerce experience.",
        "Email and lifecycle marketing became an increasingly important contributor to the business's revenue, supported by structured testing, regular reporting and continuous refinement. Over the engagement, monthly revenue from the email channel grew from approximately $30,000 to $120,000, and in January 2026 automated flow revenue was 60% higher than a year earlier.",
        "The work established a more coordinated approach to customer communications and provided the client with greater visibility over performance and future priorities."])
        + '        <p class="meta-label">Flow figure from Klaviyo reporting, January 2026 compared with January 2025.</p>\n'
        + visit("https://femmeconnection.com.au/", "Visit femmeconnection.com.au"))
    b += nxt("cnit.html", "Carl Navè Individually Tailored")
    return head("Femme Connection", "Building customer retention through CRM, loyalty and lifecycle marketing for online fashion retailer Femme Connection, delivered with Antimony Studio.") + b + FOOT


# Femme imagery
_FT = [("tile-heart", "Pink heart on black"), ("tile-f", "F monogram on pink"), ("tile-check", "Black check on sand"),
       ("tile-c", "C monogram on coral"), ("tile-star", "White star on green")]
FEMME_HERO = figure("fig-single shape-pano", [
    img("femme-connection", "garden", 2400, 1200, "A model in a printed maxi dress on a lawn in front of a country house", WIDE, lazy=False)],
    "Campaign photography courtesy of Femme Connection.")
FEMME_MID = ('    <figure class="cs-figure">\n      <div class="fig-tiles three shape-tall">\n'
    + "".join(img("femme-connection", n, 1242, 1552, alt, "(max-width: 600px) 33vw, 450px").replace("      <img", "        <img")
              for n, alt in [("vacation", "Vacation Vibes campaign: a model in a tropical print shirt and trousers"),
                             ("spring", "Spring Collection campaign: a model in a pale blue dress in a formal garden"),
                             ("beach", "A model in a blue and white printed dress on a beach")])
    + '      </div>\n      <figcaption class="meta-label">Seasonal campaigns, including Vacation Vibes and Spring Collection.</figcaption>\n    </figure>\n\n')
FEMME_BRAND = (
    ('    <figure class="cs-figure">\n      <div class="fig-tiles five shape-tile">\n'
     + "".join(img("femme-connection", n, 1000, 1500, f"Femme Connection brand graphic: {a}", "(max-width: 600px) 33vw, 270px").replace("      <img", "        <img") for n, a in _FT)
     + '      </div>\n      <figcaption class="meta-label">Brand identity by Antimony Studio.</figcaption>\n    </figure>\n\n'))


def casper():
    p = "casper-magazine"
    b = intro2("Casper Magazine", "B2B Go-to-Market Strategy | Commercial Product Development | Brand Partnerships &amp; Digital Publishing",
               "Building the commercial foundations of an independent digital publication", [
                   ("Client", "Casper Magazine, digital publishing, Melbourne"),
                   ("Engagement", "From March 2024"),
                   ("My role", "Account Director, Antimony Studio"),
               ])
    b += figure("fig-single shape-wide", [
        img(p, "hero", 1293, 862, "The Casper Magazine wordmark over a portrait of a woman in a straw hat and sunglasses", WIDE, lazy=False)])
    b += block("context", "Business context", ps([
        "Casper Magazine is an independent Melbourne publication covering fashion, beauty, wellness, design and contemporary culture.",
        "Founded by Maria Ugrinovski, its Editor-in-Chief, the publication had built an editorial identity and audience through its blog, Instagram and digital content.",
        "The next stage was to develop Casper into a more established digital publishing business, supported by a clear advertising proposition, expanded digital services and commercial partnerships."]))
    b += block("challenge", "The challenge", ps([
        "Casper had developed its editorial voice and audience, but becoming a commercially focused digital publication required a more structured business offering.",
        "Prospective advertisers needed to understand the publication's audience, the advertising opportunities available and the value of a commercial partnership.",
        "The challenge extended beyond advertising space. Casper needed a defined offering covering digital placements, sponsored content, editorial collaborations and brand partnerships.",
        "That meant market research, commercial product development, a coherent go-to-market approach and professional sales materials, all while respecting the publication's editorial identity."]))
    b += block("approach", "Our approach", subsections([
        (None, ["Antimony Studio worked across commercial strategy, brand development, digital publishing and marketing communications."]),
        ("Competitor research &amp; commercial positioning", [
            "The programme began with research into comparable publications, their advertising products and the way they structured commercial partnerships.",
            "The research identified opportunities to establish a more defined and differentiated advertising proposition."]),
        ("Go-to-market &amp; product development", [
            "A tiered advertising and partnership offering was developed, combining digital advertising, editorial services, sponsored content and brand collaborations.",
            "The intention was a structured commercial proposition that Casper could present to businesses with different objectives and budgets."]),
        ("Media kit development", [
            "The commercial offering was translated into a redesigned media kit, presenting the publication's identity, audience, advertising services and partnership opportunities in a professional, commercially focused format."]),
        ("Brand, website &amp; editorial development", [
            "The wider engagement included brand positioning, visual identity, website development and editorial communications to support the publication's evolution."]),
        ("Business development &amp; partnerships", [
            "The programme also supported the identification of prospective advertisers, commercial opportunities and suitable brand collaborations."]),
        ("Operational systems", [
            "New project management systems were introduced to improve workflow, coordination and the organisation of ongoing activities."]),
    ]))
    b += figure("fig-single shape-screen", [
        img(p, "identity", 1433, 806, "The Casper identity: a C monogram over a black and white portrait, beside the CASPER wordmark in white on black", WIDE)],
        "The Casper monogram and wordmark.")
    b += block("contribution", "My contribution", ps([
        "As Account Director, I worked directly with Casper's founder and Editor-in-Chief, Maria Ugrinovski.",
        "I conducted the competitor and market research, looking at how comparable digital publications packaged their advertising services and commercial partnerships.",
        "From that research, I developed the foundations of Casper's tiered advertising and content offering, bringing digital placements, editorial opportunities and brand collaborations together into a structured commercial proposition.",
        "I prepared and presented the offering to Maria, working with Antimony's Chief Strategist, who helped refine and approve the strategic direction.",
        "I also led the redevelopment of Casper's media kit, coordinating the commercial content, positioning and creative delivery needed to make it an effective business development tool.",
        "Beyond the media kit, I was actively involved in identifying advertising opportunities, developing prospective brand relationships and helping progress business-to-business partnerships.",
        "I introduced project management systems that improved workflow and coordination across the engagement."])
        + credit("Branding, design, digital development and specialist creative work were delivered by the wider Antimony Studio team."))
    b += figure("fig-single", [
        img(p, "proposition", 1440, 858, "Advertiser presentation slide: Print, Digital, Experiential. Casper is a 360 degree publisher with a unique ecosystem.", WIDE)],
        "The commercial proposition: print, digital and experiential.")
    b += figure("fig-single", [
        img(p, "partners", 1440, 960, "Campaign imagery from Farfetch, Adore Beauty, Hogan, Armani and Good On You, with each brand's logo", WIDE)],
        "Brand partners included Farfetch, Adore Beauty, Hogan, Armani and Good On You.")
    b += block("services", "Services &amp; deliverables", services([
        "Competitor and market research", "B2B go-to-market development",
        "Commercial positioning and product strategy", "Tiered advertising package development",
        "Digital and editorial service offering", "Advertising and sponsorship propositions",
        "Media kit strategy, content and design", "Advertiser and brand partner research",
        "Business development and partnership support", "Brand identity and digital publishing",
        "Website design and development", "Content and editorial communications",
        "Project management systems and workflow", "Senior client leadership and multidisciplinary delivery"]))
    b += figure("fig-single portrait-narrow shape-tall", [
        img(p, "phone", 579, 724, "A hand holding a phone showing the Casper digital edition and its 2024 Spring Issue", "(max-width: 600px) 80vw, 440px")])
    b += block("outcome", "Outcome", ps([
        "The engagement helped Casper strengthen the commercial foundations it needed to operate as an independent digital publication.",
        "The new advertising product structure and media kit gave Casper a clearer, more professional way to communicate its audience, services and partnership opportunities.",
        "The programme supported new advertising avenues, brand collaborations and successful business-to-business partnerships."])
        + big(["92% more website sessions", "140% more member sign-ups", "14 brand partner meetings"])
        + ps(["Antimony Studio reported a 92% increase in website sessions and a 75% increase in organic search traffic following the redesign, with member sign-ups up 140%. The advertiser pitch deck led to 14 meetings with prospective brand partners.",
              "Alongside the commercial work, improvements to brand presentation, digital experience and internal workflow gave the publication greater structure for its ongoing development."])
        + visit("https://caspermagazine.com/", "Visit caspermagazine.com"))
    b += nxt("byron-bay-bone-broth.html", "Byron Bay Bone Broth")
    return head("Casper Magazine", "Go-to-market strategy, advertising products and commercial partnerships for Melbourne's independent Casper Magazine, delivered with Antimony Studio.") + b + FOOT


def cnit():
    p = "cnit"
    rows = "".join(f"      <div><dt>{k}</dt><dd>{v}</dd></div>\n" for k, v in [
        ("Business", "Bespoke and made-to-measure menswear, Melbourne CBD"),
        ("Period", "2012 to 2024"),
        ("My role", "Founder and General Manager")])
    b = f'''    <header class="cs-head">
      <a class="cs-back" href="../#work">Selected work</a>
      <p class="meta-label cs-label">A founder's story</p>
      <h1>Carl Navè Individually Tailored</h1>
      <p class="cs-disciplines">Entrepreneurship | Brand Development | Commercial Leadership | Customer Experience</p>
      <p class="thesis">Building a premium menswear brand from the ground up</p>
    </header>

    <dl class="cs-meta">
{rows}    </dl>

'''
    b += figure("fig-single shape-wide", [
        img(p, "portrait-glasses", 2400, 1600, "A man in tortoiseshell glasses, a grey check suit and navy tie, looking down", WIDE, lazy=False)])
    b += chapter("01", "The opportunity")
    b += block("opportunity", "The opportunity", ps([
        "In 2012, I established Carl Navè Individually Tailored to make premium tailored menswear more accessible through a highly personal service.",
        "The proposition was straightforward: well-made clothing, considered design and an experience shaped around the individual rather than a conventional retail transaction.",
        "From a studio in Melbourne's CBD, the business offered bespoke and made-to-measure garments to private clients, professionals, wedding parties and corporate customers. Over the following twelve years it expanded into corporate wardrobes, wholesale manufacturing and made-to-order e-commerce."]), hidden=True)
    b += figure("fig-single shape-wide", [
        img(p, "studio", 2400, 1600, "The tailoring studio: linen curtains, a round table with timber chairs and a jacket on a stand", WIDE)],
        "The studio in Melbourne's CBD.")
    b += chapter("02", "Brand and customer experience")
    b += block("brand", "Brand and customer experience", ps([
        "The brand needed to stand for more than the garments. It was built around quality, fit, personal service and an appreciation of craftsmanship.",
        "I developed the positioning, product offering, visual identity and marketing approach, and the brand grew through editorial content, digital marketing, partnerships, events and referrals.",
        "Every relationship began with a consultation. We worked to understand each customer's needs, preferences, lifestyle and the occasions they were dressing for, then guided them through fabric selection, design, fittings and delivery.",
        "Customers returned for new garments, wardrobe updates and important occasions. Over time the business served more than 3,000 customers, and around 60% came back.",
        "That retention was built on trust, product knowledge and consistent delivery. It was also an early, practical education in customer experience: understanding what people value, managing expectations and giving them reasons to return.",
        "For me, building the brand was as much about delivering on its promise as communicating it."]), hidden=True)
    b += figure("fig-pair shape-square", [
        img(p, "hands", 1440, 1440, "Carl's hands holding tailoring shears and chalk, a tape measure hanging over his shirt"),
        img(p, "basted-jacket", 1440, 1440, "A basted navy jacket on a stand with a tape measure, ready for a fitting")],
        "Measuring, marking and fitting.")
    b += chapter("03", "Product and production")
    b += block("production", "Product and production", ps([
        "Behind the customer experience sat a complex product and production operation, from fabric sourcing, design and technical specifications to manufacturing, fittings, alterations, quality control and delivery.",
        "I developed and managed relationships with mills, manufacturers and suppliers in Melbourne and overseas, including Italy, the United Kingdom, France and China.",
        "I also managed pricing, supplier negotiations, purchasing, production planning and financial performance. The constant challenge was balancing the craft of the garments with the commercial realities of margin, capacity and customer expectations."]), hidden=True)
    b += figure("fig-single shape-wide", [
        img(p, "sewing", 2400, 1600, "Carl at an industrial sewing machine by a window, a tape measure around his neck", WIDE)],
        "In the workroom.")
    b += figure("fig-tiles three shape-square", [
        img(p, "canvas", 1440, 1440, "Hand-stitched canvas and chalk marks on navy cloth", TILE4),
        img(p, "collar", 1000, 1000, "Shirt collars in black and white", TILE4),
        img(p, "cuff", 1440, 1440, "A navy jacket cuff with working buttons", TILE4)],
        "Canvas, collar and cuff.")
    b += chapter("04", "Growth, B2B and digital")
    b += block("growth", "Growth, B2B and digital", ps([
        "As the business developed, I expanded beyond private tailoring into corporate wardrobes, wedding tailoring, club blazers, uniforms, wholesale partnerships and white-label manufacturing.",
        "The B2B work meant understanding the requirements of other retailers and corporate clients, and developing suitable product and production solutions. Clients included Barry Plant, Woodards, Buxton and Zagame's Ferrari dealership.",
        "White-label production became an established revenue stream, generating around $500,000 a year during its established operating period.",
        "Online, I introduced e-commerce and made-to-order capability so customers could engage with the brand beyond the studio. CRM and communication processes supported appointments, customer records, referrals, follow-up and repeat business.",
        "Diversification let the business serve different needs while drawing on the same design, production and service capabilities."]), hidden=True)
    b += figure("fig-single", [
        img(p, "web-home", 1600, 650, "The carlnave.com.au home page: the Carl Navè logo over tailoring tools on navy velvet, with an invitation to book a free consultation", WIDE)],
        "The carlnave.com.au home page, as archived.")
    b += figure("fig-single screen-narrow", [
        img(p, "web-store", 1600, 1602, "The made-to-order online store, with jackets shown in navy, black and charcoal", "(max-width: 900px) 100vw, 860px")],
        "The made-to-order online store, as archived.")
    b += figure("fig-pair narrow shape-tile", [
        img(p, "wedding-1", 1000, 1500, "A groom in a black velvet dinner jacket and check trousers against a navy backdrop"),
        img(p, "wedding-2", 1000, 1500, "A groom in a grey check dinner jacket and black trousers against a navy backdrop")],
        "Wedding tailoring.")
    b += figure("fig-single shape-wide", [
        img(p, "ties", 2400, 1600, "Silk ties in stripes of burgundy, navy, green and blue on a rail", WIDE)])
    b += chapter("05", "Leading the business")
    b += block("leading", "Leading the business", ps([
        "As founder, I was responsible for the business as a whole. I built and led a team of up to eight across tailoring, sales, production, administration and marketing.",
        "My responsibilities ran from business planning and financial performance to hiring, team development, supplier relationships, customer service and operations.",
        "Leading the business meant balancing customer expectations with the realities of production, cash flow, staffing and commercial commitments, and adapting to change. Lockdowns, international supply disruption and a lasting shift in how people dress for work all required adjustments to the offer, the operating model and our priorities."]), hidden=True)
    b += figure("fig-pair shape-square", [
        img(p, "studio10", 1440, 1440, "Carl with Joe Hildebrand on the Studio 10 set"),
        img(p, "zagame", 1152, 1152, "A Zagame Collection spread titled An Open Letter From a Melbourne Tailor")],
        "Dressing Joe Hildebrand for a Studio 10 designer showcase, and a Zagame Collection feature, 2019.")
    b += '''    <section class="cs-section" aria-labelledby="results">
      <h2 id="results">Commercial results</h2>
      <div class="body">
        <dl class="figures">
          <div><dt>Peak annual revenue</dt><dd>$1.2m</dd></div>
          <div><dt>Customers served</dt><dd>3,000+</dd></div>
          <div><dt>Garments produced</dt><dd>15,000+</dd></div>
          <div><dt>Repeat clientele</dt><dd>Around 60%</dd></div>
        </dl>
        <p>Over twelve years, the business grew into an established independent menswear label with a loyal customer base, a team of up to eight, an established wholesale and white-label business, B2B relationships across property and automotive, and made-to-order e-commerce.</p>
        <p class="meta-label">Revenue is a peak annual figure. Customer and garment numbers are cumulative across the life of the business.</p>
      </div>
    </section>

'''
    b += block("taught", "What it taught me", ps([
        "Building and running the business shaped how I approach commercial relationships and creative work today.",
        "I have invested in brand development, commissioned creative work, managed marketing budgets, developed products and balanced commercial ambition with operational reality. I understand what sits behind a client's decision because I have made those decisions myself.",
        "It taught me the value of good partners, clear communication and creative work that serves a genuine business purpose. That perspective continues to inform how I lead client relationships."]))
    b += figure("fig-single portrait-narrow shape-square", [
        img(p, "carl", 1440, 1440, "Carl Navè in the studio, smiling, with a tape measure around his neck", "(max-width: 600px) 80vw, 440px")])
    b += nxt("rt-edgar.html", "RT Edgar")
    return head("Carl Navè Individually Tailored", "A founder's story: twelve years building and running a premium Melbourne menswear business, from brand and customer experience to production, B2B growth and digital.") + b + FOOT


if __name__ == "__main__":
    for name, fn in [("rt-edgar", rt_edgar), ("casper-magazine", casper), ("byron-bay-bone-broth", bbbb),
                     ("elly-sofocli", elly), ("femme-connection", femme), ("cnit", cnit)]:
        (ROOT / "work" / f"{name}.html").write_text(fn())
        print("wrote", name)
