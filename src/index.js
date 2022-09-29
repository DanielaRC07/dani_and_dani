const express = require('express');
const engine = require('ejs-mate'); //para las plantillas
const path = require('path'); //para que nuestra ruta sea multiplataforma ya que en windows uele cambiar
const morgan = require('morgan');
const passport = require('passport');//para autentificacion
const session = require('express-session');
//inicializaciones
const app = express();
require('./database');
require('./passport/local.auth')
//Configuraciones del puerto, que utilice el puerto de la compu o si no lo encuentra el 3000
app.set('views', path.join(__dirname, 'views'))//establemcemos nuestra carpetas de vistas para que nodejs sepa donde esta nuestras views
app.engine('ejs', engine); //para poder utilizar el motor de plantillas
app.set('view engine', 'ejs');
app.set('port', process.env.PORT ||  3000);

//middlewares
app.use(morgan('dev')); //para saber que estamos recibiendo
app.use(express.urlencoded({extended: false})); //para poder recibir datos desde el cliente, simplemente recibiendo datos
app.use(session({
    secret: 'misessionsecreta',
    resave: false,
    saveUninitialized: false

}));
app.use(passport.initialize());
app.use(passport.session());
// routes
app.use('/', require('./routes/index'))
require('./routes/index');
//iniciando el servidor
app.listen(app.get('port'), () => {
    console.log('server on Port ', app.get('port'));
});