const mongoose = require('mongoose');
const Schema = mongoose.Schema;

let membershipSchema = new Schema({
    membershipPeriod: {type: String, required: true},
    firstName: {type: String, required: true},
    middleName: {type: String},
    lastName: {type: String},
    residenceAddress: {type: String, required: true},
    residenceCity:{type: String, required: true},
    postalCode: {type: Number, maxLength: 6, required: true},
    phoneNumber: {type: Number, maxLength:10, required: true},
    email: {type: String, required: true},
    gender: {type: String, required: true},
    maritalStatus: {type: String, required: true},
    profession:{type: String},
    officeAddress: {type: String},
    officeCity: {type: String},
    reasonToJoin: {type: String},
    emergencyName: {type: String, required: true},
    emergencyRelation: {type: String, required: true},
    emergencyPhone: {type: Number, required: true},
    parq1: {type: String, required: true},
    parq2: {type: String, required: true},
    parq3: {type: String, required: true},
    parq4: {type: String, required: true},
    parq5: {type: String, required: true},
    parq6: {type: String, required: true},
    parq7: {type: String, required: true},
    amountPaid: {type:Number, required:true},
    trainerName:{type: String},
    fileName:{type: String},
    status: {type: Number, required: true},

});

module.exports = mongoose.model('Membership', membershipSchema)