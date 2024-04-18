import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Continent } from './continent.model';

@Injectable({
  providedIn: 'root'
})
export class ContinentService {
  private apiUrl = 'http://localhost:8000/continents/';

  constructor(private http: HttpClient) { }

  getContinents(): Observable<Continent[]> {
    return this.http.get<Continent[]>(this.apiUrl);
  }
}
