const express = require('express');
const router = express.Router();

/* GET home page. */
router.get('/', function (req, res, next) {
  res.json({ message: "Welcome to my Express API project!" });
  // or
  //res.render('index', { title: 'Express' });
});

router.get('/womp', (req, res) => {
  res.json({ message: 'Womp womp' });
});

module.exports = router;
