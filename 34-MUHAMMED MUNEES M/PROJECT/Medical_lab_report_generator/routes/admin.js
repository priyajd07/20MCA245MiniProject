var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render("admin/login");
});
router.get('/index', function(req, res, next) {
  res.render("admin/index");
});
router.get('/patients', function(req, res, next) {
  res.render("admin/patients");
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
module.exports = router;
