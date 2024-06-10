import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, of } from 'rxjs';
import { Voyage } from '../month-trips/month-trips.model';

@Injectable({
  providedIn: 'root'
})
export class DestinyService {

  private apiUrl = 'http://localhost:8000/continentTrips';

  constructor(private http: HttpClient) { }

  getVoyagesByContinent(continentId: number): Observable<Voyage[]> {
    return this.http.get<Voyage[]>(`${this.apiUrl}/${continentId}`).pipe(
      catchError(error => {
        console.error('Error al cargar los viajes del continente', error);
        return of([]); // Devolvemos un arreglo vacío en caso de error
      })
    );
  }
}
