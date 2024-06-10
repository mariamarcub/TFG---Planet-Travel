import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { VoyageCity } from './voyages-client.model';


@Injectable({
  providedIn: 'root'
})
export class VoyagesClientService {

  private apiUrl = 'http://localhost:8000/voyagesByClient';

  constructor(private http: HttpClient) { }

  getVoyagesByClient(): Observable<VoyageCity[]> {
    return this.http.get<VoyageCity[]>(this.apiUrl).pipe(
      catchError(error => {
        console.error('Error al cargar los viajes del cliente', error);
        return of([]);
      })
    );
  }

  
}
