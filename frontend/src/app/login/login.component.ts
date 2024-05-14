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

  constructor(private loginService: LoginService, private router: Router) {}

  ngOnInit() {}

  registroForm() {
    this.loginService.registrarse(this.registrar).subscribe({
      next: (response) => {
        console.log('Respuesta del servidor:', response);
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
        }
      },
      error: (error) => {
        console.error('Error en la solicitud:', error);
      }
    });
  }
}



