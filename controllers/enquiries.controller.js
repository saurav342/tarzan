const { saveEnquiryData, readEnquiries } = require('../services/enquiries.service')

exports.enquiries_create = async (req, res, next) => {
    try{
        await saveEnquiryData(req.body);
    }
    catch(err){
        console.log(err)
    }

};  

exports.enquiries_read = async (req, res, next) => {
    console.log('................1......................', req.query
    )
    try{
        await readEnquiries(req,res);
    }
    catch(err){
        console.log(err)
    }

};  