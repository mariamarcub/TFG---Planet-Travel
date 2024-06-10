import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ThreadForumComponent } from './thread-forum.component';

describe('ThreadForumComponent', () => {
  let component: ThreadForumComponent;
  let fixture: ComponentFixture<ThreadForumComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ThreadForumComponent]
    });
    fixture = TestBed.createComponent(ThreadForumComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
