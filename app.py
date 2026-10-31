from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdul Bhai - Official Website</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
        body { background: #0f172a; color: #f8fafc; display: flex; flex-direction: column; min-height: 100vh; }
        nav { padding: 20px 8%; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; }
        .logo { font-size: 24px; font-weight: 700; color: #38bdf8; text-decoration: none; }
        .hero { flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 40px 20px; }
        .badge { background: #1e293b; color: #38bdf8; padding: 6px 16px; border-radius: 20px; font-size: 14px; margin-bottom: 20px; border: 1px solid #334155; }
        h1 { font-size: 48px; margin-bottom: 16px; }
        h1 span { color: #38bdf8; }
        p { font-size: 18px; color: #94a3b8; max-width: 600px; margin-bottom: 30px; line-height: 1.6; }
        .cards { display: flex; gap: 20px; flex-wrap: wrap; justify-content: center; max-width: 900px; margin-top: 20px; }
        .card { background: #1e293b; padding: 24px; border-radius: 12px; width: 260px; border: 1px solid #334155; text-align: left; }
        .card h3 { color: #38bdf8; margin-bottom: 10px; }
        .card p { font-size: 14px; margin-bottom: 0; }
        .btn { background: #38bdf8; color: #0f172a; padding: 12px 28px; border-radius: 8px; font-weight: 600; text-decoration: none; transition: 0.2s; }
        .btn:hover { background: #0284c7; color: #fff; }
        footer { text-align: center; padding: 20px; color: #64748b; font-size: 14px; border-top: 1px solid #1e293b; }
    </style>
</head>
<body>
    <nav>
        <a href="/" class="logo">AbdulBhai.com</a>
        <a href="mailto:contact@abdulbhai.com" class="btn">Contact Me</a>
    </nav>
    <div class="hero">
        <div class="badge">⚡ Powered by Python & Flask</div>
        <h1>Welcome to <span>Abdul Bhai</span></h1>
        <p>Official portal for Digital Services, Web Solutions, AI Tools, and E-Commerce projects.</p>
        <div class="cards">
            <div class="card">
                <h3>Web & Python</h3>
                <p>Fast, secure, and modern cloud web applications built on Python.</p>
            </div>
            <div class="card">
                <h3>Digital Tools & AI</h3>
                <p>Smart automation, traffic tools, and ERP solutions for businesses.</p>
            </div>
            <div class="card">
                <h3>E-Commerce</h3>
                <p>Complete online store setups and digital growth strategies.</p>
            </div>
        </div>
    </div>
    <footer>
        &copy; 2026 AbdulBhai.com | All Rights Reserved.
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(debug=True)