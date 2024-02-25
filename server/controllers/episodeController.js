const Episode = require("../models/episodeModel");
const asyncHandler = require("express-async-handler");
// const { body, validationResult } = require("express-validator")

// Display list of all episodes.
exports.episode_list = asyncHandler(async (req, res, next) => {
    const allEpisodes = await Episode.find({}, "title description")
        .sort({ title: 1 })
        .exec();

    res.send(allEpisodes);
});

// Display episode create form on GET.
// exports.episode_create_get = (req, res, next) => {
//     res.render("episode_create_form", { title: "Create Episode" });
// };

// Handle episode create on POST.
exports.episode_create_post = asyncHandler(async (req, res, next) => {
    res.send("NOT IMPLEMENTED: episode create POST");
});

// Display detail page for a specific episode.
exports.episode_detail = asyncHandler(async (req, res, next) => {
    res.send(`NOT IMPLEMENTED: episode detail: ${req.params.id}`);
});

// Display episode delete form on GET.
exports.episode_delete_get = asyncHandler(async (req, res, next) => {
    res.send("NOT IMPLEMENTED: episode delete GET");
});

// Handle episode delete on POST.
exports.episode_delete_post = asyncHandler(async (req, res, next) => {
    res.send("NOT IMPLEMENTED: episode delete POST");
});

// Display episode update form on GET.
exports.episode_update_get = asyncHandler(async (req, res, next) => {
    res.send("NOT IMPLEMENTED: episode update GET");
});

// Handle episode update on POST.
exports.episode_update_post = asyncHandler(async (req, res, next) => {
    res.send("NOT IMPLEMENTED: episode update POST");
});