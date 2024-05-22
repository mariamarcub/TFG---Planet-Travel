import { Component, OnInit } from '@angular/core';
import { VoyageService } from './voyage.service';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { VoyageInfo } from './voyage.model';

@Component({
  selector: 'app-voyage',
  templateUrl: './voyage.component.html',
  styleUrls: ['./voyage.component.css']
})
export class VoyageComponent implements OnInit {
  voyage: VoyageInfo = new VoyageInfo();
  totalDays: number = 0;
  numPersons: number = 0;


  constructor(private service: VoyageService, private navRoute: Router, private route: ActivatedRoute) {}

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      var voyageId = +params['voyage'];
      this.loadVoyageInfo(voyageId);
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
    this.navRoute.navigate([`/bookingVoyage/${voyageId}`, { numPersons: numPersons, voyagePrice: voyagePrice }]);
  }

}