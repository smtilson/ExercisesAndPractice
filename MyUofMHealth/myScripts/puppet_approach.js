const puppeteer = require('puppeteer');
const fs = require('fs');
const { urls, urls1 } = require('./urls');
const { momPassword, momUserName } = require('./creds');



const chromePath = '/mnt/c/Program\ Files/Google/Chrome/Application/chrome.exe';
const windowsVChromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const chromiumWSLPath = '/usr/bin/google-chrome-stable';

(async () => {
    const browser = await puppeteer.launch({ 
        //executablePath: windowsVChromePath,
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        headless: false }); // Change to true for background execution
    const page = await browser.newPage();
    const loginUrl = 'https://www.myuofmhealth.org/MyChart-PRD/Authentication/Login?'; // Adjust URL

    // Navigate to login page
    await page.goto(loginUrl, { waitUntil: 'networkidle2' });

    // Fill in login form
    await page.type('#Login', momUserName); // Adjust selector
    await page.type('#Password', momPassword); // Adjust selector
    await page.click('#submit'); // Adjust selector

    // Wait for navigation after login
    await page.waitForNavigation({ waitUntil: 'networkidle2' });


    let results = [];

    for (const url of urls1) {
        console.log(`Navigating to ${url}`);
        await page.goto(url, { waitUntil: 'networkidle2' });
    
        // Extract report text
        const reportText = await page.evaluate(() => {
            return document.body.innerText.trim(); // Adjust if needed
        });
    
        results.push({ url, reportText });
    }
    
        // Save results to JSON file
    fs.writeFileSync('results.json', JSON.stringify(results, null, 2));
    
    console.log('Extraction complete. Results saved to results.json');
    
    await browser.close();
})();    
    
    
    
    
    
        
