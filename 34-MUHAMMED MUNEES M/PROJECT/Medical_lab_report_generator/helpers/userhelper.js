const { resolve, reject } = require('promise')
var db = require('../config/connection')
var collection = require('../config/collections')
const { response } = require('express')
var objectId = require('mongodb').ObjectId

module.exports = {
    doLogin: (Data) => {
        return new Promise(async (resolve, reject) => {
            let loginStatus = false
            let response = {}
            let user = await db.get().collection(collection.USER_COLLECTION).findOne({ email:Data.email })
            let password = await db.get().collection(collection.USER_COLLECTION).findOne({ password:Data.password })
            if (user) {
                if (password) {
                    loginStatus = true
                }
                if (loginStatus) {
                    console.log("success");
                    response.user = user
                    response.loginStatus = true
                    resolve(response)
                } else {
                    console.log("failed");
                    resolve({ loginStatus: false })
                }

            } else {
                console.log("db failed");
                resolve({ status: false })
            }
        })
    },
    viewhmtlgy: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.HEAMETOLOGY).find({uid:id}).toArray()
            console.log(data);
            resolve(data)
        })
    },
    viewsuagar: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.BIOCHEMISTRY).find({uid:id}).sort({_id:-1}).limit(1).toArray()
            console.log(data);
            resolve(data)
        })
    },
    viewcreatinin: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.RENOFUNCTION).find({uid:id}).sort({_id:-1}).limit(1).toArray()
            console.log(data);
            resolve(data)
        })
    },
    viewbio: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.BIOCHEMISTRY).find({uid:id}).toArray()
            console.log(data);
            resolve(data)
        })
    },
    viewkft: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.RENOFUNCTION).find({uid:id}).toArray()
            console.log(data);
            resolve(data)
        })
    },
    viewlft: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.LIVERFUNCTION).find({uid:id}).toArray()
            console.log(data);
            resolve(data)
        })
    },
    bio: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.BIOCHEMISTRY).findOne({_id:objectId(id)})
            console.log(data);
            resolve(data)
        })
    }
    ,
    hmtlgy: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.HEAMETOLOGY).findOne({_id:objectId(id)})
            console.log(data);
            resolve(data)
        })
    },
    kft: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.RENOFUNCTION).findOne({_id:objectId(id)})
            console.log(data);
            resolve(data)
        })
    },
    lft: (id) => {
        return new Promise(async (resolve, reject) => {
            let data = await db.get().collection(collection.LIVERFUNCTION).findOne({_id:objectId(id)})
            console.log(data);
            resolve(data)
        })
    }
}