'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// Message to display 
const customMessage = process.env.MY_CUSTOM_MESSAGE || 'Hello World'; // Use 'Hello World' if MY_CUSTOM_MESSAGE variable is not set

// App
const app = express();
app.get('/', (req, res) => {
  res.send(`Hello World ${customMessage}`);
});

app.listen(PORT, HOST);
console.log(`Value of customMessage: ${customMessage}`);
console.log(`Running on http://${HOST}:${PORT}`);
