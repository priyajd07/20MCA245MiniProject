var express = require('express');
var router = express.Router();
const { response } = require("express");

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render("user/login");
});
router.get('/index', function(req, res, next) {
  res.render("user/index");
});
router.post('/login',(req, res, next)=> {
  console.log(req.body);
  let email=req.body.email
  let password=req.body.password
  if (email=="muneesmmm@gmail.com" && password=="123458") {
    res.redirect('/index')
  }else{
    res.redirect('/')
  }
});

module.exports = router;
