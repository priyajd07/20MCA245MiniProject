var express = require('express');
var router = express.Router();
const { response } = require("express");
const userhelper = require('../helpers/userhelper');
const verifyLogin = (req, res, next) => {
  if (req.session.loggedIn) {
    next()
  } else {
    res.redirect('/')
  }
}
/* GET home page. */
router.get('/', function (req, res, next) {
  let user = req.session.user
  if (req.session.loggedIn) {
    res.render('user/index', { user })
  }
  else {
    res.render('user/login', { "LoginErr": req.session.loginErr })
    req.session.loginErr = false
  }

})
router.get('/login', function(req, res, next) {
  res.render("user/login");
});
router.get('/',verifyLogin, function(req, res, next) {
  res.render("user/index");
});
router.get('/profile',verifyLogin,async function(req, res, next) {
  let user=req.session.user
  let data=await userhelper.viewsuagar(user._id)
  let data1=await userhelper.viewcreatinin(user._id)
  res.render("user/profile",{data,data1,user});
});
router.get('/hmtlgyrslts/:id',async function(req, res, next) {
  let data=await userhelper.viewhmtlgy(req.params.id)
  let user=req.session.user
  console.log(data);
  res.render("user/hmresults",{data,user});
});
router.get('/lftrslts/:id',async function(req, res, next) {
  let data=await userhelper.viewlft(req.params.id)
  let user=req.session.user
  console.log(data);
  res.render("user/lftresults",{data,user});
});
router.get('/biorslts/:id',async function(req, res, next) {
  let data=await userhelper.viewbio(req.params.id)
  let user=req.session.user
  console.log(data);
  res.render("user/bioresults",{data,user});
});
router.get('/results/:id',async function(req, res, next) {
  let user=req.session.user
  let data=await userhelper.viewbio(req.params.id)
  console.log(data);
  res.render("user/reports",{data,user});
});
router.get('/creatinin/:id',async function(req, res, next) {
  let user=req.session.user
  let data=await userhelper.viewkft(req.params.id)
  console.log(data);
  res.render("user/creatinin",{data,user});
});
router.get('/kftrslts/:id',async function(req, res, next) {
  let data=await userhelper.viewkft(req.params.id)
  let user=req.session.user
  console.log(data);
  res.render("user/kftresults",{data,user});
});
router.get('/hmtlgy/:id',verifyLogin,async function(req, res, next) {
  let data=await userhelper.hmtlgy(req.params.id)
  user=req.session.user
  console.log("00000000000000000",data);
  res.render("user/hmtlgy",{data,user});
});
router.get('/lft/:id',verifyLogin, async function(req, res, next) {
  let data=await userhelper.lft(req.params.id)
  user=req.session.user
  console.log("00000000000000000",data);
  res.render("user/lft",{data,user});
});
router.get('/bio/:id',verifyLogin,  async function(req, res, next) {
  let data=await userhelper.bio(req.params.id)
  user=req.session.user
  console.log("00000000000000000",data);
  res.render("user/bio",{data,user});
});
router.get('/kft/:id',verifyLogin,async function(req, res, next) {
  let data=await userhelper.kft(req.params.id)
  user=req.session.user
  console.log("00000000000000000",data);
  res.render("user/kft",{data,user});
});
router.post('/login',async (req, res) => {
  req.session.loggedIn = false
  userhelper.doLogin(req.body).then((response) => {

    if (response.loginStatus) {
      console.log(response);
      req.session.loggedIn = true
      req.session.user = response.user
      res.redirect('/')
    } else {
      req.session.loginErr = true
      res.redirect('/login')
    }


  })
})
router.get('/logout', (req, res) => {
  req.session.loggedIn = false
  req.session.user = null
  res.redirect('/')
})
module.exports = router;
