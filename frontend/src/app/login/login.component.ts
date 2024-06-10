import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from './login.service';
import { UserLogin, UserRegister } from './login.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {
  registrar: UserRegister = new UserRegister();
  iniciarSesion: UserLogin = new UserLogin();
  errorMessage: string = '';  
  registrationSuccess: boolean = false; // Variable para controlar la visibilidad del mensaje de éxito


  constructor(public loginService: LoginService, public router: Router) {}

  ngOnInit() {}

  registroForm() {    

    this.loginService.registrarse(this.registrar).subscribe({
      next: (response) => {
        console.log('Respuesta del servidor:', response);
        this.registrationSuccess = true; // Establece la variable de éxito en true
      },
      error: (error) => {
        console.error('Error en la solicitud:', error);
      }
    });
  }

  iniciarSesionForm() {
    this.loginService.iniciarSesion(this.iniciarSesion).subscribe({
      next: (response) => {
        console.log('Respuesta del servidor:', response);
        if (response && response.token) {
          this.router.navigate(['']);
          this.errorMessage = ''; // Limpia el mensaje de error si el inicio de sesión es exitoso
        }
      },
      error: (error) => {
        console.error('Error en la solicitud:', error);
        if (error.status === 401) {
          this.errorMessage = 'Credenciales incorrectas. Por favor, inténtelo de nuevo.'; // Mensaje de error específico para 401
        } else {
          this.errorMessage = 'Error en el inicio de sesión. Por favor, inténtelo de nuevo.'; // Mensaje de error genérico para otros errores
        }
      }
    });
  }
}





