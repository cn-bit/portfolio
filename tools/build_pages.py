"""One-off builder for the four case study pages.

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
<link rel="stylesheet" href="../assets/css/main.css">
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
        <li><span class="meta-label">LinkedIn</span><a href="https://www.linkedin.com/in/carlnave" target="_blank" rel="noopener">linkedin.com/in/carlnave</a></li>
      </ul>
    </div>
    <div class="colophon meta-label">
      <span>Carl Navè, Melbourne</span>
      <span>Project work shown was delivered with Antimony Studio.</span>
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


def rt_edgar():
    p = "rt-edgar"
    b = intro("RT Edgar", "Aligning brand, customer experience and digital", [
        ("Client", "RT Edgar, real estate, Melbourne"),
        ("Engagement", "From September 2024"),
        ("Workstreams", "Research, brand, customer experience, website, print and signage"),
        ("My role", "Account Director, Antimony Studio"),
    ])
    b += ('    <figure class="cs-figure fig-single">\n'
          '      <div class="panel panel-rte"><img src="../assets/img/rt-edgar/monogram-fireplace.jpg" width="578" height="722" '
          'alt="The redesigned RTE monogram, with Est 1894, over an interior with a marble fireplace"></div>\n'
          '      <figcaption class="meta-label">The redesigned RTE monogram and lock-up.</figcaption>\n'
          '    </figure>\n\n')
    b += section("context", "Business context", [
        "RT Edgar has sold and leased property in Melbourne since 1894. When the engagement began in September 2024, the group was approaching its 130th year, operating across several offices with a strong reputation in the city's established suburbs."])
    b += section("challenge", "The challenge", [
        "The group needed to modernise without losing what made its name valuable. Its heritage carried real weight with long-standing clients, but the brand also had to work online and across listings, print and signage produced by many people in many offices. Brand, customer experience and the website had to tell one consistent story."])
    b += section("approach", "The approach", [
        "The programme ran as connected workstreams rather than separate projects.",
        "It began with research: a competitor audit, audience segmentation and customer journey mapping. The findings set the strategy and shaped the creative decisions that followed.",
        "The brand was refreshed around a redesigned RTE monogram and lock-up that kept the authority of the heritage while feeling cleaner and more contemporary. A new website brought the brand, content and customer journey together, and a content and channel plan built around the 130th year gave the business a consistent way to speak across its channels. The identity was then carried into the material agents use every day: property brochures, sales boards and open home signage."])
    b += figure("fig-pair shape-wide", [
        img(p, "website-home", 2400, 1600, "The new RT Edgar website on a phone"),
        img(p, "website-agent", 2400, 1600, "An agent profile page on the RT Edgar website")],
        "The website.")
    b += section("contribution", "My contribution", [
        "I led the client relationship from the first brief to launch. That meant working with RT Edgar's senior stakeholders to agree priorities, keeping several workstreams aligned with the business's objectives, and managing the dependencies between research, brand, content and web development.",
        "I contributed to the customer experience work and the strategic recommendations that came from the research, briefed the studio team, and oversaw content and digital delivery."],
        credit("Brand design, web design and development by the Antimony Studio team."))
    b += figure("fig-pair shape-wide", [
        img(p, "brochure-blue", 2400, 1600, "RT Edgar property brochure with a pale blue cover"),
        img(p, "brochure-navy", 2400, 1600, "RT Edgar property brochure with a navy cover")],
        "Property brochures.")
    b += figure("fig-pair shape-wide", [
        img(p, "spread-feature", 1083, 722, "Brochure spread with a feature statement and interior photography"),
        img(p, "spread-details", 1083, 722, "Brochure spread with property details and a living room")],
        "Brochure spreads.")
    b += figure("fig-single shape-wide", [
        img(p, "board-street", 2025, 1350, "An RT Edgar sales board on a brick wall in a Melbourne street", WIDE)],
        "Sales boards in the street.")
    b += figure("fig-pair shape-tile", [
        img(p, "open-home-navy", 1000, 1500, "Navy open home sign with an arrow"),
        img(p, "open-home-blue", 1000, 1500, "Blue-grey open home sign with an arrow")],
        "Open home signage.")
    b += section("outcome", "Outcome", [
        "The full programme was delivered: research, a refreshed identity, a new website, and a consistent system of brochures and signage for use across the business, in time for RT Edgar's 130th year."],
        '        <p class="meta-label"><a href="https://www.rtedgar.com/" target="_blank" rel="noopener">Visit rtedgar.com</a></p>\n')
    b += nxt("byron-bay-bone-broth.html", "Byron Bay Bone Broth")
    return head("RT Edgar", "Client leadership across an integrated brand, customer experience and digital programme for Melbourne real estate group RT Edgar, delivered with Antimony Studio.") + b + FOOT


def bbbb():
    p = "byron-bay-bone-broth"
    b = intro("Byron Bay Bone Broth", "Connecting retail channel growth with a better customer experience", [
        ("Client", "Byron Bay Bone Broth, organic bone broth and wholefood nutrition"),
        ("Engagement", "From October 2024, two years"),
        ("Workstreams", "B2B and B2C campaigns, channel development, customer research, journey mapping, UX and conversion"),
        ("My role", "Account Director, then Client Services Director, Antimony Studio"),
    ])
    b += figure("fig-single shape-pano", [
        img(p, "jar-hinterland", 1728, 864, "A jar of Byron Bay Bone Broth on a mossy rock in the hinterland", WIDE, lazy=False)],
        "Campaign photography courtesy of Byron Bay Bone Broth.")
    b += section("context", "Business context", [
        "Byron Bay Bone Broth was started by two chefs with a belief in real food and local farming. When the engagement began in October 2024, the business was rolling out two newer formats, organic chicken liver capsules and dehydrated bone broth powder, and had around 20 stockists."])
    b += section("challenge", "The challenge", [
        "New products needed new routes to market. Specialty health food retailers and health practitioners were natural partners for food-first nutrition, but each needed a reason to stock and recommend the range.",
        "The same problem showed up online. Research later found that shoppers, retailers and practitioners were all being told the same story despite needing different things, and that high-intent customers weren't getting enough proof or clarity, particularly on the capsules. The two chapters below address that one problem from both ends."])
    b += chapter("Chapter one", "Commercial channel development")
    b += section("channel-approach", "The approach", [
        "Antimony developed B2B and B2C campaigns for the rollout, with distinct communication for retailers, practitioners and consumers. For practitioners, the studio developed a programme with tiered wholesale pricing, no lock-in or minimum orders, product education and guidance on presenting the range. It was approved by the client and is now in market. An ambassador programme extended the brand's reach."])
    b += figure("fig-pair shape-tall", [
        img(p, "practitioner", 1440, 1800, "A practitioner in a meadow holding a bowl of broth"),
        img(p, "capsules", 695, 869, "Organic chicken liver capsules in an open hand")])
    b += section("channel-contribution", "My contribution", [
        "I contributed to the strategic development of the campaigns, then focused on getting the products in front of the right partners. I researched and identified suitable retailers and practitioners, including early adopters who could become case studies, made introductions and supported the partnerships that followed.",
        "I also managed the creation and rollout of campaign assets with the wider Antimony team. The client's sales team handled final negotiations and account conversion."])
    b += figure("fig-pair shape-wide", [
        img(p, "retail-jars", 1550, 1033, "Three jars of Byron Bay Bone Broth"),
        img(p, "production", 1080, 720, "Broth being filled into jars in the Byron Bay kitchen")])
    b += section("channel-outcome", "Outcome", [], result(
        ["From around 20 to 48 stockists"],
        ["Over the engagement, the stockist network more than doubled, from around 20 to 48, including 10 health practitioners. This was a shared commercial result, delivered with the client's sales team."]))
    b += chapter("Chapter two", "Digital and customer experience")
    b += section("digital-approach", "The approach", [
        "Customer research identified four segments, from burnt-out millennials to strength-seeking midlife men. Their motivations differed, but each wanted simplicity, transparency and trust in a crowded supplement market. The team mapped each segment's journey from first awareness to repeat purchase and advocacy, then assessed the homepage, navigation, product pages and checkout.",
        "Recommendations were organised in four layers: trust, commerce, education and advocacy. The aim was to help customers understand the products, feel confident buying them and find reordering easy."])
    b += figure("fig-single shape-pano", [
        img(p, "website-hero", 1728, 864, "Byron Bay Bone Broth website banner showing a pouch of organic beef broth", WIDE)])
    b += section("digital-contribution", "My contribution", [
        "I led the client relationship through the research programme, contributed to the segmentation, lifecycle and journey mapping, and worked with the studio's strategists and UX team to turn the findings into a prioritised set of recommendations the client could act on."])
    b += figure("fig-pair shape-wide", [
        img(p, "farm", 1440, 960, "A farmer among pasture-raised chickens at sunrise"),
        img(p, "pouch", 1296, 864, "A pouch of organic beef bone broth beside a creek")])
    b += section("digital-outcome", "Outcome", [
        "The programme delivered a shared understanding of customers across direct, retail and practitioner channels, and a prioritised plan for the website. The conversion recommendations were implemented after user acceptance testing."],
        '        <p class="meta-label"><a href="https://byronbaybonebroth.com/" target="_blank" rel="noopener">Visit byronbaybonebroth.com</a></p>\n')
    b += nxt("elly-sofocli.html", "Elly Sofoclí")
    return head("Byron Bay Bone Broth", "Connecting B2B retail and practitioner channel growth with research-led customer experience for Byron Bay Bone Broth, delivered with Antimony Studio.") + b + FOOT


def elly():
    p = "elly-sofocli"
    b = intro("Elly Sofoclí", "Developing an international wholesale proposition for a Melbourne bridal designer", [
        ("Client", "Elly Sofoclí, bridal design, Melbourne"),
        ("Engagement", "From December 2023"),
        ("Workstreams", "Wholesale strategy, market research, business development, brand, website, content"),
        ("My role", "Account Director, Antimony Studio"),
    ])
    b += figure("fig-pair shape-tall", [
        img(p, "portrait-back", 1440, 1800, "Model in a strapless Elly Sofoclí gown with sculpted sleeves, seen from behind", lazy=False),
        img(p, "seated", 1440, 1800, "Model seated in a voluminous Elly Sofoclí gown against white drapery", lazy=False)],
        "Campaign photography courtesy of Elly Sofoclí.")
    b += section("context", "Business context", [
        "Elly Sofoclí designs contemporary bridal gowns from a flagship studio in Melbourne, with an established Australian retail business. In late 2023 the business set out to grow internationally through selected bridal boutiques."])
    b += section("challenge", "The challenge", [
        "Wholesale is a different conversation from retail. A boutique in New York or Seoul needs to understand the collection quickly, see a commercial offer that works for its own margins, and believe the label suits its customers. The proposition, the pricing and the way the brand presented itself all had to make that case before any introduction was made."])
    b += section("approach", "The approach", [
        "The programme combined commercial and creative work. On the commercial side, the team developed wholesale pricing and the product offer for partners, researched international markets, and identified boutiques that suited the brand.",
        "On the creative side, Antimony developed the brand identity, designed and built a new website, and set out a content plan, so the label presented consistently to brides and buyers alike."])
    b += section("contribution", "My contribution", [
        "I contributed to the wholesale pricing strategy and product offer, and was primarily responsible for the commercial research, initial business development and managing the creative delivery.",
        "That meant identifying markets and boutiques that were a genuine fit, making the first introductions, and coordinating the communications and creative assets that supported them across brand, web and content. Once introductions were established, Elly's sales team led final negotiations."],
        credit("Brand, design and development by the Antimony Studio team."))
    tiles = [("stationery", 1220, 1525, "The Elly Sofoclí wordmark embossed on textured stationery"),
             ("garment-bag", 1080, 1350, "Black garment bag ribbon printed with the Elly Sofoclí name"),
             ("hanger", 1440, 1800, "A black velvet hanger carrying the Elly Sofoclí wordmark"),
             ("studio", 1440, 1800, "The Elly Sofoclí studio, with a framed artwork and a white sofa")]
    b += ('    <figure class="cs-figure">\n      <div class="fig-tiles four shape-tall">\n'
          + "".join(img(p, n, w, h, a, TILE4).replace("      <img", "        <img") for n, w, h, a in tiles)
          + '      </div>\n      <figcaption class="meta-label">The identity carried through to the moments buyers and brides experience.</figcaption>\n    </figure>\n\n')
    b += section("outcome", "Outcome", [], result(
        ["Queensland", "New York", "China", "South Korea"],
        ["Stockist relationships opened through the programme in Queensland, New York, mainland China and South Korea. Elly's team then brought wholesale in-house and has continued to build the network, which now also includes boutiques in Hong Kong and Japan."],
        link=("https://www.ellysofocli.com/", "Visit ellysofocli.com")))
    b += nxt("femme-connection.html", "Femme Connection")
    return head("Elly Sofoclí", "Developing an international wholesale proposition for Melbourne bridal designer Elly Sofoclí, delivered with Antimony Studio.") + b + FOOT


def femme():
    p = "femme-connection"
    b = intro("Femme Connection", "Building customer retention through CRM, loyalty and lifecycle marketing", [
        ("Client", "Femme Connection, online womenswear, Australia"),
        ("Engagement", "2024 to 2026"),
        ("Workstreams", "Brand, website, communications strategy, Klaviyo email and SMS, Yotpo loyalty, partnerships"),
        ("My role", "Account Director, then Client Services Director, Antimony Studio"),
    ])
    tiles = [("tile-f", "F monogram on pink"), ("tile-c", "C monogram on coral"), ("tile-heart", "Pink heart on black"),
             ("tile-star", "White star on green"), ("tile-check", "Black check on sand"), ("tile-pink", "Solid pink panel")]
    b += ('    <figure class="cs-figure">\n      <div class="fig-tiles shape-tile">\n'
          + "".join(img(p, n, 1000, 1500, f"Femme Connection brand graphic: {a}", "(max-width: 600px) 33vw, 230px", lazy=False).replace("      <img", "        <img") for n, a in tiles)
          + '      </div>\n      <figcaption class="meta-label">Brand identity by Antimony Studio.</figcaption>\n    </figure>\n\n')
    b += section("context", "Business context", [
        "Femme Connection is an Australian online fashion retailer selling accessible, current womenswear, from occasion dresses to workwear."])
    b += section("challenge", "The challenge", [
        "When the engagement began, growth leaned heavily on paid social, and an audit found the ad account had no clear strategy for testing and scaling. The larger opportunity was retention: bringing first-time buyers back, rewarding loyal customers and building a channel the business owned."])
    b += section("approach", "The approach", [
        "Antimony started with the foundations: a new brand identity, website and communications strategy. A retention programme was then built on top.",
        "Klaviyo email and SMS flows covered each stage of the customer lifecycle, from welcome and abandoned cart to post-purchase and cross-sell, with A/B testing on every sequence. A Yotpo loyalty programme with VIP tiers and referrals rewarded repeat customers, while influencer, ambassador and affiliate programmes extended reach. Monthly reporting tied each channel back to revenue and set the next month's priorities."])
    b += figure("fig-pair shape-square", [
        img(p, "occasion", 688, 688, "Two models in red floral occasion dresses"),
        img(p, "everyday", 688, 688, "A model in a printed jacket and jeans seated in a sunlit room")])
    b += section("contribution", "My contribution", [
        "I led the client relationship for the length of the engagement, including the monthly performance reviews where results were reported and priorities agreed.",
        "I managed the email and CRM channel directly: planning campaigns around the retail calendar, overseeing the flow strategy and testing programme, and reviewing performance with the client. I also coordinated the studio's designers, developers and specialists across the brand, web, loyalty and partnership work."],
        credit("Brand identity, website design and development, and campaign production by the Antimony Studio team."))
    b += section("outcome", "Outcome", [], result(
        ["$30,000 to $120,000 a month"],
        ["Over the engagement, monthly revenue from the email channel grew from around $30,000 to around $120,000. Automated flows were a growing part of that: in January 2026, flow revenue was 60% higher than a year earlier, and flows were converting at a higher rate even as the audience grew."],
        note="Flow figures from Klaviyo reporting, January 2026 compared with January 2025.",
        link=("https://femmeconnection.com.au/", "Visit femmeconnection.com.au")))
    b += nxt("rt-edgar.html", "RT Edgar")
    return head("Femme Connection", "Building customer retention through CRM, loyalty and lifecycle marketing for online fashion retailer Femme Connection, delivered with Antimony Studio.") + b + FOOT


if __name__ == "__main__":
    for name, fn in [("rt-edgar", rt_edgar), ("byron-bay-bone-broth", bbbb),
                     ("elly-sofocli", elly), ("femme-connection", femme)]:
        (ROOT / "work" / f"{name}.html").write_text(fn())
        print("wrote", name)
