import { Component, OnInit } from '@angular/core';
import { VoyageService } from './voyage.service';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { VoyageInfo} from './voyage.model';
import { Opinion } from '../opinion/opinion.model';
import { LoginService } from '../login/login.service';

@Component({
  selector: 'app-voyage',
  templateUrl: './voyage.component.html',
  styleUrls: ['./voyage.component.css']
})
export class VoyageComponent implements OnInit {
  voyage: VoyageInfo = new VoyageInfo();
  totalDays: number = 0;
  numPersons: number = 0;
  opinion: Opinion = { id: 0, rating: 0, comment: '', voyage_id: 0, report_date: ''};
  isAuthenticated: boolean = false;
  comentarioCreado: boolean = false; // Variable para controlar la visibilidad del mensaje



  constructor(public service: VoyageService, public navRoute: Router, public route: ActivatedRoute, private loginService: LoginService) {}

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      var voyageId = +params['voyage'];
      this.loadVoyageInfo(voyageId);
    });

    //Ver si el usuario estar autenticado
    this.loginService.estaAutenticado().subscribe(authenticated => {
      this.isAuthenticated = authenticated;
    });
  }

  loadVoyageInfo(voyageId: number) {
    this.service.getVoyageById(voyageId).subscribe(voyage => {
      this.voyage = voyage;
      this.calculateTotalDays();
    });
  }

  calculateTotalDays(): void {
    const startDate = new Date(this.voyage.voyage_date_start);
    const endDate = new Date(this.voyage.voyage_date_end);
    const differenceInMilliseconds = endDate.getTime() - startDate.getTime();
    this.totalDays = differenceInMilliseconds / (1000 * 60 * 60 * 24);
  }

  goToBooking(voyageId: number, voyagePrice: number, numPersons: number) {
    this.navRoute.navigate([`/bookingVoyage/${voyageId}`, { 
      numPersons: numPersons, 
      voyagePrice: voyagePrice, 
    }]);
  }

  submitOpinion() {
    this.service.createOpinion(this.opinion, this.voyage.voyage_id).subscribe(response => {
      console.log('Opinión creada con éxito', response);
      this.comentarioCreado = true; // Mostrar mensaje de éxito
    });
  }

  showOpinionForm(): boolean {
    const today = new Date();
    const endDate = new Date(this.voyage.voyage_date_end);
    return this.voyage.is_purchased && this.isAuthenticated && today > endDate;
  }
}