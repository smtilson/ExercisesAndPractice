const express = require('express');
const router = express.Router();

const authenticate = (req, res, next) => {
  // Check if the request has a valid API key
  const apiKey = req.headers;
  if (isValidApiKey(apiKey)) {
    // If valid, proceed to the next middleware
    console.log(apiKey);
    console.log("valid api key");
    next();
  } else {
    // If not valid, respond with a 401 status code
    res.status(401).json({ error: 'Unauthorized' });
  }
};

const isValidApiKey = (apiKey) => {
  // Implement your logic to validate the API key
  // For example, you can check against a database or a configuration file
  // Return true if the API key is valid, false otherwise
  return true;
  //return apiKey === 'your-valid-api-key';
};


//router.use(authenticate);

/* GET users listing. */
router.get('/', function (req, res, next) {
  res.send('respond with a resource');
});

router.get('/:id', authenticate, (req, res) => {
  if (req.params.id === '1') {
    res.json({ message: 'User 1' });
  } else if (req.params.id === '2') {
    res.json({ message: 'User 2' });
  }
  else {
    res.status(404).json({ message: 'User not found' });
  }
});


module.exports = router;
