var express = require("express");
var app = express();
var morgan = require("morgan");

var users = [
    {id: 1, name: "test1"},
    {id: 2, name: "test2"},
    {id: 3, name: "test3"},
]

app.use(morgan("dev"));

// app.get("/", function(req, res) {
//     res.send("Hello World");
// });

app.get("/users", function (req, res) {
    res.json(users);
});

app.listen(3000, function() {
    console.log("server open 3000");
});

module.exports = app;