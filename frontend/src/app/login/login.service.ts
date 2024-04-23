import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { UserLogin, UserRegister } from './login.model';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private registerUrl = 'http://localhost:8000/login/registrarse/';
  private loginUrl = 'http://localhost:8000/login/';

  constructor(private http: HttpClient) { }

  registrarse(userData: UserRegister): Observable<any> {
    return this.http.post(this.registerUrl, userData);
  }

  iniciarSesion(userData: UserLogin): Observable<any> {
    return this.http.post(this.loginUrl, userData);
  }
}
