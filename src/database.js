const mongoose = require('mongoose');
const { mongodb } = require('./keys');

mongoose.connect(mongodb.URI, {})
    .then(db => console.log('Database esta conectada')) //cuando te conectes muestrame esto
    .catch(err => console.error(err))