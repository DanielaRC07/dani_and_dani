const mongoose = require('mongoose');
const bcrypt = require('bcrypt-nodejs'); //para cifrar la contraseña
const {Schema} = mongoose;
const userSchema = new Schema({ //que contendra
    email: String,
    password: String,
    //podemos preguntar mas
});
userSchema.methods.encryptPassword = (password) => { //encirptar la contraseña
    return bcrypt.hashSync(password, bcrypt.genSaltSync(10)); //las veces que ejecutaremos el algoritmo para cifrar la contraseña
};
userSchema.methods.comparePassword = function(password){ //compararemos las dos contraseñas, las de database y la ingresada por el usuario
    return bcrypt.compareSync(password, this.password);
};
module.exports = mongoose.model('users', userSchema);