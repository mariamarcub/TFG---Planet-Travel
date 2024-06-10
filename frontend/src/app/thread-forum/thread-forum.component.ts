import { Component } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { ThreadForumService } from './thread-forum.service';
import { CommentInfo } from './comment.model';

@Component({
  selector: 'app-thread-forum',
  templateUrl: './thread-forum.component.html',
  styleUrls: ['./thread-forum.component.css'],
})
export class ThreadForumComponent {
  threadTitle: string = '';
  threadId: number = 0;
  comments: CommentInfo[] = [];
  newComment: { content: string } = { content: '' };

  constructor(
    private forumService: ThreadForumService,
    public navRoute: Router,
    public route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params: Params) => {
      this.threadId = +params['thread'];
    });
    this.loadData();
  }

  loadData(): void {
    this.forumService.getComments(this.threadId).subscribe((data: any) => {
      this.comments = data.comments;
      this.threadTitle = data.thread_title;
    });
  }

  addComment(): void {
    if (this.newComment.content.trim()) {
      this.forumService
        .createComment(this.threadId, this.newComment)
        .subscribe((response) => {
          this.comments.push(response);
          this.newComment = { content: '' };
        });
    }
  }

  deleteComment(commentId: number): void {
    this.forumService.deleteComment(commentId).subscribe(() => {
      this.comments = this.comments.filter(
        (data: any) => data.id !== commentId
      );
    });
    this.loadData()
  }
}
