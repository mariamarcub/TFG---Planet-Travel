import { Component, OnInit } from '@angular/core';
import { MonthTripsService } from './month-trips.service';
import { Voyage } from './month-trips.model';
import { ActivatedRoute, Params, Router } from '@angular/router';

@Component({
  selector: 'app-month-trips',
  templateUrl: './month-trips.component.html',
  styleUrls: ['./month-trips.component.css']
})
export class MonthTripsComponent implements OnInit {
  voyages: Voyage[] = []; // Declaro la propiedad para almacenar los viajes
  monthId: number = 1; // Mes seleccionado
  selectedMonth: string = ''; // Nombre del mes seleccionado

  constructor(public service: MonthTripsService, public navRoute: Router, public route: ActivatedRoute) {}
  

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      this.monthId = +params['month'];
      this.loadVoyages(this.monthId);
      this.selectedMonth = this.getMonthName(this.monthId); // Asignar el nombre del mes seleccionado
    });
  }

  loadVoyages(monthId: number) {
    this.service.getVoyagesByMonth(monthId).subscribe(voyages => {
      this.voyages = voyages;
    });
  }
  
  viewVoyage(voyageId: number) {
    this.navRoute.navigate(['showVoyage/', voyageId]);
  }

  getMonthName(monthId: number): string {
    const monthNames = [
      'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ];
    return monthNames[monthId - 1];
  }
}
