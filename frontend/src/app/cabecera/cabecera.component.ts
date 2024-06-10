import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router'; // Importa ActivatedRoute
import { LoginService } from '../login/login.service';
import { Router } from '@angular/router'; // Importa Router


@Component({
  selector: 'app-cabecera',
  templateUrl: './cabecera.component.html',
  styleUrls: ['./cabecera.component.css']
})
export class CabeceraComponent implements OnInit {
  isAuthenticated: boolean = false;
  mostrarBody: boolean = true; // Por defecto, no mostrar la foto en la cabecera
  username: string = '';

  constructor(
    private loginService: LoginService,
    private route: ActivatedRoute, // Inyecta ActivatedRoute
    private router: Router // Inyecta Router

  ) {}

  ngOnInit() {
    this.loginService.estaAutenticado().subscribe(
      (isAuthenticated: boolean) => {
        this.isAuthenticated = isAuthenticated;
  
        // Verificar si la ruta actual está definida y tiene al menos un segmento de URL
        if (this.route.snapshot.url && this.route.snapshot.url.length > 0) {
          const currentRoute = this.route.snapshot.url[0].path; // Obtener el primer segmento de la ruta
  
          if (currentRoute === 'perfil') {
            this.mostrarBody = true; // En la página de perfil, no mostrar la foto en la cabecera
          } else {
            this.mostrarBody = false; // En la página principal, mostrar la foto en la cabecera
          }
        }
      }
    );

    this.loginService.getUsername().subscribe(
      (username: string) => {
        this.username = username;
      }
    );
  }

  logout() {
    this.loginService.salirSesion();
    this.router.navigate(['/']); // Redirigir a la página principal
  }
}






