const express = require('express');
const router = express.Router();
const enquiries_controller = require('../controllers/enquiries.controller');

router.post('/create-enquiries', enquiries_controller.enquiries_create);
router.get('/enquiries',enquiries_controller.enquiries_read);

module.exports = router;

