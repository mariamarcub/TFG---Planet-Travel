import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Observable, catchError, map, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BookingService {
  private apiUrl = 'http://localhost:8000/purchase-done/';

  constructor(private http: HttpClient) { }

  createPurchase(voyageData: FormBuilder): Observable<string> {
    return this.http.post<string>(this.apiUrl, voyageData).pipe(
      map(response => {
        if (response) {
          return 'Compra creada correctamente';
        } else {
          throw new Error('Respuesta vacía');
        }
      }),
      catchError((error: HttpErrorResponse) => {
        let errorMessage = 'Error desconocido';
        if (error.status !== 200) {
          errorMessage = `Error al crear la compra: ${error.status} - ${error.statusText}`;
        }
        console.error('Error al crear la compra', error);
        return throwError(() => new Error(errorMessage));
      })
    );
  }
}