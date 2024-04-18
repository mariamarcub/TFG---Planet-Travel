import { Component, OnInit  } from '@angular/core';
import { MonthsService } from './months.service';
import { Months } from './months.model';


@Component({
  selector: 'app-months',
  templateUrl: './months.component.html',
  styleUrls: ['./months.component.css']
})

export class MonthsComponent implements OnInit {
  months: Months[] = [];

  constructor(private MonthsService: MonthsService) {}

  ngOnInit() {
    this.MonthsService.getMonths().subscribe({
      next: (data) => {
        this.months = data;
      },
      error: (error) => {
        console.error('There was an error!', error);
      }
    });
  }
}
