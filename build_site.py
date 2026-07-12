import os
import json
from datetime import datetime
import random
import urllib.parse

SITE_URL = "https://tax-filing-guide-military.bongshai.com"
BRAND_NAME = "MilTax Guide"

ARTICLES = [
    {"slug": "military-tax-filing-basics", "title": "Military Tax Filing Basics: A Complete Guide", "category": "basics"},
    {"slug": "combat-zone-tax-exclusion", "title": "Combat Zone Tax Exclusion (CZTE) Explained", "category": "deployment"},
    {"slug": "deployment-tax-extensions", "title": "How Deployment Affects Your Tax Deadlines", "category": "deployment"},
    {"slug": "pcs-moving-expenses-tax-deductions", "title": "Are PCS Moving Expenses Tax Deductible?", "category": "deductions"},
    {"slug": "military-spouse-residency-relief-act", "title": "MSRRA: Military Spouse Residency Relief Act Guide", "category": "spouses"},
    {"slug": "state-taxes-for-active-duty", "title": "State Taxes for Active Duty Military: What to Know", "category": "state-taxes"},
    {"slug": "tax-free-allowances-bah-bas", "title": "Are BAH and BAS Taxable?", "category": "allowances"},
    {"slug": "thrift-savings-plan-taxes", "title": "Thrift Savings Plan (TSP) Tax Implications", "category": "retirement"},
    {"slug": "veterans-benefits-taxability", "title": "Are Veterans Benefits Taxable?", "category": "veterans"},
    {"slug": "earned-income-tax-credit-military", "title": "Earned Income Tax Credit (EITC) for Military", "category": "credits"},
    {"slug": "child-tax-credit-military-families", "title": "Child Tax Credit Guide for Military Families", "category": "credits"},
    {"slug": "rotc-scholarships-tax-status", "title": "Are ROTC Scholarships Taxable?", "category": "education"},
    {"slug": "gi-bill-tax-implications", "title": "GI Bill Benefits: Are They Tax-Free?", "category": "education"},
    {"slug": "military-pension-tax-guide", "title": "Military Retirement Pension Tax Guide", "category": "retirement"},
    {"slug": "survivor-benefit-plan-taxes", "title": "Survivor Benefit Plan (SBP) Tax Rules", "category": "spouses"},
    {"slug": "free-tax-filing-for-military", "title": "Best Free Tax Filing Options for Military", "category": "basics"},
    {"slug": "mil-tax-software-reviews", "title": "Top Tax Software for Military Personnel", "category": "basics"},
    {"slug": "reservist-travel-expenses", "title": "Tax Deductions for National Guard and Reservists", "category": "deductions"},
    {"slug": "uniform-deductions", "title": "Can You Deduct Military Uniforms on Your Taxes?", "category": "deductions"},
    {"slug": "home-sale-tax-exclusion-military", "title": "Home Sale Tax Exclusion for Military Families", "category": "real-estate"},
    {"slug": "va-loan-tax-deductions", "title": "VA Loan Tax Benefits and Deductions", "category": "real-estate"},
    {"slug": "rental-property-taxes-military", "title": "Renting Out Your Home During PCS: Tax Guide", "category": "real-estate"},
    {"slug": "overseas-tax-filing", "title": "Filing Taxes While Stationed Overseas", "category": "deployment"},
    {"slug": "foreign-earned-income-exclusion", "title": "Foreign Earned Income Exclusion for Spouses", "category": "spouses"},
    {"slug": "military-contractor-taxes", "title": "Tax Guide for Military Contractors Overseas", "category": "deployment"},
    {"slug": "w2-understanding-military", "title": "How to Read Your Military W-2", "category": "basics"},
    {"slug": "ira-contributions-combat-zone", "title": "IRA Contributions While in a Combat Zone", "category": "retirement"},
    {"slug": "signing-bonus-taxes", "title": "Are Military Enlistment Bonuses Taxed?", "category": "allowances"},
    {"slug": "severance-pay-taxability", "title": "Military Severance Pay Tax Rules", "category": "basics"},
    {"slug": "tax-scams-targeting-military", "title": "Common Tax Scams Targeting Military Families", "category": "basics"},
    {"slug": "audit-guide-military", "title": "What to Do If You Get Audited as a Service Member", "category": "basics"}
]

CATEGORIES = {
    "basics": "Filing Basics",
    "deployment": "Deployment & Overseas",
    "deductions": "Deductions & Expenses",
    "spouses": "Military Spouses",
    "state-taxes": "State Taxes",
    "allowances": "Allowances & Bonuses",
    "retirement": "Retirement & TSP",
    "veterans": "Veterans Benefits",
    "credits": "Tax Credits",
    "education": "Education Benefits",
    "real-estate": "Real Estate & PCS"
}

def create_directories():
    for d in ['css', 'js', 'articles', 'categories']:
        os.makedirs(d, exist_ok=True)

