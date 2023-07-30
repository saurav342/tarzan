const express = require('express');
const router = express.Router();

const membership_controller = require('../controllers/membership.controller');
router.post('/m_create',membership_controller.membership_create);

module.exports = router;

