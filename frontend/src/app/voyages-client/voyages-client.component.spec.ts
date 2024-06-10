import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VoyagesClientComponent } from './voyages-client.component';

describe('VoyagesClientComponent', () => {
  let component: VoyagesClientComponent;
  let fixture: ComponentFixture<VoyagesClientComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VoyagesClientComponent]
    });
    fixture = TestBed.createComponent(VoyagesClientComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
