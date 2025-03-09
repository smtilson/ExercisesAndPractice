// Grab all anchor elements on the page
const anchors = document.querySelectorAll('a');

// Extract the href (URL) from each anchor tag
let urls = Array.from(anchors).map(anchor => anchor.href);
urls = urls.filter(url => url.startsWith('https://myuofmhealth.org'));
urls = urls.filter(url => url.includes('visits/note?'));

// Log the URLs to the console (for now)
//console.log(urls);

// Send the URLs to your Node.js backend for saving to a file
fetch('http://localhost:3000/save-urls', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ urls })
})
  .then(response => response.json())
  .then(data => console.log('Successfully sent URLs:', data))
  .catch(error => console.error('Error sending URLs:', error));