def generate_css():
    css = """
:root {
    --primary-color: #0B2447;
    --secondary-color: #19376D;
    --accent-color: #576CBC;
    --highlight-color: #A5D7E8;
    --text-color: #333333;
    --text-light: #666666;
    --bg-color: #F8F9FA;
    --card-bg: #FFFFFF;
    --border-color: #E2E8F0;
    --success-color: #10B981;
    --nav-bg: rgba(255, 255, 255, 0.85);
    
    --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
    --font-serif: 'Merriweather', serif;
    
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 2rem;
    --spacing-xl: 4rem;
    
    --border-radius: 8px;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.05);
    --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
    
    --transition: all 0.3s ease;
}

[data-theme="dark"] {
    --primary-color: #A5D7E8;
    --secondary-color: #576CBC;
    --accent-color: #19376D;
    --text-color: #E2E8F0;
    --text-light: #94A3B8;
    --bg-color: #0F172A;
    --card-bg: #1E293B;
    --border-color: #334155;
    --nav-bg: rgba(15, 23, 42, 0.85);
}

* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-sans); color: var(--text-color); background-color: var(--bg-color); line-height: 1.6; -webkit-font-smoothing: antialiased; transition: background-color var(--transition), color var(--transition); }
h1, h2, h3, h4 { font-weight: 700; line-height: 1.2; margin-bottom: var(--spacing-md); color: var(--primary-color); }
h1 { font-size: 2.5rem; } h2 { font-size: 2rem; } h3 { font-size: 1.5rem; }
p { margin-bottom: var(--spacing-md); }
a { color: var(--accent-color); text-decoration: none; transition: var(--transition); }
a:hover { color: var(--primary-color); }

.container { max-width: 1200px; margin: 0 auto; padding: 0 var(--spacing-md); }
header { background-color: var(--nav-bg); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); position: sticky; top: 0; z-index: 1000; border-bottom: 1px solid var(--border-color); }
.nav-wrapper { display: flex; justify-content: space-between; align-items: center; height: 70px; }
.brand { font-size: 1.5rem; font-weight: 800; color: var(--primary-color); display: flex; align-items: center; gap: 0.5rem; }
.nav-links { display: flex; gap: var(--spacing-lg); list-style: none; }
.nav-links a { color: var(--text-color); font-weight: 500; position: relative; }
.nav-links a::after { content: ''; position: absolute; width: 0; height: 2px; bottom: -4px; left: 0; background-color: var(--accent-color); transition: var(--transition); }
.nav-links a:hover::after { width: 100%; }
.nav-actions { display: flex; align-items: center; gap: var(--spacing-md); }

.btn { padding: 0.5rem 1rem; border-radius: var(--border-radius); font-weight: 600; cursor: pointer; border: none; transition: var(--transition); display: inline-block; }
.btn-primary { background-color: var(--primary-color); color: #fff !important; }
.btn-primary:hover { background-color: var(--secondary-color); transform: translateY(-2px); box-shadow: var(--shadow-md); }
.theme-toggle, .menu-toggle { background: none; border: none; color: var(--text-color); cursor: pointer; }
.theme-toggle { font-size: 1.2rem; } .menu-toggle { display: none; font-size: 1.5rem; }

@media (max-width: 768px) {
    .nav-links { display: none; position: absolute; top: 70px; left: 0; width: 100%; background-color: var(--card-bg); flex-direction: column; padding: var(--spacing-md); box-shadow: var(--shadow-md); }
    .nav-links.active { display: flex; }
    .menu-toggle { display: block; }
}

.hero { padding: var(--spacing-xl) 0; background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%); color: #fff; text-align: center; border-radius: 0 0 2rem 2rem; margin-bottom: var(--spacing-xl); }
.hero h1 { color: #fff; margin-bottom: var(--spacing-md); font-size: 3rem; }
.hero p { font-size: 1.25rem; max-width: 600px; margin: 0 auto var(--spacing-lg); opacity: 0.9; }

.main-grid { display: grid; grid-template-columns: 1fr 300px; gap: var(--spacing-xl); margin-bottom: var(--spacing-xl); }
@media (max-width: 992px) { .main-grid { grid-template-columns: 1fr; } }

.article-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: var(--spacing-lg); }
.article-card { background: var(--card-bg); border-radius: var(--border-radius); padding: var(--spacing-lg); box-shadow: var(--shadow-sm); border: 1px solid var(--border-color); transition: var(--transition); display: flex; flex-direction: column; }
.article-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-lg); }
.category-tag { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: var(--accent-color); font-weight: 700; margin-bottom: var(--spacing-sm); display: inline-block; }
.article-card h2 { font-size: 1.25rem; margin-bottom: var(--spacing-sm); flex-grow: 1; }
.article-card p { color: var(--text-light); font-size: 0.9rem; margin-bottom: var(--spacing-md); }

.article-header { text-align: center; max-width: 800px; margin: 0 auto var(--spacing-xl); }
.article-meta { color: var(--text-light); font-size: 0.9rem; margin-bottom: var(--spacing-lg); display: flex; justify-content: center; gap: var(--spacing-md); }
.article-content { background: var(--card-bg); padding: var(--spacing-xl); border-radius: var(--border-radius); box-shadow: var(--shadow-md); max-width: 800px; margin: 0 auto; }
.article-content h2 { margin-top: var(--spacing-lg); }
.article-content ul, .article-content ol { margin-bottom: var(--spacing-md); padding-left: var(--spacing-lg); }
.article-content li { margin-bottom: var(--spacing-sm); }

/* Key Takeaways */
.key-takeaways { background-color: rgba(87, 108, 188, 0.1); border-left: 4px solid var(--accent-color); padding: 1.5rem; border-radius: 0 var(--border-radius) var(--border-radius) 0; margin-bottom: 2rem; }
.key-takeaways h3 { margin-bottom: 0.5rem; font-size: 1.2rem; }
.key-takeaways ul { margin-bottom: 0; }

/* Data Tables */
table { width: 100%; border-collapse: collapse; margin: 2rem 0; box-shadow: var(--shadow-sm); }
th, td { padding: 1rem; text-align: left; border-bottom: 1px solid var(--border-color); }
th { background-color: var(--primary-color); color: #fff; font-weight: 600; }
tr:nth-child(even) { background-color: rgba(0,0,0,0.02); }
[data-theme="dark"] tr:nth-child(even) { background-color: rgba(255,255,255,0.02); }

/* Social Share */
.social-share { display: flex; gap: 0.5rem; margin: 2rem 0; justify-content: center; }
.social-share a { padding: 0.5rem 1rem; border-radius: var(--border-radius); color: #fff; font-weight: 600; text-decoration: none; font-size: 0.9rem; display: flex; align-items: center; gap: 0.5rem; transition: transform 0.2s ease; }
.social-share a:hover { transform: translateY(-2px); color: #fff; }
.btn-tw { background-color: #1DA1F2; } .btn-fb { background-color: #4267B2; } .btn-li { background-color: #0077b5; }

/* Newsletter */
.newsletter-box { background: var(--primary-color); color: #fff; padding: 2rem; border-radius: var(--border-radius); text-align: center; margin: 3rem 0; }
.newsletter-box h3 { color: #fff; margin-bottom: 0.5rem; }
.newsletter-box p { color: rgba(255,255,255,0.8); margin-bottom: 1.5rem; font-size: 0.95rem; }
.newsletter-form { display: flex; gap: 0.5rem; justify-content: center; max-width: 500px; margin: 0 auto; }
.newsletter-form input { flex: 1; padding: 0.75rem; border: none; border-radius: var(--border-radius); font-size: 1rem; }
.newsletter-form button { background: var(--success-color); color: #fff; font-size: 1rem; border: none; padding: 0.75rem 1.5rem; border-radius: var(--border-radius); font-weight: bold; cursor: pointer; }
.newsletter-form button:hover { background: #059669; }
@media (max-width: 600px) { .newsletter-form { flex-direction: column; } }

.toc { background: var(--bg-color); padding: var(--spacing-lg); border-radius: var(--border-radius); margin-bottom: var(--spacing-xl); border-left: 4px solid var(--accent-color); }
.toc h3 { margin-bottom: var(--spacing-sm); font-size: 1.2rem; }
.toc ul { list-style: none; padding-left: 0; }
.toc li { margin-bottom: 0.5rem; }

.ad-placeholder { background-color: var(--border-color); color: var(--text-light); text-align: center; padding: 2rem; margin: var(--spacing-lg) 0; border: 2px dashed var(--text-light); border-radius: var(--border-radius); font-weight: bold; display: flex; align-items: center; justify-content: center; min-height: 100px; }

.sidebar-widget { background: var(--card-bg); padding: var(--spacing-lg); border-radius: var(--border-radius); box-shadow: var(--shadow-sm); margin-bottom: var(--spacing-lg); border: 1px solid var(--border-color); }
.sidebar-widget h3 { font-size: 1.2rem; margin-bottom: var(--spacing-md); padding-bottom: var(--spacing-sm); border-bottom: 2px solid var(--border-color); }
.category-list { list-style: none; }
.category-list li { margin-bottom: 0.5rem; }
.category-list a { display: flex; justify-content: space-between; color: var(--text-color); }
.category-list a:hover { color: var(--accent-color); }

footer { background-color: var(--card-bg); padding: var(--spacing-xl) 0 var(--spacing-lg); border-top: 1px solid var(--border-color); margin-top: auto; }
.footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--spacing-lg); margin-bottom: var(--spacing-lg); }
.footer-col h4 { margin-bottom: var(--spacing-md); color: var(--primary-color); }
.footer-col ul { list-style: none; }
.footer-col li { margin-bottom: 0.5rem; }
.footer-col a { color: var(--text-light); }
.footer-col a:hover { color: var(--accent-color); }
.footer-bottom { text-align: center; padding-top: var(--spacing-lg); border-top: 1px solid var(--border-color); color: var(--text-light); font-size: 0.9rem; display: flex; justify-content: space-between; flex-wrap: wrap; align-items: center; }

.cookie-banner { position: fixed; bottom: 0; left: 0; width: 100%; background-color: var(--card-bg); padding: var(--spacing-md); box-shadow: 0 -4px 10px rgba(0,0,0,0.1); display: flex; justify-content: center; align-items: center; gap: var(--spacing-lg); z-index: 2000; transform: translateY(100%); transition: transform 0.5s ease-in-out; border-top: 1px solid var(--border-color); }
.cookie-banner.show { transform: translateY(0); }

.search-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); backdrop-filter: blur(5px); z-index: 3000; display: flex; justify-content: center; align-items: flex-start; padding-top: 15vh; opacity: 0; pointer-events: none; transition: var(--transition); }
.search-overlay.active { opacity: 1; pointer-events: auto; }
.search-container { background: var(--card-bg); width: 90%; max-width: 600px; padding: var(--spacing-lg); border-radius: var(--border-radius); position: relative; }
.search-input { width: 100%; padding: 1rem; font-size: 1.2rem; border: 2px solid var(--border-color); border-radius: var(--border-radius); margin-bottom: var(--spacing-md); background: var(--bg-color); color: var(--text-color); }
.close-search { position: absolute; top: 1rem; right: 1.5rem; font-size: 1.5rem; cursor: pointer; background: none; border: none; color: var(--text-light); }
#search-results { max-height: 400px; overflow-y: auto; }
.search-result-item { padding: var(--spacing-sm) 0; border-bottom: 1px solid var(--border-color); }
.search-result-item:last-child { border-bottom: none; }
"""
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)

