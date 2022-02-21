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
router.post('/addhmtlgy',async (req, res) => {
  let data= await adminHelpers.addheamrslt(req.body)
    console.log(data)
  res.redirect('/admin/index')
})
router.get('/lft/:id', function(req, res, next) {
  let id=req.params.id
  res.render("admin/lft",{id});
});
router.post('/addlft',async (req, res) => {
  let data= await adminHelpers.addlftrslt(req.body)
    console.log(data)
  res.redirect('/admin/index')
})
router.get('/rft/:id', function(req, res, next) {
  let id=req.params.id
  res.render("admin/rft",{id});
});
router.post('/addrft',async (req, res) => {
  let data= await adminHelpers.addbiorslt(req.body)
    console.log(data)
  res.redirect('/admin/index')
})
router.get('/kft/:id', function(req, res, next) {
  let id=req.params.id
  res.render("admin/kft",{id});
});
router.post('/addkft',async (req, res) => {
  let data= await adminHelpers.addkftrslt(req.body)
    console.log(data)
  res.redirect('/admin/index')
})
router.post('/addpatients',async (req, res) => {
  adminHelpers.addpatients(req.body).then((response) => {
    console.log(response)
    req.session.admin = response
    req.session.loggedIn = true
  })
  adminHelpers.send(req.body)
  res.redirect('/admin/patients') 
});
router.get('/viewreports/:id',async function(req, res, next) {
  let data=await adminHelpers.viewhmtlgy(req.params.id)
  let data1=await adminHelpers.viewlft(req.params.id)
  let data2=await adminHelpers.viewbio(req.params.id)
  let data3=await adminHelpers.viewkft(req.params.id)
  res.render("admin/results",{data,data1,data2,data3});
});
router.get('/hmtlgyrst/:id',async function(req, res, next) {
  let data=await adminHelpers.hmtlgy(req.params.id)
  console.log("00000000000000000",data);
  res.render("admin/hmtlgyrst",{data});
});
router.get('/lftrst/:id', async function(req, res, next) {
  let data=await adminHelpers.lft(req.params.id)
  console.log("00000000000000000",data);
  res.render("admin/lftrst",{data});
});
router.get('/biorst/:id',  async function(req, res, next) {
  let data=await adminHelpers.bio(req.params.id)
  console.log("00000000000000000",data);
  res.render("admin/biorst",{data});
});
router.get('/kftrst/:id',async function(req, res, next) {
  let data=await adminHelpers.kft(req.params.id)
  console.log("00000000000000000",data);
  res.render("admin/kftrst",{data});
});

module.exports = router;
