const fs = require('fs');
const puppeteer = require('puppeteer');
const nodemailer = require("nodemailer");
const Membership = require('../models/membership.model');
const moment = require('moment');



// read the html file
const createHTML = async (reqBody) => {
    console.log('..............................2..................................');

    fs.readFile(`/home/rohit/Documents/Learning/tempelates/invoice.html`, 'utf8', function (err, data) {
        if (err) {
            return console.log(err);
        }

        // modify the html on form data

        var result = data.replace('memberName', `${reqBody.firstName + ' ' + reqBody.middleName + ' ' + reqBody.lastName}`);
        result = result.replace('inVoiceDate', moment().format('MMMM Do YYYY'));
        result = result.replace()

        // save the file using invoice-rohit-raj.html

        fs.writeFile(`/home/rohit/Documents/Learning/docs/invoice-${reqBody.firstName + reqBody.lastName}.html`, result, 'utf8', function (err) {
            if (err) return console.log(err);
        });
    });
}


//send mail
const sendMail = async (reqBody) => {
    console.log('.....logs-+ sendmail......4.........')
    const client = nodemailer.createTransport({
        service: "Gmail",
        auth: {
            user: "tester.tarzan@gmail.com",
            pass: "nqadblashtwcsvef"
        }
    });


    const toMail = ["something.czar@gmail.com"];
    let info = client.sendMail(
        {
            from: "tester.tarzan@gmail.com",
            to: "rohitgamerid@gmail.com",
            bcc: toMail,
            subject: "Membership Confirmation",
            text: `Please find below the detail of your Membership.`,
            html: `The invoice is  given below.`,
            attachments: [
                {
                    filename: `invoice-${reqBody.firstName + reqBody.lastName}.pdf`,
                    path: `/home/rohit/Documents/Learning/docs/invoice-${reqBody.firstName + reqBody.lastName}.pdf`
                }
            ]

        }
    )
    console.log("Message sent: %s", info.messageId);


}

// pupetteer createPdf
const createPdf = async (reqBody) => {
    console.log('..............................3..................................');


    

        console.log("browser");

        // Create a browser instance
        // try {
        console.log("111111111");

        const browser = await puppeteer.launch();
        console.log("222222222");

        // Create a new page
        let page;
        try {
            page = await browser.newPage();
        } catch (errr) {
            console.log(errr);
        }

        //Get HTML content from HTML file
        console.log("33333333333333");

        const html = fs.readFileSync(`/home/rohit/Documents/Learning/docs/invoice-${reqBody.firstName + reqBody.lastName}.html`, 'utf-8');
        await page.setContent(html, { waitUntil: 'domcontentloaded' });
        await page.addStyleTag({path: '/home/rohit/Documents/Learning/tempelates/membership.css'});

        console.log("html read");

        // To reflect CSS used for screens instead of print
        await page.emulateMediaType('screen');

        // Downlaod the PDF
        await page.pdf({
            path: `/home/rohit/Documents/Learning/docs/invoice-${reqBody.firstName + reqBody.lastName}.pdf`,
            format: "A4"
        });

        console.log("page created");

        // Close the browser instance
        await browser.close();
        // } catch (err) {
        //     console.log('...eeeeeeeeeeeeerrrrr.................', err);
        // }


        return true;
}


const saveMembershipData = async (reqBody, error) => {

    console.log('..............................1..................................');
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
        });

    membership.save().then(() => {
    })
        .catch((err) => {
            res.send(err);
        });
}


module.exports = {
    sendMail, createPdf, saveMembershipData, createHTML
}