def generate_js():
    js = """
document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (menuBtn) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    const themeBtn = document.querySelector('.theme-toggle');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const savedTheme = localStorage.getItem('theme');
    
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
    } else if (prefersDark) {
        document.documentElement.setAttribute('data-theme', 'dark');
    }

    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            let currentTheme = document.documentElement.getAttribute('data-theme');
            let targetTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', targetTheme);
            localStorage.setItem('theme', targetTheme);
        });
    }

    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookies = document.getElementById('accept-cookies');
    if (!localStorage.getItem('cookiesAccepted') && cookieBanner) {
        setTimeout(() => cookieBanner.classList.add('show'), 1000);
    }
    if (acceptCookies) {
        acceptCookies.addEventListener('click', () => {
            localStorage.setItem('cookiesAccepted', 'true');
            cookieBanner.classList.remove('show');
        });
    }

    const searchBtn = document.querySelector('.search-btn');
    const searchOverlay = document.getElementById('search-overlay');
    const closeSearch = document.querySelector('.close-search');
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');

    if (searchBtn && searchOverlay) {
        searchBtn.addEventListener('click', (e) => {
            e.preventDefault();
            searchOverlay.classList.add('active');
            searchInput.focus();
        });
        closeSearch.addEventListener('click', () => {
            searchOverlay.classList.remove('active');
        });
        searchOverlay.addEventListener('click', (e) => {
            if(e.target === searchOverlay) {
                searchOverlay.classList.remove('active');
            }
        });
    }
});
"""
    search_data = []
    for a in ARTICLES:
        search_data.append({
            "title": a["title"],
            "url": f"/articles/{a['slug']}.html"
        })
    
    js += f"\nwindow.searchIndex = {json.dumps(search_data)};\n"
    js += """
    const sInput = document.getElementById('search-input');
    const sResults = document.getElementById('search-results');
    if (sInput && window.searchIndex) {
        sInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            sResults.innerHTML = '';
            if (query.length < 2) return;
            
            const filtered = window.searchIndex.filter(item => item.title.toLowerCase().includes(query));
            if (filtered.length === 0) {
                sResults.innerHTML = '<p>No results found.</p>';
                return;
            }
            
            filtered.forEach(item => {
                const div = document.createElement('div');
                div.className = 'search-result-item';
                div.innerHTML = `<a href="${item.url}">${item.title}</a>`;
                sResults.appendChild(div);
            });
        });
    }

    // PWA Service Worker Registration
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js').then(registration => {
                console.log('SW registered: ', registration);
            }).catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
        });
    }
    """
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)

