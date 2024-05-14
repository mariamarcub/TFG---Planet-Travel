import { Injectable } from '@angular/core';
import {
  HttpEvent, HttpInterceptor, HttpHandler, HttpRequest
} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class LoginInterceptor implements HttpInterceptor {

  constructor() {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Obtener el token de localStorage
    const authToken = localStorage.getItem('token');
    let authReq = req;
    // Clonar la solicitud para añadir el nuevo header.
    if (authToken){
        authReq = req.clone({headers: req.headers.set('Authorization', `Token ${authToken}`)
    });
    }
    // Pasar la solicitud clonada al siguiente handler.
    return next.handle(authReq);
  }
}
