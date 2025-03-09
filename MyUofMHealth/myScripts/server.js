const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(bodyParser.json()); // Middleware to parse JSON
app.use(cors())

// Endpoint to receive URLs from the browser
app.post('/save-urls', (req, res) => {
  const urls = req.body.urls;

  if (!urls || !Array.isArray(urls)) {
    return res.status(400).send('Invalid URLs data');
  }

  const filePath = './urls.txt';
  const data = urls.join('\n');

  fs.writeFile(filePath, data, (err) => {
    if (err) {
      return res.status(500).send('Error writing to file');
    }
    res.send({ message: 'URLs saved to file successfully!' });
  });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
