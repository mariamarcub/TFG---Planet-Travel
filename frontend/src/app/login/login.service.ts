import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { UserLogin, UserRegister } from './login.model';
import { tap } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private registerUrl = 'http://localhost:8000/login/registrarse/';
  private loginUrl = 'http://localhost:8000/login/';
  private isAuthenticated = new BehaviorSubject<boolean>(false);  // BehaviorSubject para manejar el estado de autenticación
  private username = new BehaviorSubject<string>(''); // BehaviorSubject para poder llevar el nombre del usuario a otro componente

  constructor(private http: HttpClient) { }

  registrarse(userData: UserRegister): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post(this.registerUrl, userData, { headers: headers });
  }

  iniciarSesion(userData: any): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post(this.loginUrl, userData, { headers: headers })
      .pipe(tap((res: any) => {
        
        if (res && res.token) {
          localStorage.setItem('token', res.token);
          this.isAuthenticated.next(true);
          this.username.next(res.username); // Almacenar el nombre de usuario
          console.log('Nombre de usuario:', res.username); // Agregar console.log para imprimir el nombre de usuario

        }
      }));
  }

  getUsername(): Observable<string> {
    return this.username.asObservable().pipe(
      tap(username => console.log('Persona logueada:', username))
    );
  }
  

  salirSesion() {
    localStorage.removeItem('token');
    this.isAuthenticated.next(false);
  }

  estaAutenticado(): Observable<boolean> {
    const token = localStorage.getItem('token');
    this.isAuthenticated.next(!!token);
    return this.isAuthenticated.asObservable();
  }
  
  
}
