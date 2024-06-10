import { TestBed } from '@angular/core/testing';

import { AgeGroupTripsService } from './age-group-trips.service';

describe('AgeGroupTripsService', () => {
  let service: AgeGroupTripsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AgeGroupTripsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
