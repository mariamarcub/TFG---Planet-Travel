import { Component, OnInit } from '@angular/core';
import { ContinentService } from './continent.service';
import { Continent } from './continent.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-continent',
  templateUrl: './continent.component.html',
  styleUrls: ['./continent.component.css']
})
export class ContinentComponent implements OnInit {
  continents: Continent[] = [];

  constructor(private continentService: ContinentService, private router: Router) {}

  ngOnInit() {
    this.continentService.getContinents().subscribe({
      next: (data) => {
        this.continents = data;
      },
      error: (error) => {
        console.error('There was an error!', error);
      }
    });
  }

  viewVoyagesContinent(continentId: number){
    this.router.navigate(['/continentTrips', continentId]) /*Me dirige a la ruta deseada*/
  }
}