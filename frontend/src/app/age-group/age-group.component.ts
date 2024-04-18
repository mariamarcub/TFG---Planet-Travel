import { Component, OnInit } from '@angular/core';
import { AgeGroupService } from './age-group.service';
import { AgeGroup } from './age-group.model';

@Component({
  selector: 'app-age-group',
  templateUrl: './age-group.component.html',
  styleUrls: ['./age-group.component.css']
})

export class AgeGroupComponent implements OnInit {
  ageGroup: AgeGroup[] = [];

  constructor(private MonthsService: AgeGroupService) {}

  ngOnInit() {
    this.MonthsService.getAgeGroup().subscribe({
      next: (data) => {
        this.ageGroup = data;
      },
      error: (error) => {
        console.error('There was an error!', error);
      }
    });
  }
}
