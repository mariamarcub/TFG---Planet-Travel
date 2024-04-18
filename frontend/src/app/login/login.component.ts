import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'; //Permite realizar solicitudes via HTTP de tipos get,post,put y delete


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
    registrar = { //Indicamos los valores que esperamos recibir
        name: '',
        lastname:'',
        secondlastname:'',        
        password: ''
    };

    iniciarSesion = { //Indicamos los valores que esperamos recibir
      name: '',             
      password: ''
  };

    constructor(private http: HttpClient) {} // Necesitamos el constructor para capturar el HttpClient y poder realizar las solicitudes

  registroForm() {
    this.http.post('http://localhost:8000/login/', this.registrar) //Ponemos la ruta de donde cogemos los datos
                                                                  //Con userData recogemos la información del usuario que queremos guardar
      .subscribe(response => {
        console.log('Respuesta del servidor:', response);
      }, error => {
        console.error('Error en la solicitud:', error);
      });
  }

  iniciarSesionForm() {
    this.http.post('http://localhost:8000/login/', this.iniciarSesion) //Ponemos la ruta de donde cogemos los datos
                                                                  //Con userData recogemos la información del usuario que queremos guardar
      .subscribe(response => {
        console.log('Respuesta del servidor:', response);
      }, error => {
        console.error('Error en la solicitud:', error);
      });
  }

  
}





