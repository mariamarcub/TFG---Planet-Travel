import { Component, OnInit  } from '@angular/core';
import { MonthsService } from './months.service';
import { Months } from './months.model';
import { Router } from '@angular/router';


@Component({
  selector: 'app-months',
  templateUrl: './months.component.html',
  styleUrls: ['./months.component.css']
})

export class MonthsComponent implements OnInit {
  months: Months[] = [];

  constructor(private MonthsService: MonthsService, private router: Router) {}

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

  viewVoyagesMonth(month_id: number){
    this.router.navigate(['/monthTrips', month_id]) /*Me dirige a la ruta deseada*/
  }
}