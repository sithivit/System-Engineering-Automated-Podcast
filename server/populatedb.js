#! /usr/bin/env node

// Get arguments passed on command line
const userArgs = process.argv.slice(2);

const Episode = require("./models/episodeModel");

const mongoose = require("mongoose");
mongoose.set("strictQuery", false);

const mongoDB = userArgs[0];

main().catch((err) => console.log(err));

async function main() {
    console.log("Debug: About to connect");
    await mongoose.connect(mongoDB);
    console.log("Debug: Should be connected?");
    await createEpisodes();
    console.log("Debug: Closing mongoose");
    mongoose.connection.close();
}

async function episodeCreate(name, des) {
    const episode = new Episode({ title: name, description: des });
    await episode.save();
    console.log(`Added episode: ${name}`);
}

async function createEpisodes() {
    console.log("Adding episodes");
    await Promise.all([
        episodeCreate("Test", "Some Test Episode Description"),
        episodeCreate("Example", "Some Example Episode Description"),
    ]);
}