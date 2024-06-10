import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ThreadForumService {

  private apiUrl = 'http://localhost:8000/forumVoyage/thread'; // URL base de la API
  private deleteCommentUrl = 'http://localhost:8000/forumVoyage/delete-comment';

  constructor(private http: HttpClient) { }

  createComment(threadId: number, comment: { content: string }): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/${threadId}`, comment);
  }

  getComments(threadId: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/${threadId}`);
  }

  deleteComment(commentId: number): Observable<any> {
    return this.http.delete(`${this.deleteCommentUrl}/${commentId}`);
  }
}
