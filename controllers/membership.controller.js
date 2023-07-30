const {sendMail, createPdf, saveMembershipData, createHTML} = require('../services/membership.service');


exports.membership_create =  async (req, res, next) => {
        await saveMembershipData(req.body);
        await createHTML(req.body);
        await createPdf(req.body);
        await sendMail(req.body);
   
};



