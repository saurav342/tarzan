const express = require('express');
const router = express.Router();
const membership_controller = require('../controllers/membership.controller');


router.post('/m_create',membership_controller.membership_create);
router.get('/members',membership_controller.membership_read);
router.post('/admin_members',membership_controller.admin_membership_send);
router.post('/view-Pdf',membership_controller.admin_membership_showPdf);
router.post('/upload',membership_controller.admin_membership_csv);


module.exports = router;

