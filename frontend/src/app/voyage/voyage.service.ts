import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { VoyageInfo } from './voyage.model';

@Injectable({
  providedIn: 'root'
})
export class VoyageService {
  private apiUrl = 'http://localhost:8000/showVoyage';

  constructor(private http: HttpClient) { }

  getVoyageById(voyageId: number): Observable<VoyageInfo>{
    return this.http.get<VoyageInfo>(`${this.apiUrl}/${voyageId}`).pipe(
      catchError(error => {
        console.error('Error al cargar los viajes del mes', error);
        return of(); // Devolvemos un arreglo vacío en caso de error
      })
    );
  }
}
