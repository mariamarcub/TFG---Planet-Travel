import { TestBed } from '@angular/core/testing';

import { VoyagesClientService } from './voyages-client.service';

describe('VoyagesClientService', () => {
  let service: VoyagesClientService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(VoyagesClientService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
