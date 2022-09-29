const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;

const User = require('../models/user');//llamamos para poder uardatr validar etc
passport.serializeUser((user,done) => {
    done(null,user.id);
});
passport.deserializeUser(async(id,done) => {
    const user = await User.findById(id);
    done(null,user);
});
passport.use('local-registro', new LocalStrategy({
    //objeto, que vamos a recivir
    usernameField: 'email',
    passwordField: 'password',
    passReqToCallback: true
}, async(req, email,password, done) => {// registrando datos
//procesando datos
    const newUser = new User(); //creamos un nuevo usuario tipo objeto
    newUser.email = email; //le pasamos su email
    newUser.password = newUser.encryptPassword(password);//pasamos la contaseña para encriptarla
    await newUser.save();//Guardando
    done(null, newUser); //devolvemo respuestas //null para error o el nuevo usuario
}));