const mongoose = require("mongoose");

const EpisodeSchema = new mongoose.Schema({
    title: { type: String, required: true, maxLength: 100 },
    description: { type: String, required: false, maxLength: 1000 },
    audio: { type: Buffer, required: false },
}, { collection: 'Episode' });

EpisodeSchema.virtual("url").get(function () {
    return `/episodes/$(this._id)`;
});

module.exports = mongoose.model("Episode", EpisodeSchema);