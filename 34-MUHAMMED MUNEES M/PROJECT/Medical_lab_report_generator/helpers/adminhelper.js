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
    addpatients: (userData) => {
        return new Promise(async (resolve, reject) => {
            userData.password = password
            console.log(password);
            db.get().collection(collection.USER_COLLECTION).insertOne(userData)
        })
    },
    send: (reciever) => {
        console.log("Reviever", reciever)
        var username = reciever.email
        var password = reciever.password
        responseData = {}
        var transporter = nodemailer.createTransport({
            service: 'gmail',
            auth: {
                user: 'muhammedmunees@mesce.ac.in',
                pass: 'Muham@123'
            }
        });

        var mailOptions = {
            from: 'muhammedmunees@gmesce.ac.in',
            to: username,
            subject: 'Sending Email using Node.js',
            html: '<div style="margin: 20px;padding: 50px; background-color:black;border-radius: 15px;border:5px lightgray solid"><div style="justify-content:center;display: flex;"><h2 class="" style="font-family:cursive; color: blueviolet;font-weight: 700;">MEDLAR</h2></div>' +
                '<div><p style="color: rgb(161, 161, 161);"><b>Welcom to MEDLAR.Here you get your current health status and medical reports</b></p>' +
                '<table style="color: cornflowerblue;""><tr><th>email</th><td>:'+username+'</td></tr><tr><th>password</th><td>:'+password+'</td></tr></table><br><a href="medlar.tech">medlar.tech</a></div></div>'
        };

        transporter.sendMail(mailOptions, function (error, info) {
            if (error) {
                console.log(error);
            } else {
                console.log('Email sent: ' + info.response);
                responseData.message = "user registered succussfully"
                console.log(responseData.message);
            }
        });
    },
    viwqpatients: ()=>{
        return new Promise(async (resolve, reject) => {
            let users=await db.get().collection(collection.USER_COLLECTION).find().toArray()
            resolve(users)
        })
    }

}