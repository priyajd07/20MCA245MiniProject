var express = require('express');
var router = express.Router();
const adminHelpers = require('../helpers/adminhelper')
const userHelpers = require('../helpers/userhelper')
const verifyLogin = (req, res, next) => {
  if (req.session.loggedIn) {
    next()
  } else {
    res.redirect('/admin/login')
  }
}
/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render("admin/login");
});
router.get('/index', function(req, res, next) {
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
router.get('/patients',async function(req, res, next) {
  let patients=await adminHelpers.viwqpatients(req,res)
  console.log(patients);
  res.render("admin/patients",{patients});
});
// add patients
router.get('/addpatients', function(req, res, next) {
  res.render("admin/addpatients");
});
router.get('/reports/:id', function(req, res, next) {
  let id=req.params.id
  res.render("admin/reports",{id});
});
router.get('/hmtlgy/:id', function(req, res, next) {
  let id=req.params.id
  res.render("admin/hmtlgy",{id});
});
router.get('/lft/:id', function(req, res, next) {
  let id=req.params.id
  res.render("admin/lft",{id});
});
router.get('/rft/:id', function(req, res, next) {
  let id=req.params.id
  res.render("admin/rft",{id});
});
router.get('/kft/:id', function(req, res, next) {
  let id=req.params.id
  res.render("admin/kft",{id});
});
router.post('/addpatients',async (req, res) => {
  adminHelpers.addpatients(req.body).then((response) => {
    console.log(response)
    req.session.admin = response
    req.session.loggedIn = true
  })
  adminHelpers.send(req.body)
  res.redirect('/admin/patients') 
})

module.exports = router;
