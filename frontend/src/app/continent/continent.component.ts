import { Component, OnInit } from '@angular/core';
import { ContinentService } from './continent.service';
import { Continent } from './continent.model';

@Component({
  selector: 'app-continent',
  templateUrl: './continent.component.html',
  styleUrls: ['./continent.component.css']
})
export class ContinentComponent implements OnInit {
  continents: Continent[] = []; //Traemos el array que contiene los continentes de la BD de django

  constructor(private continentService: ContinentService) {}

  ngOnInit() {
    this.continentService.getContinents().subscribe({
      next: (data) => {
        this.continents = data; //Utilizamos este this.continents para después sacar los continentes por pantalla
      },
      error: (error) => {
        console.error('There was an error!', error);
      }
    });
  }
}