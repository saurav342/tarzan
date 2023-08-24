const nodemailer = require("nodemailer");
const Membership = require('../models/membership.model');
const express = require('express');
const fs = require('fs');
const path = require('path');
const multer = require('multer');
const csv = require('csvtojson');

//send mail
const sendMailAdmin = async (reqBody) => {
    const id = reqBody.id;
    const data = await Membership.find({ _id: id });
    const customerMail = data[0].email;
    const name = data[0].firstName + data[0].lastName;
    const fileName = await data.fileName;
    const client = nodemailer.createTransport({
        service: "Gmail",
        auth: {
            user: "tester.tarzan@gmail.com",
            pass: "nqadblashtwcsvef"
        }
    });

    const toMail = [customerMail];
    let info = client.sendMail(
        {
            from: "tester.tarzan@gmail.com",
            to: "",
            bcc: toMail,
            subject: "Membership Confirmation",
            text: `Please find below the detail of your Membership.`,
            html: `The invoice is  given below.`,
            attachments: [
                {
                    filename: `invoice-${name}.pdf`,
                    path: `docs/pdf/invoice-${name}.pdf`
                }
            ]
        }
    )
    console.log("Message sent");
}



// View Pdf
const viewPdf = async (reqBody,res) => {
    const id = reqBody.id;
    console.log(id)
    const data = await Membership.find({ _id: id });
    console.log(data);
    const name = data[0].firstName + data[0].lastName;
    console.log(name);
    const fileName = await data.fileName;
    const pdfPath = path.join(`/home/rohit/Documents/Learning/docs/pdf/invoice-AmanKumar.pdf`);
    res.sendFile(pdfPath);
}


// csv file to mongo db
const csvFileSave = async(req,res) =>
{
    const jsonArray=await csv().fromFile('Files/test.csv');
    try{
        Membership.insertMany(jsonArray);
        res.json("Inserted");
    }
    catch(err)
    {
        res.json("error");
    }
}

module.exports = {
    viewPdf, sendMailAdmin, csvFileSave
}