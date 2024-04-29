const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');

router.get('index.html', userController.getAllUsers);

router.post('index.html', userController.createUser);

router.put('index.html', userController.updateUser);

router.delete('index.html', userController.deleteUser);

module.exports = router;