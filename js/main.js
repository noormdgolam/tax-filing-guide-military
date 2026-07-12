
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

window.searchIndex = [{"title": "Military Tax Filing Basics: A Complete Guide", "url": "/articles/military-tax-filing-basics.html"}, {"title": "Combat Zone Tax Exclusion (CZTE) Explained", "url": "/articles/combat-zone-tax-exclusion.html"}, {"title": "How Deployment Affects Your Tax Deadlines", "url": "/articles/deployment-tax-extensions.html"}, {"title": "Are PCS Moving Expenses Tax Deductible?", "url": "/articles/pcs-moving-expenses-tax-deductions.html"}, {"title": "MSRRA: Military Spouse Residency Relief Act Guide", "url": "/articles/military-spouse-residency-relief-act.html"}, {"title": "State Taxes for Active Duty Military: What to Know", "url": "/articles/state-taxes-for-active-duty.html"}, {"title": "Are BAH and BAS Taxable?", "url": "/articles/tax-free-allowances-bah-bas.html"}, {"title": "Thrift Savings Plan (TSP) Tax Implications", "url": "/articles/thrift-savings-plan-taxes.html"}, {"title": "Are Veterans Benefits Taxable?", "url": "/articles/veterans-benefits-taxability.html"}, {"title": "Earned Income Tax Credit (EITC) for Military", "url": "/articles/earned-income-tax-credit-military.html"}, {"title": "Child Tax Credit Guide for Military Families", "url": "/articles/child-tax-credit-military-families.html"}, {"title": "Are ROTC Scholarships Taxable?", "url": "/articles/rotc-scholarships-tax-status.html"}, {"title": "GI Bill Benefits: Are They Tax-Free?", "url": "/articles/gi-bill-tax-implications.html"}, {"title": "Military Retirement Pension Tax Guide", "url": "/articles/military-pension-tax-guide.html"}, {"title": "Survivor Benefit Plan (SBP) Tax Rules", "url": "/articles/survivor-benefit-plan-taxes.html"}, {"title": "Best Free Tax Filing Options for Military", "url": "/articles/free-tax-filing-for-military.html"}, {"title": "Top Tax Software for Military Personnel", "url": "/articles/mil-tax-software-reviews.html"}, {"title": "Tax Deductions for National Guard and Reservists", "url": "/articles/reservist-travel-expenses.html"}, {"title": "Can You Deduct Military Uniforms on Your Taxes?", "url": "/articles/uniform-deductions.html"}, {"title": "Home Sale Tax Exclusion for Military Families", "url": "/articles/home-sale-tax-exclusion-military.html"}, {"title": "VA Loan Tax Benefits and Deductions", "url": "/articles/va-loan-tax-deductions.html"}, {"title": "Renting Out Your Home During PCS: Tax Guide", "url": "/articles/rental-property-taxes-military.html"}, {"title": "Filing Taxes While Stationed Overseas", "url": "/articles/overseas-tax-filing.html"}, {"title": "Foreign Earned Income Exclusion for Spouses", "url": "/articles/foreign-earned-income-exclusion.html"}, {"title": "Tax Guide for Military Contractors Overseas", "url": "/articles/military-contractor-taxes.html"}, {"title": "How to Read Your Military W-2", "url": "/articles/w2-understanding-military.html"}, {"title": "IRA Contributions While in a Combat Zone", "url": "/articles/ira-contributions-combat-zone.html"}, {"title": "Are Military Enlistment Bonuses Taxed?", "url": "/articles/signing-bonus-taxes.html"}, {"title": "Military Severance Pay Tax Rules", "url": "/articles/severance-pay-taxability.html"}, {"title": "Common Tax Scams Targeting Military Families", "url": "/articles/tax-scams-targeting-military.html"}, {"title": "What to Do If You Get Audited as a Service Member", "url": "/articles/audit-guide-military.html"}];

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
    