def get_base_html(title, desc, content, path_prefix="", schemas=None, current_url=""):
    schema_script = ""
    if schemas:
        schema_script = f'<script type="application/ld+json">\n{json.dumps(schemas, indent=2)}\n</script>'
        
    canonical = f"{SITE_URL}{current_url}"
    
    html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="en-us" href="{canonical}">
    
    <!-- PWA -->
    <link rel="manifest" href="{path_prefix}manifest.json">
    <meta name="theme-color" content="#0B2447">
    <link rel="apple-touch-icon" href="{path_prefix}icon-192x192.png">

    <!-- Fonts & CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Merriweather:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{path_prefix}css/style.css">
    
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical}">
    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    
    {schema_script}
    
    <!-- <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script> -->
</head>
<body>

    <header>
        <div class="container nav-wrapper">
            <a href="{path_prefix}index.html" class="brand">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                {BRAND_NAME}
            </a>
            <button class="menu-toggle">☰</button>
            <nav>
                <ul class="nav-links">
                    <li><a href="{path_prefix}index.html">Home</a></li>
                    <li><a href="{path_prefix}categories/basics.html">Tax Basics</a></li>
                    <li><a href="{path_prefix}categories/deployment.html">Deployment</a></li>
                    <li><a href="{path_prefix}categories/spouses.html">Spouses</a></li>
                    <li><a href="{path_prefix}about.html">About Us</a></li>
                </ul>
            </nav>
            <div class="nav-actions">
                <button class="theme-toggle" aria-label="Toggle Dark Mode">🌓</button>
                <a href="#" class="search-btn" aria-label="Search">🔍</a>
            </div>
        </div>
    </header>

    {content}

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>{BRAND_NAME}</h4>
                    <p>Your trusted guide for navigating military taxes, deductions, and financial readiness.</p>
                </div>
                <div class="footer-col">
                    <h4>Categories</h4>
                    <ul>
                        <li><a href="{path_prefix}categories/basics.html">Filing Basics</a></li>
                        <li><a href="{path_prefix}categories/deployment.html">Deployment & Overseas</a></li>
                        <li><a href="{path_prefix}categories/deductions.html">Deductions</a></li>
                        <li><a href="{path_prefix}categories/spouses.html">Military Spouses</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Legal & About</h4>
                    <ul>
                        <li><a href="{path_prefix}about.html">About Us</a></li>
                        <li><a href="{path_prefix}contact.html">Contact Us</a></li>
                        <li><a href="{path_prefix}privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="{path_prefix}terms-of-service.html">Terms of Service</a></li>
                        <li><a href="{path_prefix}disclaimer.html">Disclaimer</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; {datetime.now().year} {BRAND_NAME}. All rights reserved.</p>
                <div>
                    <a href="{path_prefix}rss.xml" style="color:var(--text-light); text-decoration:none;">RSS Feed</a> | 
                    <small>This site provides educational information and is not a substitute for professional tax or legal advice.</small>
                </div>
            </div>
        </div>
    </footer>

    <div id="search-overlay" class="search-overlay">
        <div class="search-container">
            <button class="close-search">&times;</button>
            <input type="text" id="search-input" class="search-input" placeholder="Search articles...">
            <div id="search-results"></div>
        </div>
    </div>

    <div id="cookie-banner" class="cookie-banner">
        <p>We use cookies to personalize content, show ads, and analyze traffic. By continuing, you agree to our <a href="{path_prefix}privacy-policy.html">Privacy Policy</a>.</p>
        <button id="accept-cookies" class="btn btn-primary">Accept</button>
    </div>

    <script src="{path_prefix}js/main.js"></script>
