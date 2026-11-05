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
