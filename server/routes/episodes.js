const express = require("express");
const router = express.Router();

episode_controller = require("../controllers/episodeController");

router.get("/", episode_controller.episode_list);
// router.get("/episode_create_form/", episode_controller.episode_create_get)
router.post("/generate/", episode_controller.episode_create_post);

module.exports = router;