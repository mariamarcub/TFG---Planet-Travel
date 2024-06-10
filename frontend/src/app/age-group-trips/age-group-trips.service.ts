import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, of } from 'rxjs';
import { Voyage } from '../month-trips/month-trips.model';

@Injectable({
  providedIn: 'root'
})
export class AgeGroupTripsService {

  private apiUrl = 'http://localhost:8000/ageGroupTrips'; // Asegúrate de que esta URL sea correcta y consistente con tus endpoints de backend.

  constructor(private http: HttpClient) { }


  getVoyagesByAge(ageGroup: string): Observable<Voyage[]> {
    return this.http.get<Voyage[]>(`${this.apiUrl}/${ageGroup}`).pipe(
      catchError(error => {
        console.error('Error al cargar los viajes del grupo de edad', error);
        return of([]); // Devolvemos un arreglo vacío en caso de error
      })
    );
  }
}
