const { response } = require('express');
var express = require('express');
const async = require('hbs/lib/async');
const productHelpers = require('../helpers/product-helpers');
var router = express.Router();
var productHelper = require('../helpers/product-helpers')



/* GET users listing. */
router.get('/view-products', function (req, res, next) {


  productHelpers.getAllProducts().then((products) => {
    console.log(products)
    res.render('admin/view-products', { admin: true, products })
  })


});
router.get('/', function (req, res, next) {
  res.render('admin/login', { admin: true })
})
router.post('/login', function (req, res, next) {
  let Name=req.body.Name;
  let Pass=req.body.Password
  if(Name=="admin"&&Pass=="admin"){
    res.redirect('/admin/view-products')
  }
  
})

router.get('/all-orders', function (req, res, next) {
  productHelpers.getAllOrders().then((orders) => {
    console.log(orders);
    res.render('admin/all-orders', { admin: true, orders })
  })
});

router.get('/admin/view-order-products/:id', async (req, res) => {
  let products = await productHelpers.getOrderProducts(req.params.id)

  res.render('admin/view-order-products', { admin: true, products })
})

router.get('/add-product', function (req, res) {
  res.render('admin/add-product',{admin:true})
})
router.post('/add-product', (req, res) => {
  console.log(req.body);
  console.log(req.files.Image);

  productHelpers.addProduct(req.body, (id) => {
    console.log("#####", id);
    let image = req.files.Image

    image.mv('./public/product-images/' + id + '.jpg', (err, done) => {
      if (!err) {
        res.render("admin/add-product", { admin: true })
      } else {
        console.log(err);
      }
    })

  })

})
router.get('/delete-product/:id', (req, res) => {
  let proId = req.params.id
  console.log(proId);
  productHelpers.deleteProduct(proId).then((response) => {
    res.redirect('/admin/view-products')
  })
})

router.get('/edit-product/:id', async (req, res) => {
  let product = await productHelpers.getProductDetails(req.params.id)
  console.log(product);
  res.render('admin/edit-product', { product })
})
router.post('/edit-product/:id', (req, res) => {
  let id = req.params.id
  productHelpers.updateProduct(req.params.id, req.body).then(() => {
    res.redirect('/admin')
    if (req.files.Image) {
      let image = req.files.Image
      image.mv('./public/product-images/' + id + '.jpg')

    }
  })
})
module.exports = router;
