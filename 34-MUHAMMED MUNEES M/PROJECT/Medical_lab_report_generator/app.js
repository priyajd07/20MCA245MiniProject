var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var helpers = require('handlebars-helpers')();

const fileUpload = require('express-fileupload');
const favicon = require('serve-favicon')
var usersRouter = require('./routes/users');
var adminRouter = require('./routes/admin');
var hbs = require('express-handlebars')
var app = express();
var db = require('./config/connection')
var session=require('express-session')
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hbs');
app.use(function(req, res, next) {
  if (!req.user)
      res.header('Cache-Control', 'private, no-cache, no-store, must-revalidate');
  next();
});
app.engine('hbs', hbs.engine({
  extname: 'hbs',
  defaultLayout: 'layout',
  layoutsDir: __dirname + '/views/layout/',
  partialsDir: __dirname + '/views/partials'
}))
app.use(logger('dev'));
app.use(express.json());
app.use(fileUpload());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(favicon(path.join(__dirname, 'public','favicon.png')));
app.use(session({secret:"Key",cookie:{maxAge:600002000}}))
db.connect((err) => {
  if (err) console.log("connection error" + err);
  else console.log("database connected successfully 27");

})
app.use('/', usersRouter);
app.use('/admin', adminRouter);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;