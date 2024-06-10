import { TestBed } from '@angular/core/testing';

import { ThreadForumService } from './thread-forum.service';

describe('ThreadForumService', () => {
  let service: ThreadForumService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ThreadForumService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
