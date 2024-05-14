import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Months } from './months.model'; /Referenciamos al models del componente/

@Injectable({
  providedIn: 'root'
})
export class MonthsService {
  private apiUrl = 'http://localhost:8000/months/';

  constructor(private http: HttpClient) { }

  getMonths(): Observable<Months[]> {
    return this.http.get<Months[]>(this.apiUrl);
  }
}
