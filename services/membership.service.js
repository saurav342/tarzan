const fs = require('fs');
const puppeteer = require('puppeteer');
const nodemailer = require("nodemailer");
const Membership = require('../models/membership.model');
const moment = require('moment');
const mongoose = require('mongoose');




// read the html file
const createHTML = async (reqBody) => {
    

    fs.readFile(`/home/rohit/Documents/Learning/tempelates/invoice.html`, 'utf8', function (err, data) {
        if (err) {
            return console.log(err);
        }
        var result = data.replace('memberName', `${reqBody.firstName + ' ' + reqBody.middleName + ' ' + reqBody.lastName}`);
        result = result.replace('inVoiceDate', moment().format('MMMM Do YYYY'));
        result = result.replace()

        fs.writeFile(`/home/rohit/Documents/Learning/docs/invoice-${reqBody.firstName + reqBody.lastName}.html`, result, 'utf8', function (err) {
            if (err) return console.log(err);
        });
    });
}


//send mail
const sendMail = async (reqBody) => {
    const client = nodemailer.createTransport({
        service: "Gmail",
        auth: {
            user: "tester.tarzan@gmail.com",
            pass: "nqadblashtwcsvef"
        }
    });


    const toMail = [`${reqBody.email}`];
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
                    filename: `invoice-${reqBody.firstName + reqBody.lastName}.pdf`,
                    path: `/home/rohit/Documents/Learning/docs/pdf/invoice-${reqBody.firstName + reqBody.lastName}.pdf`
                }
            ]

        }
    )
    console.log("Message sent");


}

// pupetteer createPdf
const createPdf = async (reqBody) => {
        // Create a browser instance
        // try {
        const browser = await puppeteer.launch();
        // Create a new page
        let page;
        try {
            page = await browser.newPage();
        } catch (errr) {
            console.log(errr);
        }

        //Get HTML content from HTML file

        const html = fs.readFileSync(`/home/rohit/Documents/Learning/docs/invoice-${reqBody.firstName + reqBody.lastName}.html`, 'utf-8');
        await page.setContent(html, { waitUntil: 'domcontentloaded' });
        await page.addStyleTag({path: '/home/rohit/Documents/Learning/tempelates/membership.css'});


        // To reflect CSS used for screens instead of print
        await page.emulateMediaType('screen');

        // Downlaod the PDF
        await page.pdf({
            path: `/home/rohit/Documents/Learning/docs/pdf/invoice-${reqBody.firstName + reqBody.lastName}.pdf`,
            format: "A4"
        });


        // Close the browser instance
        await browser.close();
       


        return true;
}


const saveMembershipData = async (reqBody) => {
    try
    {
    let membership = new Membership(
        {
            membershipPeriod: reqBody.membershipPeriod,
            firstName: reqBody.firstName,
            middleName: reqBody.middleName,
            lastName: reqBody.lastName,
            residenceAddress: reqBody.residenceAddress,
            residenceCity: reqBody.residenceCity,
            postalCode: reqBody.postalCode,
            phoneNumber: reqBody.phoneNumber,
            email: reqBody.email,
            gender: reqBody.gender,
            maritalStatus: reqBody.maritalStatus,
            profession: reqBody.profession,
            officeAddress: reqBody.officeAddress,
            officeCity: reqBody.officeCity,
            reasonToJoin: reqBody.reasonToJoin,
            emergencyName: reqBody.emergencyName,
            emergencyRelation: reqBody.emergencyRelation,
            emergencyPhone: reqBody.emergencyPhone,
            parq1: reqBody.parq1,
            parq2: reqBody.parq2,
            parq3: reqBody.parq3,
            parq4: reqBody.parq4,
            parq5: reqBody.parq5,
            parq6: reqBody.parq6,
            parq7: reqBody.parq7,
            amountPaid: reqBody.amountPaid,
            trainerName: reqBody.trainerName,
            fileName: "invoice-" + reqBody.firstName + reqBody.lastName.pdf,
            status: 1,
            joinedAt: moment().format("D MMMM YYYY"),

        });
    membership.save()
    }
    catch(err){
            console.log(err);
        }
}


// read all members
const readMembers = async (req,res, error) => 
{
    try{
        let query=[
      
      ];
      
      if(req.query.keyword && req.query.keyword!=''){ 
      query.push({
        $match: { 

          $or :[
            {
              firstName : { $regex: req.query.keyword }
 
            },
            {
                middleName : { $regex: req.query.keyword }
            },
            {
                lastName : { $regex: req.query.keyword }
            }
          ]
        }
      });
      }
      if(req.query.sortOrder){

        query.push({
            $sort: {_id:1}
          });	
        }else{
        query.push({
          $sort: {_id:-1}
        });	
        }
      
      if(req.query._id){		
      query.push({
          $match: { 
            created_by:mongoose.Types.ObjectId(req.query._id),
          }	
      });
      }
      
      let total = await Membership.countDocuments(query);
      let page=(req.query.page)?parseInt(req.query.page):1;
      let perPage=(req.query.perPage)?parseInt(req.query.perPage):10;
      let skip=(page-1)*perPage;
      query.push({
      $skip:skip,
      });
      query.push({
      $limit:perPage,
      });
      
      
        console.log(query);
      let members=await Membership.aggregate(query);
      return res.send({
        members
      });
      
      }
      catch(err)
      {
      
      }
    // const members = await Membership.find()
    // res.send({ members });
}

module.exports = {
    sendMail, createPdf, saveMembershipData, createHTML, readMembers
}