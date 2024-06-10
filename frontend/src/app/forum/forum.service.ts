import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ForumService {
  private apiUrl = 'http://localhost:8000/forumVoyage'; // URL base de la API
  private deleteThreadUrl = 'http://localhost:8000/forumVoyage/delete-thread'

  constructor(private http: HttpClient) { }

  createThread(threadData: any, voyageId: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/${voyageId}`, threadData);
  }

  getActiveThreads(voyageId: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/${voyageId}`);
  }

  deleteThread(threadId: number): Observable<any> {
    return this.http.delete(`${this.deleteThreadUrl}/${threadId}`);
  }
}
