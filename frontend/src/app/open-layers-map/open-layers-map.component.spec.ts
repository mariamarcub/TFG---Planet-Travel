import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OpenLayersMapComponent } from './open-layers-map.component';

describe('OpenLayersMapComponent', () => {
  let component: OpenLayersMapComponent;
  let fixture: ComponentFixture<OpenLayersMapComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [OpenLayersMapComponent]
    });
    fixture = TestBed.createComponent(OpenLayersMapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
