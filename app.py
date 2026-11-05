from flask import Flask, render_template_string, request

app = Flask(__name__)

# Base Layout with Navbar, Footer & Styling
BASE_LAYOUT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} | Abdul Bhai - Official Portal</title>
    <meta name="description" content="Official Website of Abdul Bhai (Abdul Rasool) - President Markazi Tajir Ittehad Thatta, Vice Chairman New Al-Noor Group of Companies Thatta, AI Expert, SEO Specialist & Content Writer.">
    <style>
        :root {
            --bg-dark: #090d16;
            --bg-card: #131c2e;
            --primary: #38bdf8;
            --gold: #f59e0b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border: #1e293b;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', system-ui, sans-serif; scroll-behavior: smooth; }
        body { background: var(--bg-dark); color: var(--text-main); line-height: 1.7; display: flex; flex-direction: column; min-height: 100vh; }
        
        /* Top Bar */
        .topbar { background: #05080f; border-bottom: 1px solid var(--border); padding: 8px 6%; display: flex; justify-content: space-between; font-size: 13px; color: var(--text-muted); flex-wrap: wrap; gap: 10px; }
        .topbar span strong { color: var(--gold); }

        /* Navigation */
        nav { background: rgba(19, 28, 46, 0.95); backdrop-filter: blur(10px); padding: 18px 6%; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; border-bottom: 1px solid var(--border); flex-wrap: wrap; gap: 15px; }
        .logo { font-size: 26px; font-weight: 800; color: var(--text-main); text-decoration: none; letter-spacing: 0.5px; }
        .logo span { color: var(--primary); }
        .nav-links { display: flex; gap: 22px; list-style: none; flex-wrap: wrap; align-items: center; }
        .nav-links a { color: var(--text-muted); text-decoration: none; font-weight: 500; font-size: 15px; transition: 0.2s; }
        .nav-links a:hover, .nav-links a.active { color: var(--primary); }
        .btn-nav { background: linear-gradient(135deg, var(--primary), #0284c7); color: #090d16 !important; padding: 9px 20px; border-radius: 8px; font-weight: 700 !important; }

        /* Hero & Sections */
        .container { max-width: 1200px; margin: 0 auto; padding: 60px 6%; flex: 1; width: 100%; }
        .hero { padding: 80px 6%; text-align: center; background: radial-gradient(circle at top, #1e293b 0%, var(--bg-dark) 70%); border-bottom: 1px solid var(--border); }
        .badge { display: inline-block; background: rgba(245, 158, 11, 0.12); color: var(--gold); border: 1px solid rgba(245, 158, 11, 0.4); padding: 6px 18px; border-radius: 30px; font-size: 13px; font-weight: 600; margin-bottom: 20px; }
        .hero h1 { font-size: 46px; font-weight: 800; line-height: 1.2; margin-bottom: 20px; max-width: 850px; margin-left: auto; margin-right: auto; }
        .hero h1 span { color: var(--primary); }
        .hero p { font-size: 19px; color: var(--text-muted); max-width: 750px; margin: 0 auto 35px; }
        .btn-group { display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; }
        .btn { padding: 13px 28px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 15px; transition: 0.25s; display: inline-block; border: none; cursor: pointer; }
        .btn-primary { background: var(--primary); color: #090d16; }
        .btn-primary:hover { background: #0284c7; color: #fff; }
        .btn-outline { background: transparent; color: var(--text-main); border: 1px solid var(--border); }
        .btn-outline:hover { border-color: var(--primary); color: var(--primary); }

        /* Stats Strip */
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; background: var(--bg-card); padding: 35px 6%; border-bottom: 1px solid var(--border); text-align: center; }
        .stat-box h2 { font-size: 36px; color: var(--gold); margin-bottom: 5px; }
        .stat-box p { color: var(--text-muted); font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }

        /* Grid & Cards */
        .section-title { text-align: center; margin-bottom: 45px; }
        .section-title h2 { font-size: 34px; margin-bottom: 12px; }
        .section-title h2 span { color: var(--primary); }
        .section-title p { color: var(--text-muted); max-width: 650px; margin: 0 auto; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-bottom: 50px; }
        .card { background: var(--bg-card); border: 1px solid var(--border); padding: 30px; border-radius: 14px; transition: 0.3s; }
        .card:hover { transform: translateY(-5px); border-color: var(--primary); }
        .card-tag { font-size: 12px; font-weight: 700; color: var(--gold); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; display: block; }
        .card h3 { font-size: 22px; margin-bottom: 12px; color: var(--text-main); }
        .card p { color: var(--text-muted); font-size: 15px; margin-bottom: 15px; }
        .card ul { padding-left: 18px; color: var(--text-muted); font-size: 14px; margin-bottom: 15px; }
        .card ul li { margin-bottom: 6px; }

        /* Forms & Interactive Tools */
        .form-box { background: var(--bg-card); border: 1px solid var(--border); padding: 35px; border-radius: 14px; max-width: 750px; margin: 0 auto; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px; }
        .form-group input, .form-group textarea { width: 100%; padding: 14px; background: var(--bg-dark); border: 1px solid var(--border); color: #fff; border-radius: 8px; font-size: 15px; }
        .form-group input:focus, .form-group textarea:focus { outline: none; border-color: var(--primary); }
        .alert-success { background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #34d399; padding: 15px; border-radius: 8px; margin-bottom: 20px; }

        /* FAQ & Long Content */
        .faq-item { background: var(--bg-card); border: 1px solid var(--border); padding: 22px; border-radius: 10px; margin-bottom: 15px; }
        .faq-item h4 { color: var(--primary); font-size: 18px; margin-bottom: 8px; }
        .prose h3 { color: var(--primary); margin: 25px 0 10px; }
        .prose p { color: var(--text-muted); margin-bottom: 15px; }

        /* Floating WhatsApp */
        .whatsapp-float { position: fixed; bottom: 25px; right: 25px; background: #25d366; color: #fff; padding: 12px 20px; border-radius: 50px; font-weight: 700; text-decoration: none; box-shadow: 0 8px 20px rgba(0,0,0,0.4); z-index: 999; display: flex; align-items: center; gap: 8px; font-size: 14px; }

        /* Footer */
        footer { background: #05080f; border-top: 1px solid var(--border); padding: 60px 6% 25px; margin-top: auto; }
        .footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 35px; max-width: 1200px; margin: 0 auto 40px; }
        .footer-col h4 { color: var(--text-main); margin-bottom: 16px; font-size: 18px; }
        .footer-col p, .footer-col a { color: var(--text-muted); font-size: 14px; text-decoration: none; display: block; margin-bottom: 10px; }
        .footer-col a:hover { color: var(--primary); }
        .copyright { text-align: center; border-top: 1px solid var(--border); padding-top: 25px; color: #64748b; font-size: 13px; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 32px; }
            .nav-links { gap: 12px; font-size: 14px; }
        }
    </style>
</head>
<body>
    <div class="topbar">
        <span>🏛️ <strong>President:</strong> Markazi Tajir Ittehad Thatta | <strong>Vice Chairman:</strong> New Al-Noor Group of Companies Thatta</span>
        <span>📍 Makli / Thatta, Sindh, Pakistan | ✉️ contact@abdulbhai.com</span>
    </div>

    <nav>
        <a href="/" class="logo">Abdul<span>Bhai</span>.com</a>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/about">About Abdul Bhai</a></li>
            <li><a href="/services">Business & Services</a></li>
            <li><a href="/tools">Free AI & SEO Tools</a></li>
            <li><a href="/blog">Articles & SEO Blog</a></li>
            <li><a href="/contact" class="btn-nav">Contact Us</a></li>
        </ul>
    </nav>

    {{ content | safe }}

    <a href="/contact" class="whatsapp-float">💬 Connect with Abdul Bhai</a>

    <footer>
        <div class="footer-grid">
            <div class="footer-col">
                <h4>AbdulBhai.com</h4>
                <p>Official Digital Portal of Abdul Bhai (Abdul Rasool) — Business Leader, Trade Union President, AI Automation Expert, SEO Strategist, and Content Writer in Thatta, Sindh.</p>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <a href="/">Home Page</a>
                <a href="/about">Leadership & Biography</a>
                <a href="/services">New Al-Noor Group & Tech</a>
                <a href="/tools">Free SEO Analyzer Tool</a>
            </div>
            <div class="footer-col">
                <h4>Expertise & Ventures</h4>
                <a href="/services">New Al-Noor Haier Store Makli</a>
                <a href="/services">Markazi Tajir Ittehad Thatta</a>
                <a href="/services">AI & Python Web Solutions</a>
                <a href="/services">SEO & Content Writing</a>
            </div>
            <div class="footer-col">
                <h4>Legal & Support</h4>
                <a href="/blog">Latest Tech & Business Blog</a>
                <a href="/contact">Book a Consultation</a>
                <a href="/privacy-policy">Privacy Policy & Terms</a>
            </div>
        </div>
        <div class="copyright">
            &copy; 2026 AbdulBhai.com | Powered by Python & Flask | All Rights Reserved.
        </div>
    </footer>
</body>
</html>
"""

def render_page(title, content_html):
    return render_template_string(BASE_LAYOUT, title=title, content=content_html)

# 1. HOME PAGE (LONG MULTI-SECTION)
@app.route('/')
def home():
    content = """
    <section class="hero">
        <div class="badge">⭐ Leadership • Business • Artificial Intelligence • SEO</div>
        <h1>Welcome to the Official Portal of <span>Abdul Bhai</span></h1>
        <p><strong>President of Markazi Tajir Ittehad Thatta</strong> & <strong>Vice Chairman of New Al-Noor Group of Companies Thatta</strong>. Empowering businesses across Sindh through trade leadership, modern home appliances retail, AI automation, SEO mastery, and high-converting content.</p>
        <div class="btn-group">
            <a href="/services" class="btn btn-primary">Explore Businesses & Services</a>
            <a href="/about" class="btn btn-outline">Read Full Biography</a>
        </div>
    </section>

    <section class="stats">
        <div class="stat-box">
            <h2>President</h2>
            <p>Markazi Tajir Ittehad Thatta</p>
        </div>
        <div class="stat-box">
            <h2>Vice Chairman</h2>
            <p>New Al-Noor Group Thatta</p>
        </div>
        <div class="stat-box">
            <h2>100+</h2>
            <p>AI, SEO & Web Projects</p>
        </div>
        <div class="stat-box">
            <h2>#1 Trusted</h2>
            <p>Electronics & Business Hub</p>
        </div>
    </section>

    <div class="container">
        <div class="section-title">
            <h2>Two Worlds of <span>Excellence</span></h2>
            <p>Bridging traditional commercial leadership in Thatta & Makli with global digital innovation in AI, SEO, and Content Engineering.</p>
        </div>

        <div class="grid">
            <div class="card">
                <span class="card-tag">Trade Leadership</span>
                <h3>Markazi Tajir Ittehad Thatta</h3>
                <p>Serving as President to protect, unite, and advance the business community of Thatta and Makli. Advocating for fair commerce, infrastructure growth, and trader welfare.</p>
                <ul>
                    <li>Voice of local merchants & industrialists</li>
                    <li>Dispute resolution & chamber coordination</li>
                    <li>Promoting safe & thriving local markets</li>
                </ul>
            </div>

            <div class="card">
                <span class="card-tag">Corporate & Retail</span>
                <h3>New Al-Noor Group of Companies</h3>
                <p>As Vice Chairman, spearheading commercial ventures including the flagship <strong>New Al-Noor Haier Store</strong> (Opposite DIG Petrol Pump, Makli) offering genuine home appliances.</p>
                <ul>
                    <li>Official Haier Air Conditioners & Refrigerators</li>
                    <li>LED TVs, Washing Machines & Kitchen Appliances</li>
                    <li>Affordable pricing & reliable local warranty</li>
                </ul>
            </div>

            <div class="card">
                <span class="card-tag">Digital & Tech Mastery</span>
                <h3>AI Expert, SEO & Content Writer</h3>
                <p>Helping Pakistani and international brands dominate Google rankings and automate workflows using Python, Artificial Intelligence, and semantic SEO content strategies.</p>
                <ul>
                    <li>Technical & Local SEO (#1 Google Rankings)</li>
                    <li>AI Agents, Python Web Apps & ERP Tools</li>
                    <li>High-converting SEO Content & Copywriting</li>
                </ul>
            </div>
        </div>

        <div class="section-title">
            <h2>Why Work With <span>Abdul Bhai?</span></h2>
            <p>A rare combination of real-world street-smart business acumen and cutting-edge technical expertise.</p>
        </div>

        <div class="grid">
            <div class="card">
                <h3>1. Proven Business Credibility</h3>
                <p>Leading thousands of traders in Thatta and managing multi-venture retail operations gives practical insight into what actually drives sales and customer trust.</p>
            </div>
            <div class="card">
                <h3>2. Data-Driven SEO & Content</h3>
                <p>Not just theory—every article, keyword strategy, and website structure is built to capture real buyer traffic and rank on the first page of search engines.</p>
            </div>
            <div class="card">
                <h3>3. Modern AI & Python Stack</h3>
                <p>From lightning-fast cloud websites to automated AI workflows, we build digital assets that save time and scale effortlessly.</p>
            </div>
        </div>

        <div class="section-title">
            <h2>Frequently Asked <span>Questions</span></h2>
            <p>Quick answers about our commercial stores, trade union office, and digital consulting services.</p>
        </div>

        <div class="faq-item">
            <h4>Where is New Al-Noor Haier Store located?</h4>
            <p>New Al-Noor Haier Store is conveniently located in Makli, Thatta, right opposite the DIG Petrol Pump. Visit us for the best deals on ACs, refrigerators, and home electronics.</p>
        </div>
        <div class="faq-item">
            <h4>How can I contact Abdul Bhai for SEO, AI, or Content Writing projects?</h4>
            <p>You can use our Contact Us page to send a direct message or reach out via email at contact@abdulbhai.com for website development, SEO audits, and content strategy.</p>
        </div>
        <div class="faq-item">
            <h4>How can local merchants join or approach Markazi Tajir Ittehad Thatta?</h4>
            <p>Traders and shopkeepers across Thatta and Makli can reach out through the official secretariat or contact portal for business support and community representation.</p>
        </div>
    </div>
    """
    return render_page("Home - President Markazi Tajir Ittehad & AI Expert", content)

# 2. ABOUT PAGE
@app.route('/about')
def about():
    content = """
    <section class="hero">
        <div class="badge">👤 Executive Profile & Biography</div>
        <h1>About <span>Abdul Bhai</span></h1>
        <p>Businessman, Community Leader, AI Innovator, and Digital Strategist from Thatta, Sindh.</p>
    </section>

    <div class="container prose">
        <div class="grid">
            <div class="card">
                <span class="card-tag">Mission Statement</span>
                <h3>Empowering Commerce & Technology</h3>
                <p>Abdul Bhai's mission is twofold: to uplift the local business ecosystem of Thatta through strong leadership and reliable retail enterprises, and to empower modern entrepreneurs with AI, SEO, and world-class digital content.</p>
                <h3>Core Leadership Roles</h3>
                <ul>
                    <li><strong>President:</strong> Markazi Tajir Ittehad Thatta</li>
                    <li><strong>Vice Chairman:</strong> New Al-Noor Group of Companies Thatta</li>
                    <li><strong>Founder & Technologist:</strong> AbdulBhai.com Digital & AI Hub</li>
                </ul>
            </div>
            <div class="card">
                <span class="card-tag">Digital Capabilities</span>
                <h3>The Tech & Marketing Side</h3>
                <p>Alongside leading brick-and-mortar enterprises, Abdul Bhai is a dedicated technologist and digital marketer specializing in:</p>
                <ul>
                    <li><strong>Artificial Intelligence (AI):</strong> Prompt engineering, AI workflow automation, custom AI tools, and smart business integrations.</li>
                    <li><strong>Search Engine Optimization (SEO):</strong> On-page, Off-page, Technical, and Local Google Business Profile SEO.</li>
                    <li><strong>Content Writing:</strong> Authority blog posts, commercial copywriting, product descriptions, and brand storytelling.</li>
                    <li><strong>Web Development:</strong> Python, Flask, cloud deployment, and e-commerce solutions.</li>
                </ul>
            </div>
        </div>
    </div>
    """
    return render_page("About Abdul Bhai - Biography & Leadership", content)

# 3. SERVICES & BUSINESSES PAGE
@app.route('/services')
def services():
    content = """
    <section class="hero">
        <div class="badge">💼 Ventures & Digital Solutions</div>
        <h1>Our <span>Businesses & Services</span></h1>
        <p>Explore our retail divisions under New Al-Noor Group Thatta and our global digital services in AI, SEO, and Content Writing.</p>
    </section>

    <div class="container">
        <div class="grid">
            <div class="card">
                <span class="card-tag">Retail & Electronics</span>
                <h3>New Al-Noor Haier Store (Makli)</h3>
                <p>Located opposite DIG Petrol Pump in Makli, providing 100% original Haier appliances at the most competitive prices in Thatta district.</p>
                <ul>
                    <li>DC Inverter Air Conditioners</li>
                    <li>Deep Freezers & Smart Refrigerators</li>
                    <li>Automatic Washing Machines & LEDs</li>
                </ul>
                <a href="/contact" class="btn btn-primary">Inquire About Appliances</a>
            </div>

            <div class="card">
                <span class="card-tag">Search Engine Dominance</span>
                <h3>Complete SEO Services</h3>
                <p>Rank your business website on the 1st page of Google and get consistent organic customers without paying for expensive ads.</p>
                <ul>
                    <li>Complete Website SEO Audit</li>
                    <li>High-Volume Keyword Research</li>
                    <li>Local SEO (Google Maps Ranking)</li>
                </ul>
                <a href="/contact" class="btn btn-primary">Order SEO Audit</a>
            </div>

            <div class="card">
                <span class="card-tag">Authority Writing</span>
                <h3>Professional Content Writing</h3>
                <p>Human-crafted, SEO-optimized content that engages readers, builds brand authority, and passes all search engine quality benchmarks.</p>
                <ul>
                    <li>Long-Form Blog Articles & Guides</li>
                    <li>Website Landing Page Copywriting</li>
                    <li>E-Commerce Product Descriptions</li>
                </ul>
                <a href="/contact" class="btn btn-primary">Hire Content Writer</a>
            </div>

            <div class="card">
                <span class="card-tag">Next-Gen Tech</span>
                <h3>AI Automation & Python Web Apps</h3>
                <p>Custom web portals, ERP dashboards, traffic tools, and AI-powered automation designed to modernize your business operations.</p>
                <ul>
                    <li>Python Flask / FastAPI Web Portals</li>
                    <li>Custom AI Chatbots & Agents</li>
                    <li>E-Commerce Store Development</li>
                </ul>
                <a href="/contact" class="btn btn-primary">Start Tech Project</a>
            </div>
        </div>
    </div>
    """
    return render_page("Services & New Al-Noor Group Ventures", content)

# 4. INTERACTIVE PYTHON SEO TOOL PAGE
@app.route('/tools', methods=['GET', 'POST'])
def tools():
    result_html = ""
    sample_text = ""
    if request.method == 'POST':
        sample_text = request.form.get('content_text', '')
        words = [w for w in sample_text.split() if w.strip()]
        word_count = len(words)
        char_count = len(sample_text)
        sentence_count = max(1, sample_text.count('.') + sample_text.count('!') + sample_text.count('?')) if sample_text.strip() else 0
        reading_time = round(word_count / 200, 1)
        seo_score = "Excellent (Ready to Rank!)" if word_count >= 300 else "Needs More Content (Aim for 300+ words for SEO)"
        
        result_html = f"""
        <div class="alert-success">
            <h4>📊 Live Python SEO Analysis Results:</h4>
            <p><strong>Word Count:</strong> {word_count} words | <strong>Characters:</strong> {char_count} | <strong>Sentences:</strong> {sentence_count}</p>
            <p><strong>Estimated Reading Time:</strong> {reading_time} min | <strong>SEO Verdict:</strong> {seo_score}</p>
        </div>
        """

    content = f"""
    <section class="hero">
        <div class="badge">🛠️ Powered by Python</div>
        <h1>Free <span>AI & SEO Tools</span> by Abdul Bhai</h1>
        <p>Test your article length, reading time, and SEO readiness instantly with our built-in Python Content Analyzer.</p>
    </section>

    <div class="container">
        <div class="form-box">
            {result_html}
            <form method="POST" action="/tools">
                <div class="form-group">
                    <label>Paste Your Article or Website Content Below:</label>
                    <textarea name="content_text" rows="8" placeholder="Paste your blog post or SEO article here to check word count, reading time, and SEO score...">{sample_text}</textarea>
                </div>
                <button type="submit" class="btn btn-primary">Analyze Content Now (Python)</button>
            </form>
        </div>
    </div>
    """
    return render_page("Free SEO & Content Tools", content)

# 5. BLOG / ARTICLES PAGE
@app.route('/blog')
def blog():
    content = """
    <section class="hero">
        <div class="badge">✍️ Insights & Guides</div>
        <h1>Official <span>Blog & Articles</span></h1>
        <p>Expert articles on Artificial Intelligence, SEO strategies, Content Writing, and Business Growth in Pakistan.</p>
    </section>

    <div class="container">
        <div class="grid">
            <div class="card">
                <span class="card-tag">SEO Guide • 2026</span>
                <h3>How Local Businesses in Sindh Can Rank #1 on Google Maps</h3>
                <p>A complete step-by-step guide by Abdul Bhai on optimizing your Google Business Profile to attract daily walk-in customers in cities like Thatta, Makli, and Hyderabad.</p>
            </div>
            <div class="card">
                <span class="card-tag">Artificial Intelligence</span>
                <h3>Top 5 AI Workflows Every Businessman Should Use Today</h3>
                <p>Discover how modern entrepreneurs are saving 10+ hours a week using AI tools for customer support, inventory planning, and automated content creation.</p>
            </div>
            <div class="card">
                <span class="card-tag">Home Appliances Guide</span>
                <h3>Choosing the Best Inverter AC for Intense Summer Heat</h3>
                <p>Buying advice from New Al-Noor Haier Store Makli on selecting energy-efficient DC Inverter Air Conditioners that cut electricity bills in half.</p>
            </div>
        </div>
    </div>
    """
    return render_page("Blog - AI, SEO & Business Insights", content)

# 6. CONTACT US PAGE
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    msg_alert = ""
    if request.method == 'POST':
        user_name = request.form.get('name', 'Visitor')
        msg_alert = f'<div class="alert-success">Shukriya <strong>{user_name}</strong>! Aapka message Abdul Bhai ki team ko mil gaya hai. Hum jald rabta karenge.</div>'

    content = f"""
    <section class="hero">
        <div class="badge">📞 Get In Touch</div>
        <h1>Contact <span>Abdul Bhai</span></h1>
        <p>Reach out for business collaborations, New Al-Noor Group inquiries, Markazi Tajir Ittehad matters, or AI & SEO services.</p>
    </section>

    <div class="container">
        <div class="grid">
            <div class="card">
                <span class="card-tag">Direct Channels</span>
                <h3>Office & Store Locations</h3>
                <p><strong>🏢 Corporate & Trade Office:</strong><br>Markazi Tajir Ittehad / New Al-Noor Group Secretariat, Thatta, Sindh.</p>
                <p><strong>🏬 Flagship Retail Store:</strong><br>New Al-Noor Haier Store, Opposite DIG Petrol Pump, Makli, Thatta.</p>
                <p><strong>✉️ Official Email:</strong><br>contact@abdulbhai.com</p>
            </div>

            <div class="form-box" style="margin:0; width:100%;">
                {msg_alert}
                <form method="POST" action="/contact">
                    <div class="form-group">
                        <label>Your Full Name</label>
                        <input type="text" name="name" required placeholder="Enter your name">
                    </div>
                    <div class="form-group">
                        <label>Phone / WhatsApp Number</label>
                        <input type="text" name="phone" required placeholder="0300-XXXXXXX">
                    </div>
                    <div class="form-group">
                        <label>Subject (Business / Haier Store / SEO & AI / Tajir Ittehad)</label>
                        <input type="text" name="subject" required placeholder="How can we help you?">
                    </div>
                    <div class="form-group">
                        <label>Your Message</label>
                        <textarea name="message" rows="4" required placeholder="Write your complete message here..."></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Send Message</button>
                </form>
            </div>
        </div>
    </div>
    """
    return render_page("Contact Abdul Bhai", content)

# 7. PRIVACY POLICY & TERMS PAGE (FOR GOOGLE ADSENSE & TRUST)
@app.route('/privacy-policy')
def privacy():
   
    </div>
    """
    return render_page("Privacy Policy & Terms", content)

if __name__ == '__main__':
    app.run(debug=True)
