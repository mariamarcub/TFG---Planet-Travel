import { Component } from '@angular/core';
import { MonthTripsService } from './month-trips.service';
import { Voyage } from './month-trips.model';
import { ActivatedRoute, Params, Route, Router } from '@angular/router';

@Component({
  selector: 'app-month-trips',
  templateUrl: './month-trips.component.html',
  styleUrls: ['./month-trips.component.css']
})
export class MonthTripsComponent {
  voyages: Voyage[] = []; // Declaro la propiedad para almacenar el mes seleccionado por el usuario
  mesesDisponibles: Date[] = [];

  constructor(private service: MonthTripsService, private navRoute: Router, private route: ActivatedRoute) {
    // No calculamos los meses disponibles aquí
  }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      var monthId = +params['month'];
      this.loadVoyages(monthId);
    });
  }

  loadVoyages(monthId: number){
    this.service.getVoyagesByMonth(monthId).subscribe(voyages => {
      this.voyages = voyages;
      this.calcularMesesDisponibles(); // Calcular los meses disponibles después de asignar los viajes
      console.log(this.voyages)
    })
  }
  
  viewVoyage(voyageId: number){
    debugger;
    this.navRoute.navigate(['showVoyage/', voyageId])
  }

  calcularMesesDisponibles() {
    // Obtener los meses disponibles a partir de los viajes
    const meses = new Set<number>(); // Anotación de tipo
    for (const voyage of this.voyages) {
      const mes = new Date(voyage.date_start).getMonth();
      meses.add(mes);
    }
    this.mesesDisponibles = Array.from(meses).map(month => new Date(0, month));
    console.log(this.mesesDisponibles)
  }
}
