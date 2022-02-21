const { resolve, reject } = require('promise')
var db = require('../config/connection')
var collection = require('../config/collections')
const { response } = require('express')

var objectId = require('mongodb').ObjectId
var generator = require('generate-password');
var nodemailer = require('nodemailer');
const { getMaxListeners } = require('../app')
const { ObjectId } = require('mongodb')
var password = generator.generate({
    length: 10,
    numbers: true
});
module.exports = {
    addpatients: (userData) => {
        return new Promise(async (resolve, reject) => {
            userData.password = password
            console.log(password);
            db.get().collection(collection.USER_COLLECTION).insertOne(userData).then((info) => {
                resolve(info)
            })
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
            from: 'muneesmmm@gmail.com',
            to: username,
            subject: 'Sending Email using Node.js',
            html: '<div style="margin: 20px;padding: 50px; background-color:black;border-radius: 15px;border:5px lightgray solid"><div style="justify-content:center;display: flex;"><h2 class="" style="font-family:cursive; color: blueviolet;font-weight: 700;">MEDLAR</h2></div>' +
                '<div><p style="color: rgb(161, 161, 161);"><b>Welcom to MEDLAR.Here you get your current health status and medical reports</b></p>' +
                '<table style="color: cornflowerblue;""><tr><th>email</th><td>:' + username + '</td></tr><tr><th>password</th><td>:' + password + '</td></tr></table><br><a href="medlar.tech">medlar.tech</a></div></div>'
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
    viwqpatients: () => {
        return new Promise(async (resolve, reject) => {
            let users = await db.get().collection(collection.USER_COLLECTION).find().toArray()
            resolve(users)
        })
    },
    addheamrslt: (Data) => {
        return new Promise(async (resolve, reject) => {
            date_ob = new Date()
            let day = ("0" + date_ob.getDate()).slice(-2);
            // current month
            let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
            // current year
            let year = date_ob.getFullYear();
            let hour =date_ob.getHours()
            let minutes = date_ob.getMinutes()
            Data.time=hour+":"+minutes
            Data.date=day+"-"+month+"-"+year
            console.log(Data.date);
            db.get().collection(collection.HEAMETOLOGY).insertOne(Data).then((info) => {
                resolve(info)
            })

        })
    },
    addlftrslt: (Data) => {
        return new Promise(async (resolve, reject) => {
            date_ob = new Date()
            let day = ("0" + date_ob.getDate()).slice(-2);
            // current month
            let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
            // current year
            let year = date_ob.getFullYear();
            Data.date=day+"-"+month+"-"+year
            let hour =date_ob.getHours()
            let minutes = date_ob.getMinutes()
            Data.time=hour+":"+minutes
            console.log(Data.date);
            db.get().collection(collection.LIVERFUNCTION).insertOne(Data).then((info) => {
                resolve(info)
            })

        })
    },
    addbiorslt: (Data) => {
        return new Promise(async (resolve, reject) => {
            date_ob = new Date()
            let day = ("0" + date_ob.getDate()).slice(-2);
            // current month
            let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
            // current year
            let year = date_ob.getFullYear();
            Data.date=day+"-"+month+"-"+year
            let hour =date_ob.getHours()
            let minutes = date_ob.getMinutes()
            Data.time=hour+":"+minutes
            console.log(Data.date);
            db.get().collection(collection.BIOCHEMISTRY).insertOne(Data).then((info) => {
                resolve(info)
            })

        })
    },
    addkftrslt: (Data) => {
        return new Promise(async (resolve, reject) => {
            date_ob = new Date()
            let day = ("0" + date_ob.getDate()).slice(-2);
            // current month
            let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
            // current year
            let year = date_ob.getFullYear();
            Data.date=day+"-"+month+"-"+year
            let hour =date_ob.getHours()
            let minutes = date_ob.getMinutes()
            Data.time=hour+":"+minutes
            console.log(Data.date);
            db.get().collection(collection.RENOFUNCTION).insertOne(Data).then((info) => {
                resolve(info)
            })

        })
    }, viewhmtlgy: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.HEAMETOLOGY).find({uid:id}).sort({ _id: -1 }).toArray();
            console.log(data);
            resolve(data)
        })
    },
    viewbio: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.BIOCHEMISTRY).find({uid:id}).sort({ _id: -1 }).toArray()
            console.log(data);
            resolve(data)
        })
    },
    viewkft: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.RENOFUNCTION).find({uid:id}).sort({ _id: -1 }).toArray()
            console.log(data);
            resolve(data)
        })
    },
    viewlft: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.LIVERFUNCTION).find({uid:id}).sort({ _id: -1 }).toArray()
            console.log(data);
            resolve(data)
        })
    },
    bio: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.BIOCHEMISTRY).findOne({_id:ObjectId(id)})
            data.user= await db.get().collection(collection.USER_COLLECTION).findOne({_id:ObjectId(data.uid)})
            console.log(data);
            resolve(data)
        })
    }
    ,
    hmtlgy: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.HEAMETOLOGY).findOne({_id:ObjectId(id)})
            data.user= await db.get().collection(collection.USER_COLLECTION).findOne({_id:ObjectId(data.uid)})
            console.log(data.user);
            resolve(data)
        })
    },
    kft: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.RENOFUNCTION).findOne({_id:ObjectId(id)})
            data.user= await db.get().collection(collection.USER_COLLECTION).findOne({_id:ObjectId(data.uid)})
            console.log(data);
            resolve(data)
        })
    },
    lft: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.LIVERFUNCTION).findOne({_id:ObjectId(id)})
            data.user= await db.get().collection(collection.USER_COLLECTION).findOne({_id:ObjectId(data.uid)})
            console.log(data);
            resolve(data)
        })
    }


}