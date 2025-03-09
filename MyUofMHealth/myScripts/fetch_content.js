const fs = require('fs');
const { urls, urls1 } = require('./urls');

const cookie = "MyChartLocale=en-US; MyChart_Session=u3emraiip24eq4x3dxhgmnpo; __RequestVerificationToken_L015Q2hhcnQtUFJE0=z2qv5garMA7VxodunWLJrio54F8bY_bSXvy6NfjKaScU7KtOsxHvAZngHWo9SUxUjK1kEUNqOjW-iA6bODpsBIW8zsk1; NSC_NDISU-nzvpgnifbmui.psh-ttm=ffffffff8ede0e8645525d5f4f58455e445a4a42378b; ASPSESSIONIDAUQTATDB=CPLICLDBONIMJEIHPENOALLH; MyChartAccessToken4mychart-prd=jk0l3nWcXx5WaK0k9kHSimNkwE10jO05xDY5jI6C162mPWAQq_WNMUrKykjkQB9HC1ZGtkgSkCsmnF9qtzz0vloV4DlsXvfFbU6fIvZFOdDON8esPnoLDA-Aqxg3l_Ez; MyChartSessionToken4mychart-prd=dxJbaxL1NzxV3zeDlU8mEjaOS/6J3eCRA0s4g8cFm0c=; MyChartNetAuthenticationTicket4mychart-prd=E973D9D739A63A3D78420FD9577C512D7F003C16CCDFB123C0272A7C614E9111249A6B62EBA3B11A045391AA06B10A3C4D83E9A3B40E88D47EDF0E6C749B3170B9800751832787A089CF076EDAF349721EAFCB64415D0A1903C3252A1F2050363BC155B92B10048F4A86F5D7226741AB71B4384A3E17F516FF94B89035B668373F09BEB96B446E6264F22AF82EEE8833620302B53E8CC40D859642E4C25CEBE39BA3128B; UpdateMyChartContext4mychart-prd=0";

(async () => {
    const results = [];
    
    for (const url of urls1) {
        const response = await fetch(url, {
        headers: {
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0'  // Some sites block non-browser requests
        }
    });
    if (response.status === 302) {
        console.error('You are being redirected!');
        continue;}
    else if (response.status === 301) {
            console.error('You are being redirected!');
        continue;}
    else {
        try {
            console.log(`Fetching: ${url}`);
            const response = await fetch(url); // ✅ Native fetch in Node 18+
            
            if (!response.ok) {
                console.error(`Failed to fetch ${url}: ${response.status}`);
                continue;
            }

            const text = await response.text();
            results.push({ url, content: text });

        } catch (error) {
            console.error(`Error fetching ${url}:`, error);
            }
        fs.writeFileSync('results.json', JSON.stringify(results, null, 2), 'utf-8');
        console.log('Saved content to results.json');
        }
    }
})();
