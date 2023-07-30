const mongoose = require('mongoose');
const Schema = mongoose.Schema;

let membershipSchema = new Schema({
    membershipPeriod: {type: String, required: false},
    firstName: {type: String, required: false},
    middleName: {type: String},
    lastName: {type: String},
    residenceAddress: {type: String, required: false},
    residenceCity:{type: String, required: false},
    postalCode: {type: String, maxLength: 6, required: false},
    phoneNumber: {type: String, maxLength:10, required: false},
    gender: {type: String, required: false},
    maritalStatus: {type: String, required: false},
    profession:{type: String},
    officeAddress: {type: String},
    officeCity: {type: String},
    reasonToJoin: {type: String, required: false},
    emergencyName: {type: String, required: false},
    emergencyRelation: {type: String, required: false},
    emergencyPhone: {type: String, required: false},
    parq1: {type: String, required: false},
    parq2: {type: String, required: false},
    parq3: {type: String, required: false},
    parq4: {type: String, required: false},
    parq5: {type: String, required: false},
    parq6: {type: String, required: false},
    parq7: {type: String, required: false},
});

module.exports = mongoose.model('Membership', membershipSchema)