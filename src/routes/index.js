"use strict";

const express = require("express");
const router = express.Router();

const ctrl = require("./home");

router.get("/", ctrl.output.home);

module.exports = router;