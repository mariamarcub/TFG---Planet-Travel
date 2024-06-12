import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Opinion } from './opinion.model'

@Injectable({
  providedIn: 'root'
})
export class OpinionService {
  private apiUrl = 'http://localhost:8000/opinions/';

  constructor(private http: HttpClient) {}

  getOpinions(): Observable<Opinion[]> {
    return this.http.get<Opinion[]>(this.apiUrl);
  }
}