</body>
</html>
"""
    return html

def build_home():
    schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": BRAND_NAME,
        "url": SITE_URL
    }
    
    recent_articles = ""
    for a in ARTICLES[:9]:
        recent_articles += f"""
        <article class="article-card">
            <span class="category-tag">{CATEGORIES[a['category']]}</span>
            <h2><a href="articles/{a['slug']}.html">{a['title']}</a></h2>
            <p>Learn everything you need to know about {a['title'].lower()} in this comprehensive guide for military families.</p>
            <a href="articles/{a['slug']}.html" class="read-more">Read More &rarr;</a>
        </article>
        """
        
    sidebar_cats = ""
    for k, v in CATEGORIES.items():
        sidebar_cats += f'<li><a href="categories/{k}.html">{v}</a></li>'

    content = f"""
    <main>
        <section class="hero">
            <div class="container">
                <h1>Tax Filing Guide for Military Families</h1>
                <p>Expert insights, deduction strategies, and essential tax tips to help active duty, reservists, and veterans maximize their returns.</p>
                <a href="articles/{ARTICLES[0]['slug']}.html" class="btn btn-primary">Start with the Basics</a>
            </div>
        </section>
        
        <div class="container main-grid">
            <div class="content-area">
                <div class="ad-placeholder">
                    <!-- Google AdSense - Above the Fold -->
                    [AdSense Placeholder: Responsive Display Ad]
                </div>
                
                <h2 style="margin-bottom: 2rem;">Latest Tax Guides</h2>
                <div class="article-grid">
                    {recent_articles}
                </div>
                
                <!-- Newsletter Optin -->
                <div class="newsletter-box">
                    <h3>Get Military Tax Tips Sent to Your Inbox!</h3>
                    <p>Join over 25,000 military families who receive our weekly tax strategies and deduction alerts.</p>
                    <form class="newsletter-form" action="#" method="POST">
                        <input type="email" placeholder="Your Email Address" required>
                        <button type="submit">Subscribe</button>
                    </form>
                </div>
                
                <div class="ad-placeholder">
                    <!-- Google AdSense - Mid Content -->
                    [AdSense Placeholder: In-Feed Ad]
                </div>
            </div>
            
            <aside class="sidebar">
                <div class="sidebar-widget">
                    <h3>Explore by Topic</h3>
                    <ul class="category-list">
                        {sidebar_cats}
                    </ul>
                </div>
                <div class="sidebar-widget">
                    <div class="ad-placeholder" style="min-height: 250px;">
                        <!-- Google AdSense - Sidebar -->
                        [AdSense Sidebar Ad]
                    </div>
                </div>
            </aside>
        </div>
    </main>
    """
    
    html = get_base_html(f"Home | {BRAND_NAME}", "Comprehensive tax filing guide for military families. Tips on deployment taxes, deductibles, and benefits.", content, "", [schema], "/")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

def build_articles():
    for a in ARTICLES:
        url_path = f"/articles/{a['slug']}.html"
        full_url = f"{SITE_URL}{url_path}"
        
        article_schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": a['title'],
            "author": {"@type": "Person", "name": "MilTax Editorial Team", "url": f"{SITE_URL}/about.html"},
            "publisher": {"@type": "Organization", "name": BRAND_NAME, "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/logo.png"}},
            "datePublished": "2026-07-12",
            "dateModified": "2026-07-12",
            "mainEntityOfPage": {"@type": "WebPage", "@id": full_url}
        }
        
        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
                {"@type": "ListItem", "position": 2, "name": CATEGORIES[a['category']], "item": f"{SITE_URL}/categories/{a['category']}.html"},
                {"@type": "ListItem", "position": 3, "name": a['title'], "item": full_url}
            ]
        }
        
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Is this applicable to Reservists and National Guard?",
                    "acceptedAnswer": { "@type": "Answer", "text": "Yes, but the rules can vary depending on whether you are activated on Title 10 orders or performing weekend drills." }
                },
                {
                    "@type": "Question",
                    "name": "Does this affect my spouse?",
                    "acceptedAnswer": { "@type": "Answer", "text": "Under the Military Spouse Residency Relief Act (MSRRA), spouses have specific protections regarding where they pay state income tax." }
                }
            ]
        }
        
        schemas = [article_schema, breadcrumb_schema, faq_schema]
        
        # Internal Linking
        related = [art for art in ARTICLES if art['category'] == a['category'] and art['slug'] != a['slug']]
        random.shuffle(related)
        related_articles_html = ""
        for rel in related[:3]:
            related_articles_html += f'<li><a href="{rel["slug"]}.html" title="{rel["title"]}">{rel["title"]}</a></li>'
            
        related_html_block = f"""
        <div class="related-articles" style="margin-top: 3rem; background: var(--bg-color); padding: 2rem; border-radius: var(--border-radius);">
            <h3 style="margin-bottom: 1rem;">Related Guides</h3>
            <ul>{related_articles_html}</ul>
        </div>
        """ if related_articles_html else ""
            
        img_placeholder = f"https://placehold.co/800x400/0B2447/FFFFFF.png?text={a['title'].replace(' ', '+')}"
        
        # Social Sharing Links
        enc_url = urllib.parse.quote_plus(full_url)
        enc_title = urllib.parse.quote_plus(a['title'])
        share_html = f"""
        <div class="social-share">
            <a href="https://twitter.com/intent/tweet?url={enc_url}&text={enc_title}" target="_blank" class="btn-tw">Twitter</a>
            <a href="https://www.facebook.com/sharer/sharer.php?u={enc_url}" target="_blank" class="btn-fb">Facebook</a>
            <a href="https://www.linkedin.com/shareArticle?mini=true&url={enc_url}&title={enc_title}" target="_blank" class="btn-li">LinkedIn</a>
        </div>
        """

        content = f"""
        <main class="container" style="padding-top: 3rem; padding-bottom: 3rem;">
            <article class="article-content">
                <header class="article-header">
                    <div style="font-size: 0.9rem; margin-bottom: 1rem; color: var(--text-light);">
                        <a href="../index.html">Home</a> &rsaquo; 
                        <a href="../categories/{a['category']}.html">{CATEGORIES[a['category']]}</a>
                    </div>
                    <span class="category-tag"><a href="../categories/{a['category']}.html">{CATEGORIES[a['category']]}</a></span>
                    <h1>{a['title']}</h1>
                    <div class="article-meta">
                        <span>By <a href="../about.html" style="color:inherit; text-decoration:underline;">MilTax Editorial Team</a></span>
                        <span>•</span>
                        <span>Updated July 12, 2026</span>
                    </div>
                </header>
                
                {share_html}
                
                <img src="{img_placeholder}" alt="{a['title']} - Expert Military Tax Advice" style="width:100%; height:auto; border-radius:8px; margin-bottom:2rem; box-shadow: var(--shadow-sm);">
                
                <div class="ad-placeholder">
                    <!-- Google AdSense - Top Article -->
                    [AdSense Placeholder: Top Banner]
                </div>
                
                <div class="article-body">
                    <p class="intro"><strong>Welcome to our comprehensive guide on {a['title'].lower()}.</strong> Navigating military taxes can be complicated, but understanding this topic is essential for maximizing your return and staying compliant with the IRS.</p>
                    
                    <div class="key-takeaways">
                        <h3>Key Takeaways</h3>
                        <ul>
                            <li>Always consult the latest IRS Publication 3 for Armed Forces rules.</li>
                            <li>Maintain rigorous records of your Leave and Earnings Statements (LES).</li>
                            <li>Understand your state of legal residency (SLR) protections.</li>
                        </ul>
                    </div>
                    
                    <div class="toc">
                        <h3>Table of Contents</h3>
                        <ul>
                            <li><a href="#what-is-it">What is this and how does it apply to military?</a></li>
                            <li><a href="#key-rules">Key Rules and Regulations</a></li>
                            <li><a href="#data-breakdown">Financial Impact & Data</a></li>
                            <li><a href="#how-to-claim">How to Claim on Your Tax Return</a></li>
                            <li><a href="#faqs">Frequently Asked Questions</a></li>
                        </ul>
                    </div>
                    
                    <h2 id="what-is-it">Understanding the Basics</h2>
                    <p>For service members and their families, military life brings unique financial situations. Whether it's dealing with permanent changes of station (PCS), deployments to combat zones, or navigating state residency rules, these factors significantly impact your tax liabilities.</p>
                    <p>This specific topic, {a['title']}, is one of the most common areas where military taxpayers have questions. Ensuring you have the right information can save you hundreds, if not thousands, of dollars.</p>
                    
                    <div class="ad-placeholder">
                        <!-- Google AdSense - In-Article -->
                        [AdSense Placeholder: In-Article Ad]
                    </div>
                    
                    <h2 id="key-rules">Key Rules and Regulations</h2>
                    <p>When dealing with IRS guidelines regarding military service, it's crucial to consult the latest version of IRS Publication 3 (Armed Forces' Tax Guide). The general rules stipulate that:</p>
                    <ul>
                        <li>Always maintain accurate records of your LES.</li>
                        <li>Understand the difference between taxable and non-taxable income (like BAH and BAS).</li>
                        <li>Know your state of legal residency (SLR) versus your physical duty station.</li>
                    </ul>
                    
                    <h2 id="data-breakdown">Financial Impact & Data Breakdown</h2>
                    <p>To better understand how this impacts your bottom line, consider the following historical averages and tax thresholds often relevant to military families:</p>
                    <table>
                        <thead>
                            <tr>
                                <th>Status / Rank Level</th>
                                <th>Average Exclusions</th>
                                <th>Standard Impact</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>E1 - E4 (Junior Enlisted)</td>
                                <td>High relevance for combat pay exclusions</td>
                                <td>Significantly alters AGI</td>
                            </tr>
                            <tr>
                                <td>E5 - E9 (NCO / SNCO)</td>
                                <td>Moderate impact (BAH/BAS ratios)</td>
                                <td>Affects bracket placement</td>
                            </tr>
                            <tr>
                                <td>O1 - O3 (Company Grade)</td>
                                <td>Standard deductions often apply</td>
                                <td>Minimal to Moderate</td>
                            </tr>
                        </tbody>
                    </table>
                    
                    <h2 id="how-to-claim">How to Claim on Your Tax Return</h2>
                    <p>When you sit down to file, whether you are using free military tax software like MilTax (offered via Military OneSource) or a commercial provider, you will need specific forms. Usually, your W-2 will have specific codes in Box 12 indicating military-specific tax statuses.</p>
                    <p>Always double-check your entries and consider consulting a Volunteer Income Tax Assistance (VITA) professional on your installation if you have complex issues.</p>
                    
                    <h2 id="faqs">Frequently Asked Questions</h2>
                    <div class="faq">
                        <h3>Is this applicable to Reservists and National Guard?</h3>
                        <p>Yes, but the rules can vary depending on whether you are activated on Title 10 orders or performing weekend drills. Travel expenses for drills over 100 miles from home may have different deductible statuses.</p>
                        <h3>Does this affect my spouse?</h3>
                        <p>Under the Military Spouse Residency Relief Act (MSRRA), spouses have specific protections regarding where they pay state income tax, which directly intertwines with this topic.</p>
                    </div>
                </div>
                
                {share_html}
                
                <div class="newsletter-box" style="margin-top:2rem;">
                    <h3>Stay Ahead on Military Taxes</h3>
                    <p>Get exclusive deduction tips and tax deadline reminders straight to your inbox.</p>
                    <form class="newsletter-form" action="#" method="POST">
                        <input type="email" placeholder="Your Email Address" required>
                        <button type="submit">Subscribe</button>
                    </form>
                </div>
                
                {related_html_block}
                
                <div class="ad-placeholder">
                    <!-- Google AdSense - Bottom Article -->
                    [AdSense Placeholder: Content Recommendation / Multiplex]
                </div>
                
                <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--border-color);">
                
                <div class="author-bio" style="display: flex; gap: 1rem; align-items: center; background: var(--bg-color); padding: 1.5rem; border-radius: var(--border-radius);">
                    <div style="width: 60px; height: 60px; min-width: 60px; background: var(--primary-color); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.5rem;">M</div>
                    <div>
                        <h4 style="margin-bottom: 0.25rem;"><a href="../about.html" style="color:var(--text-color);">MilTax Editorial Team</a></h4>
                        <p style="margin: 0; font-size: 0.9rem; color: var(--text-light);">With over 15 years of combined experience in military finance and taxation, our team is dedicated to providing clear, authoritative, and actionable tax information for the military community. <a href="../about.html">Read more about our expertise.</a></p>
                    </div>
                </div>
            </article>
        </main>
        """
        html = get_base_html(f"{a['title']} | {BRAND_NAME}", f"A complete guide on {a['title'].lower()} for military families and active duty personnel.", content, "../", schemas, url_path)
        with open(f"articles/{a['slug']}.html", 'w', encoding='utf-8') as f:
            f.write(html)

def build_categories():
    for cat_slug, cat_name in CATEGORIES.items():
        cat_articles = [a for a in ARTICLES if a['category'] == cat_slug]
        url_path = f"/categories/{cat_slug}.html"
        full_url = f"{SITE_URL}{url_path}"
        
        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
                {"@type": "ListItem", "position": 2, "name": cat_name, "item": full_url}
            ]
        }
        
        articles_html = ""
        for a in cat_articles:
            articles_html += f"""
            <article class="article-card">
                <h2><a href="../articles/{a['slug']}.html">{a['title']}</a></h2>
                <a href="../articles/{a['slug']}.html" class="read-more">Read Guide &rarr;</a>
            </article>
            """
            
        content = f"""
        <main class="container" style="padding-top: 3rem; padding-bottom: 3rem; min-height: 70vh;">
            <div style="font-size: 0.9rem; margin-bottom: 1rem; color: var(--text-light); text-align: center;">
                <a href="../index.html">Home</a> &rsaquo; {cat_name}
            </div>
            <div style="text-align: center; margin-bottom: 3rem;">
                <h1>{cat_name}</h1>
                <p>Browse all guides related to {cat_name.lower()}.</p>
            </div>
            
            <div class="ad-placeholder">
                [AdSense Placeholder: Top Banner]
            </div>
            
            <div class="article-grid">
                {articles_html}
            </div>
        </main>
        """
        html = get_base_html(f"{cat_name} | {BRAND_NAME}", f"Read all articles about {cat_name} for military tax filing.", content, "../", [breadcrumb_schema], url_path)
        with open(f"categories/{cat_slug}.html", 'w', encoding='utf-8') as f:
            f.write(html)

def build_core_pages():
    pages = {
        "about": {"title": "About Us", "content": "<h1>About Us</h1><p>Welcome to MilTax Guide. We are dedicated to providing clear, authoritative, and trustworthy tax information for US military service members, veterans, and their families.</p><p>Our content is created by experts who understand the unique financial challenges of military life. With over 15 years of experience in military finance, we aim to deliver the best experience and most accurate information possible.</p>"},
        "contact": {"title": "Contact Us", "content": "<h1>Contact Us</h1><p>Have a question or feedback? We'd love to hear from you.</p><p>Email: contact@bongshai.com</p><p><em>Please note: We do not provide individualized tax advice.</em></p>"},
        "privacy-policy": {"title": "Privacy Policy", "content": "<h1>Privacy Policy</h1><p>At MilTax Guide, we take your privacy seriously.</p><h2>Cookies and Tracking</h2><p>We use cookies to improve your experience on our site. Third party vendors, including Google, use cookies to serve ads based on your prior visits to this website or other websites.</p><p>Google's use of advertising cookies enables it and its partners to serve ads to you based on your visit to our site and/or other sites on the Internet.</p>"},
        "terms-of-service": {"title": "Terms of Service", "content": "<h1>Terms of Service</h1><p>By using this website, you agree to these terms. The content provided is for informational purposes only.</p>"},
        "disclaimer": {"title": "Disclaimer", "content": "<h1>Disclaimer</h1><p>The information provided on MilTax Guide does not, and is not intended to, constitute legal or financial advice; instead, all information, content, and materials available on this site are for general informational purposes only.</p><p>Always consult with a qualified tax professional or your installation's VITA center before making financial decisions.</p>"},
        "404": {"title": "Page Not Found", "content": "<div style='text-align:center; padding: 5rem 0;'><h1>404</h1><h2>Page Not Found</h2><p>The page you are looking for doesn't exist.</p><a href='index.html' class='btn btn-primary'>Go Home</a></div>"}
    }
    
    for slug, data in pages.items():
        url_path = f"/{slug}.html"
        content = f"""
        <main class="container" style="padding-top: 3rem; padding-bottom: 3rem; min-height: 60vh;">
            <div class="article-content">
                {data['content']}
            </div>
        </main>
        """
        html = get_base_html(f"{data['title']} | {BRAND_NAME}", f"{data['title']} page for MilTax Guide.", content, "", None, url_path)
        with open(f"{slug}.html", 'w', encoding='utf-8') as f:
            f.write(html)

def build_sitemap_and_robots():
    urls = [f"{SITE_URL}/", f"{SITE_URL}/about.html", f"{SITE_URL}/contact.html", f"{SITE_URL}/privacy-policy.html", f"{SITE_URL}/terms-of-service.html", f"{SITE_URL}/disclaimer.html"]
    
    for a in ARTICLES:
        urls.append(f"{SITE_URL}/articles/{a['slug']}.html")
        
    for c in CATEGORIES.keys():
        urls.append(f"{SITE_URL}/categories/{c}.html")
        
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sitemap += f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>\n  </url>\n"
    sitemap += "</urlset>"
    
    with open("sitemap.xml", 'w', encoding='utf-8') as f:
        f.write(sitemap)
        
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n"
    with open("robots.txt", 'w', encoding='utf-8') as f:
        f.write(robots)

def build_rss():
    items = ""
    for a in ARTICLES[:10]: # Top 10 for RSS
        url = f"{SITE_URL}/articles/{a['slug']}.html"
        items += f"""
        <item>
            <title>{a['title']}</title>
            <link>{url}</link>
            <guid>{url}</guid>
            <pubDate>{datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>
            <description>A complete guide on {a['title'].lower()} for military families and active duty personnel.</description>
        </item>
        """
        
    rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
    <title>{BRAND_NAME}</title>
    <link>{SITE_URL}</link>
    <description>Expert insights, deduction strategies, and essential tax tips to help active duty, reservists, and veterans maximize their returns.</description>
    <language>en-us</language>
    {items}
</channel>
</rss>
"""
    with open("rss.xml", 'w', encoding='utf-8') as f:
        f.write(rss)

def build_pwa():
    manifest = {
        "name": BRAND_NAME,
        "short_name": "MilTax",
        "description": "Tax Filing Guide for Military Families",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#F8F9FA",
        "theme_color": "#0B2447",
        "icons": [
            {
                "src": "icon-192x192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "icon-512x512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    }
    with open("manifest.json", 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=4)
        
    # Service Worker (Cache First strategy for assets, Network First for HTML)
    sw = """
const CACHE_NAME = 'miltax-cache-v1';
const urlsToCache = [
  '/',
  '/css/style.css',
  '/js/main.js',
  '/index.html'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request).then(
          function(response) {
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            var responseToCache = response.clone();
            caches.open(CACHE_NAME)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });
            return response;
          }
        );
      })
  );
});
"""
    with open("sw.js", 'w', encoding='utf-8') as f:
        f.write(sw)

def main():
    print("Creating directories...")
    create_directories()
    
    print("Generating assets...")
    generate_css()
    generate_js()
    build_pwa()
    
    print("Building pages with 10K/Day Scaling features...")
    build_home()
    build_articles()
    build_categories()
    build_core_pages()
    
    print("Building sitemap, robots, and rss...")
    build_sitemap_and_robots()
    build_rss()
    
    print("Scaling site regeneration complete!")

if __name__ == "__main__":
    main()
