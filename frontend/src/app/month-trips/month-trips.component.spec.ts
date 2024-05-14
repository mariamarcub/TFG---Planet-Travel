import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MonthTripsComponent } from './month-trips.component'; //Es el mismo nombre del constructor del archivo components.ts

describe('MonthTripsComponent', () => {
  let component: MonthTripsComponent;
  let fixture: ComponentFixture<MonthTripsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MonthTripsComponent]
    });
    fixture = TestBed.createComponent(MonthTripsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
