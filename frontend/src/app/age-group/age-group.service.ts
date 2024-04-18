import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AgeGroup } from './age-group.model'; /*Referenciamos al models del componente*/

@Injectable({
  providedIn: 'root'
})
export class AgeGroupService {
  private apiUrl = 'http://localhost:8000/ageGroup/';

  constructor(private http: HttpClient) { }

  getAgeGroup(): Observable<AgeGroup[]> {
    return this.http.get<AgeGroup[]>(this.apiUrl);
  }
}

