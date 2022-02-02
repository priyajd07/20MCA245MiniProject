const { resolve, reject } = require('promise')
var db = require('../config/connection')
var collection = require('../config/collections')
const { response } = require('express')

var objectId = require('mongodb').ObjectID
var generator = require('generate-password');
var nodemailer = require('nodemailer');
const { getMaxListeners } = require('../app')
var password = generator.generate({
    length: 10,
    numbers: true
});
module.exports = {
send: () => {
    // console.log("Reviever", reciever)
    // var username = "muneesmmm@gmail.com"
    // var password = "123458"
    var transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: 'muhammedmunees@mesce.ac.in',
            pass: 'Muham@123'
        }
    });
    
    console.log('created');
    var mailOptions = {
        from: 'muhammedmunees@mesce.ac.in',
        to: 'muneesmmm@gmail.com',
        subject: 'Sending Email using Node.js',
        text: 'Thank you for registering your hotel is added successfully you can use this username and password \n username:\t' + "username" + '\n password:\t' + 'password' + '',
        html :'<div style="margin: 20px;padding: 50px; background-color:black;border-radius: 15px;border:5px lightgray solid"><div style="justify-content:center;display: flex;"><h2 class="" style="font-family:cursive; color: blueviolet;font-weight: 700;">MEDLAR</h2></div>'+
          '<div><p style="color: rgb(161, 161, 161);"><b>Welcom to MEDLAR.Here you get your current health status and medical reports</b></p>'+
            '<table style="color: cornflowerblue;""><tr><th>email</th><td>: mns@gmail.com</td></tr><tr><th>password</th><td>: 123458</td></tr></table></div></div>'
    };

    transporter.sendMail(mailOptions, function (err, info) {
        if (err) {
            console.log(err);
            return;
        } 
            console.log('Email sent: ' + info.response);
            
            
        
    });
},
   
}