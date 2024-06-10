import { Component } from '@angular/core';
import { VoyagesClientService } from './voyages-client.service';
import { VoyageCity } from './voyages-client.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-voyages-client',
  templateUrl: './voyages-client.component.html',
  styleUrls: ['./voyages-client.component.css']
})
export class VoyagesClientComponent {
  voyagesInfo: VoyageCity[] = [];

  constructor(private voyagesClientService: VoyagesClientService, private router: Router) {}

  ngOnInit() {
    this.voyagesClientService.getVoyagesByClient().subscribe({
      next: (data) => {
        if (data) { this.voyagesInfo = data; }
        console.log(this.voyagesInfo[0]);
      },
      error: (error) => {
        console.error('There was an error!', error);
      }
    });
  }

  viewVoyageForum(voyageId: number){ /*Me dirige a la ruta deseada*/
    this.router.navigate(['/forumVoyage', voyageId]) 
  }
}
