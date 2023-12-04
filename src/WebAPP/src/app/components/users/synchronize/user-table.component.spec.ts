import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SynhronizeComponent } from './user-table.component';

describe('SynhronizeComponent', () => {
  let component: SynhronizeComponent;
  let fixture: ComponentFixture<SynhronizeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SynhronizeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SynhronizeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
