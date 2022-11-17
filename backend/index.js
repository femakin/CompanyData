const express = require("express");
const mongodb = require('mongodb');
const cors = require("cors");

require("dotenv").config();

const PORT = process.env.PORT;
const MONGODB_URI = process.env.MONGODB_URI;

let dbConnected = false;


const getMongoDB = async () => {
    const MongoClient = mongodb.MongoClient;
    let logConnString = MONGODB_URI.replace(/\/(.*:.*)@/, "//<user>:<password>@");
    console.log(`Connecting to database using ${logConnString}`);
    let db;
    try {
        const client = await MongoClient.connect(MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true });
        db = await client.db("sample_training");
        dbConnected = true;
        console.log("Database is connected and ready to go!");
        // console.log(client, 'client')
        // console.log(db, 'db')

    } catch (e) {
        console.log(e.toString());
    }
    return db;
}
let db;
let itemCollection;
getMongoDB().then(async _db => {
    db = _db;
    itemCollection = await db.collection("companies");
});


let app = express();
app.use(cors());

const log = (route, message) => {
    const now = new Date();
    const date = `${now.getDay()}/${(now.getMonth() + 1).toString().padStart(2, "0")}/${now.getFullYear()}`;
    const time = `${(now.getHours()).toString().padStart(2, "0")}:${(now.getMinutes()).toString().padStart(2, "0")}:${(now.getSeconds()).toString().padStart(2, "0")}`;
    const log = `[${date} ${time}] - (${route}) - ${message}`;
    console.log(log);
}

app.get("/", async (req, res) => {
    log("/", "GET request");
    // res.send({ status: "Ok", dbConnected }).status(200);
    // results = await itemCollection.find({})
    results = await itemCollection.find({}).toArray();
    res.send(results).status(200);
    // res.status(200).json(results)
});


app.get("/socialgroup", async (req, res) => {
    let results = {};
    log("/socialgroup", `GET request`);

    try {
        results = await itemCollection.aggregate([
            {
                $facet: {
                    // categories: [
                    //   { $match: { category: { $ne: null } } },
                    //   { $sortByCount: "$brand" }
                    // ]
                    socialgroup: [
                        {
                            $match: {
                                category_code: { $ne: null }
                            }
                        },
                        {
                            $sortByCount: "$category_code"
                        }
                    ]
                }
            }
        ]).toArray();
        console.log(results[0], 'resultsss')
    } catch (e) {
        log("/socialgroup", e.toString());
    }

    let processedResults = results[0].socialgroup;
    res.send(processedResults).status(200);
    // console.log(results, 'results')
})





app.get("/items/category/:category", async (req, res) => {
    log("/items/category/:category", `GET request with parameter ${req.params.category}`);
    let results = [];
    try {
        results = await itemCollection.find({ category_code: req.params.category }).limit(24).toArray();


        console.log(results, 'find dataaaaa')
    } catch (e) {
        log(`/items/category/${req.params.category}`, e.toString());
    }
    res.send(results).status(200);
});




app.listen(PORT, () => console.log(`Server started on port ${PORT}`));