import { Component, OnInit } from '@angular/core';
import { DestinyService } from './destiny.service';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Voyage } from '../month-trips/month-trips.model';

@Component({
  selector: 'app-destiny',
  templateUrl: './destiny.component.html',
  styleUrls: ['./destiny.component.css']
})
export class DestinyComponent implements OnInit {
  voyages: Voyage[] = []; // Lista de viajes (voyages)
  continentId: number = 1; // Continente seleccionado
  selectedContinentName: string = ''; // Nombre del continente seleccionado

 

  constructor(public destinyService: DestinyService, public navRoute: Router, public http: HttpClient, public route: ActivatedRoute) {
    this.selectedContinentName = ''; // Inicializar la propiedad en el constructor
  
  }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      var continentId = +params['continent'];
    this.loadContinents(continentId);
    this.selectedContinentName = this.getContinentName(continentId); // Usar continentId en lugar de this.continentId
    });
  }

  // Cargar la lista de continentes desde la API
  loadContinents(continentId: number) {
    this.destinyService.getVoyagesByContinent(continentId).subscribe({
      next: (data) => {
        this.voyages = data; // Corregido para almacenar en voyages
      },
      error: (error) => {
        console.error('Error al cargar los viajes del continente', error);
      }
    });
  }
  

  getContinentName(continentId: number): string {
    const continentNames = [
      'Oceania', 'Europa', 'America', 'Africa', 'Asia'
    ];
    return continentNames[continentId - 1];
  }

  viewVoyage(voyageId: number) {
    this.navRoute.navigate(['showVoyage/', voyageId]);
  }
}

