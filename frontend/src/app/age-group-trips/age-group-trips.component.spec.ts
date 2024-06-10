import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AgeGroupTripsComponent } from './age-group-trips.component';

describe('AgeGroupTripsComponent', () => {
  let component: AgeGroupTripsComponent;
  let fixture: ComponentFixture<AgeGroupTripsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AgeGroupTripsComponent]
    });
    fixture = TestBed.createComponent(AgeGroupTripsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
