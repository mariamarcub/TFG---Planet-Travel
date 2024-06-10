import { Component, OnInit } from '@angular/core';
import { AgeGroupTripsService } from './age-group-trips.service';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Voyage } from './age-group-trips.model';

@Component({
  selector: 'app-age-group-trips',
  templateUrl: './age-group-trips.component.html',
  styleUrls: ['./age-group-trips.component.css']
})
export class AgeGroupTripsComponent implements OnInit {

  voyages: Voyage[] = []; // Declaro la propiedad para almacenar los viajes
  ageGroup: string = ''; // Grupo de edad seleccionado
  selectedAge: string = ''; // Nombre del grupo edad seleccionado
  
  constructor(private service: AgeGroupTripsService, private navRoute: Router, private route: ActivatedRoute) {}
  
  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      this.ageGroup = params['ageGroup'].replace(/\\s+/g, '');
      this.loadVoyages(this.ageGroup);
      this.selectedAge = this.getAgeGroup(+this.ageGroup); // Asignar el nombre del grupo de edad seleccionado
    });
  }

  // Cargar los viajes teniendo en cuenta el grupo de edad seleccionado
  loadVoyages(ageGroup: string) {
    this.service.getVoyagesByAge(ageGroup).subscribe(voyages => {
      this.voyages = voyages;
    });
  }
  
  // Ver el viaje que se ha seleccionado en la página donde filtramos por grupo
  viewVoyage(voyageId: number) {
    this.navRoute.navigate(['showVoyage/', voyageId]);
  }

  // Igualar las posiciones registradas en la BD con la nuestra proporcionado desde el backend 
  getAgeGroup(ageId: number): string {
    const groupNames = [
      '18-30', '30-45', '45+'
    ];
    return groupNames[ageId - 1];
  }
}
