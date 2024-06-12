import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { VoyageInfo } from './voyage.model';
import { Opinion } from '../opinion/opinion.model';


@Injectable({
  providedIn: 'root'
})
export class VoyageService {
  private apiUrl = 'http://localhost:8000/showVoyage';
  private opinionUrl = 'http://localhost:8000/opinions/'; //La información de la vista en Pycharm sobre opinion


  constructor(private http: HttpClient) { }

  //El voyageId se envía por URL
  getVoyageById(voyageId: number): Observable<VoyageInfo>{
    return this.http.get<VoyageInfo>(`${this.apiUrl}/${voyageId}`).pipe(
      catchError(error => {
        console.error('Error al cargar los viajes del mes', error);
        return of(); // Devolvemos un arreglo vacío en caso de error
      })
    );
  }

  //El voyageId y opinion se envían por el body
  createOpinion(opinion: Opinion, voyageId: number): Observable<Opinion> {
    return this.http.post<Opinion>(this.opinionUrl, {'opinion': opinion, 'voyage_id': voyageId}).pipe(
      catchError(error => {
        console.error('Error al crear la opinión', error);
        return of(); // Devolvemos un arreglo vacío en caso de error
      })
    );
  }

}
