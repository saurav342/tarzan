const mongoose = require('mongoose');
const Schema = mongoose.Schema;

let enquiriesSchema = new Schema({
    name: {type: String, required: true},
    address: {type: String, required: true},
    postalCode: {type: Number, maxLength: 6, required: true},
    phoneNumber: {type: Number, maxLength:10, required: true},
    email: {type: String, required: true},
    gender: {type: String, required: true},
    maritalStatus: {type: String, required: true},
    reasonToJoin: {type: String, required: true},
});

module.exports = mongoose.model('Enquiries', enquiriesSchema)