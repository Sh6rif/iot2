const express = require("express");
const { PythonShell } = require("python-shell");
const cors = require("cors");

const app = express();
app.use(express.json());

app.set("view engine", "ejs");

// Root route
app.get("/", (req, res) => {
  res.render("home.ejs");
});

// Endpoint to change LED status
app.post("/change-led-status", async (req, res) => {
  const newValue = req.body.newValue; // Assuming the new value is passed in the request body
  PythonShell.run("pup.py", { args: [newValue] }, function (err, result) {
    if (err) {
      console.error(err);
      res.status(500).json({ error: "Failed to correct spelling" });
    } else {
      res.json({ correctedText: result[0] });
    }
  });
});

app.listen(9000, () => {
  console.log("Server is running on port 9000");
});
