const express = require("express");
const router = express.Router();

episode_controller = require("../controllers/episodeController");

router.get("/", episode_controller.episode_list);

module.exports = router;