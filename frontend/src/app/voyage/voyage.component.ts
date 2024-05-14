import { Component } from '@angular/core';
import { VoyageService } from './voyage.service';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { VoyageInfo } from './voyage.model';

@Component({
  selector: 'app-voyage',
  templateUrl: './voyage.component.html',
  styleUrls: ['./voyage.component.css']
})
export class VoyageComponent {
  voyage: VoyageInfo = new VoyageInfo(); // Declaro la propiedad para almacenar el mes seleccionado por el usuario

  constructor(private service: VoyageService, private navRoute: Router, private route: ActivatedRoute) {}

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      var monthId = +params['voyage'];
      this.loadVoyageInfo(monthId);
    });
  }

  loadVoyageInfo(voyageId: number){
    this.service.getVoyageById(voyageId).subscribe(voyage => {
      this.voyage = voyage;
    })
  }
}
