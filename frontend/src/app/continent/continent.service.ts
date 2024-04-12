import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Continent } from './continent.model';

@Injectable({
  providedIn: 'root'
})
export class ContinentService {
  private apiUrl = 'http://localhost:8000/continents/'; //Relacionamos con la URL de Django

  constructor(private http: HttpClient) { }

  getContinents(): Observable<Continent[]> { //Llamamos al método GET de django y metemos los valores en el array Continent
    return this.http.get<Continent[]>(this.apiUrl);
  }
}
