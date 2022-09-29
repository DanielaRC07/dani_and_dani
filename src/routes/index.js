const express = require('express');
const router = express.Router();
const passport = require('passport');
router.get('/',(req, res, next) => {
    res.render('index');
});


router.get('/registro', (req, res, next) =>{
    res.render('registro');
});
router.post('/registro', passport.authenticate('local-registro',{
    successRedirect: '/profile', // si todo salio bien que entre
    failureRedirect: '/registro', //si se equivoca que lo debuelva a el registro
    passReqToCallback: true
}));

router.get('/signin', (req, res, next) =>{ //con esta direccion le enviamos una ventana para que el usuario coloque usuario y contraseña

});
router.post('/signin', (req, res, next) =>{// y escuchamos los datos y a su vez validamos
    
});

router.get('/profile', (req, res, next)=>{
    res.render('profile');
});

module.exports = router;