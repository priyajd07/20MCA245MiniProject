var express = require('express');
var router = express.Router();
const adminHelpers = require('../helpers/adminhelper')
const userHelpers = require('../helpers/userhelper')

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render("admin/login");
});
router.get('/index', function(req, res, next) {
  adminHelpers.send()
    res.render("admin/index");
});
router.post('/login',(req, res, next)=> {
  console.log(req.body);
  let email=req.body.email
  let password=req.body.password
  if (email=="muneesmmm@gmail.com" && password=="123458") {
    res.redirect('/admin/index')
  }else{
    res.redirect('/')
  }
});
//view patients
router.get('/patients', function(req, res, next) {
  res.render("admin/patients");
});
// add patients
router.get('/addpatients', function(req, res, next) {
  res.render("admin/addpatients");
});
module.exports = router;
