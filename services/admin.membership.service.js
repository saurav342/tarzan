const nodemailer = require("nodemailer");
const Membership = require('../models/membership.model');
const express = require('express');
const fs = require('fs');
const pdfParse = require('pdf-parse')

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
                    path: `docs/invoice-as.pdf`
                }
            ]
        }
    )
    console.log("Message sent");
}



// View Pdf
const viewPdf = async (req) => {
    const id = reqBody.id;
    const data = await Membership.find({ _id: id });
    const name = data[0].firstName + data[0].lastName;
    const fileName = await data.fileName;
    var stream = fs.createReadStream(`/home/rohit/Documents/Learning/docs/pdf/invoice-${reqBody.firstName + reqBody.lastName}.pdf`);
  var filename = `invoice-${name}.pdf`; 
  // Be careful of special characters

  filename = encodeURIComponent(filename);
  // Ideally this should strip them

  res.setHeader('Content-disposition', 'inline; filename="' + filename + '"');
  res.setHeader('Content-type', 'application/pdf');

  stream.pipe(res);
}


module.exports = {
    viewPdf, sendMailAdmin
}