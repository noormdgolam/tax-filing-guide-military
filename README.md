# MilTax Guide - Static Website

This is a production-ready, highly optimized static website designed for the "Tax Filing Guide for Military Families" niche. It's built with pure HTML, CSS, and JS (no framework) to ensure blazing-fast load times and perfect Core Web Vitals.

## Directory Structure
- `/` - Core pages (index.html, about.html, contact.html, privacy-policy.html, terms-of-service.html, disclaimer.html, 404.html)
- `/articles/` - 31 unique SEO-optimized articles targeting military tax keywords.
- `/categories/` - Hub pages for different topics.
- `/css/style.css` - Global stylesheet with premium design, dark mode, and responsive layout.
- `/js/main.js` - Client-side search, mobile menu, and cookie banner logic.
- `sitemap.xml` - Ready for Google Search Console upload.
- `robots.txt` - Optimized for crawling.

## Adding New Articles
1. Create a new `.html` file inside the `/articles/` directory (e.g., `new-article.html`).
2. Copy the structure from an existing article (like `military-tax-filing-basics.html`).
3. Update the `<title>`, `<meta name="description">`, `<h1>`, and the JSON-LD `<script>` tag with the new content.
4. Update the content body.

## Google AdSense Setup
This site includes pre-defined placeholder zones for Google AdSense. Search the HTML files for `[AdSense Placeholder:` to find the designated ad blocks.
1. Open your HTML files.
2. Replace the `<div class="ad-placeholder">...</div>` blocks with the actual AdSense ad unit code provided in your Google AdSense dashboard.
3. Recommended ad placements are already structured for:
   - Above the fold (Homepage & Categories)
   - Top of article
   - Mid-content / In-article
   - End of article (Multiplex / Recommended)
   - Sidebar

## Search Console & Analytics
- **Sitemap**: Upload `https://tax-filing-guide-military.bongshai.com/sitemap.xml` directly to Google Search Console.
- **Analytics**: To add GA4, find the commented-out Google Tag Manager script in the `<head>` of the HTML files and replace it with your GA4 snippet.

## Developer Note
The `build_site.py` script was used to initially generate the scaffolding, templates, and 30+ pages. You do not need to run this script again unless you wish to regenerate the entire site from scratch. You can now manually edit the generated HTML files directly.
