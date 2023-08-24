const { sendMail, createPdf, saveMembershipData, createHTML, readMembers } = require('../services/membership.service');
const { sendMailAdmin,viewPdf,csvFileSave} = require('../services/admin.membership.service');


exports.membership_create = async (req, res, next) => {
        try {
                await saveMembershipData(req.body);
                await createHTML(req.body);
                await createPdf(req.body);
                await sendMail(req.body);
        }
        catch (err) {
                console.log(err);
        }

};

exports.membership_read = async (req, res) => {
        await readMembers(req, res);
};

exports.admin_membership_send = async (req, res) => {
        await sendMailAdmin(req.body);
};

exports.admin_membership_showPdf = async(req, res) =>{

        await viewPdf(req.body);
};

exports.admin_membership_csv = async(req,res) =>{
        await csvFileSave(req,res);
}





