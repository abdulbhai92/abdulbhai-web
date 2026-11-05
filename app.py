from flask import Flask, render_template_string, request

app = Flask(__name__)

# Base Layout with Navbar, Footer & Styling
BASE_LAYOUT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
  
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
