import { TestBed } from '@angular/core/testing';

import { MonthTripsService } from './month-trips.service';

describe('MonthTripsService', () => {
  let service: MonthTripsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MonthTripsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
