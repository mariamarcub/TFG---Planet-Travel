import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Voyage } from './month-trips.model'; // Asegúrate de que este modelo refleje correctamente la estructura de datos que esperas.

@Injectable({
  providedIn: 'root'
})
export class MonthTripsService {
  private apiUrl = 'http://localhost:8000/monthTrips'; // Asegúrate de que esta URL sea correcta y consistente con tus endpoints de backend.

  constructor(private http: HttpClient) { }

  getVoyagesByMonth(monthId: number): Observable<Voyage[]> {
    return this.http.get<Voyage[]>(`${this.apiUrl}/${monthId}`).pipe(
      catchError(error => {
        console.error('Error al cargar los viajes del mes', error);
        return of([]); // Devolvemos un arreglo vacío en caso de error
      })
    );
  }
}