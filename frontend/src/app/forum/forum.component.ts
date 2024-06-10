import { Component, OnInit } from '@angular/core';
import { ForumService } from './forum.service';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Thread } from './thread.model';

@Component({
  selector: 'app-forum',
  templateUrl: './forum.component.html',
  styleUrls: ['./forum.component.css']
})
export class ForumComponent implements OnInit {
  showCreateThreadForm: boolean = false;
  threadTitle: string = '';
  activeThreads: Thread[] = [];
  voyageId: number = 0;

  constructor(private forumService: ForumService, public navRoute: Router, public route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.params.subscribe((params: Params) => {
      this.voyageId = +params['voyage'];
    });
    this.loadActiveThreads();
  }

  onSubmit(): void {
    const threadData = { title: this.threadTitle, voyageId: this.voyageId };
    this.forumService.createThread(threadData, this.voyageId).subscribe(response => {
      console.log('Hilo creado:', response);
      this.showCreateThreadForm = false;
      this.threadTitle = '';
      this.loadActiveThreads(); // Recargar los hilos activos después de crear uno nuevo
    });
  }

  loadActiveThreads(): void {
    this.forumService.getActiveThreads(this.voyageId).subscribe(threads => {
      this.activeThreads = threads;
    });
  }

  deleteThread(threadId: any): void {
    this.forumService.deleteThread(threadId).subscribe(response => {
      this.loadActiveThreads();
    });
  }

  accessThread(threadId: any): void {
    this.navRoute.navigate(['forumVoyage/thread/', threadId]);
  }
}
